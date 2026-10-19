"""SCC bridge for the deterministic geometry and real Chromium viewer tests."""
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[3]
if __name__ == '__main__':
    result = subprocess.run(['node', str(ROOT/'research/strominger/checkers/check_particle_overlap_viewer.mjs')], cwd=ROOT)
    sys.exit(result.returncode)
