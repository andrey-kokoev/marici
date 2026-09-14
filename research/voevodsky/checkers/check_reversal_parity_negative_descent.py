#!/usr/bin/env python3
"""Exact audit: reversal-invariant negativity descends to a parity-folded sector."""
import json
from fractions import Fraction
from pathlib import Path

def q(A,x):return sum(x[i]*A[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
def main():
 a=Fraction(9,10);b=Fraction(-9,10);G=[[1,a,b],[a,1,a],[b,a,1]]
 # Coordinate-deletion past faces are positive.
 faces=[]
 for omit in range(3):
  ids=[i for i in range(3) if i!=omit];A=[[G[i][j] for j in ids] for i in ids];det=A[0][0]*A[1][1]-A[0][1]*A[1][0];assert det>0;faces.append(str(det))
 # Unnormalised even fold F(x,y)=(x,y,x): F^T G F.
 E=[[2*(1+b),2*a],[2*a,1]];edet=E[0][0]*E[1][1]-E[0][1]*E[1][0]
 ew=[1,-2];ev=q(E,ew);assert edet<0 and ev<0
 # Odd fold x -> (x,0,-x).
 odd=2*(1-b);assert odd>0
 result={'schema':'marici.voevodsky.reversal-parity-negative-descent.v1','rank_three_packet':[[str(x) for x in row] for row in G],'ordinary_rank_two_face_determinants':faces,'ordinary_backward_deletion_detects_negativity':False,'even_fold_matrix':[[str(x) for x in row] for row in E],'even_fold_determinant':str(edet),'even_negative_witness':ew,'even_negative_value':str(ev),'odd_fold_scalar':str(odd),'general_lemma':'If Hermitian G commutes with reversal J and q_G(v)<0, then at least one of v+=(v+Jv)/2 or v-=(v-Jv)/2 has negative value. Its parity sector has dimension ceil(n/2) or floor(n/2).','missing_incidence_theorem':'The negative parity-folded compression must be identified by a positivity-preserving source map with an already admitted earlier-rung observation. Reversal symmetry alone does not provide this identification.'}
 out=Path(__file__).parents[1]/'results'/'reversal_parity_negative_descent.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
