#!/usr/bin/python3
"""
Module to export an employee's TODO list to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

        user_response = requests.get(user_url).json()
        todos_response = requests.get(todos_url).json()

        username = user_response.get("username")
        filename = "{}.json".format(employee_id)

        task_list = []
        for task in todos_response:
            task_dict = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            task_list.append(task_dict)

        data = {str(employee_id): task_list}

        with open(filename, mode="w") as json_file:
            json.dump(data, json_file)
            