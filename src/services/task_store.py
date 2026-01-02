"""TaskStore service for in-memory task storage and CRUD operations."""

from typing import Optional

from src.models.task import Task, TaskStatus


class TaskStore:
    """
    Manages in-memory storage for tasks.

    Provides CRUD operations for task management.
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

    def update(
        self,
        task_id: int,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[TaskStatus] = None,
    ) -> Optional[Task]:
        """
        Update an existing task.

        Args:
            task_id: The unique identifier of the task.
            title: New title for the task (optional).
            description: New description for the task (optional).
            status: New status for the task (optional).

        Returns:
            Updated task if found, None otherwise.
        """
        task = self.get(task_id)
        if task is None:
            return None

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if status is not None:
            task.status = status

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

    def get_by_status(self, status: TaskStatus) -> list[Task]:
        """
        Retrieve all tasks with the given status.

        Args:
            status: The TaskStatus to filter by.

        Returns:
            List of tasks with the specified status.
        """
        return [task for task in self._tasks if task.status == status]
