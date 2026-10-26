#!/usr/bin/python3
"""
Module to export an employee's TODO list to a CSV file.
"""

import csv
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
        filename = "{}.csv".format(employee_id)

        with open(filename, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todos_response:
                completed = str(task.get("completed"))
                title = task.get("title")
                writer.writerow([str(employee_id), username, completed, title])