#!/usr/bin/python3
"""Exports the TODO lists of all employees to one JSON file."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        all_tasks[str(user_id)] = [
            {"username": username,
             "task": task.get("title"),
             "completed": task.get("completed")}
            for task in todos if task.get("userId") == user_id]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
