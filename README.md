# Agentic AI Career Assistant

An intelligent **Multi-Agent AI Career Guidance Platform** that helps students improve their resumes, prepare for placements, and build personalized learning roadmaps using Large Language Models (LLMs).

The platform analyzes resumes, identifies strengths and skill gaps, generates placement preparation roadmaps, and creates customized interview question sets based on the candidate's profile.

---

## Problem Statement

Many students struggle with:

* Understanding whether their resume is placement-ready
* Identifying missing skills required for target roles
* Creating a structured placement preparation plan
* Finding the right learning resources
* Practicing role-specific interview questions

This project addresses these challenges by providing a personalized AI-powered career assistant.

---

# Features

## Resume Analysis Agent

Analyzes uploaded resumes and provides:

* ATS Compatibility Score
* Skills Extraction
* Strength Identification
* Missing Skills Detection
* Recommended Career Roles
* Project Extraction

---

## Roadmap Agent

Generates a personalized placement roadmap based on:

* Candidate Skills
* ATS Score
* Target Role

Provides:

* Skill Gap Analysis
* 12-Week DSA Preparation Plan
* CS Fundamentals Plan
* Development Roadmap
* Project Recommendations
* Placement Resources

---

## Interview Preparation Agent

Generates customized interview preparation content including:

### Technical Questions

* Programming
* Development
* Frameworks

### Core CS Subjects

* DBMS
* Operating Systems
* OOPS
* Computer Networks
* SQL

### Other Interview Categories

* HR Questions
* Behavioral Questions
* Resume-Based Questions
* Project-Based Questions

Each question includes expected answers for preparation.

---

## Planner Agent

Acts as a routing layer between user requests and backend agents.

Examples:

| User Query                   | Selected Agent  |
| ---------------------------- | --------------- |
| Review my resume             | Resume Agent    |
| Create a placement roadmap   | Roadmap Agent   |
| Generate interview questions | Interview Agent |

---

## 💾 Memory System

Stores analyzed resume information to avoid repeated processing and provide a seamless user experience.

---

# System Architecture

```text
                Resume PDF
                     │
                     ▼
              PDF Reader Tool
                     │
                     ▼
            Resume Analysis Agent
                     │
                     ▼
               Resume Memory
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
 Planner Agent   Roadmap Agent  Interview Agent
         │           │           │
         └───────────┴───────────┘
                     │
                     ▼
            Streamlit Dashboard
```

---

# Tech Stack

## Frontend

* Streamlit
* HTML
* CSS
* Custom Dark UI Design

## Backend

* Python
* LangChain
* Groq API
* Llama 3.3 70B Versatile

## AI Components

* Resume Agent
* Roadmap Agent
* Interview Agent
* Planner Agent

## Data Storage

* JSON-Based Memory System

---

# Project Structure

```text
agentic-ai-career-assistant/

├── agents/
│   ├── resume_agent_v2.py
│   ├── roadmap_agent_v2.py
│   ├── interview_agent.py
│   └── planner_agent.py
│
├── frontend/
│   ├── app.py
│   ├── components/
│   ├── pages_ui/
│   └── utils/
│
├── memory/
│   ├── memory_manager.py
│   └── resume_data.json
│
├── tools/
│   └── pdf_reader.py
│
├── screenshots/
│
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Lasyaaa/agentic-ai-career-assistant.git
cd agentic-ai-career-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
streamlit run frontend/app.py
```

---

# Future Enhancements

* AI Career Coach
* Internship Recommendations
* Job Matching System
* Cloud Deployment
* User Authentication
* Progress Tracking Dashboard
* Placement Analytics

---

# Author

**Lasya Priya**

B.Tech Information Technology

VNR Vignana Jyothi Institute of Engineering and Technology

Passionate about AI, Full Stack Development, and Building Solutions for Student Success.

---

⭐ If you found this project useful, consider giving it a star.
