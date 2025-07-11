# Asana CRUD CLI

A command-line interface for managing Asana tasks with full CRUD (Create, Read, Update, Delete) operations.

## Features

- **Create Tasks**: Add new tasks to Asana projects
- **Read Tasks**: View detailed information about existing tasks
- **Update Tasks**: Modify task names and notes
- **Delete Tasks**: Remove tasks from Asana
- **Interactive CLI**: User-friendly menu-driven interface

## Prerequisites

- Python 3.6 or higher
- Asana Personal Access Token
- Valid Asana workspace and project IDs

## Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd Asana_CRUD-main
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Asana Personal Access Token**
   ```bash
   export ASANA_TOKEN="your_personal_access_token_here"
   ```
   
   **To get your Personal Access Token:**
   - Go to your Asana profile settings
   - Navigate to Apps > Manage Developer Apps > Personal Access Tokens
   - Create a new token and copy it

## Usage

### Running the CLI

```bash
python asana_tasks.py
```

### Menu Options

1. **Create Task** - Add a new task to a project
2. **Read Task** - View details of an existing task
3. **Update Task** - Modify task name or notes
4. **Delete Task** - Remove a task
5. **Exit** - Close the application

### Finding Your IDs

**Project ID:**
- Open your project in Asana web app
- Look at the URL: `https://app.asana.com/0/workspace_id/project_id`
- The project ID is the long number after the second slash

**Task ID:**
- Open a task in Asana
- Look at the URL: `https://app.asana.com/0/project_id/task_id`
- The task ID is the long number at the end

**Workspace ID:**
- Open any project in your workspace
- Look at the URL: `https://app.asana.com/0/workspace_id/project_id`
- The workspace ID is the long number after the first slash

## Example Usage

```
Asana Task CRUD CLI
1. Create Task
2. Read Task
3. Update Task
4. Delete Task
5. Exit
Select an option (1-5): 1

Enter Project ID: 1234567890123456
Enter Task Name: Complete project documentation
Enter Assignee: john@example.com
DEBUG: Sending body to Asana: {'name': 'Complete project documentation', 'assignee': 'john@example.com', 'projects': ['1234567890123456']}
Task created: 9876543210987654
```

## Troubleshooting

### Common Issues

1. **"ASANA_TOKEN environment variable not set"**
   - Make sure you've set the environment variable correctly
   - Try: `echo $ASANA_TOKEN` to verify it's set

2. **"You should specify one of workspace, parent, projects"**
   - Ensure you're providing a valid Project ID
   - Double-check that the project exists in your workspace

3. **"Invalid option"**
   - Make sure to enter a number between 1-5
   - Check for extra spaces or characters

4. **Task creation fails**
   - Verify your Personal Access Token has the necessary permissions
   - Ensure the assignee email exists in your Asana workspace
   - Check that the project ID is correct and accessible

### Getting Help

- **Asana API Documentation**: https://developers.asana.com/docs
- **Personal Access Token Guide**: https://developers.asana.com/docs/personal-access-token
- **Python Asana Client**: https://github.com/Asana/python-asana

## File Structure

```
Asana_CRUD-main/
├── asana_tasks.py      # Main CLI script
├── requirements.txt     # Python dependencies
└── README.md          # This documentation
```

## Requirements

- `asana>=3.2.2` - Official Asana Python client library

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this CLI tool.