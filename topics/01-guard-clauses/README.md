# Topic 01 — Guard Clauses / Hardening

## What this page is for
A focused study guide for hardening small APIs with guard clauses, input validation, and domain-specific exceptions. Work alongside `topics/01-guard-clauses/example_operations.py`, `skeleton.py`, and `test_operations_defensive.py`.

## Learning objectives
- Write concise guard clauses that fail early with clear messages.
- Implement input validation that rejects booleans, NaN, and infinities when numeric inputs are required.
- Design and raise domain-specific exceptions (e.g., `InvalidOperandError`, `DivisionByZeroError`).
- Write tests that exercise both happy and error paths.

## Time estimate
45–90 minutes

## Read / Study (core resources)
- Refactoring.Guru — Guard Clauses: https://refactoring.guru/replace-nested-conditional-with-guard-clauses
- Python docs — Floating point helpers and math.isfinite: https://docs.python.org/3/library/math.html#math.isfinite
- Real Python — Exceptions and Best Practices: https://realpython.com/python-exceptions/
- PyTest docs — Writing good tests: https://docs.pytest.org/en/stable/how-to/index.html

## Learn-by-doing workflow
1. Read `topics/01-guard-clauses/assignment.md` and `topics/01-guard-clauses/example_operations.py`.
2. Run the starter to see current behavior:

```bash
python topics/01-guard-clauses/starter.py
```

3. Inspect `topics/01-guard-clauses/skeleton.py` and implement the following checks:
   - `a` and `b` must be numbers (int/float) but not booleans.
   - Reject NaN / infinities using `math.isfinite`.
   - Raise a clear `ValueError` or a domain-specific exception for division by zero.
4. Run the topic tests and iterate until they pass:

```bash
PYTHONPATH=. pytest -q topics/01-guard-clauses/test_operations_defensive.py
```

5. Add at least two tests of your own (e.g., `test_nan_rejected`, `test_bool_rejected`).
6. Reflect: Document (README or commit message) the reasoning for rejecting `bool` as a numeric input.

## Tests and acceptance criteria
- `test_operations_defensive.py` passes.
- Custom exceptions are used when appropriate.
- No bare `except:` blocks in the implementation.

## Edge cases and exercises
- Handle string inputs like "3.14" — decide whether to accept them (explicit conversion) and document your choice.
- Add property-based tests (hypothesis) to randomly generate edge inputs.

## Further reading
- "Refactoring" catalog (guards): https://refactoring.guru
- Effective Python, Fluent Python for defensive API design
- Articles on numerical stability and edge-case handling

## TDD and hidden autograder tests

Instructor-visible Part A tests live in this folder. Hidden autograder tests are in `grading/hidden_tests/` and run during CI. Implement the skeletons to pass Part A tests first; then ensure your implementation also satisfies hidden tests (instructors can run them locally).
