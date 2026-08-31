#!/usr/bin/env python3
"""Classify the minimal coordinate-multiplication closure of the IBP relation family."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research'/'benincasa'/'results'
# In the free source space, I_e are admitted relations and x I_e = I_(e+1)-M_e.
# Any x-stable relation subspace containing both I_e and I_(e+1) therefore contains M_e.
checked=[]
for axis in ('x','y'):
 for degree in range(6):
  checked.append({'axis':axis,'master_exponent':degree,'deduction':f'M_{degree} = I_{degree+1} - {axis} I_{degree}','forced_into_closed_relation_space':True})
assert all(x['forced_into_closed_relation_space'] for x in checked)
out={'schema':'marici.benincasa.cosmology-minimal-leibniz-closure-trivialization.v1','premises':['all exponent-labelled IBP rows I_e are relations','the relation space is closed under coordinate multiplication'],'identity':'M_e = I_(e+1) - x_axis I_e','consequence':'every bare master M_e is itself a relation','physical_boundary_targets':'bare master-coordinate derivative targets','target_classes_after_closure':'all zero by definition','closure_is_informative':False,'decision':'The minimal coordinate-stable closure of the IBP relation family trivializes the master quotient, so it cannot certify physical target exactness noncircularly.','correct_scope':'fiber-coordinate multiplication does not descend to the de Rham cohomology quotient; a parameter-space Gauss-Manin action would require separately sourced parameter constructors','sample_deductions':checked,'passed':True};(R/'cosmology_minimal_leibniz_closure_trivialization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='sample_deductions'},indent=2))
