# Skill: Requirements Compliance

**Agent Owner:** `review-agent`

**Filename:** `qa.requirements-compliance.md`

---

## Purpose

Validate all deliverables against Hackathon II Phase I requirements and the project constitution. Ensures strict adherence to the defined constraints: Python 3.13+ console app, in-memory storage only, basic 5 CRUD features, PEP 8 compliance, and no external dependencies beyond the standard library.

---

## When to Use

- Before feature completion declaration
- Before submission or merge
- When constitution is updated
- During final compliance check
- After any implementation change

---

## Inputs

- Source code files: `todo.py`, all Python modules
- Constitution file: `.specify/memory/constitution.md`
- Hackathon II Phase I requirements document
- User stories and acceptance criteria from `spec.md`
- Import statements in all Python files

---

## Step-by-Step Process

1. **Validate Python version requirement**
   - Check for `from __future__` imports (Python < 3.10 compatibility)
   - Verify no version-specific workarounds for Python < 3.13
   - Check type hints use syntax compatible with 3.13+

2. **Validate in-memory constraint**
   - Verify no file I/O operations (no `open()`, no `json.load/dump`)
   - Verify no database imports (`sqlite3`, `sqlalchemy`, etc.)
   - Verify no network operations (`requests`, `urllib`, sockets)
   - Verify data storage uses `list` or `dict` in memory only

3. **Validate feature scope (basic 5 features)**
   - Verify `list` operation exists and works
   - Verify `add` operation exists and works
   - Verify `update` operation exists and works
   - Verify `delete` operation exists and works
   - Verify `exit` operation exists and works

4. **Validate no external dependencies**
   - Check `import` statements for third-party packages
   - Verify only `python -m` standard library imports exist
   - Check `requirements.txt` (if exists) is empty or contains only comments

5. **Validate constitution compliance**
   - Check code style matches constitution guidelines
   - Verify naming conventions match constitution
   - Verify error handling patterns match constitution
   - Verify documentation standards match constitution

6. **Validate acceptance criteria coverage**
   - Match each P1 user story to implementation
   - Match each P1 acceptance criterion to test
   - Verify no missing P1 requirements
   - Flag any scope creep beyond Phase I

7. **Generate compliance report**
   - Pass/fail for each constraint category
   - Detailed violation list with file:line references
   - Recommendations for non-compliant items

---

## Output

Requirements compliance report containing:
- Python version compliance: PASS/FAIL
- In-memory storage compliance: PASS/FAIL
- Feature scope compliance: PASS/FAIL
- External dependencies compliance: PASS/FAIL
- Constitution compliance: PASS/FAIL
- Overall compliance status
- Violation details with remediation steps

---

## Failure Handling

| Scenario | Handling |
|----------|----------|
| External dependency found | FAIL - Remove non-standard library dependency |
| File I/O operation detected | FAIL - Use in-memory storage only |
| Missing core feature | FAIL - Implement missing CRUD operation |
| Python version incompatibility | FAIL - Update to Python 3.13+ syntax |
| Constitution violation | FAIL - Align with project constitution |
| Scope creep detected | FAIL - Remove features outside Phase I |
| No requirements document | FAIL - Cannot validate without requirements |
