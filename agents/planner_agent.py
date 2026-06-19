from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

def route_query(user_query):

    prompt = f"""
You are an intelligent planner agent.

Available agents:

1. resume_agent
   - Resume analysis
   - ATS score
   - Skill analysis

2. roadmap_agent
   - Learning roadmap
   - Placement preparation
   - Skill gap analysis

3. interview_agent
   - Interview questions
   - Mock interview preparation

User Query:
{user_query}

Return ONLY ONE of:

resume_agent
roadmap_agent
interview_agent
"""

    response = llm.invoke(prompt)

    return response.content.strip()