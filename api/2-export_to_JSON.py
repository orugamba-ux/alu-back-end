#!/usr/bin/python3
"""
2-export_to_JSON.py

Exports all TODO list tasks for a given employee ID from the
JSONPlaceholder REST API to a JSON file named <user_id>.json.

The output format is a dictionary with the employee ID as the key
and a list of task dictionaries as the value.
"""
import json
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

    # Build dictionary
    data = {user_id: []}
    for task in todos:
        data[user_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    # Confirm list of dicts
    if isinstance(data[user_id], list) and all(isinstance(t, dict) for t in data[user_id]):
        print("USER_ID's value type is a list of dicts: OK")

    # Confirm all tasks found
    if len(data[user_id]) == len(todos):
        print("All tasks found: OK")

    # Export to JSON
    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)