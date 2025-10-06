# Topic 04 — Decorators (Pre/Post Implementation)

## What this page is for
A study guide to build robust decorators that can be used to implement pre- and post-conditions. Use `topics/04-decorators/example_decorators.py`, `skeleton.py`, and `test_decorators.py`.

## Learning objectives
- Implement decorators that preserve function metadata and work with positional and keyword arguments.
- Use decorators to implement contract checks and informative failures.
- Test decorated functions thoroughly including error messages.

## Time estimate
60–120 minutes

## Read / Study (core resources)
- Real Python — Primer on decorators: https://realpython.com/primer-on-python-decorators/
- Python docs — functools and wrap tools: https://docs.python.org/3/library/functools.html
- Refactoring.Guru — Decorator pattern: https://refactoring.guru/design-patterns/decorator
- PyPI libraries (for inspiration): icontract, deal

## Learn-by-doing workflow
1. Read `topics/04-decorators/assignment.md` and inspect `example_decorators.py`.
2. Run the starter to see a trivial decorator example:

```bash
python topics/04-decorators/starter.py
```

3. Implement or improve `pre` and `post` in `example_decorators.py` so they:
   - Accept positional and keyword arguments.
   - Preserve the wrapped function's `__name__` and `__doc__` using `functools.wraps`.
   - Raise `ContractError` with informative messages (include result for post failures).
4. Apply the decorators to `safe_divide` (see `test_decorators.py`) and run tests:

```bash
PYTHONPATH=. pytest -q topics/04-decorators/test_decorators.py
```

5. Add tests to exercise kwargs, large numeric results, and non-numeric inputs.
6. Reflect: create a short note about when to use decorators for contracts vs inline checks.

## Exercises
- Implement a decorator that optionally logs contract failures to a file with timestamps.
- Add automation to run contract checks only in development mode (env var), and measure performance impact.

## Further reading
- Real Python and official docs (decorators & functools)
- Libraries implementing contracts (icontract, deal) to learn advanced API designs

## TDD and hidden autograder tests

Visible Part A tests live in this topic. Hidden autograder tests under `grading/hidden_tests/` will be run in CI and check stricter behaviors such as metadata preservation and QUITE mode for decorators. Run visible tests, implement the skeleton, then instructors can run hidden tests to validate assignments.
