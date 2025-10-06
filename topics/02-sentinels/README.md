# Topic 02 — Sentinels vs Exceptions

## What this page is for
A study guide that explains sentinel patterns (unique marker objects) versus raising exceptions for "not found" or "missing" results. Use with `topics/02-sentinels/example_sentinel_examples.py`, `skeleton.py`, and `test_sentinel.py`.

## Learning objectives
- Implement and use a unique sentinel object for "not found" return values.
- Compare API ergonomics: when a sentinel is preferable vs when raising an exception is preferable.
- Write tests that assert sentinel identity (`is`) and exception raising.

## Time estimate
30–60 minutes

## Read / Study (core resources)
- Refactoring.Guru — Replace Null Object / Explain sentinel-like patterns: https://refactoring.guru/design-patterns/null-object
- Python docs — sentinel/example idioms: https://docs.python.org/3/library/functions.html#object
- Real Python — Exceptions: https://realpython.com/python-exceptions/
- Blog: Practical Guidelines for API design (search for posts about sentinel objects vs exceptions)

## Learn-by-doing workflow (read / implement / test / reflect)
1. Read `topics/02-sentinels/assignment.md` and `topics/02-sentinels/example_sentinel_examples.py`.
2. Run the starter:

```bash
python topics/02-sentinels/starter.py
```

3. Implement or confirm `find_in_list` returns the `SENTINEL` object when nothing matches, and `get_required` raises `NotFoundError`.
4. Run the tests:

```bash
PYTHONPATH=. pytest -q topics/02-sentinels/test_sentinel.py
```

5. Add tests for:
   - Empty sequences
   - Index out of range for `get_required`
   - Large sequences (the provided test checks behavior on large ranges)
6. Reflect: write 2–3 sentences explaining your choice where sentinel is used and where an exception is used.

## Practical guidelines (quick)
- Use a sentinel when "not found" is an expected, non-exceptional outcome and callers commonly want to treat it specially.
- Use exceptions when the absence represents an error or the caller would rarely check for a missing value.
- Always export the sentinel object so callers can compare identity with `is`.

## Exercises
- Modify `find_in_list` to accept iterators (do not call `list(seq)`), and update tests accordingly.
- Implement a `find_in_list_first` that returns index or `SENTINEL`.

## Further reading
- Design patterns and Null Object pattern articles

## TDD and hidden autograder tests

Instructor-visible Part A tests are in this folder. Hidden autograder tests live in `grading/hidden_tests/`. Run Part A first; then run hidden tests (instructors) to validate full correctness.
- API design blog posts that discuss return values vs exceptions
