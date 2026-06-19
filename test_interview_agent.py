from tools.pdf_reader import extract_text_from_pdf
from agents.resume_agent_v2 import analyze_resume_v2
from agents.interview_agent import generate_interview_questions

resume_text = extract_text_from_pdf(
    "Resumeamazon.pdf"
)

resume_data = analyze_resume_v2(
    resume_text
)

questions = generate_interview_questions(
    resume_data,
    "Software Engineer"
)

print(questions)