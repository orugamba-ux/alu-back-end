#!/usr/bin/python3
import requests
import json
if __name__ == "__main__":
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()
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
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)