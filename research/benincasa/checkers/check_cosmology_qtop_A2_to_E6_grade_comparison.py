#!/usr/bin/env python3
"""Construct the integral A2-to-E6 occurrence-grade map and test its typed reach."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
source=json.loads((R/'cosmology_qtop_A2_tensor_connection_source.json').read_text());e6=json.loads((R/'clifford_e6_cyclic_equivariance.json').read_text());line=json.loads((R/'cosmology_qtop_e6_scalar_connection_promotion.json').read_text());assert source['passed']
P=((0,0,1),(1,0,0),(0,1,0));Q=((0,-1),(1,-1));B=((1,0),(-1,1),(0,-1))
def mm(A,C):return tuple(tuple(sum(A[i][k]*C[k][j] for k in range(len(C))) for j in range(len(C[0]))) for i in range(len(A)))
assert mm(P,B)==mm(B,Q)
minors=[B[0][0]*B[1][1]-B[0][1]*B[1][0],B[0][0]*B[2][1]-B[0][1]*B[2][0],B[1][0]*B[2][1]-B[1][1]*B[2][0]];assert math.gcd(*map(abs,minors))==1
out={'schema':'marici.benincasa.cosmology-qtop-A2-to-E6-grade-comparison.v1','comparison_matrix':[list(r) for r in B],'target':e6['target'],'rank':2,'maximal_minors':minors,'primitive_image':True,'cyclic_intertwining':True,'source_homogeneity':e6['source_homogeneity'],'target_homogeneity':e6['target_homogeneity'],'algebraic_associated_grade_comparison_constructed':True,'connection_domain':'L_top tensor A2_const with d + alpha I_A2','horizontal_comparison_verified':False,'missing_horizontal_data':['restriction of the E6 connection to all three occurrence lines','proof that cycle scales 2,3,1/6 are horizontal connection gauges','intertwiner residual nabla_E6 B - B nabla_top'], 'available_corner_equality':line['proved_equality'],'corner_equality_sufficient':False,'rank12_extension_lift_constructed':False,'conclusion':'a primitive cyclic integral map identifies A2 with the E6 occurrence-difference grade, but its horizontality is not implied by one corner coefficient or common homogeneity','next_test':'test whether the three constant cycle scales are horizontal gauges for the E6 occurrence-line connections','passed':True};(R/'cosmology_qtop_A2_to_E6_grade_comparison.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
