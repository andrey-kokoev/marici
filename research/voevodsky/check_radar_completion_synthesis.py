"""Fresh headless audit of the scoped radar chain; modifies only own receipts."""
from pathlib import Path
import subprocess
import sys
import json
import hashlib
from datetime import datetime,timezone

root=Path(__file__).resolve().parents[2];base=Path(__file__).resolve().parent
jobs=(
 ('check_causal_radar_completion.py','causal-radar-completion.json',42),
 ('check_radar_curvature_inverse.py','radar-curvature-inverse.json',28),
 ('check_finite_radar_protocol.py','finite-radar-protocol.json',21),
 ('check_physical_radar_protocol.py','physical-radar-protocol.json',18),
 ('check_radar_frame_comparison.py','radar-frame-comparison.json',16),
 ('check_radar_apparatus_certificate.py','radar-apparatus-certificate.json',42))
results=[]
for script,receipt,expected in jobs:
    proc=subprocess.run([sys.executable,str(base/script)],cwd=root,capture_output=True,text=True,timeout=180)
    log=root/'temp'/('radar-synthesis-'+script+'.log');log.parent.mkdir(exist_ok=True)
    log.write_text(proc.stdout+'\n'+proc.stderr,encoding='utf-8')
    data=json.loads((base/receipt).read_text(encoding='utf-8')) if proc.returncode==0 else {}
    checks=data.get('checks',{})
    results.append(dict(script=str((base/script).relative_to(root)),exit_code=proc.returncode,
        check_count=len(checks),expected_count=expected,
        passed=proc.returncode==0 and data.get('passed') is True and len(checks)==expected and all(checks.values()),
        script_sha256=hashlib.sha256((base/script).read_bytes()).hexdigest(),
        receipt=str((base/receipt).relative_to(root)),receipt_sha256=hashlib.sha256((base/receipt).read_bytes()).hexdigest() if (base/receipt).exists() else None,
        log=str(log.relative_to(root))))
    if not results[-1]['passed']:print(proc.stdout[-3000:]+proc.stderr[-3000:])
owner_paths=['research/nima/native-table-equivalence.md','research/nima/agda/NativeTidalTableReadout.agda']
owner_evidence={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in owner_paths}
out=dict(passed=all(r['passed'] for r in results),fresh_utc=datetime.now(timezone.utc).isoformat(),python=sys.version,
    runs=results,total_exact_checks=sum(r['check_count'] for r in results),
    owner_source_read_hashes=owner_evidence,
    owner_verification_scope='Current published note and direct tidal source read; owner Agda not freshly compiled by this audit and no owner artifact modified.',
    scientific_scope='Written analytic theorems, finite exact controls and rational physical-ray enclosures; no empirical validation or owner admission of the radar package.')
(base/'radar-completion-synthesis.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
