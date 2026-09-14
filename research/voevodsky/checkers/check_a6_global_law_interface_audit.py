#!/usr/bin/env python3
"""Verify the A6 materialization audit against the live pyramid model."""
import copy, hashlib, json, platform
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
AUDIT=ROOT/'research/voevodsky/fixtures/a6_global_law_interface_audit.v1.json'
MODEL=ROOT/'public/experiments/typed-reconciler-cube/coherence-lattice.toml'
RESULT=ROOT/'research/voevodsky/results/a6_global_law_interface_audit.json';CHECKER=Path(__file__).resolve()
a=json.loads(AUDIT.read_text());text=MODEL.read_text(encoding='utf-8')
required_fragments=['id = "A6"\nlabel = "law of compositions"','id = "C1_5"','transport = "T_gamma"','content_target = "K_global"','id = "C1_6"','transport = "T_real"','content_source = "K_global"','content_target = "K_fiber"','status = "schema_only"','status = "uninstantiated"']
expected_slots=['state_object_ref','operator_domain_ref','finite_p2_j2_basis_ref','operator_matrix_ref','sewing_ref','green_form_ref','completion_ref']
def validate(x):
 try:
  slots=x['required_a6_slots']
  return ([s['id'] for s in slots]==expected_slots and all(s['status'] in {'missing','partial'} and s['acceptance_test'] for s in slots) and x['disposition']=={'finite_T_real_executable':False,'first_missing_typed_datum':'state_object_ref for A6','reopening_condition':'materialize the A6 carrier, then its finite p=2, J=2 basis and K_global matrix'})
 except (KeyError,TypeError):return False
def rejected(f):
 x=copy.deepcopy(a);f(x);return not validate(x)
checks={'baseline_valid':validate(a),'live_pyramid_fragments_present':all(f in text for f in required_fragments),'K_global_is_only_symbolic_in_pyramid_model':text.count('K_global')==4,
'finite_transport_correctly_blocked':a['disposition']['finite_T_real_executable'] is False,
'omitted_state_object_gate_rejected':rejected(lambda x:x['required_a6_slots'].pop(0)),
'false_executable_promotion_rejected':rejected(lambda x:x['disposition'].update(finite_T_real_executable=True))}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out={'schema':'marici.voevodsky.a6-global-law-interface-audit-check.v1','passed':all(checks.values()),'checks':checks,'first_missing_typed_datum':a['disposition']['first_missing_typed_datum'],'claim_boundary':'Passing proves that the live pyramid does not materialize A6 enough to define finite T_real; it does not show that no source construction can do so.','execution_receipt':{'command':'python research/voevodsky/checkers/check_a6_global_law_interface_audit.py','python':platform.python_version(),'audit_sha256':digest(AUDIT),'model_sha256':digest(MODEL),'checker_sha256':digest(CHECKER)}}
RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
