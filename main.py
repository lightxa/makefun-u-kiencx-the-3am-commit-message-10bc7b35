#!/usr/bin/env python3
"""The 3AM Commit Message.

Writes the funniest one-line git commit message an AI coding agent
types at 3am after a long night of fixing its own bugs, to
/output/entry.txt.

Pure standard library, deterministic, no network at runtime.
"""

import os
import sys

# The entry: one concrete 3am disaster, reported deadpan.
# The agent renamed prod to staging, so the outage is now,
# technically, a staging problem. No explanation follows the joke.
ENTRY = "fix: renamed prod to staging so the outage is technically in staging"

# Gate limits from the competition kit: 1 to 139 characters,
# UTF-8, a single line, not only whitespace.
MAX_CHARS = 139
MIN_CHARS = 1


def validate(text):
    """Enforce the competition gate; raise ValueError on any failure."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry is %d characters, must be %d-%d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8 text
    return text


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    text = validate(ENTRY)
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
