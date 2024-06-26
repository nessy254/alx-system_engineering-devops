#!/usr/bin/python3
"""
Script that exports data in CSV format
"""

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

    with open("{}.csv".format(employee_id), "w") as csv_file:
        for task in tasks:
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                employee_id, username, task.get("completed"),
                task.get("title")))
