#!/usr/bin/env python3
"""Construct the minimal formal integral source-extension presentation."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
obs=json.loads((R/'cosmology_primitive_lift_obstruction_synthesis.json').read_text());assert obs['passed']
e=(0,1);u=(1,0);w=(u[0]+e[0],u[1]+e[1]);boundary=(0,-2,2);obstruction=(0,2,-2)
assert w==(1,1) and sum(boundary)==0 and tuple(a+b for a,b in zip(boundary,obstruction))==(0,0,0)
assert abs(u[0]*e[1]-u[1]*e[0])==1 and math.gcd(*map(abs,boundary))==2
shears=[]
for k in range(-8,9):
 uk=(1,k);wk=(uk[0]+(1-k)*e[0],uk[1]+(1-k)*e[1]);assert wk==(1,1);shears.append({'k':k,'u':[1,k],'target_coefficients':[1,1-k]})
out={'schema':'marici.benincasa.cosmology-universal-minimal-integral-source-extension.v1','presentation':{'existing_exceptional_generator':{'column':list(e)},'adjoined_formal_generator_u':{'column':list(u),'ordered_boundary':list(boundary)},'primitive_lift_w':'u+e','target_column':list(w)},'chain_checks':{'boundary_cancels_literal_obstruction':True,'boundary_is_cocycle_sum_zero':True,'hence_d_squared_zero_in_ordered_triangle_complex':True,'g23_g31_routed_with_coefficients':[-2,2]},'integral_checks':{'det_u_e':1,'u_primitive':True,'boundary_content':2},'Rees_shear_family':shears,'normal_form':'u has exceptional coordinate 0; every shear u+k e yields the same target after coefficient adjustment','universal_scope':'initial free presentation among integral extensions equipped with a chosen generator of column (1,0) and ordered boundary (0,-2,2)','source_authorized':False,'reason_not_source_authorized':'a formal initial presentation supplies no geometric source object or comparison morphism','next_test':'seek a source-realization functor into this presentation, preserving labels, boundary, and the target column','passed':True};(R/'cosmology_universal_minimal_integral_source_extension.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
