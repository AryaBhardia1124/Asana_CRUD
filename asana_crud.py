import os
import argparse
import asana

# Get Asana Personal Access Token from environment variable
ASANA_TOKEN = os.getenv('ASANA_TOKEN')
if not ASANA_TOKEN:
    print("Error: Please set your Asana Personal Access Token in the ASANA_TOKEN environment variable.")
    exit(1)

client = asana.Client.access_token(ASANA_TOKEN)

# CREATE
def create_task(workspace_id, project_id, name, notes):
    result = client.tasks.create_task({
        'workspace': workspace_id,
        'projects': [project_id],
        'name': name,
        'notes': notes
    })
    print("Task created:", result['gid'])
    return result

# READ
def read_task(task_id):
    result = client.tasks.get_task(task_id)
    print("Task details:")
    for k, v in result.items():
        print(f"{k}: {v}")
    return result

# UPDATE
def update_task(task_id, name=None, notes=None):
    data = {}
    if name:
        data['name'] = name
    if notes:
        data['notes'] = notes
    if not data:
        print("Nothing to update.")
        return
    result = client.tasks.update_task(task_id, data)
    print("Task updated:", result['gid'])
    return result

# DELETE
def delete_task(task_id):
    client.tasks.delete_task(task_id)
    print("Task deleted:", task_id)


def main():
    parser = argparse.ArgumentParser(description='Asana Task CRUD CLI')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Create
    parser_create = subparsers.add_parser('create', help='Create a new task')
    parser_create.add_argument('--workspace', required=True, help='Workspace ID')
    parser_create.add_argument('--project', required=True, help='Project ID')
    parser_create.add_argument('--name', required=True, help='Task name')
    parser_create.add_argument('--notes', default='', help='Task notes')

    # Read
    parser_read = subparsers.add_parser('read', help='Read a task')
    parser_read.add_argument('--id', required=True, help='Task ID')

    # Update
    parser_update = subparsers.add_parser('update', help='Update a task')
    parser_update.add_argument('--id', required=True, help='Task ID')
    parser_update.add_argument('--name', help='New task name')
    parser_update.add_argument('--notes', help='New task notes')

    # Delete
    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument('--id', required=True, help='Task ID')

    args = parser.parse_args()

    if args.command == 'create':
        create_task(args.workspace, args.project, args.name, args.notes)
    elif args.command == 'read':
        read_task(args.id)
    elif args.command == 'update':
        update_task(args.id, args.name, args.notes)
    elif args.command == 'delete':
        delete_task(args.id)

if __name__ == '__main__':
    main() 