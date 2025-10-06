# Assignment 4: Pre/Post Condition Decorators

## Goal
Learn to write decorators that implement pre- and post-conditions and apply them to small APIs.


Two-part workflow (tests-first and implementation-first)

Part 1 — Tests-first (student writes tests)
- Use the student test template `test_template_for_students_04_decorators.py` in this folder to write tests that target helper functions (e.g., `basic_add`) and decorator behavior.
- Run student tests with:

```bash
PYTHONPATH=. pytest -q defensive_programming_v2/topics/04-decorators/test_template_for_students_04_decorators.py
```

Part 2 — Implementation-first (instructor-driven)
-- Instructor canonical Part A tests are stored under `defensive_programming_v2/topics/04-decorators/instructor_tests/`.
- Run instructor Part A tests with:

```bash
PYTHONPATH=. pytest -q defensive_programming_v2/topics/04-decorators/instructor_tests/test_partA_04_decorators.py
```

Acceptance criteria
- Part 1: student-written tests pass for helper functions / basic decorator behavior.
- Part 2: instructor Part A tests pass after implementing the decorators in `example_decorators.py` or `skeleton.py`.

TDD note & hidden tests

Run visible Part A tests first. Hidden autograder tests in `grading/hidden_tests/` will run in CI and perform stricter validation (metadata preservation, error messages, etc.).
