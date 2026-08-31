#!/usr/bin/env python3
"""Gate promotion of the A2 e6 grade morphism to full rank-twelve transport."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
d=json.loads((R/'clifford_e6_cyclic_equivariance.json').read_text());assert all(d['checks'].values())
# Two triangular lifts have the same diagonal/graded restriction but distinct shear.
lifts=[[[1,u],[0,1]] for u in (0,1)]
assert lifts[0]!=lifts[1]
assert [[ [M[0][0],0], [0,M[1][1]] ] for M in lifts]==[[[1,0],[0,1]],[[1,0],[0,1]]]
out={'schema':'marici.benincasa.cosmology-e6-rank12-triangular-transport-gate.v1','established':{'domain':'A2 Clifford relational grade','codomain':'A2 e6 occurrence-difference grade','cyclic_equivariance':True,'common_weight':-2},'missing':{'marked_quotient_q0_action':True,'off_diagonal_shear':'C2 dlog(X3/X2)','full_rank12_connection':True,'connector_naturality_components':True},'underdetermination_witness':{'two_lifts':lifts,'same_associated_graded':True,'distinct_triangular_shear':True},'promotion_allowed':False,'reason':'a morphism on the associated relational grade does not determine an extension morphism; the shear is independent extension data','detector_limit':'the invariant (1,1,1) detector annihilates A2 and cannot recover the missing shear','next_test':'census existing rank-twelve connection artifacts for a source-derived q0-to-e6 off-diagonal shear with cyclic coherence','passed':True};(R/'cosmology_e6_rank12_triangular_transport_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
