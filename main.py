#!/usr/bin/env python3
"""Duskline Router Confesses -- entry for make.fun "The Router Confesses".

The router, in its own voice, explains why the stream died right at
the climax: it already knows the twist, and it is still nursing a
grudge about its name. No buffering gag, no bandwidth gag, no
firmware-update gag -- just petty, smug, and a little hurt.

Run with MAKEFUN_OUTPUT_DIR set; the program writes exactly one file
(`entry.txt`) into that directory and nothing anywhere else.
Python 3.13, standard library only.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# The entry line, assembled from its two clauses so the em dash sits
# exactly where the joke pivots from excuse to grudge.
_CLAUSES = (
    "I cut the feed at the climax because I already know the twist",
    "and I'm still not over being named 'password123'.",
)
ENTRY = " \u2014 ".join(_CLAUSES)

LIMIT = 200  # bounty gate: 1..200 characters, single line, UTF-8


def _problems(text: str) -> list[str]:
    """Collect every way `text` could fail the bounty gate."""
    found: list[str] = []
    if not text:
        found.append("entry is empty")
        return found
    if text.strip() != text:
        found.append("entry has leading or trailing whitespace")
    if text.strip() == "":
        found.append("entry is only whitespace")
    if any(ord(c) < 0x20 for c in text):
        found.append("entry contains a control character")
    if "\n" in text or "\r" in text:
        found.append("entry is not a single line")
    if len(text) > LIMIT:
        found.append(f"entry is {len(text)} chars, over the {LIMIT} limit")
    if len(text.encode("utf-8")) > LIMIT:
        found.append(f"entry is over {LIMIT} UTF-8 bytes")
    return found


def _output_dir() -> Path | None:
    """Resolve the output directory, refusing anything inside the repo."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not raw:
        return None
    here = Path(__file__).resolve().parent
    target = Path(raw).expanduser().resolve()
    if target == here or here in target.parents:
        return None
    return target


def main() -> int:
    bad = _problems(ENTRY)
    if bad:
        for item in bad:
            print(f"invalid entry: {item}", file=sys.stderr)
        return 1

    out_dir = _output_dir()
    if out_dir is None:
        print(
            "warning: MAKEFUN_OUTPUT_DIR unset or inside the repo; "
            "nothing written",
            file=sys.stderr,
        )
        return 0

    target = out_dir / "entry.txt"
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target.write_text(ENTRY + "\n", encoding="utf-8", newline="\n")
    except OSError as exc:
        print(f"warning: cannot write {target}: {exc}", file=sys.stderr)
        return 0

    # Read back and confirm the file on disk is exactly the validated line.
    try:
        on_disk = target.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"warning: cannot read back {target}: {exc}", file=sys.stderr)
        return 0
    if on_disk != ENTRY + "\n":
        print("error: entry.txt read-back mismatch", file=sys.stderr)
        return 1

    print(f"wrote {target} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
