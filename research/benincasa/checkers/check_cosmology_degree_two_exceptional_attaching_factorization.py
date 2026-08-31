#!/usr/bin/env python3
"""Audit whether degree-two exceptional incidence is sourced independently of the principal leg."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
orbit=json.loads((R/'cosmology_source_sum_asymmetric_connection_orbit_two_prime.json').read_text())
blow=json.loads((ROOT/'research/voevodsky/results/cosmology_blowup_exceptional_cell_gate.json').read_text())
assert orbit['passed'] and blow['passed']
assert orbit['source_sum_principal_face_coefficient']==-2
assert orbit['difference_principal_face_coefficient']==0
# The orbit receipt has no ordered Cech boundary/attaching vector for the difference.
serialized=' '.join(orbit.keys()).lower()
has_difference_boundary=('difference_boundary' in serialized or 'attaching' in serialized)
assert not has_difference_boundary
out={'schema':'marici.benincasa.cosmology-degree-two-exceptional-attaching-factorization.v1','candidate_a':{'object':'literal five-mark source sum','principal':-2,'exceptional_multiplicity':'even but coupled to the even principal occurrence','independent':False},'candidate_b':{'object':'connection-generated antisymmetric difference','principal':0,'integral_orbit_membership_two_prime':True,'ordered_boundary_serialized':False,'independent_degree_two_attaching_map_established':False},'candidate_c':{'object':'blow-up exceptional cell','column':[0,1],'degree_two':False},'disposition':'not constructed in the current interface','precise_gap':'compute the ordered Cech boundary of the provenance-preserved antisymmetric connection word; principal coefficient zero alone does not define an attaching map','parity_consequence':'even if candidate_b supplies (0,-2,2), it corrects the boundary but still requires a separate sourced odd-principal leg','passed':True};(R/'cosmology_degree_two_exceptional_attaching_factorization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
