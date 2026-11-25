#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, then the unsent message
itself, one line written exactly as it was typed, no explanation after.
"""

import os

TO_LINE = "To: my brother"
MESSAGE = (
    "The voicemail where you said you'd call back on Tuesday is still "
    "on my phone, and I keep it because deleting it would mean "
    "admitting you never will."
)

ENTRY = TO_LINE + "\n" + MESSAGE + "\n"


def main() -> None:
    assert 1 <= len(ENTRY.strip()) <= 260, "entry must be 1-260 chars"
    assert len(MESSAGE) <= 200, "message must be at most 200 chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
