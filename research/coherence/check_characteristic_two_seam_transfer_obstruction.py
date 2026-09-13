#!/usr/bin/env python3
"""Audit the seam/asymptotic Green transfer over finite characteristics."""

import json
from pathlib import Path

def rank_mod(A,p):
 M=[[x%p for x in r] for r in A];r=0
 for c in range(len(M[0])):
  q=next((i for i in range(r,len(M)) if M[i][c]),None)
  if q is None:continue
  M[r],M[q]=M[q],M[r];iv=pow(M[r][c],-1,p);M[r]=[(x*iv)%p for x in M[r]]
  for i in range(len(M)):
   if i!=r:
    a=M[i][c];M[i]=[(x-a*y)%p for x,y in zip(M[i],M[r])]
  r+=1
 return r
def main():
 rows=[]
 for p in (2,3,5,7,11):
  y=1;yi=1
  # Twice the Green transfer, avoiding division by two.
  A=[[-yi,-yi],[y,-y]]
  r=rank_mod(A,p);assert r==(1 if p==2 else 2)
  rows.append({'characteristic':p,'rank_of_twice_transfer':r,'minus_one_equals_plus_one':((-1)%p==1)})
 result={'schema':'marici.coherence.characteristic-two-seam-transfer-obstruction.v1','rows':rows,'determinant_of_twice_transfer':'2 for reciprocal weights','characteristic_two_rank_drop':True,'reflection_parity_collapse':True,'required_for_seam_asymptotic_isomorphism':'two is invertible'}
 Path(__file__).with_name('characteristic-two-seam-transfer-obstruction.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
