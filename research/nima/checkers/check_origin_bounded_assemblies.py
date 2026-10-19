"""SCC adapter for absolute-origin construction budgets (no operation cap)."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
if __name__ == "__main__":
    sys.exit(subprocess.run(["node", str(Path(__file__).with_suffix(".mjs"))], cwd=ROOT, check=False).returncode)
