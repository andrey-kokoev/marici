"""Fresh bounded replay of the fixed-chart source audit."""
from pathlib import Path
import subprocess

if __name__ == '__main__':
    done = subprocess.run(
        ['node', 'research/strominger/checkers/check_su32_release_source_audit.mjs'],
        cwd=Path(__file__).resolve().parents[3], capture_output=True,
        text=True, encoding='utf-8',
    )
    print(done.stdout)
    if done.returncode:
        print(done.stderr)
    raise SystemExit(done.returncode)
