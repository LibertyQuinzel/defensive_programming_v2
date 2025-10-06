````markdown
# Assignment 3: Design by Contract

## Goal
Implement and use pre- and post-condition checks for small functions.

Two-part workflow (tests-first and implementation-first)

Part 1 — Tests-first (student writes tests)
- Use the student test template `test_template_for_students_03_contracts.py` in this folder to write Part 1 tests that exercise the provided helper functions (e.g., `validated_reciprocal`).
- Run student tests with:

```bash
PYTHONPATH=. pytest -q defensive_programming_v2/topics/03-design-by-contract/test_template_for_students_03_contracts.py
```

Part 2 — Implementation-first (instructor-driven)
- The instructor canonical Part A tests that define the contract for the instructor-target functions live under:

```
defensive_programming_v2/topics/03-design-by-contract/instructor_tests/test_partA_03_contracts.py
```

- Run the instructor Part A tests with:

```bash
PYTHONPATH=. pytest -q defensive_programming_v2/topics/03-design-by-contract/instructor_tests/test_partA_03_contracts.py
```

Acceptance criteria
- Part 1: student-written tests pass for the helper functions.
- Part 2: instructor Part A tests pass after implementing or adapting `skeleton.py` to use `@pre` / `@post` decorators.

TDD note & hidden tests

Run visible Part A tests first. Hidden autograder tests in `grading/hidden_tests/` will run in CI and include stricter checks.

Beginner walkthrough and hints
- Inspect `example_contracts.py` for decorator factories, use `functools.wraps` when writing decorators, and implement small focused tests that target a single contract violation at a time.
