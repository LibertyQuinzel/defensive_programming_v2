# Assignment 2: Sentinel Values vs Exceptions

## Goal
Explore when to use sentinel values and when to raise exceptions. Implement a small API that uses a sentinel for "not found" and another API that raises an exception — justify your choice.

Two-part workflow (tests-first and implementation-first)

Part 1 — Tests-first (student writes tests)
- Implement small tests for the provided helper(s) using the student template file `test_template_for_students_02_sentinels.py` in this folder. Copy or rename it and add tests for `validated_choose`/helpers.
- Run student tests with:

```bash
PYTHONPATH=. pytest -q defensive_programming_v2/topics/02-sentinels/test_template_for_students_02_sentinels.py
```

Part 2 — Implementation-first (instructor-driven)
-- Instructor canonical Part A tests are stored under `defensive_programming_v2/topics/02-sentinels/instructor_tests/`.
- Run instructor Part A tests with:

```bash
PYTHONPATH=. pytest -q defensive_programming_v2/topics/02-sentinels/instructor_tests/test_partA_02_sentinels.py
```

Acceptance criteria
- Part 1: student-written tests pass against the implemented helper functions.
- Part 2: instructor Part A tests pass after implementing the target functions in `skeleton.py`.

TDD note & hidden tests

Visible Part A tests are provided in this folder (instructor tests under `instructor_tests/`). Hidden autograder tests are available in `grading/hidden_tests/` and will run in CI.
