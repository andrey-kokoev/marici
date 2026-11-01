"""Fresh SCC replay of the global-wiring boundary extraction and hostile."""
from pathlib import Path
import json
import subprocess

if __name__ == '__main__':
    done = subprocess.run(
        ['node', 'research/strominger/checkers/check_su32_native_boundary_extraction.mjs'],
        cwd=Path(__file__).resolve().parents[3], capture_output=True,
        text=True, encoding='utf-8',
    )
    if done.returncode:
        print(done.stdout)
        print(done.stderr)
        raise SystemExit(done.returncode)
    print(json.dumps(json.loads(done.stdout), indent=2))
