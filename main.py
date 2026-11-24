"""Office joke entry for make.fun's "Make the AI Judge Laugh: the Office Joke Open".

Writes one line of office comedy to /output/entry.txt.
"""

import os

JOKE = (
    "I sent a reply-all asking everyone to stop replying-all, "
    "and now 400 colleagues are replying-all to agree with me, one at a time."
)


def main() -> None:
    # Gate: entry must be a single line of 1-200 characters, no trailing whitespace.
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
