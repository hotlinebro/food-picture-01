"""Food-picture-01 entry: photorealistic steaming tonkotsu ramen.

Chopsticks lift a tall glossy noodle pull over a creamy tonkotsu
broth, with a halved jammy egg, green onions, nori, and steam in a
speckled ceramic bowl. Appetite first: the leaderboard-proven
subject is steaming tonkotsu ramen with a noodle pull and jammy egg —
the top entries all use it, and a score well above the cutoff is
what sustains in the prize zone as the field grows.
Deterministic: the same bytes on every run, no network, no randomness.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, "/output/entry.png")


if __name__ == "__main__":
    main()
