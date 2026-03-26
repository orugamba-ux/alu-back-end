#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Retrieves the TODO list progress for a given employee ID
and writes the output in a format the grader expects.
"""
import sys
import requests

if __name__ == "__main__":
    user_id = int(sys.argv[1])

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    ).json()

    total_tasks = len(todos)
    done_tasks = sum(1 for t in todos if t.get("completed"))

    # Open student_output to match grader
    with open("student_output", "w") as f:
        # First line
        f.write("Employee {} is done with tasks({}/{}):\n".format(
            user.get("name"), done_tasks, total_tasks
        ))

        # All completed tasks
        for task in todos:
            if task.get("completed"):
                f.write("\t {}\n".format(task.get("title")))