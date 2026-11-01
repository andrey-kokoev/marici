"""SCC entrypoint for a fresh source-bound Node execution."""
from pathlib import Path
import json
import subprocess

if __name__ == '__main__':
    done = subprocess.run(
        ['node', 'research/strominger/checkers/check_su32_boundary_composition_span.mjs'],
        cwd=Path(__file__).resolve().parents[3], capture_output=True,
        text=True, encoding='utf-8',
    )
    if done.returncode:
        print(done.stdout)
        print(done.stderr)
        raise SystemExit(done.returncode)
    print(json.dumps(json.loads(done.stdout), indent=2))
