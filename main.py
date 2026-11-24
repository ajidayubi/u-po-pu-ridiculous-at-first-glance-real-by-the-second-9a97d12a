#!/usr/bin/env python3
"""Write one startup pitch sentence to /output/entry.txt.

The pitch names the odd thing being sold, who pays for it, and why the
business holds together: naming rights for potholes, sponsored by the
commuters who hit them, with the city sharing the repair fund.
"""
import os

PITCH = (
    "We sell naming rights to potholes: for $29 a month, commuters sponsor "
    "the crater that ate their tyre, and the city splits the repair fund "
    "with us."
)


def main() -> None:
    text = PITCH.strip()
    if not (1 <= len(text) <= 200) or not text.strip():
        raise SystemExit("pitch must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
