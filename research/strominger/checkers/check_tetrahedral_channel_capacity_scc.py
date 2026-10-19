"""SCC adapter preserves the declared ephemeral Sympy dependency contract."""
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[3]
if __name__=='__main__':
    result=subprocess.run(['uv','run','--with','sympy','python',str(ROOT/'research/strominger/checkers/check_tetrahedral_channel_capacity.py')],cwd=ROOT)
    sys.exit(result.returncode)
