"""Student test template for Topic 04 - Decorators.

Template to exercise the `announce` decorator in `skeleton.py`.

Run from the repository root:

    PYTHONPATH=. pytest -q defensive_programming_v2/topics/04-decorators/test_template_for_students.py
"""

from pathlib import Path
import importlib.util
import pytest

skel_path = Path(__file__).parent / "skeleton.py"
spec = importlib.util.spec_from_file_location("topic04_decorators", skel_path)
skeleton = importlib.util.module_from_spec(spec)
spec.loader.exec_module(skeleton)


def test_announce_basic(capsys):
    # Part 1: tests-first for a small implemented helper
    assert skeleton.basic_add(2, 3) == 5


def test_announce_quiet(monkeypatch):
    monkeypatch.setenv("QUIET", "1")

    @skeleton.announce
    def add(a, b):
        return a + b

    assert add(1, 1) == 2


#########################################################################
# Part 2: Implementation-first exercise (instructor-provided tests exist for
# `announce`. Students implement the decorator to satisfy those tests.)
#########################################################################


def test_announce_basic_prints(capsys):
    @skeleton.announce
    def mul(a, b):
        return a * b

    assert mul(2, 3) == 6
    captured = capsys.readouterr()
    assert "Calling mul" in captured.out


def test_announce_quiet_disables(monkeypatch):
    monkeypatch.setenv("QUIET", "1")

    @skeleton.announce
    def mul(a, b):
        return a * b

    assert mul(1, 1) == 1
