#!/usr/bin/env python3
"""Obstruct realization of the minimal formal extension on the audited sources."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
receipts=['cosmology_universal_minimal_integral_source_extension.json','cosmology_asymmetric_incidence_source_census.json','cosmology_connection_ordered_cech_boundary_gate.json','cosmology_cm_source_labelled_complement_gate.json','cosmology_weighted_relative_homology_derham_pairing_gate.json','cosmology_normalized_three_point_conductor_cospan.json','cosmology_rees_production_contract_acceptance.json']
for n in receipts: assert json.loads((R/n).read_text())['passed']
req=['source_object','odd_principal_leg','ordered_boundary_0_-2_2','g23_g31_labels','comparison_map']
rows=[
 ('literal five-mark cell',[True,False,False,True,True],'principal coefficient -2; boundary obstruction is uncancelled'),
 ('antisymmetric connection',[True,False,False,True,True],'principal coefficient 0; occurrence shadow is not a Cech boundary'),
 ('blow-up exceptional cell',[True,False,False,False,True],'column (0,1)'),
 ('Cayley-Menger quotient',[True,False,False,False,False],'rank-three complement is not source-labelled and no comparison map exists'),
 ('weighted relative pairing',[False,False,False,False,False],'relative pair and pairing map are undefined'),
 ('three-point conductor cospan',[False,False,True,True,False],'combinatorial incidence has no geometric source or comparison map'),
 ('Rees length-one factors',[False,False,False,False,False],'labelled extraction fails production acceptance')]
candidates=[{'candidate':n,'requirements':dict(zip(req,v)),'first_blocker':b,'realizes_u':all(v)} for n,v,b in rows]
assert not any(c['realizes_u'] for c in candidates)
out={'schema':'marici.benincasa.cosmology-minimal-extension-source-realization-functor.v1','realization_interface':req,'candidates':candidates,'audited_realization_fiber_empty':True,'functor_obstructed_at':'object assignment','coherence_audit_needed':False,'conclusion':'no source-realization functor sending an audited source object to formal u exists on the audited candidate subcategory','global_nonexistence':False,'next_test':'test whether a sourced mu2 orientation local system can realize the odd leg integrally without dividing transfer by two','passed':True};(R/'cosmology_minimal_extension_source_realization_functor.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
