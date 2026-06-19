from tools.pdf_reader import extract_text_from_pdf
from agents.resume_agent import analyze_resume

resume_text = extract_text_from_pdf("Resumeamazon.pdf")

analysis = analyze_resume(resume_text)

print(analysis)