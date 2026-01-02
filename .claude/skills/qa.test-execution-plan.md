# Skill: Test Execution Plan

**Agent Owner:** `review-agent`

**Filename:** `qa.test-execution-plan.md`

---

## Purpose

Generate and validate a comprehensive test execution plan for Todo App Phase I. Covers all happy paths for the 5 basic features, all edge cases identified by the domain expert, and all error scenarios. Ensures testable acceptance criteria and complete coverage before implementation.

---

## When to Use

- After acceptance criteria are defined
- Before Red phase (test writing)
- After domain expert provides edge cases
- When validating test coverage completeness
- Before quality gate for test adequacy

---

## Inputs

- `spec.md` with user stories and acceptance criteria
- Domain expert edge case inventory
- Task entity definition (id, title, description, status, timestamps)
- CRUD operation specifications
- Error taxonomy from domain expert

---

## Step-by-Step Process

1. **Map features to test cases**
   - List all 5 features: list, add, update, delete, exit
   - Create test case for each feature's happy path
   - Map each acceptance criterion to at least one test case

2. **Generate CRUD happy path tests**
   - **List:** Empty list, single task, multiple tasks
   - **Add:** Valid title, valid title with description, auto-generated ID
   - **Update:** Update title, update description, update status
   - **Delete:** Delete existing, verify removal from list
   - **Exit:** Clean exit, confirm no data loss

3. **Generate edge case tests from inventory**
   - Empty title input (validation failure)
   - Title exceeds max length (validation failure)
   - Whitespace-only title (validation failure)
   - Non-existent task ID for update (not found error)
   - Non-existent task ID for delete (not found error)
   - Duplicate task handling (if required)
   - Maximum tasks limit (if any)

4. **Generate status transition tests**
   - pending → in_progress
   - pending → completed
   - in_progress → completed
   - in_progress → pending (if allowed)
   - completed → in_progress (if allowed)

5. **Generate error handling tests**
   - Invalid menu selection
   - Non-numeric menu input
   - Empty menu selection
   - Invalid task ID type

6. **Validate test coverage**
   - Verify all P1 acceptance criteria have tests
   - Verify all critical edge cases have tests
   - Verify all CRUD operations have happy path test
   - Verify all error paths have tests

7. **Generate test execution plan**
   - Organize tests by feature (list, add, update, delete, exit)
   - Order tests: happy paths first, then edge cases, then errors
   - Estimate execution order and dependencies
   - Specify test data requirements

---

## Output

Test execution plan containing:
- Test case inventory by feature
- Happy path test count (target: 1 per feature minimum)
- Edge case test count (target: all critical + major)
- Error path test count (target: all defined errors)
- Test execution order with dependencies
- Test data setup requirements
- Coverage matrix (acceptance criteria → test cases)
- Pass/fail criteria for each test

---

## Failure Handling

| Scenario | Handling |
|----------|----------|
| Missing happy path test | FAIL - Add test for core feature |
| Missing test for critical edge case | FAIL - Add edge case test |
| Acceptance criterion not covered | FAIL - Add test mapping to criterion |
| No specification available | FAIL - Cannot create plan without spec |
| No edge case inventory | FAIL - Request from domain expert first |
| Test has external dependency | FAIL - Use in-memory test data only |
| Test is non-deterministic | FAIL - Make test deterministic |
