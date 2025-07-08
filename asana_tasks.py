import os
import asana
from asana.rest import ApiException

# Get Asana Personal Access Token from environment variable
ASANA_TOKEN = os.getenv('ASANA_TOKEN')
if not ASANA_TOKEN:
    print("Error: Please set your Asana Personal Access Token in the ASANA_TOKEN environment variable.")
    exit(1)

# Configure Asana API client (v5+)
configuration = asana.Configuration()
configuration.access_token = ASANA_TOKEN
api_client = asana.ApiClient(configuration)
tasks_api = asana.TasksApi(api_client)

def create_task():
    workspace_id = input("Enter Workspace ID: ").strip()
    project_id = input("Enter Project ID: ").strip()
    name = input("Enter Task Name: ").strip()
    notes = input("Enter Task Notes: ").strip()
    assignee = input("Enter Assignee: ").strip()
    try:
        result = tasks_api.create_task(
            body={
                'workspace': workspace_id,
                'projects': [project_id],
                'name': name,
                'notes': notes,
                'assignee': assignee,
            },
            opts={}
        )
        print("Task created:", result['gid'])
    except ApiException as e:
        print(f"Exception when creating task: {e}")

def read_task():
    task_id = input("Enter Task ID: ")
    try:
        result = tasks_api.get_task(task_id, opts={})
        print("Task details:")
        for k, v in result.items():
            print(f"{k}: {v}")
    except ApiException as e:
        print(f"Exception when reading task: {e}")

def update_task():
    task_id = input("Enter Task ID: ")
    name = input("Enter new Task Name (leave blank to keep unchanged): ")
    notes = input("Enter new Task Notes (leave blank to keep unchanged): ")
    data = {}
    if name:
        data['name'] = name
    if notes:
        data['notes'] = notes
    if not data:
        print("Nothing to update.")
        return
    try:
        result = tasks_api.update_task(task_id, data, opts={})
        print("Task updated:", result['gid'])
    except ApiException as e:
        print(f"Exception when updating task: {e}")

def delete_task():
    task_id = input("Enter Task ID: ")
    try:
        tasks_api.delete_task(task_id)
        print("Task deleted:", task_id)
    except ApiException as e:
        print(f"Exception when deleting task: {e}")

def main():
    while True:
        print("\nAsana Task CRUD CLI")
        print("1. Create Task")
        print("2. Read Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            create_task()
        elif choice == '2':
            read_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main() 