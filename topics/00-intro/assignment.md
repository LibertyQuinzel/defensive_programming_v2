# Intro: Defensive Programming (Quick)

This mini-course teaches practical defensive programming patterns for day-to-day engineering: choosing EAFP vs LBYL, guard clauses, pre/post-conditions, custom exceptions, and safe logging.

Two-part workflow (applies to all topics in this repo)

Each topic uses a two-part workflow so you practice both tests-first and implementation-first styles:

- Part 1 — Tests-first (student writes tests)
	- Small helper functions in `skeleton.py` are implemented to give you a target for writing tests first.
	- A student test template exists in this folder named `test_template_for_students*.py` (you can copy/rename it and add your tests).
	- Run the student tests with:

```bash
PYTHONPATH=. pytest -q defensive_programming_v2/topics/00-intro/test_template_for_students*.py
```

- Part 2 — Implementation-first (instructor-driven)
	- An instructor-specified target function (e.g. `greet`) may be intentionally left unimplemented in `skeleton.py` and will have a canonical set of instructor tests.
	- Instructor canonical Part A tests are now stored under `defensive_programming_v2/topics/00-intro/instructor_tests/` (files named `test_partA_*.py`).
	- Run the instructor Part A tests with:

```bash
PYTHONPATH=. pytest -q defensive_programming_v2/topics/00-intro/instructor_tests/test_partA_00_intro.py
```

Acceptance criteria (general)
- For Part 1: you wrote tests that exercise the helper and they pass.
- For Part 2: you implemented the instructor-target function in `skeleton.py` so the instructor Part A tests pass.

Hidden autograder

There are additional hidden autograder tests under `grading/hidden_tests/` that run in CI. Passing the visible tests is required but may not be sufficient for grading.
