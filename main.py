import json
import os
from datetime import datetime


filename = 'todo_list.json'

def load_todo_list():
    if not os.path.exists(filename):
        todo_list = []
        with open(filename, 'w') as f:
            json.dump(todo_list, f)
        return todo_list
    with open(filename, 'r') as f:
        return json.load(f)

def save_todo_list(todo_list):
    with open(filename, 'w') as f:
        json.dump(todo_list, f)

def add_todo(todo_list):
    task = input("Enter the task: ")
    added_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    scheduled_time = input("Enter the scheduled time (YYYY-MM-DD HH:MM:SS): ")
    todo_item = {
        'task': task,
        'added_time': added_time,
        'scheduled_time': scheduled_time
    }
    todo_list.append(todo_item)
    save_todo_list(todo_list)
    view_todo(todo_list)

def delete_task(todo_list):
    index = int(input("Enter the index of the task to delete: "))
    del todo_list[index - 1]
    save_todo_list(todo_list)
    view_todo(todo_list)

def view_todo(todo_list):
    for i, item in enumerate(todo_list):
        print(f"\tTask {i+1}: {item['task']}")
        print(f"\tAdded Time: {item['added_time']}")
        print(f"\tScheduled Time: {item['scheduled_time']}")

if __name__ == '__main__':
    todo_list = load_todo_list()
    view_todo(todo_list)
    while True:
        choice = input("Enter 'a' to add a task, 'd' to delete a task, 'v' to view the To Do list, 'q' to quit: ")
        if choice == 'a':
            add_todo(todo_list)
        elif choice == 'v':
            view_todo(todo_list)
        elif choice == 'd':
            delete_task(todo_list)
        elif choice == 'q':
            break
