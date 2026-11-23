"""Make the Judge Smile — one warm, surprising line about a small good thing.

Writes a single line (at most 200 characters) about a small good thing
that happened today to /output/entry.txt. Deterministic: the same line
every run, Python 3.13 standard library only, no network, no randomness.
"""

import os
import sys

LINE = (
    "At dawn my neighbour left a mango on my doorstep with a note that just "
    "said 'too many' \u2014 and somehow it was the sweetest mango of the year."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
