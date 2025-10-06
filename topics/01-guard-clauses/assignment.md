# Assignment 1: Harden the Operations Module

## Goal
Harden the `examples.operations` module by adding clear contracts, guard clauses, and custom exceptions. Add tests for error paths.

Two-part workflow (tests-first and implementation-first)

This topic contains two complementary exercises so you get practice with both styles:

1) Tests-first practice (student writes tests)
   - Function: `validated_add(a, b)` — implemented in `skeleton.py` as a small helper.
   - Student task: write tests for `validated_add` using the provided template `test_template_for_students_01_guarded.py`.
   - Run student tests with:

```bash
PYTHONPATH=. pytest -q defensive_programming_v2/topics/01-guard-clauses/test_template_for_students_01_guarded.py
```

2) Implementation-first practice (instructor-driven)
   - Function: `guarded_divide(a, b)` — intentionally left unimplemented in `skeleton.py` (it raises `NotImplementedError`).
   - Canonical instructor Part A tests that specify the contract are stored under:

```
defensive_programming_v2/topics/01-guard-clauses/instructor_tests/test_partA_01_guarded_divide.py
```

   - Run the instructor Part A tests with:

```bash
PYTHONPATH=. pytest -q defensive_programming_v2/topics/01-guard-clauses/instructor_tests/test_partA_01_guarded_divide.py
```

Acceptance criteria
- For Part 1: you created tests for `validated_add` and they pass locally.
- For Part 2: you implemented `guarded_divide` so the instructor Part A tests pass.

Hints and resources
- Refer to `topics/01-guard-clauses/example_operations.py` for a robust reference implementation.
- Use `math.isfinite` to filter out `nan` and `inf` where appropriate.

TDD note & hidden tests

Hidden autograder tests are available in `grading/hidden_tests/` and will run in CI. Passing the visible Part A tests is required before attempting hidden tests.
