#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
import requests


if __name__ == "__main__":
    json_user = requests.get(
                'https://jsonplaceholder.typicode.com/users/').json()
    json_todo = requests.get(
                'https://jsonplaceholder.typicode.com/todos/').json()
    completed_tasks = []
    dico = {}
    usernamedict = {}
    for user in json_user:
        uid = user.get("id")
        dico[uid] = []
        usernamedict[uid] = user.get("username")

    for task in json_todo:
        task_dico = {}
        task_dico["username"] = usernamedict.get(uid)
        uid = task.get("userId")
        task_dico["task"] = task.get('title')
        task_dico["completed"] = task.get('completed')
        dico.get(uid).append(task_dico)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(dico, jsonfile)
