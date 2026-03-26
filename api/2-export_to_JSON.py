#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Retrieves all TODO list tasks for a given employee ID from the
JSONPlaceholder REST API and exports them to a JSON file named
<user_id>.json.

Usage:
    python 0-gather_data_from_an_API.py <user_id>

The output JSON format is:
{
    "<user_id>": [
        {
            "task": "<task title>",
            "completed": <true/false>,
            "username": "<username>"
        },
        ...
    ]
}
"""
import sys
import json
import requests


if __name__ == "__main__":
    # Ensure an employee ID argument was provided
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user information from the API
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ).json()

    # Fetch TODO list for the given user
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    ).json()

    # Prepare the data dictionary
    data = {user_id: []}

    for task in todos:
        # Append each task as a dictionary with relevant fields
        data[user_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    # Write the data to a JSON file named <user_id>.json
    with open("{}.json".format(user_id), "w") as f:
    json.dump(data, f)