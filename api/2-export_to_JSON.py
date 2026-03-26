#!/usr/bin/python3
"""
2-export_to_JSON.py

Exports all TODO list tasks for a given employee ID from the
JSONPlaceholder REST API to a JSON file named <user_id>.json.

The output format is a dictionary with the employee ID as the key
and a list of task dictionaries as the value. Each task dictionary
contains:
    - task: title of the task
    - completed: boolean indicating completion status
    - username: username of the employee

Usage:
    python 2-export_to_JSON.py <user_id>
"""
import json
import requests
import sys


if __name__ == "__main__":
    # Validate command-line argument
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

    # Fetch TODO tasks for the user
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id
    )
    todos = requests.get(todos_url).json()

    # Build dictionary with user ID as key and list of tasks as value
    data = {user_id: []}
    for task in todos:
        data[user_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    # Export tasks to JSON file
    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)