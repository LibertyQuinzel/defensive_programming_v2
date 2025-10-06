# Defensive Programming Course Syllabus

Course length: 4–6 hours (self-paced mini-course)

Audience: Intermediate Python developers who know pytest and virtual environments.

Structure (step-by-step)
1. Intro & Setup (00-intro.md)
2. Harden an operations module (01-hardening.md)
3. Sentinel values vs exceptions (02-sentinels.md)
4. Design by contract and assertions (03-design-by-contract.md)
5. Decorators for pre/post conditions (04-decorators.md)

Each module contains:
- Learning objectives
- Short lecture notes and examples
- Hands-on exercise with autograder hints
- Tests that validate behavior and error handling

Delivery & assessment
- Local: run the provided pytest suite and follow acceptance criteria in each assignment
- CI: GitHub Actions runs tests and flake8 on push/PR
- Grading: use rubric.md for manual review or adapt autograder hints for automatic scoring
