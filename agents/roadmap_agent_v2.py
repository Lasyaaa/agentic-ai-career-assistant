from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def generate_roadmap_v2(resume_data, target_role):

    prompt = f"""
    You are an expert placement mentor.

    Candidate Information:

    ATS Score:
    {resume_data['ats_score']}

    Skills:
    {resume_data['skills']}

    Missing Skills:
    {resume_data['missing_skills']}

    Recommended Roles:
    {resume_data['recommended_roles']}

    Target Role:
    {target_role}

    Create:

    1. Skill Gap Analysis
    2. 12 Week DSA Plan
    3. CS Fundamentals Plan
    4. Development Roadmap
    5. Project Recommendations
    6. Interview Preparation Strategy
    7. Placement Readiness Score

    Make it highly personalized.
    """

    response = llm.invoke(prompt)

    return response.content