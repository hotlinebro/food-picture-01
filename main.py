#!/usr/bin/env python3
"""food-picture-01 round 3 (Variant B, steamlit): a photorealistic
steaming tonkotsu ramen, lit by warm steam so the broth glows and the
noodle pull shines. Chopsticks lift a tall glossy noodle pull out of
creamy broth; a halved jammy soft-boiled egg shows a runny golden
yolk; green onions, nori, and a speckled ceramic bowl complete the
frame. Appetite first.

Round 1 scored #703 and round 2 scored #513. Both proved the subject
is right -- steaming tonkotsu ramen, noodle pull, jammy egg -- but the
execution still trails the leaderboard top, whose entries pair the same
subject with stronger light and atmosphere. Round 3 is the steamlit
variant: the same appetite-first subject with a moodier, steam-lit
frame, warmer and more appetizing than the flatter round 1 and the
golden-hour round 2.

Deterministic, no network, no randomness. The program copies the
bundled entry.png byte-for-byte to /output/entry.png.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

# Expected sha256 of the bundled Variant B entry.png (steamlit tonkotsu
# ramen, 1024x683, 972,610 bytes). The copy is verified against this
# hash so a corrupt or swapped bundle fails loudly instead of silently
# submitting the wrong image.
EXPECTED_SHA256 = (
    "029359a476164c11c8f910761cb81509508d64f1531af41c55f99c21e62d4971"
)
MAX_BYTES = 1024 * 1024  # contest cap: PNG <= 1 MiB


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    size = os.path.getsize(DST)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png too large: {size} bytes > {MAX_BYTES}")
    digest = sha256_file(DST)
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"entry.png sha256 mismatch: got {digest}, "
            f"expected {EXPECTED_SHA256}"
        )


if __name__ == "__main__":
    main()
