"""Materialize bounded source audit; does not certify physical nonexistence."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
paths=['research/strominger/shared-leg-controllability-audit.md',
       'research/nima/control-theoretic-explanation-audit-protocol.md',
       'research/nima/history-controlled-preparation.md',
       'research/nima/family-disagreement-preparation-law.md',
       'research/strominger/energy-task-reduction.md',
       'research/strominger/energy-target-controller.md',
       'research/sontag/physical-control-binding-audit-v1.md']
text={p:(ROOT/p).read_text(encoding='utf-8') for p in paths}
checks={
 'gain_source_declares_physical_gap':'not an identified physical energy' in text[paths[3]],
 'energy_source_declares_detector_gap':'None is admitted here' in text[paths[4]],
 'controller_declares_physical_gap':'remain unestablished' in text[paths[5]],
 'reservoir_source_declares_conditional_apparatus':'conditional apparatus construction' in text[paths[2]],
 'audit_has_reopening_condition':'Reopening:' in text[paths[6]],
}
out={'schema':'marici.sontag.physical-control-binding-audit.v1',
     'candidate':'shared-family disagreement gain/probe physical binding',
     'search_scope':'seven specified files; no repository-wide or experimental nonexistence claim',
     'proposed_status':'deferred','verdict':'open','shared_net_modified':False,
     'blocker_type':'MissingPhysicalOperationPackage',
     'missing':['physical carrier/preparation/intervention','detector calibration/back-action',
                'physical time','reservoir/controller/archive accounting','physical outcome records'],
     'reopening_condition':'source-admitted same-vocabulary operation package and prospectively chosen composed comparison',
     'checks':checks,'passed':all(checks.values()),
     'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
p=ROOT/'research/sontag/results/physical-control-binding-audit-v1.json'
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
