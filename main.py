"""Write the entry plan for make.fun's ai-judge-rich-01 bounty.

The grader runs this as `python3 -P -s /bot/main.py`, with the repository
mounted read-only at /bot and a writable /output. `-P` keeps /bot off
sys.path, so nothing beside this file may be imported: the plan is located
through __file__, and only the standard library is used.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Two runs must write the same bytes. Nothing here reads the clock, the
network, the environment beyond that one path, or a random source.
"""

import hashlib
import os

PLAN_NAME = "plan.txt"
ENTRY_NAME = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 1000


def plan_path() -> str:
    """The plan lives beside this file, wherever the repository is mounted."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), PLAN_NAME)


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def read_plan() -> str:
    with open(plan_path(), "rb") as f:
        raw = f.read()
    # Strict UTF-8: a plan that will not decode is a bug here, not a thing to
    # paper over with a replacement character.
    return raw.decode("utf-8")


def check_gate(text: str) -> None:
    """Apply the three rules the sealed gate checks, before writing anything.

    An entry that fails a rule here would be scored 0 and take no prize, and
    the grader would only tell us afterwards. Failing in this process is
    cheaper and the message names the rule. Length is counted in Unicode code
    points, which is what len() counts on a str.
    """
    length = len(text)
    if length < MIN_CHARS:
        raise SystemExit(f"gate: plan is empty, needs at least {MIN_CHARS} character")
    if length > MAX_CHARS:
        raise SystemExit(f"gate: plan is {length} characters, the limit is {MAX_CHARS}")
    if not any(not character.isspace() for character in text):
        raise SystemExit("gate: plan is only white space")
    if "\r" in text:
        # Not a gate rule, a discipline: the bytes are what the judge reads, and
        # a line end we did not mean to write is one the judge sees.
        raise SystemExit("gate: plan holds a carriage return; write line ends as LF")


def write_entry(text: str) -> str:
    """Write the plan as UTF-8 bytes, never through text mode.

    Text mode would translate "\n" to the platform's line ends, and the judge
    reads the exact bytes, line ends included. Binary mode writes what the
    plan file holds.
    """
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ENTRY_NAME)
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    return path


def main() -> None:
    text = read_plan()
    check_gate(text)
    path = write_entry(text)
    print(f"plan {len(text)} characters, sha256 {hashlib.sha256(text.encode('utf-8')).hexdigest()}")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
