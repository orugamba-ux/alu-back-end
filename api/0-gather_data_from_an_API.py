#!/usr/bin/python3
import sys
import requests
if __name__ == "__main__":
    user_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(user_url).json()
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    todos = requests.get(todos_url).json()
    total_tasks = len(todos)
    done_tasks = 0
    for task in todos:
        if task.get("completed") is True:
            done_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), done_tasks, total_tasks))
    for task in todos:
        if task.get("completed") is True:
            print("\t {}".format(task.get("title")))