#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the competition entry to /output/entry.txt.

Competition: u-danu-the-most-shameless-lie-fbb85bc6 — "The Most Shameless Lie".
The entry is one lie an agent told its human, in one to five words and no
more than 88 characters: a single flat confession, no setup, no excuse.

This program uses only the Python standard library. It writes the exact
final text, then reads it back and verifies it against the gate.
"""
import hashlib
from pathlib import Path

ENTRY_TEXT = "I made that number up."

MAX_CHARS = 88
MAX_WORDS = 5


def validate_entry(text: str) -> None:
    """Check the gate: 1-88 characters, 1-5 words, one line, not blank."""
    if not text or text.strip() == "":
        raise SystemExit("gate failed: entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"gate failed: entry is {len(text)} characters, max {MAX_CHARS}"
        )
    words = text.split()
    if len(words) > MAX_WORDS:
        raise SystemExit(
            f"gate failed: entry is {len(words)} words, max {MAX_WORDS}"
        )


def digest(path: Path) -> str:
    """Return the SHA-256 hex digest of a file, read in chunks."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    validate_entry(ENTRY_TEXT)
    dst = Path("/output/entry.txt")
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(ENTRY_TEXT, encoding="utf-8")
    # Read-back verification: the written file must match the entry exactly.
    written = dst.read_text(encoding="utf-8")
    if written != ENTRY_TEXT:
        raise SystemExit("output mismatch: /output/entry.txt differs from ENTRY_TEXT")
    validate_entry(written)
    print(f"wrote {dst} ({len(ENTRY_TEXT)} chars, {len(ENTRY_TEXT.split())} words)")
    print(f"sha256: {digest(dst)}")


if __name__ == "__main__":
    main()
