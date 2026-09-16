#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3];p=R/'research/aspect/contracts/fixed-k-four-chart-twistor-rotation.v1.json';x=json.loads(p.read_text())
# Finite chart-label model; retained m is untouched.
def tau(i,n=1): return ((i-1+n)%4)+1
checks={
 'four_charts':x['common_carrier']['charts']==[f'V_tilde_{i},k' for i in range(1,5)],
 'fixed_k':x['parameter']['meaning'].startswith('fixed parameter'),
 'one_turn':all(tau(i)==(i%4)+1 for i in range(1,5)),
 'inverse':all(tau(tau(i,-1))==i for i in range(1,5)),
 'fourth_power':all(tau(i,4)==i for i in range(1,5)),
 'edge_C12':x['edge_restrictions']['C12']=='e_2,k e_1,k^-1',
 'edge_C23':x['edge_restrictions']['C23']=='e_3,k e_2,k^-1',
 'edge_C34':x['edge_restrictions']['C34']=='e_4,k e_3,k^-1',
 'edge_C41':x['edge_restrictions']['C41']=='e_1,k e_4,k^-1',
 'transported_continuity':x['operator']['continuous'] and x['operator']['homeomorphism'],
 'no_scalar_inverse':x['claim_boundary']['scalar_trace_inverted'] is False,
 'no_unanchored_topology_claim':x['claim_boundary']['unanchored_output_topology_identified'] is False,
 'no_cross_dimension_seam':x['parameter']['cross_dimension_seam'] is False,
 'rh_not_promoted':x['claim_boundary']['rh_implication'] is False}
out={'schema':'marici.scc.fixed-k-four-chart-twistor-rotation-check.v1','passed':all(checks.values()),'checks':checks,'orbit_from_chart_1':[tau(1,n) for n in range(5)],'verdict':'fixed-k common-graph quarter rotation constructed with tau_k^4=id; topology claim restricted to transported chart topology'}
q=R/'research/aspect/results/fixed_k_four_chart_twistor_rotation.json';q.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
