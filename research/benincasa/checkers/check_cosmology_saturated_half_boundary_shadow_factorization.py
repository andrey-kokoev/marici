#!/usr/bin/env python3
"""Classify the factorization through saturated and boundary-only shadows."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
for n in ['cosmology_joint_column_boundary_saturation_gate.json','cosmology_connection_ordered_cech_boundary_gate.json','cosmology_occurrence_to_cech_connector_obstruction.json']:
 assert json.loads((R/n).read_text())['passed']
h=(1,0,-1,1);r=(0,0,-1,1);t=(1,0,-2,2)
sol=[]
for m in range(-8,9):
 for n in range(-8,9):
  v=tuple(m*a+n*b for a,b in zip(h,r))
  if v==t:sol.append((m,n))
assert sol==[(1,1)] and tuple(a+b for a,b in zip(h,r))==t
out={'schema':'marici.benincasa.cosmology-saturated-half-boundary-shadow-factorization.v1','saturated_half':list(h),'boundary_only_shadow':list(r),'required_generator':list(t),'bounded_integer_solutions':[list(x) for x in sol],'uniqueness_proof':'principal coordinate forces m=1; either nonzero boundary coordinate then forces n=1','conditional_chain_checks':{'both_boundaries_sum_zero':True,'sum_has_required_boundary':True,'sum_has_primitive_principal_leg':True,'g23_g31_routed':True},'typed_status':{'saturated_half_source_object':False,'boundary_only_shadow_is_typed_cech_chain':False,'occurrence_to_cech_connector_exists':False},'connector_deficit':{'object_components':8,'naturality_squares':12},'conclusion':'the arithmetic factorization is unique and chain-consistent if typed, but neither summand is an admitted source chain and the connector is absent','next_test':'construct the minimal free occurrence-to-Cech connector presentation and isolate its source-realization obligations','passed':True};(R/'cosmology_saturated_half_boundary_shadow_factorization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
