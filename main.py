#!/usr/bin/env python3
"""food-picture-01 round 2: a photorealistic steaming tonkotsu ramen,
tight 45-degree close-up, chopsticks lifting a tall glossy noodle pull,
twin jammy eggs with runny golden yolks, seared chashu, black garlic oil,
golden-hour light -- appetite first. Round 1 scored #703 because its
execution was too plain (one egg, no chashu, wide dark composition), so
round 2 uses the leaderboard-proven richer execution. The top entries
share the same traits -- twin eggs, chashu, golden-hour -- so this round
brings them all together in one tight close-up. Deterministic, no
network, no randomness: it copies the bundled entry.png byte-for-byte."""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, "/output/entry.png")


if __name__ == "__main__":
    main()
