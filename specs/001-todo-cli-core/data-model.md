# Data Model: todo-cli-core

## Task Entity

### Overview

The Task entity represents a single todo item in the in-memory task list.

### Class Definition

```python
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class TaskStatus(Enum):
    """Enumeration of possible task states."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


@dataclass
class Task:
    """
    Represents a single task in the todo list.

    Attributes:
        id: Unique identifier, auto-assigned on creation.
        title: Short description of the task (required).
        description: Optional detailed information about the task.
        status: Current state of the task (default: pending).
        created_at: Timestamp when the task was created.
        updated_at: Timestamp when the task was last modified.
    """

    title: str
    description: str = ""
    status: TaskStatus = TaskStatus.PENDING
    id: int = 0  # Set by TaskStore
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """Validate and normalize task data after initialization."""
        self.title = self.title.strip()
        self.description = self.description.strip()
        self._validate()

    def _validate(self) -> None:
        """Validate task state. Raises ValueError if invalid."""
        if not self.title:
            raise ValueError("Task title cannot be empty")
        if len(self.title) > 1000:
            raise ValueError("Task title exceeds maximum length of 1000 characters")

    def update_timestamp(self) -> None:
        """Update the updated_at timestamp to current time."""
        self.updated_at = datetime.now()
```

### Field Specifications

| Field | Type | Required | Default | Validation |
|-------|------|----------|---------|------------|
| id | int | No (auto) | 0 | Must be unique in TaskStore |
| title | str | Yes | N/A | Not empty, max 1000 chars |
| description | str | No | "" | Max 10000 chars (optional) |
| status | TaskStatus | No | PENDING | Valid enum value |
| created_at | datetime | No | now() | Valid datetime |
| updated_at | datetime | No | now() | Valid datetime |

### Status Transitions

```text
PENDING ──────► IN_PROGRESS ──────► COMPLETED
    │               │                   │
    │               │                   │
    └─────► COMPLETED ◄─────────────────┘
```

**Valid Transitions**:
- PENDING → IN_PROGRESS (start working)
- PENDING → COMPLETED (complete without starting)
- IN_PROGRESS → COMPLETED (finish working)
- IN_PROGRESS → PENDING (pause work, optional)
- COMPLETED → IN_PROGRESS (reopen, optional)

**Invalid Transitions**:
- PENDING → PENDING (self-loop)
- COMPLETED → COMPLETED (self-loop)

## TaskStore Service

### Overview

The TaskStore class manages in-memory task storage and CRUD operations.

### Class Definition

```python
from typing import Optional


class TaskStore:
    """
    Manages in-memory storage for tasks.

    Provides thread-safe (optional) CRUD operations for task management.
    All operations are O(n) for list operations except where noted.
    """

    def __init__(self) -> None:
        """Initialize an empty task store with auto-incrementing ID."""
        self._tasks: list[Task] = []
        self._next_id: int = 1

    def add(self, task: Task) -> Task:
        """
        Add a new task to the store.

        Args:
            task: Task instance to add (id will be set automatically).

        Returns:
            The added task with assigned ID.

        Raises:
            ValueError: If task validation fails.
        """
        task.id = self._next_id
        self._next_id += 1
        self._tasks.append(task)
        return task

    def get(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by ID.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            Task if found, None otherwise.
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def get_all(self) -> list[Task]:
        """
        Retrieve all tasks.

        Returns:
            List of all tasks in creation order.
        """
        return list(self._tasks)

    def update(self, task_id: int, **kwargs: str | None) -> Optional[Task]:
        """
        Update an existing task.

        Args:
            task_id: The unique identifier of the task.
            kwargs: Field updates (title, description, status).

        Returns:
            Updated task if found, None otherwise.
        """
        task = self.get(task_id)
        if task is None:
            return None

        if "title" in kwargs and kwargs["title"] is not None:
            task.title = kwargs["title"]
        if "description" in kwargs and kwargs["description"] is not None:
            task.description = kwargs["description"]
        if "status" in kwargs and kwargs["status"] is not None:
            task.status = kwargs["status"]

        task.update_timestamp()
        return task

    def delete(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            True if deleted, False if not found.
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                return True
        return False

    def count(self) -> int:
        """Return the number of tasks in the store."""
        return len(self._tasks)

    def clear(self) -> None:
        """Remove all tasks from the store (for testing)."""
        self._tasks.clear()
        self._next_id = 1
```

### TaskStore Performance

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| add() | O(1) amortized | O(1) |
| get() | O(n) | O(1) |
| get_all() | O(n) | O(n) |
| update() | O(n) | O(1) |
| delete() | O(n) | O(1) |
| count() | O(1) | O(1) |

## Validation Rules

### Title Validation

```python
def validate_title(title: str) -> str:
    """
    Validate and normalize task title.

    Args:
        title: Raw title input from user.

    Returns:
        Trimmed and validated title.

    Raises:
        ValueError: If title is empty or too long.
    """
    trimmed = title.strip()
    if not trimmed:
        raise ValueError("Task title cannot be empty")
    if len(trimmed) > 1000:
        raise ValueError("Task title exceeds maximum length of 1000 characters")
    return trimmed
```

### ID Validation

```python
def validate_task_id(task_id: str) -> int:
    """
    Validate and parse task ID from user input.

    Args:
        task_id: Raw input string from user.

    Returns:
        Parsed integer task ID.

    Raises:
        ValueError: If ID is invalid.
    """
    try:
        value = int(task_id.strip())
        if value <= 0:
            raise ValueError("Task ID must be a positive integer")
        return value
    except ValueError as e:
        if "invalid literal for int" in str(e):
            raise ValueError("Task ID must be a number")
        raise
```
