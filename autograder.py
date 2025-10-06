"""Simple autograder: runs pytest for assignment tests and writes JSON results.

This is a minimal autograder that runs pytest and writes a small JSON summary.
"""
import json
import subprocess
import sys

from pathlib import Path

ROOT = Path(__file__).parent
RUN = ROOT / "autograder_result.json"


def run():
    cmd = [sys.executable, "-m", "pytest", "-q", "--maxfail=1"]
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    result = {
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }

    RUN.write_text(json.dumps(result))

    print(f"Autograder finished: wrote {RUN}")

    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(run())
