
# Defensive Programming Course — Beginner Friendly

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/LibertyQuinzel/defensive_programming_v2/workflows/Tests/badge.svg)](https://github.com/LibertyQuinzel/defensive_programming_v2/actions)

This repository contains a hands-on course on **defensive programming in Python**. Learn to write robust, error-resistant code through practical exercises covering guard clauses, sentinels, design-by-contract, and decorators.

## 🎯 Course Overview

**Duration**: ~6-8 hours | **Level**: Beginner to Intermediate | **Prerequisites**: Basic Python knowledge

### What You'll Master
- ✅ **Guard Clauses**: Early input validation and error prevention
- ✅ **Sentinel Objects**: Elegant alternatives to exceptions for "not found" cases  
- ✅ **Design by Contract**: Pre/post-conditions with decorators
- ✅ **Test-Driven Development**: Writing tests before implementation
- ✅ **Defensive Patterns**: Real-world error handling techniques

## 🚀 Quick Start

### For Students
```bash
# 1. Clone and navigate to the repository
git clone https://github.com/LibertyQuinzel/defensive_programming_v2.git
cd defensive_programming_v2

# 2. Run the automated setup
./setup_student.sh

# 3. Start learning!
cd defensive_programming_v2/topics/00-intro
python starter.py
```

**📖 New to the course?** Read the [**Student Guide**](STUDENT_GUIDE.md) for detailed instructions and tips!

### For Instructors
```bash
# Quick verification that everything works
python -m defensive_programming_v2.autograder
python defensive_programming_v2/topics/run_partA_tests.py
```

See [**Instructor Notes**](instructor_notes.md) for classroom integration.

## 📚 Course Structure

| Topic | Concept | Key Skills | Duration |
|-------|---------|------------|----------|
| [**00-intro**](defensive_programming_v2/topics/00-intro/) | Basic guard clauses | Input validation, early returns | 1 hour |
| [**01-guard-clauses**](defensive_programming_v2/topics/01-guard-clauses/) | Defensive arithmetic | Type checking, error handling | 1.5 hours |
| [**02-sentinels**](defensive_programming_v2/topics/02-sentinels/) | Sentinel objects | Alternative to exceptions | 1.5 hours |
| [**03-design-by-contract**](defensive_programming_v2/topics/03-design-by-contract/) | Pre/post-conditions | Contract programming | 2 hours |
| [**04-decorators**](defensive_programming_v2/topics/04-decorators/) | Validation decorators | Reusable patterns | 2 hours |

### Each Topic Includes
- 📋 **Assignment guide** with learning objectives
- 🎮 **Interactive starter** to explore concepts  
- ✏️ **Test templates** for hands-on practice
- 🔧 **Implementation skeletons** to complete
- ✅ **Instructor tests** providing specifications

## 🛠️ Project Structure

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

| Topic | Assignment (GitHub) |
|---|---|
| 00 — Intro | [View on GitHub](https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/00-intro/assignment.md) |
| 01 — Guard Clauses | [View on GitHub](https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/01-guard-clauses/assignment.md) |
| 02 — Sentinels | [View on GitHub](https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/02-sentinels/assignment.md) |
| 03 — Design by Contract | [View on GitHub](https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/03-design-by-contract/assignment.md) |
| 04 — Decorators | [View on GitHub](https://github.com/LibertyQuinzel/defensive_programming_v2/blob/main/defensive_programming_v2/topics/04-decorators/assignment.md) |

Troubleshooting

- If pytest can't find modules, ensure PYTHONPATH points at the package directory:
	`export PYTHONPATH=$(pwd)/defensive_programming_v2`
- Run style checks with `flake8 defensive_programming_v2 --max-line-length=100`.

License & contact

For questions, see `instructor_notes.md` or open an issue in the repository.

