#!/usr/bin/env python3
"""Exact observer-by-observer recovery of finite labelled Green packets."""

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
def det(A):
 M=[r[:] for r in A];d=Fraction(1)
 for j in range(len(M)):
  p=next(i for i in range(j,len(M)) if M[i][j])
  if p!=j:M[j],M[p]=M[p],M[j];d=-d
  q=M[j][j];d*=q
  for i in range(j+1,len(M)):
   a=M[i][j]/q
   for k in range(j+1,len(M)):M[i][k]-=a*M[j][k]
 return d
def main():
 n=10;ys=[Fraction(i+1) for i in range(n)];schedule=[-1,1,0,2,-2,3,-3,4,-4,5]
 rows=[]
 for m in range(1,n+1):
  exponents=schedule[:m];A=[[y**e for y in ys] for e in exponents];r=rank(A);assert r==m
  rows.append({'observers':m,'exponents':exponents,'rank':r,'unresolved_dimension':n-r})
 A=[[y**e for y in ys] for e in schedule];d=det(A);assert d
 result={'schema':'marici.coherence.exponential-observer-growth.v1','contexts':n,'schedule':schedule,'rows':rows,'all_exact':True,'rank_gain_per_observer':1,'full_reconstruction_at':n,'full_determinant_nonzero':True,'principle':'distinct Laurent exponents form a generalized Vandermonde observer ladder on distinct positive positions'}
 Path(__file__).with_name('exponential-observer-growth.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
