"""SCC entrypoint: fresh Agda rank lemma, then the source-bound occurs check."""
from pathlib import Path
import json
import subprocess
import sys

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[3]
    commands = [
        [sys.executable, 'research/strominger/checkers/check_finite_payload_occurs_agda.py'],
        ['node', 'research/strominger/checkers/check_su32_static_payload_identification.mjs'],
    ]
    for command in commands:
        done = subprocess.run(command, cwd=root, capture_output=True, text=True, encoding='utf-8')
        if done.returncode:
            print(done.stdout)
            print(done.stderr)
            raise SystemExit(done.returncode)
        result = json.loads(done.stdout)
        if not result.get('passed'):
            print(done.stdout)
            raise SystemExit(1)
    print(json.dumps(result, indent=2))
