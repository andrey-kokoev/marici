#!/usr/bin/env python3
"""Check ten-field SCC/Green conformance coverage without promoting G4."""
import copy, hashlib, json, platform
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
MANIFEST=ROOT/'research/voevodsky/fixtures/g4_green_interface_conformance_manifest.v1.json'
SCC=ROOT/'research/aspect/contracts/theta-rh-interaction-net-state.v2.json'
RESULT=ROOT/'research/voevodsky/results/g4_green_interface_conformance_manifest.json'
CHECKER=Path(__file__).resolve();m=json.loads(MANIFEST.read_text());s=json.loads(SCC.read_text())
green=next(x for x in s['constructors'] if x['id']=='conservative_green_complex')
required=green['required_interface_fields']; rows={x['id']:x for x in m['rows']}
allowed_source={'constructed','constructed_at_finite_cutoff','candidate_constructed','codiagonal_only','entire_source_theorem_and_finite_J2_fixture'}
def validate(x):
 try:
  rr={r['id']:r for r in x['rows']}
  return (list(rr)==required and all(r['source_status'] in allowed_source for r in rr.values()) and
   all(r['g4_comparison_status']=='blocked' for r in rr.values()) and
   all((ROOT/r['evidence']).is_file() and r['residual'] for r in rr.values()) and
   x['promotion_gate']['current']=='blocked')
 except (KeyError,TypeError):return False
def rejected(f):
 x=copy.deepcopy(m);f(x);return not validate(x)
checks={
'baseline_valid':validate(m),'exact_scc_field_order':list(rows)==required,'ten_fields_present':len(rows)==10,
'scc_green_cell_is_open':green['status']=='open' and green['authority_class']=='formal_slot',
'all_evidence_paths_exist':all((ROOT/r['evidence']).is_file() for r in rows.values()),
'all_g4_comparisons_blocked':all(r['g4_comparison_status']=='blocked' for r in rows.values()),
'no_empty_residual':all(bool(r['residual']) for r in rows.values()),
'omitted_field_rejected':rejected(lambda x:x['rows'].pop()),
'false_comparison_promotion_rejected':rejected(lambda x:x['rows'][0].update(g4_comparison_status='compared')),
'missing_evidence_rejected':rejected(lambda x:x['rows'][0].update(evidence='research/voevodsky/missing.md'))}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out={'schema':'marici.voevodsky.g4-green-interface-conformance-check.v1','passed':all(checks.values()),'checks':checks,
'coverage':{'required':10,'source_constructed':sum(r['source_status'] in {'constructed','constructed_at_finite_cutoff'} for r in rows.values()),'source_candidates_or_partial':sum(r['source_status'] not in {'constructed','constructed_at_finite_cutoff'} for r in rows.values()),'g4_compared':0,'g4_blocked':10},
'first_executable_after_exposure':m['promotion_gate']['first_executable_after_exposure'],
'claim_boundary':'Passing certifies complete blocker accounting against the live SCC contract. It certifies no G4 comparison.',
'execution_receipt':{'command':'python research/voevodsky/checkers/check_g4_green_interface_conformance_manifest.py','python':platform.python_version(),'manifest_sha256':digest(MANIFEST),'scc_sha256':digest(SCC),'checker_sha256':digest(CHECKER)}}
RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,indent=2,sort_keys=True));raise SystemExit(0 if out['passed'] else 1)
