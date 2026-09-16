#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3];x=json.loads((R/'research/aspect/contracts/fixed-k-four-chart-twistor-rotation.v2.json').read_text())
def rot(i,n=1):return ((i-1+n)%4)+1
c={
'v2':x['schema'].endswith('.v2'),
'abstract_order_four':all(rot(i,4)==i for i in range(1,5)),
'four_projectors':x['additive_tate_orbit']['character_projectors']==4,
'orbit_forms_typed':'Q_k(' in x['additive_tate_orbit']['orbit_forms'],
'vectors_not_presentations':x['typing_correction'].startswith('D_i,k=') and 'not presentation objects' in x['typing_correction'],
'hilbert_only':x['additive_tate_orbit']['boundary_hilbert_form_invariant'] is True,
'weil_open':x['additive_tate_orbit']['completed_weil_form_invariant']=='not_constructed',
'four_chi_missing':len(x['semilocal_chart_identification']['required_maps'])==4 and x['semilocal_chart_identification']['constructed'] is False,
'C_identification_open':x['semilocal_chart_identification']['adjacent_C_maps_identified_with_F_k_restrictions'] is False,
'projection_not_independent':x['abstract_common_graph']['projection_evidence']=='definitional_not_independent_identification',
'topology_boundary':x['topology']['independent_product_subspace_continuity']=='open_inverse_estimate',
'no_promotion':not x['claim_boundary']['semilocal_four_chart_twistor_identified'] and not x['claim_boundary']['rh_implication']}
o={'schema':'marici.scc.fixed-k-four-chart-twistor-rotation-v2-check.v1','passed':all(c.values()),'checks':c,'verdict':'abstract order-four rotations constructed; natural isometries to semilocal charts and completed Weil invariance open'}
(R/'research/aspect/results/fixed_k_four_chart_twistor_rotation_v2.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));raise SystemExit(0 if o['passed'] else 1)
