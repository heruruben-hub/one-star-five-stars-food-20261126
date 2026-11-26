#!/usr/bin/env python3
"""Entry for make.fun — "One Star, Five Stars for the Food".

Writes a single sentence (at most 200 characters) to /output/entry.txt:
a one-star review of Earth from an alien tourist that still slips in a
real compliment about the food.

The sentence is validated against the competition gate before writing:
1-200 characters, not only white space, a single line.
"""

import os

ENTRY = (
    "One star: it rains without warning, the locals worship glowing "
    "rectangles, and the toilets are a puzzle — but the street noodles "
    "taste like the universe apologising."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: a single terminal full stop, and no other
    # sentence-ending punctuation hiding a second sentence inside.
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    if "!" in text or "?" in text:
        raise ValueError("entry must be exactly one sentence")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
