#!/usr/bin/python3
"""
Module to gather and display an employee's TODO list progress from a REST API.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

        user_response = requests.get(user_url).json()
        todos_response = requests.get(todos_url).json()

        employee_name = user_response.get("name")
        total_tasks = len(todos_response)
        completed_tasks = [task for task in todos_response if task.get("completed")]
        number_of_done = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done, total_tasks))
        for task in completed_tasks:
            print("\t {}".format(task.get("title")))
            