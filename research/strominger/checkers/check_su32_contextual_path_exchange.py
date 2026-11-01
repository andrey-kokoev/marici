"""Fresh replay of the contextual exchange and derived attachment lift."""
from pathlib import Path
import subprocess

if __name__ == '__main__':
    done = subprocess.run(
        ['node', 'research/strominger/checkers/check_su32_contextual_path_exchange.mjs'],
        cwd=Path(__file__).resolve().parents[3], capture_output=True,
        text=True, encoding='utf-8',
    )
    print(done.stdout)
    if done.returncode:
        print(done.stderr)
    raise SystemExit(done.returncode)
