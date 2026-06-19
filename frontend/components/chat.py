"""
chat.py
-------
AI Assistant chat interface. User types a request in natural language,
the Planner Agent (select_agent) routes it to the correct backend agent,
and the result is rendered as a chat message.
"""

import streamlit as st

from utils.backend_bridge import (
    route_query,
    run_resume_analysis,
    run_roadmap_generation,
    run_interview_questions,
    persist_resume_data,
    BackendError,
)

AGENT_DISPLAY_NAMES = {
    "resume_agent": "Resume Agent",
    "roadmap_agent": "Roadmap Agent",
    "interview_agent": "Interview Agent",
}

SUGGESTED_PROMPTS = [
    "Analyze my resume",
    "Generate a roadmap for SDE roles",
    "Generate interview questions for Backend Developer",
]


def render_chat():
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    st.markdown(
        '<div class="section-label">AI Assistant</div>'
        '<div class="section-heading">Ask your Career Assistant</div>'
        '<div class="section-desc">The Planner Agent routes your request to the right specialist agent automatically.</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state["chat_history"]:
        st.markdown('<div style="margin-bottom: 1rem;">', unsafe_allow_html=True)
        cols = st.columns(len(SUGGESTED_PROMPTS))
        for col, prompt in zip(cols, SUGGESTED_PROMPTS):
            with col:
                if st.button(prompt, key=f"suggest_{prompt}", use_container_width=True):
                    _handle_user_message(prompt)
        st.markdown('</div>', unsafe_allow_html=True)

    chat_container = st.container()
    with chat_container:
        for msg in st.session_state["chat_history"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    user_input = st.chat_input("Ask me to analyze your resume, build a roadmap, or generate interview questions...")
    if user_input:
        _handle_user_message(user_input)


def _handle_user_message(user_query: str):
    st.session_state["chat_history"].append({"role": "user", "content": user_query})

    try:
        with st.spinner("Routing your request..."):
            agent_key = route_query(user_query)

        agent_label = AGENT_DISPLAY_NAMES.get(agent_key, agent_key)

        response_text = _dispatch_to_agent(agent_key, user_query)

        prefixed = f"**Routed to: {agent_label}**\n\n{response_text}"
        st.session_state["chat_history"].append({"role": "assistant", "content": prefixed})

    except BackendError as e:
        st.session_state["chat_history"].append({"role": "assistant", "content": f"⚠️ {str(e)}"})
    except Exception as e:
        st.session_state["chat_history"].append({"role": "assistant", "content": f"⚠️ Something went wrong. ({e})"})

    st.rerun()


def _dispatch_to_agent(agent_key: str, user_query: str) -> str:
    resume_data = st.session_state.get("resume_data")
    resume_text = st.session_state.get("resume_text")
    target_role = st.session_state.get("target_role", "Software Engineer")

    if agent_key == "resume_agent":
        if not resume_text:
            return "I don't have a resume on file yet. Please upload your resume PDF from the Overview tab first."
        resume_data = run_resume_analysis(resume_text)
        st.session_state["resume_data"] = resume_data
        persist_resume_data(resume_data)
        skills = ", ".join(resume_data.get("skills", [])[:8]) or "—"
        return (
            f"Your resume scored **{resume_data.get('ats_score', '—')}/100** on ATS compatibility.\n\n"
            f"**Top skills detected:** {skills}\n\n"
            f"Head to the **Resume Analysis** tab for the full breakdown."
        )

    if agent_key == "roadmap_agent":
        if not resume_data:
            return "I need an analyzed resume first. Please upload your resume from the Overview tab."
        roadmap_text = run_roadmap_generation(resume_data, target_role)
        st.session_state["roadmap_text"] = roadmap_text
        return f"Your personalized roadmap is ready. Here's a preview:\n\n{roadmap_text[:600]}...\n\nSee the full plan in the **Roadmap** tab."

    if agent_key == "interview_agent":
        if not resume_data:
            return "I need an analyzed resume first. Please upload your resume from the Overview tab."
        interview_text = run_interview_questions(resume_data, target_role)
        st.session_state["interview_text"] = interview_text
        return f"Interview questions generated. Here's a preview:\n\n{interview_text[:600]}...\n\nSee all questions in the **Interview Prep** tab."

    return f"I routed this to `{agent_key}`, but I don't recognize that agent type yet."