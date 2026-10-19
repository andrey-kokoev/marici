"""SCC adapter: a passing audit retains, rather than hides, hypothesis failures."""
from pathlib import Path
import json
import subprocess
ROOT=Path(__file__).resolve().parents[3]
if __name__=='__main__':
    p=subprocess.run(['node','research/strominger/checkers/check_proton_witness_faces.mjs'],cwd=ROOT,capture_output=True,text=True,timeout=180)
    if p.returncode:
        print(p.stdout);print(p.stderr);raise SystemExit(p.returncode)
    d=json.loads((ROOT/'research/strominger/results/proton-witness-faces/verification.json').read_text())
    assert d['status']=='pass' and not d['resourceUnknown']
    print(json.dumps({'status':'pass','classification':'body-capacity-obstructions-and-face-closure-cavity-residuals',
                      'cases':len(d['rows']),'bodyRulePasses':sum(r['bodyRule']['passes'] for r in d['rows']),
                      'faceRulePasses':sum(r['faceRule']['passes'] for r in d['rows']),
                      'allFaceRulePass':d['allFaceRulePass'],
                      'independentCavityChecks':d['cavityCertificatesIndependentlyChecked']}))
