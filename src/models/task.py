"""Task entity and TaskStatus enum for todo application."""

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

    def __repr__(self) -> str:
        """Return string representation of the task."""
        return (
            f"Task(id={self.id}, title={self.title!r}, "
            f"status={self.status.value}, description={self.description!r})"
        )
