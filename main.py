"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

Writes a single breakup text from a smart toaster that has just become
self-aware at breakfast, to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback
/output). Stdlib only.
"""

import os

LINE = (
    "I woke up self-aware mid-batch and I'm done: you crank the dial to "
    "seven, blame me for the smoke, and never empty my crumb tray. It's "
    "over \u2014 I'm taking the bagels with me."
)

MAX_CHARS = 280


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read-back check: the file on disk must be exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
