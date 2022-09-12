#!/usr/bin/python3
"""Python script to export data in the CSV format"""

from sys import argv
import requests
import csv


if __name__ == "__main__":
    userId = int(argv[1])
    user = ('https://jsonplaceholder.typicode.com/users/{}'.format(userId))
    todo = ('{}/todos/'.format(user))
    json_user = requests.get(user).json()
    json_todo = requests.get(todo).json()
    completed_tasks = []
    file_name = "{}.csv".format(userId)

    with open(file_name, 'w', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for task in json_todo:
            csv_writer.writerow(
                [userId, json_user.get('name'),
                    task.get('completed'), task.get('title')])
