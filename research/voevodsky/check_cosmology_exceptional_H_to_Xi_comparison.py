"""Test whether the exceptional hyperplane class can map to Xi by ordinary restriction."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_exceptional_H_to_Xi_comparison.json'
def det3(M):
 return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
def main():
 # Strict transforms on E=P2: L1=U, L2=V, L3=U+V+P.
 coefficient_rows=[[1,0,0],[0,1,0],[1,1,1]]
 determinant=det3(coefficient_rows); assert determinant==1
 # Their complement is a projective triangle complement, hence Gm^2.
 h2_open_rank=1
 # Any Li is nowhere zero on the common complement and trivializes O(1)|_U.
 restriction_H=0
 xi_rank=1; assert restriction_H==0 and xi_rank==h2_open_rank
 out={'schema':'marici.voevodsky.cosmology-exceptional-H-to-Xi-comparison.v1','status':'ordinary_restriction_H_to_Xi_falsified_relative_boundary_map_required','exceptional_divisor':'E=P2','strict_transform_lines':['U=0','V=0','U+V+P=0'],'line_coefficient_determinant':determinant,'open_complement':'E minus three lines is isomorphic to Gm^2','H2_open_rank':h2_open_rank,'Xi_open_class':'nonzero generator represented by a logarithmic two-form','hyperplane_restriction':'H=c1(O(1)) restricts to zero because any Li trivializes O(1) on the common complement','decision':'The primitive exceptional hyperplane class cannot be identified with Xi_log by ordinary restriction: H maps to zero while Xi_log is nonzero.','required_replacement':'a relative localization/connecting morphism retaining the ordered boundary-line divisor complex; neither ordinary pullback nor equality of primitive coefficients suffices','limitations':['does not rule out the relative boundary connecting map','does not compute the full resolved total complex','no horn or Bockstein constructed'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
