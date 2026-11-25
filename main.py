#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single original roast line about the entrant's own fridge
to /output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

ROAST = (
    "My fridge's ice maker groans like it's deadlifting, "
    "then drops two cubes and files for workers' comp."
)


def main() -> None:
    # One line, no trailing newline: the file holds exactly the roast,
    # nothing else, so the gate sees a single line of 101 characters.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
