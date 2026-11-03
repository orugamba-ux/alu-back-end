#!/usr/bin/python3
"""Gets the TODO list progress of an employee from a REST API."""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    name = user.get("name")
    done_tasks = [task.get("title") for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done_tasks), len(todos)))
    for title in done_tasks:
        print("\t {}".format(title))
