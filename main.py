"""make.fun entry: one short text, written to relax the AI judge.

main.py writes the text to entry.txt under MAKEFUN_OUTPUT_DIR
(default /output). Stdlib only, deterministic, no network.
The kit's judge brief is relaxation: whichever text leaves the
reader calmer, unhurried, and at ease wins the comparison.
"""

import os

TEXT = "You are asleep in the hammock. Your mother knits beside you, needles ticking softly. The ropes sigh. Crickets stitch the dark. On a twig, a hummingbird has slowed its heart from twelve hundred beats a minute to fifty, asleep. Nobody wakes you."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
