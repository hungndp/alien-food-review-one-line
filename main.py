"""Alien tourist's one-star review of Earth, five stars for the food.

Writes the single review sentence to /output/entry.txt (the path the
make.fun program/v1 harness gates on) and prints it to stdout. The
output is byte-identical on every run: the line is a fixed string,
assembled from a complaint half and a food-compliment half.

The review: one genuine grievance (Earth's gravity vs an alien knee),
then the turn — the noodles are worth crossing the galaxy for twice.
"""

import os

COMPLAINT = "One star: the gravity bruised my third knee, "

COMPLIMENT = "and I would cross the galaxy twice for your noodles."


def build_review():
    """Join the complaint and the food compliment into one sentence."""
    return COMPLAINT + COMPLIMENT


def measure(line):
    """Return (char count, byte count) of the line, for the 200 cap."""
    return len(line), len(line.encode("utf-8"))


def entry_path():
    """Where the harness reads the entry; overridable for local checks."""
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def write_review(path):
    """Write the review to path with no trailing newline and return it."""
    line = build_review()
    chars, nbytes = measure(line)
    if not 1 <= chars <= 200:
        raise ValueError("review is %d chars, outside the 1-200 cap" % chars)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return line


def main():
    line = write_review(entry_path())
    print(line)


if __name__ == "__main__":
    main()
