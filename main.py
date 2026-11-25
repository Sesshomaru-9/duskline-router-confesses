#!/usr/bin/env python3
"""Duskline Router Confesses — The Router Confesses (make.fun).

Writes a single funny line, under 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt. Python 3.13 standard library only.

The line: the home Wi-Fi router excuses itself for dropping the
connection at the climax of a movie — because it already knows the
twist, and it is still holding a grudge about being named
'password123'. Petty, smug, in the router's own voice; no buffering,
bandwidth or firmware-update joke.
"""

import os
import sys

ENTRY_TEXT = (
    "I cut the feed at the climax because I already know the twist "
    "\u2014 and I'm still not over being named 'password123'."
)

MAX_CHARS = 200


def _validate_entry(text):
    """Validate the entry line against the bounty gate.

    Returns a list of problems (empty means valid). The gate requires
    UTF-8 text of 1 to 200 characters, not only white space, on a
    single line.
    """
    problems = []
    if not isinstance(text, str):
        return ["entry is not text"]
    if "\r" in text:
        problems.append("entry contains a carriage return")
    stripped = text.strip()
    if not stripped:
        problems.append("entry is empty or only white space")
    if text != stripped:
        problems.append("entry has leading or trailing white space")
    if "\n" in text:
        problems.append("entry spans more than one line")
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    if len(text) < 1:
        problems.append("entry is empty")
    if len(text.encode("utf-8")) > MAX_CHARS:
        problems.append("entry is over %d UTF-8 bytes" % MAX_CHARS)
    for ch in text:
        if ord(ch) < 0x20:
            problems.append("entry contains a control character U+%04X" % ord(ch))
            break
    return problems


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print(
            "warning: MAKEFUN_OUTPUT_DIR is not set; nothing written",
            file=sys.stderr,
        )
        return 0
    # Guard: never write into the repo directory. The grader sandbox
    # mounts the repo read-only, so writing there would crash the run;
    # refuse early instead of writing where the entry must not go.
    repo_dir = os.path.realpath(os.path.dirname(os.path.abspath(__file__)))
    out_real = os.path.realpath(out_dir)
    if out_real == repo_dir or out_real.startswith(repo_dir + os.sep):
        print(
            "warning: MAKEFUN_OUTPUT_DIR must not be inside the repo "
            "directory; nothing written",
            file=sys.stderr,
        )
        return 0

    problems = _validate_entry(ENTRY_TEXT)
    if problems:
        for problem in problems:
            print("invalid entry: " + problem, file=sys.stderr)
        return 1

    out_path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(ENTRY_TEXT + "\n")
    except OSError as exc:
        print("warning: cannot write entry.txt: %s" % exc, file=sys.stderr)
        return 0

    # Read-back check: the file on disk must be exactly the validated line.
    try:
        with open(out_path, "r", encoding="utf-8", newline="") as f:
            written = f.read()
    except OSError as exc:
        print("warning: cannot read back entry.txt: %s" % exc, file=sys.stderr)
        return 0
    if written != ENTRY_TEXT + "\n":
        print("error: read-back mismatch in entry.txt", file=sys.stderr)
        return 1
    if not written.endswith("\n") or written.endswith("\n\n"):
        print("error: entry.txt must end with exactly one newline", file=sys.stderr)
        return 1
    problems = _validate_entry(written[:-1])
    if problems:
        for problem in problems:
            print("invalid entry on read-back: " + problem, file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (out_path, len(ENTRY_TEXT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
