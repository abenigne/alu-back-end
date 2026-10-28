#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    username = user.get("username")

    data = {user_id: [{"task": t.get("title"),
                       "completed": t.get("completed"),
                       "username": username} for t in todos]}

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(data, json_file)
