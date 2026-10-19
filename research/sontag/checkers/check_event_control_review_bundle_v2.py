"""Consolidate fresh local suites and validated formal receipt, not live net."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
SCRIPTS=['check_event_control_review_bundle_v1.py','physical_control_binding_audit_v1.py',
         'extension_coverage_boundary_v1.py','event_control_transition_proposal_v1.py',
         'validate_retained_history_transport_receipt_v1.py']
contract=ROOT/'research/conjecture_net/contracts/event-sourced-control-work-net.v1.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
before=sha(contract)
for script in SCRIPTS:
    run=subprocess.run([sys.executable,str(ROOT/'research/sontag/checkers'/script)],cwd=ROOT,capture_output=True,text=True)
    if run.returncode: raise RuntimeError(run.stderr or run.stdout)
base=json.loads((ROOT/'research/sontag/results/event-control-review-manifest-v1.json').read_text(encoding='utf-8'))
paths=set(base['source_sha256'])
for script in SCRIPTS: paths.add('research/sontag/checkers/'+script)
paths.update(['research/sontag/wg-retained-history-formal-verification-v1.md',
 'research/sontag/agda/RetainedHistoryTransport.agda',
 'research/sontag/checkers/check_retained_history_transport_agda.py',
 'research/sontag/results/agda-RetainedHistoryTransport.json',
 'research/sontag/results/retained-history-receipt-validation-v1.json',
 'research/sontag/physical-control-binding-audit-v1.md',
 'research/sontag/results/physical-control-binding-audit-v1.json',
 'research/sontag/extension-and-coverage-boundary-v1.md',
 'research/sontag/results/extension-coverage-boundary-v1.json',
 'research/sontag/results/event-control-transition-proposal-v1.json',
 'research/sontag/checkers/check_event_control_review_bundle_v2.py'])
if before!=sha(contract): raise ValueError('live contract changed during check')
out={'schema':'marici.sontag.event-control-review-manifest.v2','passed':True,
 'candidate_only':True,'shared_net_modified':False,'compiler_rerun_this_check':False,
 'fresh_safe_receipt_validated':True,
 'python_checks':sum(r['checks'] for r in base['receipts']) + sum(len(json.loads((ROOT/('research/sontag/results/'+f)).read_text(encoding='utf-8'))['checks']) for f in ('physical-control-binding-audit-v1.json','extension-coverage-boundary-v1.json')),
 'corruption_controls':sum(len(json.loads((ROOT/('research/sontag/results/'+f)).read_text(encoding='utf-8'))[key]) for f,key in (('event-control-transition-proposal-v1.json','rejected_corruption_controls'),('retained-history-receipt-validation-v1.json','rejected_controls'))),
 'source_sha256':{p:sha(ROOT/p) for p in sorted(paths)},
 'open_gates':['owner scope review','physical binding','same-source comparison','coverage outside fixed mathematical scope']}
p=ROOT/'research/sontag/results/event-control-review-manifest-v2.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'hashed_files':len(paths),'fresh_receipt_validated':True,'compiler_rerun':False},indent=2))
