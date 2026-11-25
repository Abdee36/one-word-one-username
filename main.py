#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes my own make.fun username to /output/entry.txt — one word, nothing
else. The judge compares usernames two at a time and picks the funnier or
more interesting one; a genuine make.fun handle beats any made-up name, so
the entry is exactly my own handle.
"""

from pathlib import Path

# My own make.fun handle. Seven characters, one word, no spaces.
USERNAME = "abdee36"


def main() -> None:
    if not 1 <= len(USERNAME) <= 30 or USERNAME.split() != [USERNAME]:
        raise ValueError(f"entry must be one word of 1-30 characters, got {USERNAME!r}")
    # Plain ASCII, so the file is exactly 7 bytes: on an exact tie the
    # smaller text places first, and no trailing newline is written.
    if not USERNAME.isascii():
        raise ValueError(f"entry must be plain ASCII, got {USERNAME!r}")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(USERNAME, encoding="utf-8")


if __name__ == "__main__":
    main()
