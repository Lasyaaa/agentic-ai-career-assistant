from dotenv import load_dotenv
from langchain_groq import ChatGroq
import json

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def analyze_resume_v2(resume_text):

    prompt = f"""
    Analyze the following resume and return ONLY valid JSON.

    ATS Score must be an integer between 0 and 100.

    {{
        "ats_score": number,
        "skills": [],
        "strengths": [],
        "weaknesses": [],
        "missing_skills": [],
        "recommended_roles": []
    }}

    Resume:
    {resume_text}
    """

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Remove markdown code fences
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    print("\nCleaned JSON:\n")
    print(content)

    data = json.loads(content)

    return data