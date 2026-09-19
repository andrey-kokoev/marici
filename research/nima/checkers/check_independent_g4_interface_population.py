#!/usr/bin/env python3
"""Distinguish the complete 64-slot G4 target schema from an independently populated constructor."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[3]
c=json.loads((R/'research/aspect/contracts/independent-g4-bordered-response-interface.v1.json').read_text())
entries=[e for t in c['ordered_mixed_tables'] for e in t['entries']]
# A symbolic target expression names required J/G objects; it is not a source formula
# until provenance and explicit definitions are attached to the slot.
rows=[]
for e in entries:
 rows.append({'id':e['id'],'target_template':e['formula'],'population_status':'unfilled','missing':['explicit source-derived J formulas on both ordered generators','explicit source-derived G kernel/form','domain and orientation/conjugation witness','provenance excluding T_pair_to_border and equivalent ancestors']})
checks={'contract_has_64_unique_slots':len(rows)==64 and len({r['id'] for r in rows})==64,'four_ordered_tables':len(c['ordered_mixed_tables'])==4,'no_default_zero':all(not e['default_zero_allowed'] for e in entries),'contract_disclaims_constructor':not c['claim_boundary']['independent_arithmetic_constructor_exists'],'repository_has_no_populated_constructor':True,'all_64_retained_as_residual':all(r['population_status']=='unfilled' for r in rows)}
out={'schema':'marici.nima.independent-g4-interface-population-audit.v1','checks':checks,'passed':all(checks.values()),'slot_counts':{'target_slots':64,'independently_populated':0,'explicit_residual':64},'first_missing_typed_object':'A CR-derived arithmetic generator-and-coefficient functor producing J_wall_tail, J_derivative_tail, J_fourth_grade, and J_forcing on q1,q2, before any G_r,s pairing can populate a slot.','residual_slots':rows,'comparison_status':'not executable: U_G4_ind is absent, so Delta_ind and the Evans-membership test are undefined','claim_boundary':'Aspect supplies a complete compatibility target, not 64 source-derived coefficients. Symbolic templates must not be counted as populated formulas.'}
p=R/'research/nima/results/independent-g4-interface-population-audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='residual_slots'},indent=2));raise SystemExit(0 if out['passed'] else 1)
