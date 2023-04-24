#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests

def get_employee_todo_progress(employee_id):
    """
    Fetches the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The employee ID for which to fetch the TODO list progress.

    Returns:
        None
    """
    # Make GET request to fetch employee data
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = response.json()

    # Make GET request to fetch employee's TODO list
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_data = response.json()

    # Extract TODO list progress
    total_tasks = len(todo_data)
    done_tasks = sum(todo['completed'] for todo in todo_data)

    # Display TODO list progress
    print(f"Employee {employee_data['name']} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todo_data:
        if todo['completed']:
            print("\t", todo['title'])

# Accept employee ID as input
employee_id = int(input("Enter employee ID: "))
get_employee_todo_progress(employee_id)
