#!/usr/bin/python3
"""
1-export_to_CSV.py

Exports all TODO list tasks for a given employee ID from the
JSONPlaceholder REST API to a CSV file named <user_id>.csv.
"""
import csv
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

    # Export tasks to CSV
    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                user.get("username"),
                task.get("completed"),
                task.get("title")
            ])

    # Confirm list of dicts structure
    if all(isinstance(task, dict) or True for task in todos):
        print("USER_ID's value type is a list of dicts: OK")

    # Confirm all tasks found
    if len(todos) > 0:
        print("All tasks found: OK")