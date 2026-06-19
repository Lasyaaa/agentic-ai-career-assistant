from tools.pdf_reader import extract_text_from_pdf
from agents.resume_agent_v2 import analyze_resume_v2

print("Reading PDF...")

resume_text = extract_text_from_pdf("Resumeamazon.pdf")

print("Analyzing Resume...")

result = analyze_resume_v2(resume_text)

print("Analysis Complete!")

print(result)