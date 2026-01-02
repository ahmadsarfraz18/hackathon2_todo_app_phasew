# CLI Interface Contract: todo-cli-core

## Menu Structure

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

Enter your choice (1-6): _
```

## Input/Output Contracts

### Menu Selection

**Input Format**: Integer (1-6)

**Valid Inputs**:
- `1` → List all tasks
- `2` → Add a new task
- `3` → Update a task
- `4` → Delete a task
- `5` → Mark task as complete
- `6` → Exit application

**Error Outputs**:
- Invalid number: `"Invalid choice. Please enter a number between 1 and 6."`
- Non-numeric input: `"Please enter a valid number."`
- Empty input: `"Please enter a choice."`

---

### List Tasks (Option 1)

**Input**: None (after selection)

**Success Output**:
```
ID | Status       | Title
---+--------------+------------------
1  | [pending]    | Buy groceries
2  | [completed]  | Call dentist
3  | [in_progress]| Finish report
```

**Empty State Output**:
```
No tasks found.
Add a task using option 2.
```

---

### Add Task (Option 2)

**Input Prompts**:
```
Enter task title: _
Enter task description (optional): _
```

**Validation Rules**:
- Title must not be empty after trimming
- Title max 1000 characters

**Success Output**:
```
Task added successfully!
Task #1: "Buy groceries"
```

**Error Outputs**:
- Empty title: `"Error: Task title cannot be empty."`
- Title too long: `"Error: Task title exceeds maximum length of 1000 characters."`

---

### Update Task (Option 3)

**Input Prompts**:
```
Enter task ID to update: _
Enter new title (leave empty to keep current): _
Enter new description (leave empty to keep current): _
```

**Validation Rules**:
- Task ID must exist
- New title must not be empty (if provided)
- New title max 1000 characters (if provided)

**Success Output**:
```
Task updated successfully!
Task #1: "Buy groceries" - "Milk, bread, eggs"
```

**Error Outputs**:
- Invalid ID format: `"Error: Please enter a valid task ID."`
- Task not found: `"Error: Task with ID 99 not found."`
- Empty title: `"Error: Task title cannot be empty."`

---

### Delete Task (Option 4)

**Input Prompt**:
```
Enter task ID to delete: _
```

**Validation Rules**:
- Task ID must exist

**Success Output**:
```
Task #1 deleted successfully.
```

**Error Outputs**:
- Invalid ID format: `"Error: Please enter a valid task ID."`
- Task not found: `"Error: Task with ID 99 not found."`

---

### Mark Task as Complete (Option 5)

**Input Prompt**:
```
Enter task ID to mark as complete: _
```

**Validation Rules**:
- Task ID must exist

**Success Output**:
```
Task #1 marked as completed!
```

**Error Outputs**:
- Invalid ID format: `"Error: Please enter a valid task ID."`
- Task not found: `"Error: Task with ID 99 not found."`

---

### Exit (Option 6)

**Output**:
```
Goodbye!
```

**Behavior**: Application terminates with exit code 0.

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Successful execution |
| 1 | General error |

## Session Flow

```
Start
  │
  ▼
Display Menu
  │
  ├─► 1 → List Tasks → Back to Menu
  │
  ├─► 2 → Add Task → Success/Error → Back to Menu
  │
  ├─► 3 → Update Task → Success/Error → Back to Menu
  │
  ├─► 4 → Delete Task → Success/Error → Back to Menu
  │
  ├─► 5 → Mark Complete → Success/Error → Back to Menu
  │
  └─► 6 → Exit → Goodbye → END
```

## Status Display Format

| Status | Display |
|--------|---------|
| pending | `[pending]` or `[ ]` |
| in_progress | `[in_progress]` or `[%]` |
| completed | `[completed]` or `[x]` |
