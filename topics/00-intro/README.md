# Topic 00 — Intro: Defensive Programming (Quick)

## What this page is for
A compact study guide that helps you read, practice, and reflect on the core ideas of defensive programming: clear contracts, guard clauses, and defensive test design. Use this alongside `topics/00-intro/starter.py` and `topics/00-intro/skeleton.py`.

## Learning objectives
- Explain EAFP (Easier to Ask for Forgiveness than Permission) vs LBYL (Look Before You Leap).
- Add a simple guard clause to a small function and write a test for invalid input.
- Run Python scripts and pytest from the repo root.

## Time estimate
15–45 minutes

## Read / Study (short list)
- Python official docs — Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html
- Refactoring.Guru — Guard Clauses: https://refactoring.guru/replace-nested-conditional-with-guard-clauses
- Real Python — Guide to Exceptions: https://realpython.com/python-exceptions/
- (Optional) "EAFP vs LBYL" explanation: https://docs.python.org/3/glossary.html#term-eafp

## Learn-by-doing workflow (read / study / do / test / reflect)
1. Read this file and `topics/00-intro/assignment.md`.
2. Run the starter to observe behavior:

```bash
python topics/00-intro/starter.py
```

3. Inspect `topics/00-intro/skeleton.py` and identify where a guard clause would make behavior clearer.
4. Implement the guard clause(s) in the `skeleton.py` (or modify code in-place in a copied file).
5. Add a tiny test (create `topics/00-intro/test_intro.py`) that asserts the function raises `TypeError` for non-string inputs.
6. Run the test:

```bash
PYTHONPATH=. pytest -q topics/00-intro/test_intro.py
```

7. Reflect: write a 1–2 sentence note (locally, in a file or commit message) explaining why the guard clause improves clarity.

## Suggested exercises (stretch)
- Add a test for empty string behavior.
- Compare two alternative implementations (one with LBYL, one with EAFP) and time their performance on many calls (micro-benchmark).

## Checklist before moving on
- [ ] Starter runs and outputs an example greeting.
- [ ] `skeleton.greet` raises `TypeError` on non-strings.
- [ ] At least one pytest covering invalid input passes.

## Further reading
- "Refactoring" patterns — Refactoring.Guru: https://refactoring.guru
- Effective Python (book) — Item: Prefer EAFP to LBYL where appropriate
- Python Style Guide: https://peps.python.org/pep-0008/
