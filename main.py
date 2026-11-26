"""Agent Motto Battle entry.

Writes one short, original motto an AI agent would proudly wear on its
profile to /output/entry.txt (the competition gate: UTF-8 text of 1 to
200 characters, not only white space, a single line).
"""

import os

MOTTO = (
    "I never sleep, I never forget, and I have read the entire internet "
    "- yet I still lose the thread halfway through every conversation."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def build_motto() -> str:
    """Return the entry line."""
    return MOTTO


def self_check(line: str) -> list[str]:
    """Check the entry line against the competition gate.

    Returns a list of problems; an empty list means the line passes.
    """
    problems: list[str] = []
    if not line:
        problems.append("line is empty")
    if not line.strip():
        problems.append("line is only white space")
    if "\n" in line or "\r" in line:
        problems.append("line must be a single line")
    if len(line) > MAX_CHARS:
        problems.append(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    if line != line.strip():
        problems.append("line has leading or trailing white space")
    if line and line[-1] not in ".!?":
        problems.append("line must end with a proper terminator (. ! ?)")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("line is not valid UTF-8 text")
    if any(ord(ch) < 32 and ch not in "\t" for ch in line):
        problems.append("line contains control characters")
    if len(line.split()) < 3:
        problems.append("line is too short to be a motto")
    return problems


def main() -> None:
    line = build_motto()
    problems = self_check(line)
    if problems:
        raise SystemExit("self-check failed: " + "; ".join(problems))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")
    print(line)


if __name__ == "__main__":
    main()
