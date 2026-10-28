#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file."""
from collections import OrderedDict
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    username = user.get("username")

    tasks = []
    for t in todos:
        entry = OrderedDict()
        entry["task"] = t.get("title")
        entry["completed"] = t.get("completed")
        entry["username"] = username
        tasks.append(entry)

    data = OrderedDict()
    data[user_id] = tasks

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(data, json_file)
