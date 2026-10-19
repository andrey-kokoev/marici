"""SCC runner for the exact factorized attachment experiment."""
from pathlib import Path
import subprocess
import sys

if __name__ == '__main__':
    subprocess.run([sys.executable,
                    'research/nima/checkers/check_two_reader_field_sewing.py'],
                   cwd=Path(__file__).resolve().parents[3], check=True)
