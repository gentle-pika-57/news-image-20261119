"""news-image-20261119 entry: copy the repo's entry.png to the output dir.

Runs with no network. Writes the same bytes on every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> None:
    if not SRC.is_file():
        raise SystemExit(f"missing image next to main.py: {SRC}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()
