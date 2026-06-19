from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)


def generate_roadmap_v2(resume_data, target_role):

    prompt = f"""
You are an expert placement mentor helping a student prepare for placements.

Candidate Information:

ATS Score:
{resume_data['ats_score']}

Skills:
{resume_data['skills']}

Missing Skills:
{resume_data['missing_skills']}

Recommended Roles:
{resume_data['recommended_roles']}

Projects:
{resume_data.get('projects', [])}

Target Role:
{target_role}

Create a highly personalized placement roadmap.

========================================
1. SKILL GAP ANALYSIS
========================================
- Current strengths
- Missing skills
- Improvement areas

========================================
2. 12-WEEK DSA PLAN
========================================
For each phase include:
- Topics to learn
- Recommended LeetCode problems
- Best YouTube resources
- Best practice platforms

Suggested Topics:
- Arrays
- Strings
- Linked Lists
- Stacks & Queues
- Hashing
- Sliding Window
- Binary Search
- Trees
- Graphs
- Dynamic Programming

========================================
3. CS FUNDAMENTALS PLAN
========================================

DBMS:
- Important topics
- Best YouTube channels
- Practice resources

Operating Systems:
- Important topics
- Best YouTube channels
- Practice resources

OOPS:
- Important topics
- Best YouTube channels
- Practice resources

Computer Networks:
- Important topics
- Best YouTube channels
- Practice resources

SQL:
- Important topics
- Practice resources

========================================
4. DEVELOPMENT ROADMAP
========================================
Include:
- Technologies to learn
- Learning sequence
- Suggested projects
- Best resources

========================================
5. PROJECT RECOMMENDATIONS
========================================

Provide:

Beginner Project
- Idea
- Tech Stack

Intermediate Project
- Idea
- Tech Stack

Advanced Project
- Idea
- Tech Stack

========================================
6. INTERVIEW PREPARATION STRATEGY
========================================
Include:

- Technical Interview Preparation
- HR Interview Preparation
- Mock Interview Platforms
- Resume Preparation Tips

========================================
7. PLACEMENT READINESS SCORE
========================================
Rate:
- DSA
- CS Fundamentals
- Development Skills
- Communication Skills
- Overall Placement Readiness

========================================
RESOURCES TO RECOMMEND
========================================

Use resources such as:
- Striver A2Z DSA Sheet
- NeetCode
- CodeHelp by Babbar
- Kunal Kushwaha
- Gate Smashers
- Jenny's Lectures
- Love Babbar DSA Sheet
- LeetCode
- HackerRank
- Codeforces
- InterviewBit
- GeeksforGeeks

Make recommendations specific to the candidate's profile and target role.
"""

    response = llm.invoke(prompt)

    return response.content