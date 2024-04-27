#!/usr/bin/python3
"""
Script that exports data in JSON format using REST API
"""

import json
import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    username = response.json().get("username")

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    dictionary = {employee_id: []}

    for task in tasks:
        dictionary[employee_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(dictionary, json_file)
