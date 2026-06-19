"""
sidebar.py
----------
Premium sidebar navigation. Pure session_state routing — no
multipage file-based routing, so we control the look fully.
"""

import streamlit as st

NAV_ITEMS = [
    {"key": "overview", "label": "Overview", "icon": "◈"},
    {"key": "resume_analysis", "label": "Resume Analysis", "icon": "▤"},
    {"key": "roadmap", "label": "Roadmap", "icon": "◷"},
    {"key": "interview_prep", "label": "Interview Prep", "icon": "◎"},
    {"key": "resources", "label": "Resources", "icon": "▥"},
    {"key": "ai_assistant", "label": "AI Assistant", "icon": "✦"},
]


def render_sidebar():
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="sidebar-brand-mark">CA</div>
                <div>
                    <div class="sidebar-brand-text">Career Assistant</div>
                    <div class="sidebar-brand-sub">Agentic AI Platform</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        has_resume = st.session_state.get("resume_data") is not None

        st.markdown(
            '<div class="section-label" style="margin-top:0.2rem;">Navigate</div>',
            unsafe_allow_html=True,
        )

        for item in NAV_ITEMS:
            is_active = st.session_state.get("active_page") == item["key"]
            disabled = (item["key"] != "overview") and (not has_resume) and (item["key"] != "ai_assistant")

            wrapper_class = "nav-active" if is_active else ""
            st.markdown(f'<div class="{wrapper_class}">', unsafe_allow_html=True)
            if st.button(
                f"{item['icon']}   {item['label']}",
                key=f"nav_{item['key']}",
                use_container_width=True,
                disabled=disabled,
            ):
                st.session_state["active_page"] = item["key"]
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div style="margin-top: 1.6rem;"></div>', unsafe_allow_html=True)

        if has_resume:
            rd = st.session_state["resume_data"]
            score = rd.get("ats_score", "—")
            st.markdown(
                f"""
                <div class="glass-card" style="padding: 1rem; margin-top: 0.5rem;">
                    <div style="font-size: 0.72rem; color: var(--text-tertiary); font-weight:600; text-transform:uppercase; letter-spacing:0.06em;">Current Resume</div>
                    <div style="font-size: 1.6rem; font-weight: 800; margin-top: 0.3rem;">{score}<span style="font-size:0.95rem; color:var(--text-tertiary);">/100</span></div>
                    <div style="font-size: 0.78rem; color: var(--text-secondary);">ATS Score</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("↺  Analyze New Resume", key="nav_reset", use_container_width=True):
                for k in ["resume_data", "resume_text", "roadmap_text", "interview_text", "active_page"]:
                    st.session_state.pop(k, None)
                st.session_state["active_page"] = "overview"
                st.rerun()
        else:
            st.markdown(
                """
                <div class="glass-card" style="padding: 1rem;">
                    <div style="font-size: 0.82rem; color: var(--text-secondary); line-height:1.5;">
                        Upload your resume from the Overview tab to unlock your dashboard.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )