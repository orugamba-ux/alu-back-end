#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Retrieves the TODO list progress for a given employee ID from the
JSONPlaceholder REST API and displays completed tasks.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(user_url).json()
    if not user:
        print("User with ID {} not found.".format(user_id))
        sys.exit(1)
    else:
        print("Correct USER_ID: OK")

    # Fetch TODO tasks
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id
    )
    todos = requests.get(todos_url).json()

    total_tasks = len(todos)
    done_tasks = 0
    for task in todos:
        if task.get("completed") is True:
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), done_tasks, total_tasks
    ))

    for task in todos:
        if task.get("completed") is True:
            print("\t {}".format(task.get("title")))

    # Confirm all tasks found
    if len(todos) == total_tasks:
        print("All tasks found: OK")