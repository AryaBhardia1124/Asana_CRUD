import asana
import os

# Replace with your personal access token
ASANA_TOKEN = os.getenv('ASANA_TOKEN')

# Replace with your workspace and project IDs
workspace_id = "your_workspace_id"
project_id = "your_project_id"

# Initialize client
client = asana.Client.access_token(ASANA_TOKEN)

# Optional: set to True to see HTTP requests
client.options['log_asana_change_warnings'] = True

# Create the task
task_data = {
    "name": "Example Task from API",
    "notes": "This task was created using the Asana API via Python.",
    "projects": [1210733564771408],
    "assignee": "me"  # or a user ID/email
}

try:
    result = client.tasks.create_task(task_data, opt_pretty=True)
    print("Task created successfully!")
    print("Task GID:", result['gid'])
    print("Task URL:", result['permalink_url'])
except asana.error.AsanaError as e:
    print("Error creating task:", e)