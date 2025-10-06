"""Public examples package used by tests.

This package re-exports the instructor example modules copied from the
`topics/*/example_*.py` files so tests can import `examples.*`.
"""

from . import operations  # noqa: F401
from . import sentinel_examples  # noqa: F401
from . import contracts  # noqa: F401
from . import decorators  # noqa: F401
