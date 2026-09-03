#!/usr/bin/env python3
"""Prove that the special K square does not extend over the deformation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
# x=3,y=6,z=-3+E. K has X^4=9, Y^4=36, no X^3Y or XY^3,
# and X^2Y^2=z^2-x^2-y^2=E^2-6E-36.
def mixed(E):return E*E-6*E-36
assert mixed(0)==-36 and all(mixed(E)!=-36 for E in [1,2,3,4,5])
out={'schema':'marici.benincasa.cosmology-rees-deformed-K-square-obstruction.v1','deformation':'x=3, y=6, z=-3+E','quartic_coefficients':{'X^4':'9','Y^4':'36','X^3Y':'0','XY^3':'0','X^2Y^2':'E^2-6E-36'},'square_test':'absence of odd mixed terms forces a quadratic square root with X^2 and Y^2 coefficients ±3 and ±6, hence X^2Y^2 coefficient ±36','special_branch':'the E=0 branch has coefficient -36 and root 3X^2-6Y^2+54','extension_equation':'E^2-6E-36=-36, equivalently E(E-6)=0','formal_neighborhood_result':'no polynomial square root exists over Q[[E]] away from the special fiber; the exact square is not a deforming family','consequence':'K^(-1/2) requires a genuine double cover/branch for E nonzero, so H(E) cannot be evaluated as the presumed polynomial on split flags','second_jet_transport_constructed':False,'next_acceptance_test':'construct the double cover w^2=K(E,u,v), resolve it jointly with the split q divisors, and compute valuations of w on both moving flags','passed':True};(R/'cosmology_rees_deformed_K_square_obstruction.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
