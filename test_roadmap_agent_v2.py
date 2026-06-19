from tools.pdf_reader import extract_text_from_pdf
from agents.resume_agent_v2 import analyze_resume_v2
from agents.roadmap_agent_v2 import generate_roadmap_v2

resume_text = extract_text_from_pdf("Resumeamazon.pdf")

resume_data = analyze_resume_v2(resume_text)

roadmap = generate_roadmap_v2(
    resume_data,
    "Software Engineer"
)

print(roadmap)