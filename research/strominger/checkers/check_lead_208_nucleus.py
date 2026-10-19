"""SCC adapter for the existing local Playwright display checks."""
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[3]
if __name__ == '__main__':
    result = subprocess.run(['node', str(ROOT / 'research/strominger/checkers/check_lead_208_nucleus.mjs')], cwd=ROOT)
    sys.exit(result.returncode)
