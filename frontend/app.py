"""
app.py
------
Entry point for the Agentic AI Career Assistant frontend.

Run with:
    streamlit run frontend/app.py

This file owns:
- Page config
- CSS injection
- Session state initialization
- Top-level routing between dashboard sections

It does NOT contain any backend logic — all backend calls go through
utils/backend_bridge.py.
"""

import os
import sys
# Make project root importable (so `agents`, `tools`, `memory` resolve
# regardless of the working directory Streamlit is launched from).
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
import streamlit as st

from utils import save_uploaded_file

from tools.pdf_reader import extract_text_from_pdf

from components.sidebar import render_sidebar
from pages_ui import (
    overview,
    resume_analysis,
    roadmap,
    interview_prep,
    resources,
    ai_assistant
)

FRONTEND_DIR = os.path.dirname(os.path.abspath(__file__))
if FRONTEND_DIR not in sys.path:
    sys.path.insert(0, FRONTEND_DIR)


# ----------------------------------------------------------------------
# Page config — must be the first Streamlit call
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Career Assistant · Agentic AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ----------------------------------------------------------------------
# Inject premium CSS theme
# ----------------------------------------------------------------------
def load_css():
    css_path = os.path.join(FRONTEND_DIR, "style.css")
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()


# ----------------------------------------------------------------------
# Session state initialization
# ----------------------------------------------------------------------
def init_session_state():
    defaults = {
        "active_page": "overview",
        "resume_data": None,
        "resume_text": None,
        "roadmap_text": None,
        "interview_text": None,
        "target_role": None,
        "chat_history": [],
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()


# ----------------------------------------------------------------------
# Render sidebar + route to active page
# ----------------------------------------------------------------------
render_sidebar()

PAGE_ROUTER = {
    "overview": overview.render,
    "resume_analysis": resume_analysis.render,
    "roadmap": roadmap.render,
    "interview_prep": interview_prep.render,
    "resources": resources.render,
    "ai_assistant": ai_assistant.render,
}

active_page = st.session_state.get("active_page", "overview")
render_fn = PAGE_ROUTER.get(active_page, overview.render)
render_fn()