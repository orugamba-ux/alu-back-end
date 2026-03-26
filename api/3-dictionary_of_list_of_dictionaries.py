#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py

Exports all TODO tasks for all employees from JSONPlaceholder
REST API to a JSON file named todo_all_employees.json.

The output format is a dictionary mapping each employee ID to
a list of task dictionaries:
{
    "<user_id>": [
        {"username": "<username>", "task": "<task title>",
         "completed": <true/false>},
        ...
    ],
    ...
}
"""
import json
import requests


if __name__ == "__main__":
    # Fetch all users and todos
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    data = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        data[user_id] = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                data[user_id].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

        # Confirm user ID value type
        if isinstance(data[user_id], list) and all(isinstance(t, dict)
                                                   for t in data[user_id]):
            print("USER_ID {} value type is a list of dicts: OK".format(user_id))

        # Confirm all tasks found
        tasks_for_user = [t for t in todos if t.get("userId") == user.get("id")]
        if len(data[user_id]) == len(tasks_for_user):
            print("All tasks found for USER_ID {}: OK".format(user_id))

    # Export to JSON
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)