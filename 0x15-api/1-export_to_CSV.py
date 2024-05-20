#!/usr/bin/python3
"""Module contains function to gather data from API"""
import csv
import requests
import sys


def gather_employee_todo_progress(employee_id):
    """gathers API data"""
    try:
        # Get employee details
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()
        if 'name' not in user_data:
            print(f"No employee found with ID {employee_id}")
            return

        employee_name = user_data['name']

        # Get TODO list for the employee
        todos_url = f"https://jsonplaceholder.typicode.com/todos?\
                                    userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Calculate the number of completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]
        number_of_done_tasks = len(completed_tasks)

        # Display the results
        print(f"Employee {employee_name} is done with tasks\
        ({number_of_done_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            csv_writer.writerow([employee_id, employee_name,
                                 task['completed'], task['title']])
    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        gather_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
