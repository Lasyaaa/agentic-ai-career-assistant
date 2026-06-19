from memory.memory_manager import (
    save_resume_data,
    load_resume_data
)

sample_data = {
    "name": "Lasya",
    "role": "Software Engineer",
    "skills": [
        "Python",
        "C++",
        "MERN"
    ]
}

save_resume_data(sample_data)

data = load_resume_data()

print(data)