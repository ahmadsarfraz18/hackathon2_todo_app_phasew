---

description: "Task list for todo-cli-core - In-Memory Python Console App"
---

# Tasks: todo-cli-core

**Constitution Version**: 1.0.0
**Input**: Design documents from `/specs/001-todo-cli-core/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Constitution Compliance

Before starting implementation:
- [x] Spec-Driven Development verified (spec.md exists and reviewed)
- [x] Phase-appropriate constraints identified (stdlib only for Phase I)
- [x] Reusable intelligence design confirmed (skill/agent reusable)
- [x] Code generation mode confirmed (Claude Code will generate)

**Tests**: Unit tests included for core functionality. Integration test for CLI flow.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- All paths relative to repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/
- [X] T002 Create src/__init__.py
- [X] T003 [P] Create src/models/__init__.py
- [X] T004 [P] Create src/services/__init__.py
- [X] T005 [P] Create src/cli/__init__.py
- [X] T006 [P] Create tests/__init__.py
- [X] T007 [P] Create tests/unit/__init__.py
- [X] T008 [P] Create tests/integration/__init__.py
- [X] T009 Create empty requirements.txt with Phase I note

**Checkpoint**: Project structure ready for foundational code

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [X] T010 Create TaskStatus enum in src/models/task.py
- [X] T011 [P] Create Task dataclass in src/models/task.py
- [X] T012 Implement Task validation in __post_init__ in src/models/task.py
- [X] T013 Create TaskStore class in src/services/task_store.py
- [X] T014 [P] Implement add() method in TaskStore
- [X] T015 [P] Implement get() method in TaskStore
- [X] T016 [P] Implement get_all() method in TaskStore
- [X] T017 [P] Implement update() method in TaskStore
- [X] T018 [P] Implement delete() method in TaskStore
- [X] T019 [P] Implement count() method in TaskStore
- [X] T020 Implement unit tests for Task dataclass in tests/unit/test_task.py
- [X] T021 Implement unit tests for TaskStore in tests/unit/test_task_store.py

**Checkpoint**: Foundation ready - Task entity and TaskStore CRUD operations complete

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Users can add new tasks with title and optional description

**Independent Test**: Add a task via prompts, verify task appears in list

- [ ] T022 Create input validation helpers in src/cli/prompts.py
- [ ] T023 [P] Implement validate_title() in src/cli/prompts.py
- [ ] T024 [P] Implement validate_task_id() in src/cli/prompts.py
- [ ] T025 Create add task prompts in src/cli/prompts.py
- [ ] T026 Implement CLI handler for add operation in src/cli/menu.py
- [ ] T027 Add add_task_to_list() function in src/cli/menu.py
- [ ] T028 [P] Add unit tests for prompts validation in tests/unit/test_prompts.py
- [ ] T029 Add unit test for add CLI handler in tests/unit/test_menu.py

**Checkpoint**: User Story 1 complete - users can add tasks

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Users can view all tasks with their status

**Independent Test**: Add tasks, view list, verify all tasks display correctly

- [ ] T030 Create task display formatter in src/cli/menu.py
- [ ] T031 [P] Implement format_task() for single task display
- [ ] T032 [P] Implement display_task_list() for multiple tasks
- [ ] T033 [P] Implement display_empty_list() message
- [ ] T034 Create CLI handler for view operation in src/cli/menu.py
- [ ] T035 Add view_tasks() function in src/cli/menu.py
- [ ] T036 [P] Add unit tests for display functions in tests/unit/test_menu.py

**Checkpoint**: User Story 2 complete - users can view all tasks

---

## Phase 5: User Story 3 - Delete Task (Priority: P1)

**Goal**: Users can delete tasks by ID

**Independent Test**: Add task, delete it, verify it no longer appears

- [ ] T037 Create delete confirmation prompts in src/cli/prompts.py
- [ ] T038 [P] Implement confirm_delete() prompt
- [ ] T039 Create CLI handler for delete operation in src/cli/menu.py
- [ ] T040 Add delete_task() function in src/cli/menu.py
- [ ] T041 [P] Add unit tests for delete functionality in tests/unit/test_menu.py

**Checkpoint**: User Story 3 complete - users can delete tasks

---

## Phase 6: User Story 4 - Update Task (Priority: P1)

**Goal**: Users can update task title and/or description by ID

**Independent Test**: Add task, update it, verify changes reflect

- [ ] T042 Create update prompts in src/cli/prompts.py
- [ ] T043 [P] Implement get_update_input() for title/description
- [ ] T044 Create CLI handler for update operation in src/cli/menu.py
- [ ] T045 Add update_task() function in src/cli/menu.py
- [ ] T046 [P] Add unit tests for update functionality in tests/unit/test_menu.py

**Checkpoint**: User Story 4 complete - users can update tasks

---

## Phase 7: User Story 5 - Mark Task as Complete (Priority: P1)

**Goal**: Users can mark tasks as complete by ID

**Independent Test**: Add task, mark complete, verify status changes

- [ ] T047 Create complete prompts in src/cli/prompts.py
- [ ] T048 [P] Implement get_task_id_for_complete() prompt
- [ ] T049 Create CLI handler for complete operation in src/cli/menu.py
- [ ] T050 Add mark_task_complete() function in src/cli/menu.py
- [ ] T051 [P] Add unit tests for complete functionality in tests/unit/test_menu.py

**Checkpoint**: User Story 5 complete - users can mark tasks complete

---

## Phase 8: User Story 6 - Interactive Menu Interface (Priority: P1)

**Goal**: Menu-driven interface for all operations

**Independent Test**: Launch app, verify menu displays, navigate all options

- [ ] T052 Create main menu display in src/cli/menu.py
- [ ] T053 [P] Implement display_menu() function
- [ ] T054 [P] Implement get_user_choice() function
- [ ] T055 Create menu routing logic in src/cli/menu.py
- [ ] T056 Implement route_choice() function
- [ ] T057 Create main application loop in src/main.py
- [ ] T058 Implement main() entry point
- [ ] T059 Add exit handler and goodbye message
- [ ] T060 Create integration test for CLI flow in tests/integration/test_cli_flow.py
- [ ] T061 [P] Add integration test for full add-view-delete cycle

**Checkpoint**: User Story 6 complete - full application functional

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Code quality, documentation, and final validation

- [ ] T062 Add comprehensive docstrings to all public functions
- [ ] T063 Verify all functions have type hints
- [ ] T064 Run PEP 8 compliance check
- [ ] T065 Run all unit tests and verify pass
- [ ] T066 Run integration test and verify pass
- [ ] T067 Validate quickstart.md instructions work

---

## Dependencies & Execution Order

### Phase Dependencies

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup (1) | None | Foundational |
| Foundational (2) | Setup | All User Stories |
| User Stories (3-8) | Foundational | Polish |
| Polish (9) | All User Stories | None |

### User Story Dependencies

All user stories can proceed in parallel after Foundational phase completes:
- **US1 (Add Task)**: Can start after Foundational - No other dependencies
- **US2 (View List)**: Can start after Foundational - No other dependencies
- **US3 (Delete)**: Can start after Foundational - No other dependencies
- **US4 (Update)**: Can start after Foundational - No other dependencies
- **US5 (Complete)**: Can start after Foundational - No other dependencies
- **US6 (Menu)**: Can start after Foundational - Depends on US1-US5 completion

### Within Each User Story

1. Prompts before CLI handler
2. CLI handler before tests
3. Tests verify handler works

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel
- All User Stories can start in parallel after Foundational
- US6 (Menu) should be last as it integrates all other stories

---

## Implementation Strategy

### MVP First (User Story 1 + US2 + US6)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: US1 (Add Task)
4. Complete Phase 4: US2 (View List)
5. Complete Phase 8: US6 (Menu)
6. **STOP and VALIDATE**: Test add-view cycle
7. Demo: Basic add/view functionality

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add US3 (Delete) → Test → Demo
3. Add US4 (Update) → Test → Demo
4. Add US5 (Complete) → Test → Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: US1 (Add) + US2 (View)
   - Developer B: US3 (Delete) + US4 (Update)
   - Developer C: US5 (Complete) + US6 (Menu)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests pass before considering story complete
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- US6 (Menu) depends on all other stories being complete

---

## Task Summary

| Phase | Tasks | Description |
|-------|-------|-------------|
| 1 | T001-T009 | Setup (9 tasks) |
| 2 | T010-T021 | Foundational (12 tasks) |
| 3 | T022-T029 | US1: Add Task (8 tasks) |
| 4 | T030-T036 | US2: View List (7 tasks) |
| 5 | T037-T041 | US3: Delete Task (5 tasks) |
| 6 | T042-T046 | US4: Update Task (5 tasks) |
| 7 | T047-T051 | US5: Mark Complete (5 tasks) |
| 8 | T052-T061 | US6: Menu Interface (10 tasks) |
| 9 | T062-T067 | Polish (6 tasks) |
| **Total** | **67 tasks** | |
