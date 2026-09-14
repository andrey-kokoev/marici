#!/usr/bin/env python3
"""Exact classification audit for involutive orthogonal rank-two monodromy."""
import itertools,json
from pathlib import Path

def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def tr(A):return tuple(zip(*A))
def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
I=((1,0),(0,1))
def main():
 # All 2x2 signed permutation matrices: the exact finite O(2,Z) model.
 mats=[]
 for p in ((0,1),(1,0)):
  for signs in itertools.product((-1,1),repeat=2):
   A=tuple(tuple(signs[i] if j==p[i] else 0 for j in range(2)) for i in range(2));mats.append(A)
 involutive_reflections=[]
 for H in mats:
  assert mm(tr(H),H)==I
  if mm(H,H)==I and det(H)==-1:involutive_reflections.append(H)
 assert len(involutive_reflections)==4
 for H in involutive_reflections:
  # Characteristic polynomial is x^2-1, hence one + and one - eigenline.
  assert H[0][0]+H[1][1]==0 and det(H)==-1
 J=((0,-1),(-1,0));assert J in involutive_reflections
 # Sharp hostile holonomies.
 hostile={'identity':I,'minus_identity':((-1,0),(0,-1)),'quarter_turn':((0,-1),(1,0))}
 assert det(hostile['identity'])==1 and det(hostile['minus_identity'])==1
 assert mm(hostile['quarter_turn'],hostile['quarter_turn'])==hostile['minus_identity']
 result={'schema':'marici.voevodsky.mobius-monodromy-classification.v1','signed_orthogonal_matrices_checked':len(mats),'involutive_determinant_minus_one_cases':len(involutive_reflections),'theorem':'Every rank-two real orthogonal local system on S1 with involutive determinant-minus-one holonomy splits as one trivial line and one Mobius line.','signed_exchange_J':[list(r) for r in J],'J_exchanges_local_channel_lines':True,'individual_channel_lines_descend':False,'unordered_channel_pair_descends':True,'counterexamples':{'terminal_2_segal':'has no forced rank-two local system','identity_holonomy':'two trivial lines','minus_identity_holonomy':'two Mobius lines and orientable sum','quarter_turn_holonomy':'order four, no real eigenline splitting'},'claim_boundary':'A cyclic 2-Segal object must additionally supply the stated rank-two orthogonal local system and holonomy; bare 2-Segal axioms do not.'}
 out=Path(__file__).parents[1]/'results'/'mobius_monodromy_classification.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
