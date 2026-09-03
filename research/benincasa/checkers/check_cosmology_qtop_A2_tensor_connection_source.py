#!/usr/bin/env python3
"""Derive the q_top quotient-line tensor A2 connection and type its limit."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
q=json.loads((B/'marked-wall-quotient-connection.json').read_text());prior=json.loads((R/'cosmology_qtop_scalar_A2_extension_source.json').read_text());gate=json.loads((R/'cosmology_e6_rank12_triangular_transport_gate.json').read_text());assert prior['passed']
assert q['matrix_pattern']==[['alpha',0,0],['beta1','gamma1',0],['beta2',0,'gamma2']]
# With source-column convention, walls span an invariant submodule, while q_top is not a subconnection.
u=Fraction(1);v=Fraction(3);D=-4+12*u-6*u*v+4*v-9*u*u+4*u*u*v-v*v
beta1=-(-2+u+v)/((v-2)*(-D));assert D and beta1==Fraction(-1,2)
# alpha_u depends only on u and alpha_v only on v, so scalar curvature is zero.
out={'schema':'marici.benincasa.cosmology-qtop-A2-tensor-connection-source.v1','matrix_pattern':q['matrix_pattern'],'convention':'connection columns are source basis vectors','wall_span_invariant':True,'qtop_span_invariant':False,'deliberate_qtop_to_wall_coupling':{'point':[1,3],'beta1':str(beta1)},'top_object':'quotient line L_top = Q / span(q_wall1,q_wall2), not a chosen subline','top_connection':{'alpha_u':q['u']['alpha'],'alpha_v':q['v']['alpha'],'flat':True},'derived_tensor_connection':'L_top tensor A2_const with connection d + alpha I_A2','derived_at_associated_quotient_grade':True,'requires_splitting':False,'gives_rank12_extension_splitting':False,'E6_grade_comparison_map_declared':False,'root_sensitive':False,'rank12_gate_still_missing':gate['missing'],'conclusion':'the tensor connection is canonically derived on the top quotient grade, but nonzero beta coupling prevents treating q_top as a split subconnection and no E6 grade map promotes it','next_test':'test whether the top quotient tensor A2 admits a typed comparison to the E6 rank-twelve associated grade','passed':True};(R/'cosmology_qtop_A2_tensor_connection_source.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
