"""Fresh SCC adapter for the set-valued layer-4 candidate test."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
if __name__ == '__main__':
    done = subprocess.run(['node','research/strominger/checkers/check_su32_layer4_comparison.mjs','--record'],cwd=ROOT,capture_output=True,text=True)
    if done.returncode:
        print(done.stdout)
        print(done.stderr)
        raise SystemExit(done.returncode)
    result = json.loads(done.stdout)
    result['admitted_scope'] = 'Set-valued fiber-product candidate at native comparison incidences; retains both derivations; no native filler or phase-law admission'
    result['next_falsifier'] = result.pop('next')
    print(json.dumps(result,indent=2))
