from tools.pdf_reader import extract_text_from_pdf
from agents.resume_agent import analyze_resume
from agents.roadmap_agent import generate_roadmap

# Step 1: Extract resume text
resume_text = extract_text_from_pdf("Resumeamazon.pdf")

# Step 2: Analyze resume
resume_analysis = analyze_resume(resume_text)

# Step 3: Define target role
target_role = "Software Engineer"

# Step 4: Generate roadmap
roadmap = generate_roadmap(resume_analysis, target_role)

# Step 5: Print results
print("\n========== RESUME ANALYSIS ==========\n")
print(resume_analysis)

print("\n========== ROADMAP ==========\n")
print(roadmap)