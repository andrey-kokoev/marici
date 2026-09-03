#!/usr/bin/env python3
"""Finite exact model of the jointly faithful localization constraint on M."""
import json
from pathlib import Path
import sympy as s
# Feature localizers: jointly faithful coordinate projections.
B1=s.Matrix([[1,0],[0,0]]);B2=s.Matrix([[0,0],[0,1]])
stack=B1.col_join(B2)
assert stack.rank()==2
common_kernel_dim=2-stack.rank();assert common_kernel_dim==0
# Hostile incomplete cover leaves an undetected feature direction.
incomplete=B1
hostile_kernel_dim=2-incomplete.rank();assert hostile_kernel_dim==1
out={'schema':'marici.benincasa.multivalued-feature-localization-constraint.v1','claim':'If T0 M_chi_j = B_j T0, every localized relation is closable, and the feature localizers B_j are jointly faithful, then the global multivalued part M is zero. More generally M is contained in the intersection of ker B_j.','derivation':['for y in M choose f_n -> 0 with T0 f_n -> y','intertwining gives B_j T0 f_n = T0 M_chi_j f_n','localized closability forces B_j y=0','hence y lies in every ker B_j'],'exact_model':{'joint_stack_rank':stack.rank(),'common_kernel_dimension':common_kernel_dim,'incomplete_cover_kernel_dimension':hostile_kernel_dim},'hostile_disposition':'A non-jointly-faithful localization family leaves a one-dimensional possible M, so local closability alone is insufficient.','application_gate':'For corrected gamma-plus-prime, supply feature operators B_j, exact intertwining, localized closability, and joint-faithfulness. Current chart/partition data do not materialize these objects.','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'multivalued_feature_localization_constraint.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
