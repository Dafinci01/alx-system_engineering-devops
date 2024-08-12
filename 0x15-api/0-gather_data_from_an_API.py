#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the API endpoint
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        # Make a GET request to the API
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()
        # Parse the JSON response
        todos = response.json()
        
        # Calculate the number of completed and total tasks
        completed_tasks = [todo['title'] for todo in todos if todo['completed']]
        total_tasks = len(todos)
        number_of_done_tasks = len(completed_tasks)
        
        # Get employee name
        employee_name = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()['name']
        
        # Display the results
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for employee ID.")

