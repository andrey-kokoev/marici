#!/usr/bin/env python3
"""Saturate the literal joint principal-column/ordered-boundary graph."""
import json, math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
for n in ['cosmology_principal_lattice_saturation_source_gate.json','cosmology_connection_ordered_cech_boundary_gate.json','cosmology_ordered_boundary_odd_principal_source_classification.json']:
 assert json.loads((R/n).read_text())['passed']
literal=(-2,0,2,-2) # principal,b12,b23,b31
g=math.gcd(*map(abs,literal));assert g==2
primitive=tuple(x//g for x in literal);odd=tuple(-x for x in primitive)
required=(1,0,-2,2);residual=tuple(a-b for a,b in zip(required,odd))
assert odd==(1,0,-1,1) and residual==(0,0,-1,1)
# Rank-one rational-span membership is fixed by the nonzero principal coordinate.
q=Fraction(required[0],literal[0]);pred=tuple(q*x for x in literal);assert tuple(map(Fraction,required))!=pred
out={'schema':'marici.benincasa.cosmology-joint-column-boundary-saturation-gate.v1','joint_coordinates':['principal','b12','b23','b31'],'literal_generator':list(literal),'content':g,'saturated_primitive_generator':list(odd),'saturated_ordered_boundary':[0,-1,1],'matches_antisymmetric_occurrence_shadow':True,'required_formal_generator':list(required),'required_in_rational_span':False,'required_in_saturation':False,'exact_residual_after_saturated_half':list(residual),'interpretation':'joint saturation canonically produces the half-boundary occurrence shadow, not the doubled correction required by the primitive lift','source_authorized':False,'next_test':'test the exact factorization of the required pair as saturated half plus a boundary-only occurrence shadow and isolate the missing typed connector','passed':True};(R/'cosmology_joint_column_boundary_saturation_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
