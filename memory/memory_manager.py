import json
import os


def save_resume_data(data):

    with open(
        "memory/resume_data.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_resume_data():

    if os.path.exists(
        "memory/resume_data.json"
    ):

        with open(
            "memory/resume_data.json",
            "r"
        ) as file:

            return json.load(file)

    return None