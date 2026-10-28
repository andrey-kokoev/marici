"""SCC entrypoint: fresh Node execution, no cached test-success inference."""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
if __name__ == '__main__':
    done = subprocess.run(['node', 'research/strominger/checkers/check_su32_signed_reference_encoder.mjs', '--record'], cwd=ROOT, capture_output=True, text=True)
    if done.returncode:
        print(done.stdout)
        print(done.stderr)
        raise SystemExit(done.returncode)
    result = json.loads(done.stdout)
    result['passed'] = result['status'] == 'passed'
    result['admitted_scope'] = 'Occurrence-reference encoding and finite static-cell-label obstruction, not global payload transport or a native phase law'
    result['residuals'] = ['Signed-record-to-five-slot encoding absent', 'Occurrence transition and reconciliation maps absent', 'Incidence admits both common and independent phase actions']
    result['next_falsifier'] = 'Test a source-specified occurrence transition on shared records and its claimed phase intertwiner.'
    print(json.dumps(result, indent=2))
