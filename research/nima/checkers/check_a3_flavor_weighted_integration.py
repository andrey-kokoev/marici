#!/usr/bin/env python3
"""Cross-audit the maximal free flavor presentation against the exact weighted complex."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[3]
def load(p): return json.loads((R/p).read_text())
f=load(Path('research/figueiredo/results/coherent-resolution-maximal-free-flavor-presentation.json'))
w=load(Path('research/nima/results/a3-weighted-local-system-code-audit.json'))
a=load(Path('research/nima/results/a3-coherent-resolution.json'))
checks={
 'inputs_pass':f['passed'] and w['passed'] and a['passed'],
 'same_chain_dimensions':list(f['target']['groups'].values())==[14,21,9,1] and list(a['basis'].values())==[14,21,9,1],
 'same_ranks':list(w['weighted_ranks'].values())==[a['ranks']['d1'],a['ranks']['d2'],a['ranks']['d3']],
 'free_map_is_chain_isomorphism':f['kernel_ranks']==[0,0,0,0] and f['image_ranks']==[14,21,9,1],
 'flat_line_gauge_trivial_in_both_audits':f['coefficient_transport'].startswith('gauge-trivial') and w['disposition']['flat_positive_transport'].startswith('trivial gauge twist'),
 'no_physical_flavor_comparison':f['physical_comparison']['status']=='undefined',
 'mod2_not_silently_available':not w['mod2']['all_gauge_values_F2_units'],
 'false_maps_detected':len(f['false_descent']['nonzero_residual_entries'])==2 and w['hostile_naive_face_insertion']['curvature_rank']==1,
}
out={'schema':'marici.nima.a3-flavor-weighted-integration.v1','checks':checks,'passed':all(checks.values()),'accepted_theorem':'At finite A3 over Q, the maximal free flavor relabeling is a chain isomorphism and the completed positive coefficient line is a diagonal gauge twist, hence introduces neither homology nor flavor quotient data.','separated_obstructions':{'physical_flavor':'No sourced map from Carrier vertices to weak-basis Yukawa orbits; physical16 and physical10 are not composable.','binary_code':'The selected rational gauges are not all 2-adic units, so no direct F2 local-system descent is licensed.','exchange_defect':'A naive face-incidence insertion is curved and is not an operational syndrome without a physical-error-to-chain map.'},'claim_boundary':'Finite A3 over Q only. Free presentation labels are not Yukawa flavor states, and gauge triviality does not construct a physical quotient or code.'}
p=R/'research/nima/results/a3-flavor-weighted-integration.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
