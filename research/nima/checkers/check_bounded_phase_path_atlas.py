"""SCC adapter for the source-bound Node atlas checker; no alternate semantics."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
if __name__ == "__main__":
    result = subprocess.run(
        ["node", str(Path(__file__).with_suffix(".mjs"))], cwd=ROOT, check=False
    )
    sys.exit(result.returncode)
