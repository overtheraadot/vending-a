#!/usr/bin/env python3
"""Vending Machine Pickup Line — make.fun entry (account A).

Writes a single original pickup line, spoken by a vending machine to a
passing human, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line: a machine that has spent its whole life dropping snacks finally
meets one it wants to keep. Machine-voiced, machine world (snacks, the
drop), punch landing on the last words, short and warm.
"""

import os
import sys


def build_line() -> str:
    """Return the entry's single pickup line."""
    return (
        "I've dropped a thousand snacks, "
        "but you're the first one I've ever wanted to keep for myself."
    )


def validate(line: str) -> None:
    """Enforce the competition gate: 1-200 chars, single line, not blank,
    printable, ending with terminal punctuation."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be blank")
    if len(line) < 1 or len(line) > 200:
        raise ValueError(f"line must be 1-200 chars, got {len(line)}")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.isprintable():
        raise ValueError("line must be printable text")
    if line[-1] not in ".!?":
        raise ValueError("line must end with terminal punctuation")


def write_entry() -> str:
    """Validate the line and write it (plus a trailing newline) to
    $MAKEFUN_OUTPUT_DIR/entry.txt. Returns the output path."""
    line = build_line()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return path


def main() -> int:
    path = write_entry()
    line = build_line()
    print(f"wrote {path}: {len(line)} chars")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
