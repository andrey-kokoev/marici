#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
p=R/'research/aspect/contracts/c13-pointed-hermitian-presentation-state.v1.json'
x=json.loads(p.read_text())
placements=[]
for j in range(7):
    edges=['id_Q1']*j+['eta13']+['id_Q3']*(6-j)
    nondegenerate=[e for e in edges if not e.startswith('id_')]
    placements.append({'slot':j,'edges':edges,'composite':'eta13','normalized':nondegenerate})
checks={
 'pointed_universe':x['universe']['basepoint']=='(Q1,id_Q1)',
 'complete_forms_equal':x['endpoint']['complete_hermitian_forms_equal'] is True,
 'common_carrier':x['endpoint']['common_observer_carrier'] is True,
 'equivalence_and_inverse':x['scc_status']['one_universe_equivalence']=='constructed' and x['scc_status']['inverse_path']=='constructed',
 'seven_placements':len(placements)==x['seven_slot_factorizations']['placement_count']==7,
 'one_edge_each':all(y['normalized']==['eta13'] for y in placements),
 'same_composite':all(y['composite']=='eta13' for y in placements),
 'six_unit_coherences':x['seven_slot_factorizations']['unit_coherence_comparisons']==6,
 'nondegenerate_blocked':x['seven_slot_factorizations']['nondegenerate_analytic_subdivision_constructed'] is False,
 'six_presentations_missing':x['seven_slot_factorizations']['missing_intermediate_presentations']==6,
 'external_gate_open':x['endpoint']['external_centered_source_formula_verified'] is False,
 'rh_not_promoted':x['scc_status']['rh_implication'] is False}
out={'schema':'marici.scc.c13-pointed-hermitian-presentation-state-check.v1','passed':all(checks.values()),'checks':checks,'placements':placements,'verdict':'degenerate seven-slot SCC path constructed; nondegenerate analytic subdivision not constructed; external source verification open'}
q=R/'research/aspect/results/c13_pointed_hermitian_presentation_state.json';q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
