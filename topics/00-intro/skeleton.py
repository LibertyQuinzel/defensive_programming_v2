"""Skeleton for Assignment 00 - Intro.

Fill in the TODOs and run the starter to verify.
"""

def validated_greet(name: str) -> str:
    """Student-facing implemented helper for tests-first exercises.

    Return a friendly greeting. Behavior:
    - non-empty string -> "Hello, {name}"
    - empty string -> "Hello, stranger"
    - non-string -> raise TypeError
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if name == "":
        return "Hello, stranger"
    return f"Hello, {name}"


def greet(name: str) -> str:
    """Instructor-target function for Part A (intentionally unimplemented).

    Students: implement this function for Part B to satisfy the instructor
    Part A tests. For TDD flow the skeleton raises until implemented.
    """
    # Instructor-target function for Part A (intentionally unimplemented).
    # Students: implement this function for Part B to satisfy the instructor
    # Part A tests. For TDD flow the skeleton raises until implemented.
    raise NotImplementedError("Implement greet(name) in the skeleton for Part B")
