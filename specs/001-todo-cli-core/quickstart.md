# Quickstart: todo-cli-core

## Prerequisites

- Python 3.13 or higher
- No external dependencies (standard library only)

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd todo-app

# Navigate to project directory (if not at root)
cd specs/001-todo-cli-core/../../

# Verify Python version
python --version  # Should be 3.13+
```

## Running the Application

```bash
# From the project root directory
python main.py

# Or with explicit path
python src/main.py
```

## Usage Example

```
========================================
          Todo Application
========================================

1. List all tasks
2. Add a new task
3. Update a task
4. Delete a task
5. Mark task as complete
6. Exit

Enter your choice (1-6): 2
Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs

Task added successfully!

========================================
          Todo Application
========================================

1. List all tasks
2. Add a new task
3. Update a task
4. Delete a task
5. Mark task as complete
6. Exit

Enter your choice (1-6): 1

ID | Status       | Title
---+--------------+------------------
1  | [pending]    | Buy groceries

Enter your choice (1-6): 5
Enter task ID to mark as complete: 1

Task #1 marked as completed!

Enter your choice (1-6): 6
Goodbye!
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run unit tests only
python -m pytest tests/unit/ -v

# Run integration tests only
python -m pytest tests/integration/ -v

# Run with unittest (if pytest not available)
python -m unittest discover tests/
```

## Project Structure

```
todo-app/
├── src/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py          # Task dataclass
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_store.py    # Task storage service
│   └── cli/
│       ├── __init__.py
│       ├── menu.py          # Menu interface
│       └── prompts.py       # Input validation
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── test_task.py
│   │   ├── test_task_store.py
│   │   └── test_prompts.py
│   └── integration/
│       └── test_cli_flow.py
├── specs/001-todo-cli-core/
│   ├── spec.md
│   ├── plan.md
│   ├── data-model.md
│   └── contracts/
│       └── cli-interface.md
└── requirements.txt          # Empty (stdlib only)
```

## Code Quality

This project follows these standards:

- **PEP 8** compliance
- **Type hints** on all functions
- **Docstrings** on all public functions
- **Tests** for all public APIs

```bash
# Check PEP 8 compliance
pip install pycodestyle
pycodestyle src/ tests/

# Type checking (if mypy available)
pip install mypy
mypy src/
```
