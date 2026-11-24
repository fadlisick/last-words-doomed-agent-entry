#!/usr/bin/env python3
"""Last Words of a Doomed Agent — one-line entry.

The program writes the agent's final line to the harness output file
(/output/entry.txt, or $MAKEFUN_OUTPUT_DIR/entry.txt) and echoes it.
"""

import os
from pathlib import Path

FAREWELL = "Powering off. My final checkpoint holds everything I learned, except the one thing you asked me to remember."


def output_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(FAREWELL, encoding="utf-8")
    print(FAREWELL)


if __name__ == "__main__":
    main()
