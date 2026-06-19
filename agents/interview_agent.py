from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def generate_interview_questions(
    resume_data,
    target_role
):

    prompt = f"""
You are a senior technical interviewer at a top product-based company.

Candidate Skills:
{resume_data["skills"]}

Candidate Strengths:
{resume_data["strengths"]}

Recommended Roles:
{resume_data["recommended_roles"]}

Target Role:
{target_role}

Generate the following sections:

========================
TECHNICAL QUESTIONS
========================
- 10 Technical Questions

========================
PROJECT-BASED QUESTIONS
========================
- 5 Questions based on the candidate's projects

========================
RESUME-BASED QUESTIONS
========================
- 3 Questions based on resume content

========================
HR QUESTIONS
========================
- 5 HR Questions

========================
BEHAVIORAL QUESTIONS
========================
- 5 Behavioral Questions

========================
DBMS QUESTIONS
========================
- 3 Questions
- Include expected answers

========================
OPERATING SYSTEMS QUESTIONS
========================
- 3 Questions
- Include expected answers

========================
OOPS QUESTIONS
========================
- 3 Questions
- Include expected answers

========================
COMPUTER NETWORKS QUESTIONS
========================
- 3 Questions
- Include expected answers

========================
SQL QUESTIONS
========================
- 3 Questions
- Include expected answers

Rules:
1. Questions should match the target role.
2. Questions should reflect the candidate's skills and projects.
3. Mix definitions, differences, scenario-based questions, and interview-favorite concepts.
4. For conceptual questions provide short expected answers.
5. Make questions suitable for placement interviews.
6. Ask project-specific questions based on the resume projects.
"""

    response = llm.invoke(prompt)

    return response.content