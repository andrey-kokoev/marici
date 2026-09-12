#!/usr/bin/env python3
"""Verify the canonical Pfaffian-cofactor null line at odd relational rank."""

import json, random
from fractions import Fraction
from pathlib import Path


def pf(A):
 n=len(A)
 if n==0:return Fraction(1)
 total=Fraction(0)
 for j in range(1,n):
  sub=[[A[r][c] for c in range(n) if c not in (0,j)] for r in range(n) if r not in (0,j)]
  total+=(1 if j%2 else -1)*A[0][j]*pf(sub)
 return total

def chain(xs):
 n=len(xs)+1;A=[[Fraction(0) for _ in range(n)] for _ in range(n)]
 for i in range(n):
  for j in range(i+1,n):
   z=Fraction(1)
   for k in range(i,j):z*=xs[k]
   A[i][j]=z;A[j][i]=-z
 return A

def main():
 rng=random.Random(20260912);reports=[]
 for n in (3,5,7,9):
  for trial in range(8):
   gaps=[Fraction(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(n-1)]
   A=chain(gaps);v=[]
   for i in range(n):
    minor=[[A[r][c] for c in range(n) if c!=i] for r in range(n) if r!=i]
    v.append((1 if i%2==0 else -1)*pf(minor))
   residual=[sum(A[i][j]*v[j] for j in range(n)) for i in range(n)]
   assert all(x==0 for x in residual) and any(v)
   reports.append({'rank':n,'trial':trial,'null_vector':[str(x) for x in v]})
 result={'schema':'marici.coherence.odd-chain-pfaffian-kernel.v1','cases':len(reports),'odd_ranks':[3,5,7,9],'all_cofactor_vectors_nonzero_and_annihilated':True,'reports':reports}
 Path(__file__).with_name('odd-chain-pfaffian-kernel.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','odd_ranks','all_cofactor_vectors_nonzero_and_annihilated')},indent=2))
if __name__=='__main__':main()
