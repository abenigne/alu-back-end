#!/usr/bin/python3
"""
Module to export all employees' TODO lists to a single JSON file.
"""

import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url).json()
    todos_response = requests.get(todos_url).json()

    all_data = {}
    users_dict = {}

    for user in users_response:
        user_id = user.get("id")
        users_dict[user_id] = user.get("username")
        all_data[str(user_id)] = []

    for task in todos_response:
        user_id = task.get("userId")
        username = users_dict.get(user_id)
        task_dict = {
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        if str(user_id) in all_data:
            all_data[str(user_id)].append(task_dict)

    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(all_data, json_file)