#!/usr/bin/env python3
"""Gate the ordered Cech boundary of the antisymmetric connection word."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
orb=json.loads((R/'cosmology_source_sum_asymmetric_connection_orbit_two_prime.json').read_text())
prov=json.loads((R/'cosmology_asymmetric_connection_orbit_provenance_summary.json').read_text())
typ=json.loads((R/'deletion_occurrence_projector_typing.json').read_text())
assert orb['passed'] and prov['passed']
assert orb['difference_principal_face_coefficient']==0
assert 'source-derived connector' in typ['verdict']
out={'schema':'marici.benincasa.cosmology-connection-ordered-cech-boundary-gate.v1','connection_word':{'source_cells':['(g1,g2,g3,g31)','(g1,g2,g3,g23)'],'combination':'first minus second','principal_coefficient':0,'exact_orbit_replay_two_prime':True},'candidate_occurrence_shadow':[0,-1,1],'candidate_doubled_shadow':[0,-2,2],'ordered_cech_boundary_constructed':False,'reason':'the source word is a q-cell/master-row combination; the existing occurrence projector does not type a map to the ordered Cech deletion complex','forbidden_inference':'reading g31-g23 labels as a Cech boundary without a source-derived connector','disposition':'boundary computation blocked at the domain map, not numerically falsified','next_required_map':'q-cell occurrence module -> ordered pair-face Cech chain module, compatible with the connection action and deletion variance','passed':True};(R/'cosmology_connection_ordered_cech_boundary_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
