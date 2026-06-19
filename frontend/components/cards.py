"""
cards.py
--------
Reusable premium UI primitives: metric cards, pills, score displays,
section headers, empty states. Used across all dashboard pages so
visual language stays consistent.
"""

import streamlit as st


def section_header(label: str, heading: str, desc: str = ""):
    """Small uppercase label + large heading + optional description."""
    html = f"""
    <div class="section-label">{label}</div>
    <div class="section-heading">{heading}</div>
    """
    if desc:
        html += f'<div class="section-desc">{desc}</div>'
    st.markdown(html, unsafe_allow_html=True)


def metric_card(icon: str, value, label: str, trend: str = None, trend_type: str = "up"):
    """
    A single glass metric card.
    trend_type: 'up' | 'warn' | 'down' -> controls trend color.
    """
    trend_class = {"up": "trend-up", "warn": "trend-warn", "down": "trend-down"}.get(trend_type, "trend-up")
    trend_html = f'<div class="metric-trend {trend_class}">{trend}</div>' if trend else ""

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
            {trend_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_row(metrics: list):
    """
    Render a row of metric cards.
    metrics: list of dicts -> {icon, value, label, trend, trend_type}
    """
    cols = st.columns(len(metrics))
    for col, m in zip(cols, metrics):
        with col:
            metric_card(
                icon=m.get("icon", "•"),
                value=m.get("value", "—"),
                label=m.get("label", ""),
                trend=m.get("trend"),
                trend_type=m.get("trend_type", "up"),
            )


def pill_list(items: list, variant: str = "default"):
    """
    Render a wrapped list of pills.
    variant: 'default' | 'accent' | 'success' | 'warning' | 'danger'
    """
    variant_class = {
        "default": "pill",
        "accent": "pill pill-accent",
        "success": "pill pill-success",
        "warning": "pill pill-warning",
        "danger": "pill pill-danger",
    }.get(variant, "pill")

    if not items:
        st.markdown(
            '<span style="color: var(--text-tertiary); font-size: 0.88rem;">None identified</span>',
            unsafe_allow_html=True,
        )
        return

    html = "".join(f'<span class="{variant_class}">{item}</span>' for item in items)
    st.markdown(f'<div>{html}</div>', unsafe_allow_html=True)


def glass_card_start(extra_style: str = ""):
    st.markdown(f'<div class="glass-card" style="{extra_style}">', unsafe_allow_html=True)


def glass_card_end():
    st.markdown('</div>', unsafe_allow_html=True)


def ats_score_display(score: int):
    """Large ATS score with a colored ring-style progress bar."""
    try:
        score = int(score)
    except (ValueError, TypeError):
        score = 0

    if score >= 75:
        color = "var(--success)"
        verdict = "Strong"
    elif score >= 50:
        color = "var(--warning)"
        verdict = "Needs Improvement"
    else:
        color = "var(--danger)"
        verdict = "Weak"

    st.markdown(
        f"""
        <div class="score-ring-wrap">
            <div>
                <div class="score-ring-number" style="color:{color};">{score}<span style="font-size:1.2rem; color: var(--text-tertiary);">/100</span></div>
                <div style="color: var(--text-secondary); font-size: 0.85rem; margin-top:0.2rem;">ATS Compatibility Score · <span style="color:{color}; font-weight:600;">{verdict}</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(min(max(score, 0), 100) / 100)


def empty_state(icon: str, title: str, desc: str):
    st.markdown(
        f"""
        <div class="empty-state">
            <div class="empty-state-icon">{icon}</div>
            <div class="empty-state-title">{title}</div>
            <div class="empty-state-desc">{desc}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def divider():
    st.markdown('<hr class="thin-divider" />', unsafe_allow_html=True)


def render_markdown_block(content: str):
    """Render agent-generated markdown (roadmap / interview prep) in a styled container."""
    st.markdown('<div class="content-block">', unsafe_allow_html=True)
    st.markdown(content)
    st.markdown('</div>', unsafe_allow_html=True)