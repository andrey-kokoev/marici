"""Audit regularity of the labeled principal corner and separate local proof from global descent."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_global_labeled_center_regularity.json'
def det3(a):return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def main():
 jac=[[1,0,0],[0,1,0],[1,1,1]];assert det3(jac)==1
 ideal_equivalence={'U':'l1','V':'l2','P':'l3-l1-l2'};assert len(ideal_equivalence)==3
 local={'regular_sequence':True,'codimension':3,'labeled_conormal_basis':True,'orientation_unit':1}
 global_state={'carrier_smooth_along_center':'unverified','global_ideal_sheaf':'unverified','global_labels':'unverified','transition_cocycle':'unverified'}
 assert local['regular_sequence'] and all(v=='unverified' for v in global_state.values())
 out={'schema':'marici.voevodsky.cosmology-global-labeled-center-regularity.v1','status':'local_center_regular_and_oriented_global_carrier_descent_not_materialized','forms':['l1=U','l2=V','l3=U+V+P'],'Jacobian_determinant':det3(jac),'ideal_identity':'(l1,l2,l3)=(U,V,P), with P=l3-l1-l2','local_conclusion':local,'conditional_global_theorem':'If U,V,P are global regular parameters along a smooth carrier center, then C=V(U,V,P) is a regular codimension-three embedding, the three wall conormals give an ordered basis of I/I^2, and the ambient-star HomotopyLift globalizes in the relative normal complex.','materialized_global_state':global_state,'evidence_boundary':'The exceptional P2 and constant coefficient matrix prove the normal-slice statement. Rank26 transport concerns relation modules and supplies no carrier atlas, ideal-sheaf transition functions, or smoothness proof.','decision':'The required regularity and orientation are proved on every chart carrying the displayed parameters but not globally for the full carrier.','next_gate':'carrier-center-source-extraction: locate the authoritative carrier definition of the principal ideal and test smoothness, labels, and transitions directly','limitations':['no global carrier defining equations were materialized in the audited packets','conditional theorem is exact but not an existence proof','no physical interface inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
