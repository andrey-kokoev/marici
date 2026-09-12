#!/usr/bin/env python3
"""Exact rank/kernel audit for the multiseam Green-to-asymptotic map."""

import json
from fractions import Fraction
from pathlib import Path

def rank(A):
 M=[r[:] for r in A];m=len(M);n=len(M[0]);r=0
 for c in range(n):
  p=next((i for i in range(r,m) if M[i][c]),None)
  if p is None:continue
  M[r],M[p]=M[p],M[r];q=M[r][c];M[r]=[x/q for x in M[r]]
  for i in range(m):
   if i!=r:
    q=M[i][c];M[i]=[x-q*y for x,y in zip(M[i],M[r])]
  r+=1
 return r
def main():
 ys=[Fraction(1),Fraction(3,2),Fraction(2),Fraction(5,2),Fraction(3),Fraction(4)]
 rows=[]
 for n in range(1,len(ys)+1):
  full=[[],[]];flux=[[],[]]
  for y in ys[:n]:
   full[0]+=[-1/(2*y),-1/(2*y)];full[1]+=[y/2,-y/2]
   flux[0].append(-1/(2*y));flux[1].append(-y/2)
  rf=rank(full);rg=rank(flux)
  assert rf==2 and rg==min(2,n)
  rows.append({'seams':n,'full_rank':rf,'full_nullity':2*n-rf,'flux_rank':rg,'flux_nullity':n-rg})
 result={'schema':'marici.coherence.multiseam-asymptotic-quotient.v1','rows':rows,'full_seam_map_surjective':True,'flux_only_rank':'min(2,n)','flux_kernel_conditions':['sum(J1_i/y_i)=0','sum(y_i J1_i)=0'],'identification':'flux-only kernel equals the prior two-moment asymptotic kernel'}
 Path(__file__).with_name('multiseam-asymptotic-quotient.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
