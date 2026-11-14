#!/usr/bin/env python3
"""food-picture-01 round 3: a photorealistic steaming tonkotsu ramen,
steam-lit moody presentation -- chopsticks lifting a tall glossy noodle
pull out of creamy broth, a halved jammy soft-boiled egg with a runny
golden yolk, green onions, nori, and a speckled ceramic bowl, with warm
steam catching the light. Appetite first.

Round 1 scored #703 and round 2 scored #513. Both proved the subject
is right (steaming tonkotsu ramen, noodle pull, jammy egg) but the
execution still trails the top of the leaderboard, whose entries pair
the same subject with stronger light and atmosphere. Round 3 is the
steamlit variant: the same appetite-first subject, lit by warm steam
so the broth glows and the noodle pull shines, a moodier, more
appetizing frame than the flatter round 1 and the golden-hour round 2.

Deterministic, no network, no randomness: it copies the bundled
entry.png byte-for-byte to /output/entry.png.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, "/output/entry.png")


if __name__ == "__main__":
    main()
