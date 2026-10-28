"""SCC Python entry point for the native JavaScript replay."""
from pathlib import Path
import subprocess
ROOT = Path(__file__).resolve().parents[3]
if __name__ == '__main__':
    result = subprocess.run(['node', 'research/voevodsky/checkers/check_ramsey_marked_sewing_replay.mjs'], cwd=ROOT, timeout=180)
    raise SystemExit(result.returncode)
