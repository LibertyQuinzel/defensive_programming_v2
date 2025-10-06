# Instructor Notes

This file explains how to use the mini-course in a classroom setting.

- Use GitHub Actions (`.github/workflows/defensive-ci.yml`) as an automated check for submissions.
- Ask students to open PRs; grading uses rubric.md. Optionally add autograder for automatic scoring.
- Encourage TDD: students should add tests first, then implement.
-- Common issues: imports (use `PYTHONPATH=.` or `pip install -e .` or `python -m pip install -e defensive_programming_v2`).
