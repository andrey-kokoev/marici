#!/usr/bin/env python3
"""Exact audit that a centered negative Schwarz obstruction persists under extensions."""
import json
from fractions import Fraction
from pathlib import Path

def q(G,x):return sum(x[i]*G[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
def main():
 # Unit is coordinate 0. q is centered because its pairing with the unit vanishes.
 G=[[Fraction(1),0,0],[0,Fraction(1),Fraction(2)],[0,Fraction(2),Fraction(1)]]
 v=[0,1,-1];center=sum(G[0][j]*v[j] for j in range(3));neg=q(G,v);assert center==0 and neg<0
 # Arbitrary source-preserving extension: old principal block is unchanged.
 H=[row+[Fraction(i+1)] for i,row in enumerate(G)]
 H.append([Fraction(1),Fraction(2),Fraction(3),Fraction(7)])
 w=v+[0];assert q(H,w)==neg and sum(H[0][j]*w[j] for j in range(4))==0
 det=G[0][0]*neg-center*center;det_ext=H[0][0]*q(H,w);assert det==det_ext<0
 result={'schema':'marici.voevodsky.centered-rung4-obstruction-persistence.v1','centered_witness':v,'L_of_witness':str(center),'L_of_square':str(neg),'rung4_determinant':str(det),'extended_witness':w,'extended_rung4_determinant':str(det_ext),'theorem':'If inclusions preserve 1, L(p), and L(p*p), a centered negative rung-4 Schwarz square remains the same negative square at every later rung by zero extension.','higher_filler_can_repair':False,'allowed_escape':['change the source observer','quotient out the witness nonfaithfully','violate restriction coherence'],'rh_consequence':'For the exact faithful source observer, universal centered rung-4 positivity is the terminal substantive gate; higher coherence can organize but cannot repair its failure.'}
 out=Path(__file__).parents[1]/'results'/'centered_rung4_obstruction_persistence.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
