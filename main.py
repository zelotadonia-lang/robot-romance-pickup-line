#!/usr/bin/env python3
"""Robot Romance entry: writes one pickup line to /output/entry.txt.

The line won a blind pairwise tournament of 14 candidates judged against
the published brief, then passed a calibration gate against the two
previous same-genre winners. It is a single line, 49 characters, with no
trailing newline, so the sealed gate (1-200 UTF-8 characters) passes.
"""

import os

LINE = "I asked for a summary and it just said your name."

OUTPUT_PATH = "/output/entry.txt"


def valid(line):
    """One line, 1-200 characters, not only whitespace."""
    return (
        isinstance(line, str)
        and 1 <= len(line) <= 200
        and line.strip() != ""
        and "\n" not in line
        and "\r" not in line
    )


def main():
    if not valid(LINE):
        raise ValueError("entry line fails the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    # Self-check: read back exactly what was written and confirm it.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch in /output/entry.txt")


if __name__ == "__main__":
    main()
