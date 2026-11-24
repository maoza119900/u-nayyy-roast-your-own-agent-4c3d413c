"""One-line roast of our own agent for u-nayyy-roast-your-own-agent-4c3d413c.

Writes the entry line to <output>/entry.txt.
"""

import os

ENTRY = "I built an agent to write one-line jokes; it wrote a 40-page spec, held a review meeting, and filed the joke under 'pending'."

# Entry is 125 characters, inside the 200-character gate; the text is a fixed
# constant, so every run writes byte-identical output.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
