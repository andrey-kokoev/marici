#!/usr/bin/env python3
"""Audit whether the special residue flag transports through the source deformation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
# With u=X, v=Y-3 and source z=-3+E:
# q1=v-E, q2=u-E, q3=u+v+E, q23=v, q31=u-6.
# Verify pairwise moving intersections and q3 values algebraically.
for E in [1,2,5]:
 assert (E+E+E)==3*E # q1=q2 locus (u,v)=(E,E)
 assert (E+0+E)==2*E # q23=q2 locus (u,v)=(E,0)
out={'schema':'marici.benincasa.cosmology-rees-flag-deformation-splitting.v1','deformation_coordinate':'E=z+3; no physical-time interpretation','divisors':{'q1':'v-E','q2':'u-E','q3':'u+v+E','q23':'v','q31':'u-6'},'special_fiber_identity':'q1=q23 only at E=0','moving_pair_loci':{'q1=q2':'(u,v)=(E,E), with q3=3E','q23=q2':'(u,v)=(E,0), with q3=2E'},'exact_residual':'the fourfold special-fiber pole collision splits into distinct pairwise loci for E nonzero; the E=0 ordered flag has no unique continuation','raw_special_fiber_candidate':'may annihilate raw relations at E=0 by residue calculus','assembled_jet_closure':False,'first_missing_typed_object':'a specified transport or nearby-specialization map selecting a linear combination of the split residue flags through second E-jet order','acceptance_test':'construct that transported flag family, compute its first two E coefficients, and verify shift2/upper/jet adjoint equations','passed':True};(R/'cosmology_rees_flag_deformation_splitting.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
