# Topic 03 — Design by Contract (Pre/Post Conditions)

## What this page is for
A study guide for learning and applying design-by-contract ideas in small Python functions using `@pre` and `@post` decorators. Use `topics/03-design-by-contract/example_contracts.py`, `skeleton.py`, and `test_contracts.py`.

## Learning objectives
- Understand preconditions and postconditions and why they make APIs clearer.
- Use decorator factories to apply pre/post checks that raise `ContractError` on violation.
- Compose multiple decorators and preserve metadata with `functools.wraps`.

## Time estimate
60–120 minutes

## Read / Study (core resources)
- Wikipedia — Design by Contract: https://en.wikipedia.org/wiki/Design_by_contract
- Real Python — Decorators (useful background): https://realpython.com/primer-on-python-decorators/
- Refactoring.Guru — Encapsulate what varies (decorator patterns): https://refactoring.guru
- Python docs — functools.wraps: https://docs.python.org/3/library/functools.html#functools.wraps

## Learn-by-doing workflow
1. Read `assignment.md` and follow the beginner walkthrough to set up a virtual environment if needed.
2. Run the starter:

```bash
python topics/03-design-by-contract/starter.py
```

3. Inspect `topics/03-design-by-contract/example_contracts.py` to study `pre` and `post` decorator factories and the sample `reciprocal` function.
4. Implement or adapt functions in `skeleton.py` to use `@pre` and `@post` and ensure they raise `ContractError` when violated.
5. Run tests:

```bash
PYTHONPATH=. pytest -q topics/03-design-by-contract/test_contracts.py
```

6. Add tests to assert both precondition and postcondition failures.
7. Reflect: write a short note explaining one real-world API that would benefit from contracts.

## Common pitfalls and tips
- Ensure predicates accept the same arguments as the wrapped function (or adapt with wrappers).
- Use `functools.wraps` so decorated functions keep their original name/documentation.
- Avoid expensive checks in `@post` that significantly slow down hot code paths; contracts are often development-time checks.

## Exercises
- Add a function with both `@pre` and `@post` that checks input ranges and guarantees invariants on outputs.
- Implement a debug-mode toggle that disables contract checks for production (document trade-offs).

## Further reading
- "Design by Contract" articles and blog posts
- Libraries: icontract, deal (contract libraries for Python) for more advanced patterns

## TDD and hidden autograder tests

Run visible Part A tests in this folder first. Hidden autograder tests in `grading/hidden_tests/` will run in CI and contain stricter checks. Implement skeletons to satisfy both visible and hidden tests.
