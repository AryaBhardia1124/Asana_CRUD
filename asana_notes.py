import os
import argparse
import asana

# Get Asana Personal Access Token from environment variable
ASANA_TOKEN = os.getenv('ASANA_TOKEN')
if not ASANA_TOKEN:
    print("Error: Please set your Asana Personal Access Token in the ASANA_TOKEN environment variable.")
    exit(1)

client = asana.Client.access_token(ASANA_TOKEN)

# CREATE (with notes)
def create_task_with_notes(workspace_id, project_id, name, notes):
    result = client.tasks.create_task({
        'workspace': workspace_id,
        'projects': [project_id],
        'name': name,
        'notes': notes
    })
    print("Task created:", result['gid'])
    return result

# READ notes
def read_notes(task_id):
    result = client.tasks.get_task(task_id, fields=['notes'])
    print("Task notes:")
    print(result.get('notes', ''))
    return result.get('notes', '')

# UPDATE notes
def update_notes(task_id, notes):
    result = client.tasks.update_task(task_id, {'notes': notes})
    print("Notes updated for task:", result['gid'])
    return result

# DELETE notes (clear notes field)
def clear_notes(task_id):
    result = client.tasks.update_task(task_id, {'notes': ''})
    print("Notes cleared for task:", result['gid'])
    return result


def main():
    parser = argparse.ArgumentParser(description='Asana Task Notes CRUD CLI')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Create
    parser_create = subparsers.add_parser('create', help='Create a new task with notes')
    parser_create.add_argument('--workspace', required=True, help='Workspace ID')
    parser_create.add_argument('--project', required=True, help='Project ID')
    parser_create.add_argument('--name', required=True, help='Task name')
    parser_create.add_argument('--notes', default='', help='Task notes')

    # Read
    parser_read = subparsers.add_parser('read', help='Read notes of a task')
    parser_read.add_argument('--id', required=True, help='Task ID')

    # Update
    parser_update = subparsers.add_parser('update', help='Update notes of a task')
    parser_update.add_argument('--id', required=True, help='Task ID')
    parser_update.add_argument('--notes', required=True, help='New notes')

    # Delete (clear notes)
    parser_delete = subparsers.add_parser('delete', help='Clear notes of a task')
    parser_delete.add_argument('--id', required=True, help='Task ID')

    args = parser.parse_args()

    if args.command == 'create':
        create_task_with_notes(args.workspace, args.project, args.name, args.notes)
    elif args.command == 'read':
        read_notes(args.id)
    elif args.command == 'update':
        update_notes(args.id, args.notes)
    elif args.command == 'delete':
        clear_notes(args.id)

if __name__ == '__main__':
    main() 