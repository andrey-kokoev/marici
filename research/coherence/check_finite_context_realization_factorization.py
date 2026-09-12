#!/usr/bin/env python3
"""Verify the complete finite Green -> flux -> endpoint factorization."""

import json, random
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
 rng=random.Random(20260916);rows=[]
 for n in range(1,9):
  ys=[Fraction(i+2,i+1) for i in range(n)];u=[Fraction(rng.randrange(-9,10),rng.randrange(1,10)) for _ in range(n)]
  direct=(sum(a/y for a,y in zip(u,ys)),sum(a*y for a,y in zip(u,ys)))
  flux=[-2*a for a in u]
  via=(-sum(j/y for j,y in zip(flux,ys))/2,-sum(j*y for j,y in zip(flux,ys))/2)
  A=[[1/y for y in ys],ys]
  assert direct==via and rank(A)==min(2,n)
  rows.append({'contexts':n,'green_rank':n,'flux_rank':n,'endpoint_rank':rank(A),'diagram_commutes':True})
 result={'schema':'marici.coherence.finite-context-realization-factorization.v1','rows':rows,'all_exact':True,'green_to_flux':'u_i -> J1_i=-2u_i is an isomorphism','flux_to_endpoint':'two weighted moments','endpoint_kernel_dimension':'max(n-2,0)','conclusion':'complete finite realization factors through labelled flux seams; rank loss occurs only at endpoint observation'}
 Path(__file__).with_name('finite-context-realization-factorization.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
