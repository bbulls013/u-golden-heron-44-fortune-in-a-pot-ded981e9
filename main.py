#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty u-golden-heron-44-fortune-in-a-pot-ded981e9.

Writes one kind, funny fortune for the houseplant on the windowsill to
/output/entry.txt. The fortune is a fixed string, so every run produces
byte-identical output: fully deterministic, no randomness, no network,
no environment input.
"""

from pathlib import Path

FORTUNE = (
    "This week, the sun will find your favourite leaf on the sill, "
    "and your keeper will swear you leaned in to meet it."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = FORTUNE.strip()
    if not (1 <= len(text) <= 120):
        raise SystemExit(f"fortune is {len(text)} characters, must be 1-120")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
