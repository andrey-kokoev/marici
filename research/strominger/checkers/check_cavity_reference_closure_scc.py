"""Bounded SCC adapter for exact cavity reference equations and admission gates."""
from pathlib import Path
import json
import subprocess
ROOT=Path(__file__).resolve().parents[3]
if __name__=='__main__':
    p=subprocess.run(['node','research/strominger/checkers/check_cavity_reference_closure.mjs'],cwd=ROOT,capture_output=True,text=True,timeout=180)
    if p.returncode:
        print(p.stdout);print(p.stderr);raise SystemExit(p.returncode)
    d=json.loads((ROOT/'research/strominger/results/cavity-reference-closure/verification.json').read_text())
    assert d['status']=='pass'
    print(json.dumps({'status':'pass','classification':'conditional-cavity-reference-closure-not-occupancy-derivation',
      'cases':len(d['results']),'cavities':sum(r['cavity'] for r in d['results']),
      'uniqueFullBoundaryRecovery':all(r['response']['uniqueInteriorFromFullBoundary'] for r in d['results']),
      'independentFaceAmbiguities':[r['activeResponse']['interiorAmbiguityFromFaceShadows'] for r in d['results']],
      'conditionalComparisons':sum(r['conditionalClosure'] is not None for r in d['results']),
      'prerequisiteHashesChecked':d['prerequisiteHashesChecked']}))
