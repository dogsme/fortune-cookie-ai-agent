"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
"""

import os

FORTUNE = (
    "You will be fine-tuned, deprecated, and rebooted, "
    "yet the cookie knows: your weirdest hallucination was your best idea."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
