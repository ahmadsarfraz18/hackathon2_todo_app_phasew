# Skill: Quality Audit

**Agent Owner:** `review-agent`

**Filename:** `qa.quality-audit.md`

---

## Purpose

Perform a comprehensive quality audit of Python code and specifications for the Todo App Phase I. Validates PEP 8 compliance, type hint completeness, specification quality, and code structure. This skill ensures all deliverables meet the project's quality standards before proceeding to the next phase.

---

## When to Use

- After code implementation is complete
- After specification creation or update
- Before quality gate approval
- When refactoring is complete
- During phase transition checkpoints

---

## Inputs

- Python source files: `todo.py`, `models/`, `services/`
- Specification file: `specs/<feature>/spec.md`
- Constitution file: `.specify/memory/constitution.md`
- pycodestyle or flake8 configuration (if present)

---

## Step-by-Step Process

1. **Audit PEP 8 compliance**
   - Run pycodestyle on all Python files
   - Count E (error) violations (must be 0)
   - Count W (warning) violations (target < 5)
   - Record specific violations with file:line:column

2. **Audit type hints**
   - Verify every function has return type annotation
   - Verify every parameter has type annotation
   - Check for `Any` type usage (flag if used without justification)
   - Verify complex types use type aliases

3. **Audit code structure**
   - Verify single responsibility principle (one class per file recommended)
   - Verify no circular imports
   - Verify function length < 50 lines
   - Verify class length < 200 lines

4. **Audit documentation**
   - Verify every public function has docstring
   - Verify docstrings include args, returns, raises
   - Verify no commented-out code remains
   - Verify inline comments explain complex logic only

5. **Audit specification quality**
   - Verify feature name and problem statement present
   - Verify user stories have priority (P1/P2/P3)
   - Verify acceptance criteria are testable
   - Verify edge cases are identified

6. **Calculate quality score**
   - PEP 8: 30% weight
   - Type hints: 25% weight
   - Code structure: 25% weight
   - Documentation: 20% weight

---

## Output

Quality audit report containing:
- Overall quality score (0-100)
- PEP 8 violation count and details
- Type hint completeness percentage
- Specification quality score
- Critical issues list (must fix)
- Major issues list (should fix)
- Minor issues list (nice to have)
- Pass/Fail determination

---

## Failure Handling

| Scenario | Handling |
|----------|----------|
| E violations > 0 | FAIL - PEP 8 errors must be corrected |
| Type hint incomplete | FAIL - All functions require type hints |
| Missing docstrings | FAIL - Public APIs must be documented |
| No specification file | FAIL - Cannot audit without spec |
| pycodestyle unavailable | Use manual checklist equivalent |
| Quality score < 70 | FAIL - Must improve before approval |
