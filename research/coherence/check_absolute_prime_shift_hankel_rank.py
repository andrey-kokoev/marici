#!/usr/bin/env python3
"""Exact Hankel ranks for f(x)=exp(-|x|) on the signed log-prime lattice."""

import json
from fractions import Fraction
from itertools import product
from pathlib import Path

PRIMES=(2,3,5,7)
def vectors(k):return [v for v in product(range(-k,k+1),repeat=4) if sum(abs(x) for x in v)<=k]
def ratio(v):
 r=Fraction(1)
 for p,n in zip(PRIMES,v):r*=Fraction(p)**n
 return r
def response(v):
 r=ratio(v);return r if r<=1 else 1/r
def rank(A):
 A=[r[:] for r in A];rows=len(A);cols=len(A[0]);r=0
 for c in range(cols):
  p=next((i for i in range(r,rows) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];z=A[r][c]
  for i in range(r+1,rows):
   if A[i][c]:
    q=A[i][c]/z
    for j in range(c,cols):A[i][j]-=q*A[r][j]
  r+=1
 return r
def main():
 rows=[]
 for k in range(4):
  V=vectors(k);H=[[response(tuple(x+y for x,y in zip(u,v))) for v in V] for u in V];r=rank(H)
  rows.append({'depth':k,'contexts':len(V),'hankel_rank':r})
 assert rows[-1]['hankel_rank']>2 and all(rows[i+1]['hankel_rank']>=rows[i]['hankel_rank'] for i in range(3))
 result={'schema':'marici.coherence.absolute-prime-shift-hankel-rank.v1','source':'f(x)=exp(-abs(x))','exact_response':'min(product p^nu, product p^-nu)','ranks':rows,'rank_exceeds_hyperbolic_double':True,'conclusion':'even one fixed reciprocal exponential source does not factor through the two-state common-translation model when four labelled signed shifts are independently executable'}
 Path(__file__).with_name('absolute-prime-shift-hankel-rank.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
