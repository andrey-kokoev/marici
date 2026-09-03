#!/usr/bin/env python3
"""Reduce q0/naturality for the normalized Cartan identity shear."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
cart=json.loads((R/'cosmology_A2_Cartan_covector_shear.json').read_text());gate=json.loads((R/'cosmology_e6_rank12_triangular_transport_gate.json').read_text());conn=json.loads((R/'cosmology_minimal_occurrence_cech_connector_presentation.json').read_text())
assert cart['passed'] and cart['normalized_orbit_sum']==[[1,0],[0,1]] and gate['passed'] and conn['passed']
I=((1,0),(0,1))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def sub(A,B):return tuple(tuple(A[i][j]-B[i][j] for j in range(2)) for i in range(2))
# For M=I, U M - M V = U-V.
U=((1,0),(0,0));V=((0,0),(0,1));res=sub(mm(U,I),mm(I,V));assert res==((1,0),(0,-1))
out={'schema':'marici.benincasa.cosmology-normalized-Cartan-shear-q0-naturality.v1','candidate_shear':[list(r) for r in I],'q0_intertwiner_equation':'Q_top M = M Q_bottom','identity_reduction':'Q_top = Q_bottom','connector_reduction':'the two transport representations must agree under every one of the twelve component identifications','deliberate_unequal_q0_residual':[list(r) for r in res],'deliberate_failure_nonzero':True,'serialized_q0_top':False,'serialized_q0_bottom':False,'serialized_connector_components':0,'required_connector_components':8,'serialized_naturality_squares':0,'required_naturality_squares':12,'q0_naturality_verified':False,'root_sensitive_extension_encoded':False,'conclusion':'identity shear is compatible only under unproved equality of q0 and transport actions and still carries no dlog-root information','next_test':'census source artifacts for a common marked q0 action on the two A2 extension grades','passed':True};(R/'cosmology_normalized_Cartan_shear_q0_naturality.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
