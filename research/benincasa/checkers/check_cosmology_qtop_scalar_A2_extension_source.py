#!/usr/bin/env python3
"""Separate formal scalar extension on A2 from source promotion to rank twelve."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
q=json.loads((B/'marked-wall-quotient-connection.json').read_text());census=json.loads((B/'marked-extension-fixed-final-block-census.json').read_text());prior=json.loads((R/'cosmology_qtop_e6_scalar_connection_promotion.json').read_text());cart=json.loads((R/'cosmology_A2_Cartan_covector_shear.json').read_text());gate=json.loads((R/'cosmology_e6_rank12_triangular_transport_gate.json').read_text())
assert q['basis'].count('q_top')==1 and census['source_columns'].count('q_top')==1
assert prior['passed'] and cart['normalized_orbit_sum']==[[1,0],[0,1]]
# Scalar matrices commute with cyclic Q and identity shear over any coefficient ring.
Q=((0,-1),(1,-1));I=((1,0),(0,1))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
assert mm(I,Q)==mm(Q,I)==Q and mm(I,I)==I
out={'schema':'marici.benincasa.cosmology-qtop-scalar-A2-extension-source.v1','qtop_basis_copy_count':1,'final_block_qtop_column_count':1,'correction':'two occurrence-labelled q_top copies are not algebraically required to define scalar multiplication on A2','formal_construction':'on A2 tensor K, alpha acts as alpha I_A2','formal_construction_cyclic':True,'formal_construction_commutes_with_identity_shear':True,'formal_construction_occurrence_sensitive':False,'source_tensor_product_connection_declared':False,'A2_to_rank12_extension_grade_map_declared':False,'marked_q0_action_promoted':False,'rank12_gate_still_missing':gate['missing'],'conclusion':'alpha I_A2 exists canonically as a formal scalar action, but no source tensor-product connection or A2-to-rank12 grade map promotes it to the marked q0 action','next_test':'test whether the q_top line and constant A2 local system admit a source-declared tensor-product connection compatible with the E6 grade','passed':True};(R/'cosmology_qtop_scalar_A2_extension_source.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
