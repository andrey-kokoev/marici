#!/usr/bin/env python3
"""Exact audit: the discrete wave mesh charge is a polarized increment pairing."""
import json
from fractions import Fraction
from pathlib import Path

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def main():
 vectors=[(Fraction(1),Fraction(0)),(Fraction(2),Fraction(1)),(Fraction(-1),Fraction(3))]
 X=[[dot(x,y) for y in vectors] for x in vectors];rows=[]
 for i in range(2):
  for j in range(2):
   C=X[i][j]+X[i+1][j+1]-X[i][j+1]-X[i+1][j]
   di=tuple(vectors[i][k]-vectors[i+1][k] for k in range(2));dj=tuple(vectors[j][k]-vectors[j+1][k] for k in range(2));pair=dot(di,dj)
   assert C==pair;rows.append({'i':i,'j':j,'mesh_charge':str(C),'increment_pairing':str(pair)})
 result={'schema':'marici.voevodsky.mesh-charge-as-increment-pairing.v1','wave_equation':'C_ij=X_ij+X_(i+1,j+1)-X_(i,j+1)-X_(i+1,j)','primitive_increment':'d_i=v_i-v_(i+1)','identity':'C_ij=<d_i,d_j>','rows':rows,'diagonal_consequence':'C_ii=||d_i||^2>=0 in a common positive carrier','matrix_consequence':'The whole C matrix is PSD, so every rung-4 minor obeys |C_ij|^2<=C_ii C_jj.','converse_warning':'Scalar positivity of mesh charges does not construct a common carrier or prove the C matrix PSD.','source_gate':'Identify the kinematic X_ij with polarized RH primitive readings before applying the identity.'}
 out=Path(__file__).parents[1]/'results'/'mesh_charge_as_increment_pairing.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
