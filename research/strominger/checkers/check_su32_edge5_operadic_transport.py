"""SCC entrypoint: execute the Node checker afresh, preserving failure status."""
from pathlib import Path
import json
import subprocess

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[3]
    done = subprocess.run(
        ['node', 'research/strominger/checkers/check_su32_edge5_operadic_transport.mjs'],
        cwd=root, capture_output=True, text=True, encoding='utf-8',
    )
    if done.returncode:
        print(done.stdout)
        print(done.stderr)
        raise SystemExit(done.returncode)
    print(json.dumps(json.loads(done.stdout), indent=2))
