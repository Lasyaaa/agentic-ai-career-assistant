from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm=ChatGroq(
    model="llama-3.3-70b-versatile"
)
def generate_roadmap(resume_analysis, target_role):

    prompt = f"""
    You are an expert placement mentor.

    Resume Analysis:
    {resume_analysis}

    Target Role:
    {target_role}

    Create a detailed roadmap specifically for this role.

    Include:

    1. Skill Gap Analysis
    2. DSA Roadmap
    3. CS Fundamentals Roadmap
    4. Development Skills Roadmap
    5. Project Suggestions
    6. Interview Preparation Plan

    Be role-specific.
    """
    response=llm.invoke(prompt)
    return response.content