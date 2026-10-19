from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[3]
if __name__ == '__main__':
    sys.exit(subprocess.run(['node', str(ROOT / 'research/strominger/checkers/check_three_realization_axes.mjs')], cwd=ROOT).returncode)
