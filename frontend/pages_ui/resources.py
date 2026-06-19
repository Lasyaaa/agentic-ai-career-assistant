"""
resources.py
------------
Static curated learning resources by topic (DSA, DBMS, OS, OOPS, CN, SQL).
This is presentation-layer content, not backend-generated, so it's
maintained directly in the frontend per the project spec.
"""

import streamlit as st

from components.cards import section_header, glass_card_start, glass_card_end

RESOURCES = {
    "DSA": {
        "icon": "◷",
        "items": [
            ("Striver's A2Z DSA Sheet", "https://takeuforward.org/strivers-a2z-dsa-course-sheet-2"),
            ("NeetCode 150", "https://neetcode.io/practice"),
            ("LeetCode Top Interview 150", "https://leetcode.com/studyplan/top-interview-150/"),
            ("CP-Algorithms", "https://cp-algorithms.com/"),
        ],
    },
    "DBMS": {
        "icon": "▤",
        "items": [
            ("GeeksforGeeks DBMS Notes", "https://www.geeksforgeeks.org/dbms/"),
            ("Database System Concepts (Silberschatz)", "https://www.db-book.com/"),
            ("SQLBolt Interactive Lessons", "https://sqlbolt.com/"),
        ],
    },
    "OS": {
        "icon": "◈",
        "items": [
            ("Operating System Concepts (Galvin)", "https://www.os-book.com/"),
            ("GeeksforGeeks OS Notes", "https://www.geeksforgeeks.org/operating-systems/"),
            ("MIT 6.S081 OS Engineering", "https://pdos.csail.mit.edu/6.S081/"),
        ],
    },
    "OOPS": {
        "icon": "✦",
        "items": [
            ("GeeksforGeeks OOP Concepts", "https://www.geeksforgeeks.org/object-oriented-programming-oops-concept-in-java/"),
            ("Refactoring Guru - Design Patterns", "https://refactoring.guru/design-patterns"),
        ],
    },
    "CN": {
        "icon": "◎",
        "items": [
            ("Computer Networking: Top-Down Approach", "https://gaia.cs.umass.edu/kurose_ross/index.php"),
            ("GeeksforGeeks Computer Networks", "https://www.geeksforgeeks.org/computer-network-tutorials/"),
        ],
    },
    "SQL": {
        "icon": "▥",
        "items": [
            ("LeetCode SQL 50", "https://leetcode.com/studyplan/top-sql-50/"),
            ("Mode SQL Tutorial", "https://mode.com/sql-tutorial/"),
            ("SQLZoo", "https://sqlzoo.net/"),
        ],
    },
}


def render():
    section_header(
        "Resources",
        "Curated learning resources",
        "Hand-picked references across core CS subjects and DSA preparation.",
    )

    topics = list(RESOURCES.keys())
    tabs = st.tabs(topics)

    for tab, topic in zip(tabs, topics):
        with tab:
            data = RESOURCES[topic]
            glass_card_start()
            st.markdown(
                f'<div class="section-label">{data["icon"]} {topic} Resources</div>',
                unsafe_allow_html=True,
            )
            for title, url in data["items"]:
                st.markdown(
                    f"""
                    <div style="padding: 0.7rem 0; border-bottom: 1px solid var(--border-subtle); display:flex; justify-content:space-between; align-items:center;">
                        <span style="color: var(--text-primary); font-size: 0.92rem; font-weight: 500;">{title}</span>
                        <a href="{url}" target="_blank" style="color: var(--accent); text-decoration:none; font-size: 0.85rem; font-weight:600;">Visit →</a>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            glass_card_end()