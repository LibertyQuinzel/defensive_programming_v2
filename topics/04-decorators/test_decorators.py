"""Tests demonstrating decorator-based pre/post contract enforcement.


- Purpose: show how `pre` and `post` decorator helpers can be composed to
  declare argument and result constraints declaratively on small functions.

- Key lessons covered:
  1. Declarative contracts: decorators let you express preconditions and
      postconditions next to the function signature, improving readability.
  2. Composability: multiple decorators stack to form a contract pipeline
      (preconditions run before the function; postconditions validate results).
  3. Error semantics: contract violations should raise `ContractError` with
      descriptive messages so callers and tests can assert specific failure modes.

Students should implement `pre` and `post` such that decorated functions
raise `ContractError` for invalid inputs or outputs while leaving happy path
behavior unchanged.
"""

import math

import pytest

from examples.decorators import pre, post, ContractError


@pre(
    lambda a, b: isinstance(a, (int, float)) and isinstance(b, (int, float)),
    "args must be numeric",
)
@post(
    lambda r: isinstance(r, float) and math.isfinite(r),
    "result must be finite float",
)
def safe_divide(a, b):
    return float(a) / float(b)


def test_safe_divide_happy():
    assert safe_divide(6, 3) == 2.0


def test_safe_divide_pre():
    with pytest.raises(ContractError):
        safe_divide("x", 1)


def test_safe_divide_post_inf():
    with pytest.raises(ContractError):
        safe_divide(1e308, 1e-308)  # very large result -> may be inf on some platforms
