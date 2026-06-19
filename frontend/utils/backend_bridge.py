"""
backend_bridge.py
------------------
SINGLE integration point between the Streamlit frontend and the existing
backend agents. No backend logic lives here or is duplicated here —
this module only imports and calls real backend functions, and adds
light error handling / caching so the UI stays resilient.

If any backend function signature changes, this is the ONLY file
that needs to be updated.
"""

import sys
import os

# Ensure project root is importable when running `streamlit run frontend/app.py`
ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from agents.resume_agent_v2 import analyze_resume_v2
from agents.roadmap_agent_v2 import generate_roadmap_v2
from agents.interview_agent import generate_interview_questions
from agents.planner_agent import route_query as planner_route_query
from tools.pdf_reader import extract_text_from_pdf
from memory.memory_manager import (
    save_resume_data,
    load_resume_data
)


class BackendError(Exception):
    """Raised when a backend agent call fails, with a user-friendly message."""
    pass


# ----------------------------------------------------------------------
# PDF / Resume extraction
# ----------------------------------------------------------------------
def read_resume_pdf(pdf_path: str) -> str:
    """Extract raw text from an uploaded resume PDF."""
    try:
        return extract_text_from_pdf(pdf_path)
    except Exception as e:
        raise BackendError(f"Could not read the PDF file. ({e})")


# ----------------------------------------------------------------------
# Resume Agent
# ----------------------------------------------------------------------
def run_resume_analysis(resume_text: str) -> dict:
    """
    Calls analyze_resume_v2(resume_text) -> dict with:
    ats_score, skills, strengths, weaknesses, projects,
    missing_skills, recommended_roles
    """
    try:
        result = analyze_resume_v2(resume_text)
        if not isinstance(result, dict):
            raise BackendError("Resume agent returned an unexpected format.")
        return result
    except BackendError:
        raise
    except Exception as e:
        raise BackendError(f"Resume analysis failed. ({e})")


# ----------------------------------------------------------------------
# Roadmap Agent
# ----------------------------------------------------------------------
def run_roadmap_generation(resume_data: dict, target_role: str) -> str:
    """Calls generate_roadmap_v2(resume_data, target_role) -> markdown string."""
    try:
        return generate_roadmap_v2(resume_data, target_role)
    except Exception as e:
        raise BackendError(f"Roadmap generation failed. ({e})")


# ----------------------------------------------------------------------
# Interview Agent
# ----------------------------------------------------------------------
def run_interview_questions(resume_data: dict, target_role: str) -> str:
    """Calls generate_interview_questions(resume_data, target_role) -> markdown string."""
    try:
        return generate_interview_questions(resume_data, target_role)
    except Exception as e:
        raise BackendError(f"Interview question generation failed. ({e})")


# ----------------------------------------------------------------------
# Planner Agent
# ----------------------------------------------------------------------

from agents.planner_agent import route_query as planner_route_query

def route_user_query(user_query: str) -> str:
    """
    Returns:
    resume_agent
    roadmap_agent
    interview_agent
    """
    try:
        return planner_route_query(user_query)
    except Exception as e:
        raise BackendError(f"Could not route your request. ({e})")
def route_query(user_query: str) -> str:
    return route_user_query(user_query)
# ----------------------------------------------------------------------
# Memory
# ----------------------------------------------------------------------
def persist_resume_data(data: dict) -> None:
    try:
        save_resume_data(data)
    except Exception:
        # Memory persistence failure should never break the UI session.
        pass


def fetch_saved_resume_data():
    try:load_resume_data()
    except Exception:
        return None