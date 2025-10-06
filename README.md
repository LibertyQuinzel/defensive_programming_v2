
# Defensive Programming Course — Beginner Friendly

This repository contains a short, hands-on course on defensive programming in Python. It is organized into topic folders with assignments, starter code, skeletons, and tests so learners can practice both tests-first and implementation-first workflows.

Highlights
- `topics/` — per-topic assignments, starter code, skeletons, and tests
- `autograder.py` — run the autograder locally to reproduce CI grading
- `requirements.txt` — development dependencies (pytest, flake8)

Quick links
- Course package: `defensive_programming_v2/`
- Topics folder: `defensive_programming_v2/topics/`
- Autograder: `defensive_programming_v2/autograder.py`
- Hidden (CI) tests: `defensive_programming_v2/grading/hidden_tests/`
- Examples: `defensive_programming_v2/examples/`
- Solutions: `defensive_programming_v2/solutions/`

GitHub links
- Repository: https://github.com/LibertyQuinzel/defensive_programming_v2
- Design-by-Contract assignment: https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/03-design-by-contract/assignment.md
- Topics index: https://github.com/LibertyQuinzel/defensive_programming_v2/tree/main/defensive_programming_v2/topics
- Autograder: https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/autograder.py
- Hidden tests (CI): https://github.com/LibertyQuinzel/defensive_programming_v2/tree/main/defensive_programming_v2/grading/hidden_tests
- Examples folder: https://github.com/LibertyQuinzel/defensive_programming_v2/tree/main/defensive_programming_v2/examples


Quick start (copy/paste)

1) Create and activate a virtual environment (recommended)

```bash
# from repo root
python3 -m venv .venv
source .venv/bin/activate
```

2) Install the course dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r defensive_programming_v2/requirements.txt
```

3) Run the tests (examples)

```bash
# Run the full test suite
PYTHONPATH=$(pwd)/defensive_programming_v2 pytest -q

# Run the autograder to produce autograder_result.json
PYTHONPATH=$(pwd)/defensive_programming_v2 python -m defensive_programming_v2.autograder
cat autograder_result.json || true
```

Running topic tests (common commands)

-- Run a student test template (Part 1, tests-first):

```bash
PYTHONPATH=$(pwd)/defensive_programming_v2 pytest -q defensive_programming_v2/topics/01-guard-clauses/test_template_for_students_01_guarded.py
```

- Run the instructor Part A tests for a topic (implementation-first spec):

```bash
PYTHONPATH=$(pwd)/defensive_programming_v2 pytest -q defensive_programming_v2/topics/01-guard-clauses/instructor_tests/test_partA_01_guarded_divide.py
```

- Discover and run all instructor Part A tests across topics with the helper:

```bash
PYTHONPATH=$(pwd)/defensive_programming_v2 python defensive_programming_v2/topics/run_partA_tests.py
```

- Run all tests for a single topic:

```bash
PYTHONPATH=$(pwd)/defensive_programming_v2 pytest -q defensive_programming_v2/topics/03-design-by-contract
```

Student workflow (recommended)

1. Read the assignment: `defensive_programming_v2/topics/<NN>-<name>/assignment.md`
2. Run the starter examples in `starter.py` to understand the intent.
3. For tests-first: copy or rename the student test template `test_template_for_students_*.py` and write tests.
4. Implement the functions in `skeleton.py` and run the topic tests (`pytest` on the topic folder).
5. Optionally run the autograder and the hidden tests before submitting:

```bash
PYTHONPATH=$(pwd)/defensive_programming_v2 python -m defensive_programming_v2.autograder
PYTHONPATH=$(pwd)/defensive_programming_v2 pytest -q defensive_programming_v2/grading/hidden_tests
```

Per-topic quick links

| Topic | Assignment (local) | Assignment (GitHub) |
|---|---|---|
| 00 — Intro | `defensive_programming_v2/topics/00-intro/assignment.md` | [View on GitHub](https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/00-intro/assignment.md) |
| 01 — Guard Clauses | `defensive_programming_v2/topics/01-guard-clauses/assignment.md` | [View on GitHub](https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/01-guard-clauses/assignment.md) |
| 02 — Sentinels | `defensive_programming_v2/topics/02-sentinels/assignment.md` | [View on GitHub](https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/02-sentinels/assignment.md) |
| 03 — Design by Contract | `defensive_programming_v2/topics/03-design-by-contract/assignment.md` | [View on GitHub](https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/03-design-by-contract/assignment.md) |
| 04 — Decorators | `defensive_programming_v2/topics/04-decorators/assignment.md` | [View on GitHub](https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/04-decorators/assignment.md) |

Troubleshooting

- If pytest can't find modules, ensure PYTHONPATH points at the package directory:
	`export PYTHONPATH=$(pwd)/defensive_programming_v2`
- Run style checks with `flake8 defensive_programming_v2 --max-line-length=100`.

License & contact

For questions, see `instructor_notes.md` or open an issue in the repository.

