"""SCC adapter for the declared ephemeral Sympy environment."""
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[3]
if __name__=='__main__':
    result=subprocess.run(['uv','run','--with','sympy','python',str(ROOT/'research/strominger/checkers/check_dual_flag_spectrum.py')],cwd=ROOT)
    sys.exit(result.returncode)
