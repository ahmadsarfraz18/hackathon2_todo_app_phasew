"""Unit tests for the Task dataclass."""

import pytest
from datetime import datetime

from src.models.task import Task, TaskStatus


class TestTaskStatus:
    """Tests for TaskStatus enum."""

    def test_status_values(self) -> None:
        """Test that all status values are correct."""
        assert TaskStatus.PENDING.value == "pending"
        assert TaskStatus.IN_PROGRESS.value == "in_progress"
        assert TaskStatus.COMPLETED.value == "completed"

    def test_status_enum_members(self) -> None:
        """Test that enum has all expected members."""
        members = list(TaskStatus)
        assert len(members) == 3
        assert TaskStatus.PENDING in members
        assert TaskStatus.IN_PROGRESS in members
        assert TaskStatus.COMPLETED in members


class TestTaskCreation:
    """Tests for Task creation."""

    def test_create_task_with_title_only(self) -> None:
        """Test creating a task with only a title."""
        task = Task(title="Test task")
        assert task.title == "Test task"
        assert task.description == ""
        assert task.status == TaskStatus.PENDING
        assert task.id == 0
        assert isinstance(task.created_at, datetime)
        assert isinstance(task.updated_at, datetime)

    def test_create_task_with_all_fields(self) -> None:
        """Test creating a task with all fields."""
        task = Task(
            title="Buy groceries",
            description="Milk, bread, eggs",
            status=TaskStatus.IN_PROGRESS,
            id=5,
        )
        assert task.title == "Buy groceries"
        assert task.description == "Milk, bread, eggs"
        assert task.status == TaskStatus.IN_PROGRESS
        assert task.id == 5

    def test_default_status_is_pending(self) -> None:
        """Test that default status is PENDING."""
        task = Task(title="Test")
        assert task.status == TaskStatus.PENDING


class TestTaskValidation:
    """Tests for Task validation."""

    def test_empty_title_raises_error(self) -> None:
        """Test that empty title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            Task(title="")

    def test_whitespace_only_title_raises_error(self) -> None:
        """Test that whitespace-only title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            Task(title="   ")

    def test_title_trimmed(self) -> None:
        """Test that title is trimmed."""
        task = Task(title="  Test task  ")
        assert task.title == "Test task"

    def test_description_trimmed(self) -> None:
        """Test that description is trimmed."""
        task = Task(title="Test", description="  Test description  ")
        assert task.description == "Test description"

    def test_title_max_length_1000(self) -> None:
        """Test that title longer than 1000 characters raises error."""
        long_title = "a" * 1001
        with pytest.raises(ValueError, match="Task title exceeds maximum length"):
            Task(title=long_title)

    def test_title_exactly_1000_characters_allowed(self) -> None:
        """Test that title of exactly 1000 characters is allowed."""
        title = "a" * 1000
        task = Task(title=title)
        assert len(task.title) == 1000


class TestTaskTimestampUpdate:
    """Tests for task timestamp updates."""

    def test_update_timestamp_changes_value(self) -> None:
        """Test that update_timestamp changes the updated_at value."""
        task = Task(title="Test")
        original_updated_at = task.updated_at

        # Small delay to ensure different timestamp
        task.update_timestamp()

        assert task.updated_at > original_updated_at

    def test_created_at_not_changed_by_update(self) -> None:
        """Test that update_timestamp does not change created_at."""
        task = Task(title="Test")
        original_created_at = task.created_at

        task.update_timestamp()

        assert task.created_at == original_created_at


class TestTaskRepr:
    """Tests for Task string representation."""

    def test_repr_contains_task_info(self) -> None:
        """Test that repr contains relevant task information."""
        task = Task(title="Test task", id=1, status=TaskStatus.PENDING)
        repr_str = repr(task)

        assert "Task" in repr_str
        assert "id=1" in repr_str
        assert "Test task" in repr_str
        assert "pending" in repr_str


class TestTaskEquality:
    """Tests for Task equality."""

    def test_tasks_with_same_data_are_equal(self) -> None:
        """Test that tasks with same data are equal (ignoring timestamps)."""
        # Create tasks with same explicit timestamps
        now = datetime.now()
        task1 = Task(title="Test", id=1, created_at=now, updated_at=now)
        task2 = Task(title="Test", id=1, created_at=now, updated_at=now)

        assert task1 == task2

    def test_different_tasks_are_not_equal(self) -> None:
        """Test that tasks with different data are not equal."""
        task1 = Task(title="Test1", id=1)
        task2 = Task(title="Test2", id=1)

        assert task1 != task2

    def test_same_instance_is_equal(self) -> None:
        """Test that a task is equal to itself."""
        task = Task(title="Test")
        assert task == task

    def test_different_ids_are_not_equal(self) -> None:
        """Test that tasks with different IDs are not equal."""
        task1 = Task(title="Test", id=1)
        task2 = Task(title="Test", id=2)

        assert task1 != task2
