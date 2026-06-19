"""
overview.py
-----------
Dashboard overview: key metrics + upload zone (if no resume yet).
"""

import streamlit as st

from frontend.components.cards import (
    section_header,
    metric_row,
    divider
)

from frontend.components.upload import (
    render_hero,
    render_upload_zone
)


def render():
    resume_data = st.session_state.get("resume_data")

    if not resume_data:
        render_hero()
        render_upload_zone()
        return

    section_header(
        "Dashboard",
        "Welcome back",
        "Here's a snapshot of your placement readiness.",
    )

    skills = resume_data.get("skills", []) or []
    projects = resume_data.get("projects", []) or []
    roles = resume_data.get("recommended_roles", []) or []
    ats_score = resume_data.get("ats_score", 0)

    try:
        ats_score_int = int(ats_score)
    except (ValueError, TypeError):
        ats_score_int = 0

    if ats_score_int >= 75:
        trend, trend_type = "Strong profile", "up"
    elif ats_score_int >= 50:
        trend, trend_type = "Room to improve", "warn"
    else:
        trend, trend_type = "Needs work", "down"

    metric_row([
        {"icon": "◈", "value": f"{ats_score_int}", "label": "ATS Score", "trend": trend, "trend_type": trend_type},
        {"icon": "▤", "value": len(skills), "label": "Skills Identified"},
        {"icon": "◷", "value": len(projects), "label": "Projects Listed"},
        {"icon": "✦", "value": len(roles), "label": "Recommended Roles"},
    ])

    divider()

    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-label">Next Steps</div>
                <div class="section-heading" style="font-size:1.15rem;">Continue your prep</div>
            """,
            unsafe_allow_html=True,
        )
        steps = [
            ("▤", "Review your full Resume Analysis", "resume_analysis"),
            ("◷", "Generate your personalized Roadmap", "roadmap"),
            ("◎", "Practice with Interview Questions", "interview_prep"),
        ]
        for icon, text, page_key in steps:
            c1, c2 = st.columns([5, 1])
            with c1:
                st.markdown(f'<div style="padding: 0.5rem 0; color: var(--text-secondary); font-size:0.9rem;">{icon}&nbsp;&nbsp;{text}</div>', unsafe_allow_html=True)
            with c2:
                if st.button("→", key=f"goto_{page_key}"):
                    st.session_state["active_page"] = page_key
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-label">Recommended Roles</div>
            """,
            unsafe_allow_html=True,
        )
        if roles:
            for r in roles[:5]:
                st.markdown(
                    f'<div style="padding: 0.45rem 0; border-bottom: 1px solid var(--border-subtle); font-size: 0.88rem; color: var(--text-primary);">{r}</div>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown('<div style="color: var(--text-tertiary); font-size: 0.85rem;">No roles identified yet.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)