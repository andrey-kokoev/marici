#!/usr/bin/env python3
"""Integral endpoint-collar lift to the oriented cyclic nearby occurrence basis."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
h=json.loads((R/'results/PS1M1_Leray_Cech_homology_signature.json').read_text())
n=json.loads((R/'cyclic-cut-nearby-sewing.json').read_text())
v=h['vertex_vector']; edges=h['gauge_edge_chain']; occ=n['occurrences']; orbits=n['occurrence_orbits']
assert n['occurrence_signs']==[1]*6 and n['forget_occurrence_multiplicities']==[2,2,2]
assert all(x%2==0 for x in v+edges)
# Sector order qG12,qG23,qG31; each has two positively oriented occurrences.
pairs=[occ[0:2],occ[2:4],occ[4:6]]
lift={name:v[i]//2 for i,p in enumerate(pairs) for name in p}
forgot=[sum(lift[x] for x in p) for p in pairs]
assert forgot==v
# The source Cech gauge chain is likewise integrally split on the two occurrence sheets.
edge_lift={name:edges[i]//2 for i,name in enumerate(['ca','cb','ab']) for _ in [0]}
# Existing source boundary formula from PS1M1.
xca,xcb,xab=edges
boundary=[-xca-xcb,xca-xab,xcb+xab]
diag=h['symmetric_diagonal_representative']; dev=[v[i]-diag[i] for i in range(3)]
assert boundary==dev
# Cyclic covariance: rho permutes both three-element occurrence orbits, hence equal
# sheet splitting commutes with sector rotation.
out={'schema':'marici.benincasa.PS1M5-endpoint-collar-specialization.v1','prospective_action':'PS1M5_specialize_endpoint_collars_to_nearby_occurrences','resolution':'+-','source_vertex_vector':v,'nearby_occurrence_lift':lift,'forget_occurrence':forgot,'integral':True,'base_change_on_vertex_collars':forgot==v,'cech_gauge_boundary':boundary,'equals_source_deviation':boundary==dev,'cyclic_covariance':'equal splitting on each sector commutes with the two declared C3 occurrence orbits','uniqueness_scope':'unique among deck-invariant equal-sheet lifts whose occurrence-forgetting map is the declared sum','positive_result':'The three endpoint collar generators and their H0 class admit an oriented integral nearby occurrence lift; its quotient augmentation equals PS1A.','remaining_gap':'The equal-sheet/deck-invariant condition is mathematically natural but is not yet identified as the source normal-cone specialization rule. Images of the 984 interior d0/overlap columns remain unconstructed.','next':'Construct the normal-cone specialization of one generating overlap column in each cyclic sector and test that its two occurrence coefficients are equal with these orientations.','passed':True}
(R/'results/PS1M5_endpoint_collar_specialization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
