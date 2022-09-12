#!/usr/bin/python3
"""Python script to export data in the JSON format"""

from sys import argv
import requests
import json


if __name__ == "__main__":
    userId = int(argv[1])
    user = ('https://jsonplaceholder.typicode.com/users/{}'.format(userId))
    todo = ('{}/todos/'.format(user))
    json_user = requests.get(user).json()
    json_todo = requests.get(todo).json()
    completed_tasks = []

    for task in json_todo:
        task_dico = {}
        task_dico["task"] = task.get('title')
        task_dico["completed"] = task.get('completed')
        task_dico["username"] = task.get('name')
        completed_tasks.append(task_dico)
    json_obj = {}
    json_obj[userId] = completed_tasks
    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(json_obj, jsonfile)
