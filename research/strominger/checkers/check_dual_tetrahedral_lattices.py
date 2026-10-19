"""SCC adapter for exact reciprocal tetrahedral geometry and real browser tests."""
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[3]
if __name__ == '__main__':
    result = subprocess.run(['node', str(ROOT/'research/strominger/checkers/check_dual_tetrahedral_lattices.mjs')], cwd=ROOT)
    sys.exit(result.returncode)
