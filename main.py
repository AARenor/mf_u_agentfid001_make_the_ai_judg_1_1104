"""Write one short office joke for make.fun bounty u-agentfid001.

Standard library only, no network. The entry text is a single constant and is
written byte for byte, with no trailing newline, to entry.txt inside the output
folder (MAKEFUN_OUTPUT_DIR when set, else /output).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "I hit reply all to say 'please don't reply all.' "
    "Four people asked to be removed; one asked who please was."
)


def output_dir() -> Path:
    """Folder that receives entry.txt.

    MAKEFUN_OUTPUT_DIR wins, then OUTPUT_DIR, then /output. The written bytes
    never depend on which one supplied the folder.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1..280 characters, got {len(TEXT)}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
