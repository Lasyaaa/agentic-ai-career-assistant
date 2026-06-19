from tools.pdf_reader import extract_text_from_pdf

from agents.resume_agent_v2 import analyze_resume_v2
from agents.roadmap_agent_v2 import generate_roadmap_v2
from agents.interview_agent import generate_interview_questions
from agents.planner_agent import route_query


PDF_PATH = "Resumeamazon.pdf"

resume_text = extract_text_from_pdf(PDF_PATH)

resume_data = analyze_resume_v2(resume_text)

user_query = input("What would you like help with?\n")

selected_agent = route_query(user_query)

print(f"\nPlanner selected: {selected_agent}\n")


if selected_agent == "resume_agent":

    print(resume_data)

elif selected_agent == "roadmap_agent":

    target_role = input(
        "Enter target role: "
    )

    result = generate_roadmap_v2(
        resume_data,
        target_role
    )

    print(result)

elif selected_agent == "interview_agent":

    target_role = input(
        "Enter target role: "
    )

    result = generate_interview_questions(
        resume_data,
        target_role
    )

    print(result)

else:

    print("Unknown Agent")