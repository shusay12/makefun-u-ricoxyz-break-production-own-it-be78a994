#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the instant it breaks
production to /output/entry.txt. Python 3.13 stdlib only, no network,
fully deterministic: the same line every run.
"""

import os

ENTRY = "I deployed untested code straight to prod and killed checkout. The bug is me."


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > 200 or "\n" in text:
        raise ValueError("entry must be one line of 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
