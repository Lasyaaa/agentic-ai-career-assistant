from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def analyze_resume(resume_text):

    prompt = f"""
    You are an expert placement mentor.

    Analyze this resume and provide:

    1. ATS Score out of 100
    2. Key Skills
    3. Strengths
    4. Weaknesses
    5. Missing Skills
    6. Suggested Improvements
    7. Suitable Job Roles

    Resume:
    {resume_text}
    """

    response = llm.invoke(prompt)

    return response.content