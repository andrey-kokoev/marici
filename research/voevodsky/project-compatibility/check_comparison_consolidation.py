"""Fresh headless closure of eight scoped comparison/source audits."""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
checks=[
 ('check_spectral_observer_completion.py','spectral-observer-compatible-completion.json'),
 ('check_contact_primary_typing.py','contact-primary-operator-typing.json'),
 ('check_contact_external_legs.py','contact-external-leg-comparison.json'),
 ('check_contact_physical_scaling.py','contact-physical-boundary-scaling.json'),
 ('check_contact_route_density.py','contact-route-density-restoration.json'),
 ('check_positive_sheet_normal_jets.py','positive-sheet-normal-integration.json'),
 ('check_restored_threshold_continuation.py','restored-period-threshold-continuation.json'),
 ('check_threshold_regulator_match.py','threshold-regulator-consolidation.json')]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before={name:digest(HERE/name) for name,_ in checks};results=[]
for name,receipt in checks:
 run=subprocess.run([sys.executable,str(HERE/name)],capture_output=True,text=True,timeout=120)
 if run.returncode:raise RuntimeError(name+'\n'+run.stdout+'\n'+run.stderr)
 packet=json.loads((HERE/receipt).read_text(encoding='utf-8'))
 assert packet['passed'] and packet['source_unchanged'],name
 results.append({'checker':name,'receipt':receipt,'passed':True,'receipt_sha256':digest(HERE/receipt)})
assert before=={name:digest(HERE/name) for name,_ in checks}
report={'passed':True,'checker_count':len(checks),'checker_sources_unchanged':True,'results':results,'scope':'Fresh finite headless audits. Written analytic proofs, physical contour/readout admission and uncontracted operator lift remain separate.'}
(HERE/'comparison-consolidation-closure.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
