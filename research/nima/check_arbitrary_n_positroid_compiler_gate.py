#!/usr/bin/env python3
"""Necessary codimension law and endpoint-locality gate for an NNMHV positroid compiler."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'));from nnmhv_coherence_paths import compile_nnmhv_histories
match=json.loads((ROOT/'research/nima/results/seven-point-history-parity-cell-matching.json').read_text());actual={m['history_index']:set(range(1,8))-set(m['simplex']) for m in match['matches']};hs=compile_nnmhv_histories(7)
rows=[]
for i,h in enumerate(hs):
 endpoints=set(h.outer_pair+h.inner_pair);rows.append({'history_index':i,'endpoint_labels':sorted(endpoints),'certified_vanishing_cyclic_minor_indices':sorted(actual[i]),'endpoint_set_equals_boundary_set':endpoints==actual[i],'boundary_indices_not_in_endpoints':sorted(actual[i]-endpoints)})
law=[{'n':n,'ambient_dimension':2*(n-2),'cell_dimension':8,'required_codimension':2*n-12,'new_constraints_per_increment':2} for n in range(6,13)]
checks={'codimension_zero_at_seed':law[0]['required_codimension']==0,'codimension_grows_by_two':all(b['required_codimension']-a['required_codimension']==2 for a,b in zip(law,law[1:])),'naive_endpoint_boundary_rule_fails_at_n7':any(not r['endpoint_set_equals_boundary_set'] for r in rows),'some_certified_boundaries_are_not_endpoint_labels':any(r['boundary_indices_not_in_endpoints'] for r in rows)}
out={'schema':'marici.nima.arbitrary-n-positroid-compiler-gate.v1','dimension_law':'codim_G+(2,n)(cell_h)=2(n-2)-8=2n-12','growth':law,'seven_point_endpoint_locality_test':rows,'checks':checks,'passed':all(checks.values()),'conclusion':'Each cutoff step must add two independent positroid constraints, but their labels are not a local function of the four R-invariant endpoints. Boundary-update/branch incidence or an on-shell graph is essential.'};p=ROOT/'research/nima/results/arbitrary-n-positroid-compiler-gate.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
