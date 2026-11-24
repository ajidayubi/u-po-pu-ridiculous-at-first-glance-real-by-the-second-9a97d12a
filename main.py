#!/usr/bin/env python3
"""One-sentence absurd-invention pitch writer.

Writes one pitch sentence to /output/entry.txt: naming rights to potholes,
sponsored for $29 a month by the commuters whose tyres the crater ate,
with the city splitting the repair fund. Ridiculous at first glance, real
on a second look. The write is atomic and independent of the working
directory.
"""

import os

PITCH = (
    "We sell naming rights to potholes: for $29 a month, commuters sponsor "
    "the crater that ate their tyre, and the city splits the repair fund "
    "with us."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    pitch = PITCH.strip()
    if not pitch or len(pitch) > MAX_CHARS:
        raise ValueError("pitch must be 1-200 non-blank characters")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(pitch)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
