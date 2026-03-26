#!/usr/bin/python3
import requests
import sys
import json
if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    ).json()
    data = {
        user_id: []
    }
    for task in todos:
        data[user_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })
    with open("{}.json".format(user_id), "w") as f:
        json.dump(data, f)