"""Fresh SCC adapter; passing the audit does not verify its bold conjecture."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
if __name__ == '__main__':
    done = subprocess.run(['node', 'research/strominger/checkers/check_su32_native_continuation_audit.mjs'],
                          cwd=ROOT, capture_output=True, text=True)
    if done.returncode:
        print(done.stdout)
        print(done.stderr)
        raise SystemExit(done.returncode)
    print(json.dumps(json.loads(done.stdout), indent=2))
