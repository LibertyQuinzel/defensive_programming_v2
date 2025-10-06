"""Tests illustrating sentinel-based APIs vs exceptions.

- Purpose: teach the trade-offs between returning sentinel values and raising
  exceptions when a search or lookup fails. These tests clarify the API contract
  for `find_in_list` and helper `get_required`.

- Key lessons covered:
  1. Sentinel semantics: when APIs return a sentinel (like `SENTINEL`) it allows
      callers to decide how to handle absence without exception control flow.
  2. Distinct sentinel: the sentinel should be a clear, distinct object so it
      cannot be confused with legitimate results (avoid overloaded values like
      None unless explicitly documented).
  3. Complementary helpers: `get_required` demonstrates a stricter API that
      converts absence into an exception to simplify callers who expect a value.

Students should view these tests as a concise specification: implement
`find_in_list` to return `SENTINEL` when the predicate matches nothing, and
implement `get_required` to raise `NotFoundError` for missing values.
"""

from examples.sentinel_examples import (
     SENTINEL,
     find_in_list,
     get_required,
     NotFoundError,
)


def test_find_returns_sentinel_when_missing():
    seq = [1, 2, 3]
    res = find_in_list(seq, lambda x: x == 10)
    assert res is SENTINEL


def test_get_required_raises():
    with __import__("pytest").raises(NotFoundError):
        get_required([], 0)


def test_find_large_sequence_performance():
    seq = range(100000)
    res = find_in_list(seq, lambda x: x == 99999)
    assert res == 99999
