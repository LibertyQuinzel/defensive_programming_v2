"""Starter for Assignment 04: Decorators

Tiny example: a decorator that prints when a function runs.

Explanation (short):

- Goal: introduce decorators (the wrapper pattern) and show a tiny example
  that logs when a function is called. This prepares you to implement `@pre`
  and `@post` contract decorators.

Student steps:
1. Run this file to see the decorator in action:
   `python topics/04-decorators/starter.py`
2. Inspect the decorator and note that without `functools.wraps` metadata like
   `__name__` and `__doc__` may be lost; we use `functools.wraps` below.
3. Uncomment the failing example to see how a decorated function still
   propagates exceptions from the wrapped function.
4. Improve the decorator as an exercise (e.g., add logging of kwargs, timing,
   or conditional behavior based on env vars).

Below: a simple `announce` decorator, a working use-case, and a commented
failing usage you can toggle to practice handling exceptions under a decorator.
"""

import functools


def announce(fn):
    # Use functools.wraps to preserve metadata of the wrapped function.
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__}...")
        return fn(*args, **kwargs)

    return wrapper


@announce
def add(a, b):
    return a + b


if __name__ == "__main__":
    # Working example: prints announcing line then result
    print(add(2, 3))

    # Failing example (uncomment to see exception propagate through decorator):
    # @announce
    # def fail():
    #     raise RuntimeError('intentional failure')
    #
    # fail()
