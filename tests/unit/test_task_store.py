"""Unit tests for the TaskStore service."""

import pytest
from src.models.task import Task, TaskStatus
from src.services.task_store import TaskStore


class TestTaskStoreCreation:
    """Tests for TaskStore initialization."""

    def test_initial_state_is_empty(self) -> None:
        """Test that a new TaskStore is empty."""
        store = TaskStore()
        assert store.count() == 0
        assert store.get_all() == []

    def test_next_id_starts_at_1(self) -> None:
        """Test that the first task gets ID 1."""
        store = TaskStore()
        task = Task(title="Test")
        result = store.add(task)
        assert result.id == 1


class TestTaskStoreAdd:
    """Tests for TaskStore.add() method."""

    def test_add_task_returns_task_with_id(self) -> None:
        """Test that add returns task with assigned ID."""
        store = TaskStore()
        task = Task(title="Test task")
        result = store.add(task)

        assert result.id == 1
        assert result.title == "Test task"

    def test_add_multiple_tasks_increments_ids(self) -> None:
        """Test that adding multiple tasks increments IDs."""
        store = TaskStore()
        task1 = store.add(Task(title="Task 1"))
        task2 = store.add(Task(title="Task 2"))
        task3 = store.add(Task(title="Task 3"))

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

    def test_add_task_stores_in_list(self) -> None:
        """Test that added task is stored in the list."""
        store = TaskStore()
        task = Task(title="Test task")
        store.add(task)

        assert store.count() == 1
        assert store.get(1) is not None


class TestTaskStoreGet:
    """Tests for TaskStore.get() method."""

    def test_get_existing_task_returns_task(self) -> None:
        """Test that getting an existing task returns it."""
        store = TaskStore()
        added = store.add(Task(title="Test"))
        result = store.get(added.id)

        assert result is not None
        assert result.title == "Test"

    def test_get_non_existent_task_returns_none(self) -> None:
        """Test that getting a non-existent task returns None."""
        store = TaskStore()
        result = store.get(999)

        assert result is None

    def test_get_all_returns_all_tasks(self) -> None:
        """Test that get_all returns all tasks."""
        store = TaskStore()
        store.add(Task(title="Task 1"))
        store.add(Task(title="Task 2"))
        store.add(Task(title="Task 3"))

        all_tasks = store.get_all()
        assert len(all_tasks) == 3


class TestTaskStoreUpdate:
    """Tests for TaskStore.update() method."""

    def test_update_title(self) -> None:
        """Test updating task title."""
        store = TaskStore()
        task = store.add(Task(title="Original"))
        result = store.update(task.id, title="Updated")

        assert result is not None
        assert result.title == "Updated"

    def test_update_description(self) -> None:
        """Test updating task description."""
        store = TaskStore()
        task = store.add(Task(title="Test"))
        result = store.update(task.id, description="New description")

        assert result is not None
        assert result.description == "New description"

    def test_update_status(self) -> None:
        """Test updating task status."""
        store = TaskStore()
        task = store.add(Task(title="Test"))
        result = store.update(task.id, status=TaskStatus.COMPLETED)

        assert result is not None
        assert result.status == TaskStatus.COMPLETED

    def test_update_multiple_fields(self) -> None:
        """Test updating multiple fields at once."""
        store = TaskStore()
        task = store.add(Task(title="Test", description="Original"))
        result = store.update(
            task.id,
            title="New Title",
            description="New Description",
        )

        assert result is not None
        assert result.title == "New Title"
        assert result.description == "New Description"

    def test_update_non_existent_returns_none(self) -> None:
        """Test that updating non-existent task returns None."""
        store = TaskStore()
        result = store.update(999, title="New")

        assert result is None

    def test_update_timestamp_changes(self) -> None:
        """Test that update changes the updated_at timestamp."""
        store = TaskStore()
        task = store.add(Task(title="Test"))
        original_updated = task.updated_at

        store.update(task.id, title="Updated")

        assert task.updated_at > original_updated


class TestTaskStoreDelete:
    """Tests for TaskStore.delete() method."""

    def test_delete_existing_task_returns_true(self) -> None:
        """Test that deleting an existing task returns True."""
        store = TaskStore()
        task = store.add(Task(title="Test"))
        result = store.delete(task.id)

        assert result is True
        assert store.count() == 0

    def test_delete_non_existent_returns_false(self) -> None:
        """Test that deleting non-existent task returns False."""
        store = TaskStore()
        result = store.delete(999)

        assert result is False

    def test_delete_one_task_keeps_others(self) -> None:
        """Test that deleting one task keeps other tasks."""
        store = TaskStore()
        task1 = store.add(Task(title="Task 1"))
        task2 = store.add(Task(title="Task 2"))
        store.delete(task1.id)

        remaining = store.get_all()
        assert len(remaining) == 1
        assert remaining[0].id == task2.id


class TestTaskStoreCount:
    """Tests for TaskStore.count() method."""

    def test_count_empty_store(self) -> None:
        """Test count returns 0 for empty store."""
        store = TaskStore()
        assert store.count() == 0

    def test_count_reflects_added_tasks(self) -> None:
        """Test count reflects number of added tasks."""
        store = TaskStore()
        store.add(Task(title="Task 1"))
        store.add(Task(title="Task 2"))
        store.add(Task(title="Task 3"))

        assert store.count() == 3

    def test_count_after_delete(self) -> None:
        """Test count decreases after delete."""
        store = TaskStore()
        task = store.add(Task(title="Task"))
        store.delete(task.id)

        assert store.count() == 0


class TestTaskStoreClear:
    """Tests for TaskStore.clear() method."""

    def test_clear_removes_all_tasks(self) -> None:
        """Test that clear removes all tasks."""
        store = TaskStore()
        store.add(Task(title="Task 1"))
        store.add(Task(title="Task 2"))

        store.clear()

        assert store.count() == 0

    def test_clear_resets_next_id(self) -> None:
        """Test that clear resets the next ID counter."""
        store = TaskStore()
        store.add(Task(title="Task"))
        store.clear()

        task = store.add(Task(title="New task"))
        assert task.id == 1


class TestTaskStoreGetByStatus:
    """Tests for TaskStore.get_by_status() method."""

    def test_get_by_status_returns_matching_tasks(self) -> None:
        """Test that get_by_status returns tasks with matching status."""
        store = TaskStore()
        store.add(Task(title="Pending 1", status=TaskStatus.PENDING))
        store.add(Task(title="Pending 2", status=TaskStatus.PENDING))
        store.add(Task(title="Completed", status=TaskStatus.COMPLETED))

        pending = store.get_by_status(TaskStatus.PENDING)
        assert len(pending) == 2
        assert all(t.status == TaskStatus.PENDING for t in pending)

    def test_get_by_status_returns_empty_list_for_no_matches(self) -> None:
        """Test that get_by_status returns empty list when no matches."""
        store = TaskStore()
        store.add(Task(title="Task", status=TaskStatus.PENDING))

        completed = store.get_by_status(TaskStatus.COMPLETED)
        assert completed == []
