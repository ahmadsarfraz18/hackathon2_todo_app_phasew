# Research: todo-cli-core

## Overview

Research findings for the todo-cli-core implementation based on Phase I constraints and Python 3.13+ standard library.

## Python 3.13+ Standard Library Choices

### Data Classes vs Named Tuples vs Dataclasses

**Decision**: Use `@dataclass` decorator

**Rationale**:
- Type hints are fully supported with `@dataclass`
- Auto-generated `__init__`, `__repr__`, `__eq__`
- Field defaults are straightforward
- Better IDE support and readability

**Alternatives considered**:
- NamedTuple: Less flexible, harder to modify
- TypedDict: No runtime validation
- Plain class: Too much boilerplate

### datetime vs time vs dataclasses

**Decision**: Use `datetime.datetime` for timestamps

**Rationale**:
- Built-in timezone support if needed later
- Easy formatting and comparison
- ISO 8601 format compatible

### In-Memory Storage

**Decision**: Use `list[Task]` with integer ID counter

**Rationale**:
- Simple, no external dependencies
- O(1) append, O(n) search by ID
- ID generation: max + 1 strategy

**Alternatives considered**:
- dict[int, Task]: O(1) lookup but same storage
- UUID: Overkill for single-user local app

### Input Validation

**Decision**: Standard library `input()` with manual validation

**Rationale**:
- No third-party libraries allowed in Phase I
- Custom validation provides better error messages
- Consistent with constitution constraints

## CLI Design Patterns

### Menu-Driven Interface

**Decision**: Numbered menu with input() loop

**Pattern**:
```python
while True:
    display_menu()
    choice = get_input()
    if choice == 5:  # Exit
        break
    route_to_handler(choice)
```

### Error Handling

**Decision**: Use ValueError with user-friendly messages

**Rationale**:
- Pythonic exception handling
- Easy to catch and display
- No external error handling libraries needed

## PEP 8 and Type Hints Compliance

### Type Hints Strategy

- All function signatures include type annotations
- Return types specified for all public functions
- Use `None` for optional return values
- Use `dataclasses.field(default=...)` for defaults

### Docstring Format

- Google-style docstrings
- Args, Returns, Raises sections
- Example usage for complex functions

## Code Organization

### Package Structure

```
src/
├── models/     # Data classes (Task)
├── services/   # Business logic (TaskStore)
├── cli/        # User interaction (menu, prompts)
└── main.py     # Entry point
```

**Rationale**:
- Clear separation of concerns
- Easy to test each layer
- Reusable across phases

### Circular Import Prevention

- models/ imports nothing
- services/ imports from models/
- cli/ imports from services/
- main.py imports from cli/

## Testing Approach

### pytest vs unittest

**Decision**: pytest (if available) with unittest fallback

**Rationale**:
- pytest is widely used and installed
- unittest is in stdlib as fallback
- Constitution allows both

### Test Categories

- **Unit tests**: Task dataclass, TaskStore methods
- **Integration tests**: CLI menu flow
- **No contract tests**: No API endpoints in Phase I

## Summary

All technical decisions align with Phase I constraints:
- Python 3.13+ stdlib only
- No file I/O
- No database
- In-memory storage
- Menu-driven CLI
