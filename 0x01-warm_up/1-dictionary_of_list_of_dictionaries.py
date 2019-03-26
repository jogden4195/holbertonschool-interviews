#!/usr/bin/python3
""" Module for gathering employee information """
import requests
import json


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    mega_dict = {}

    # Getting employees
    employees = requests.get(url + 'users/')
    e_json = employees.json()

    # Getting all employees' tasks
    todos = requests.get(url + 'todos/')
    todos_dicts = todos.json()

    # Create a dict of list of dict for all employees
    for e in e_json:
        mega_tasks = []
        eid = e['id']
        un = e['username']
        e_todos = [i for i in todos_dicts if i['userId'] == int(eid)]
        for t in e_todos:
            t_dict = {}
            t_dict['username'] = un
            t_dict['task'] = t['title']
            t_dict['completed'] = t['completed']
            mega_tasks.append(t_dict)
        mega_dict[str(e['id'])] = mega_tasks

    # Save mega_dict to a json file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(mega_dict, f)
