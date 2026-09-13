#!/usr/bin/env python3
"""Exact canonical dual observers from the Green Markov innovation basis."""

import json, random
from fractions import Fraction
from pathlib import Path
import check_green_gram_tridiagonal_precision as core

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def inverse(A):
 n=len(A);M=[r[:]+[Fraction(i==j) for j in range(n)] for i,r in enumerate(A)]
 for j in range(n):
  p=next(i for i in range(j,n) if M[i][j]);M[j],M[p]=M[p],M[j];q=M[j][j];M[j]=[x/q for x in M[j]]
  for i in range(n):
   if i!=j:
    q=M[i][j];M[i]=[x-q*y for x,y in zip(M[i],M[j])]
 return [r[n:] for r in M]
def main():
 rng=random.Random(20260928);rows=[]
 for n in range(1,13):
  rs=[Fraction(rng.randrange(1,10),10) for _ in range(n-1)];R=[[Fraction(i==j) for j in range(n)] for i in range(n)]
  for i,r in enumerate(rs,1):R[i][i-1]=-r
  B=tr(inverse(R));Q=core.precision(rs);G=mm(mm(B,Q),tr(B));d=[Fraction(1)]+[1-r*r for r in rs]
  assert all(G[i][j]==(1/d[i] if i==j else 0) for i in range(n) for j in range(n))
  for i in range(n):
   expected=[Fraction(0)]*i+[Fraction(1)]
   z=Fraction(1)
   for r in rs[i:]:z*=r;expected.append(z)
   assert B[i]==expected
  rows.append({'points':n,'dual_gram_diagonal':[str(1/x) for x in d],'tail_profiles_exact':True})
 result={'schema':'marici.coherence.canonical-green-dual-observers.v1','rows':rows,'all_exact':True,'observer_i':'zero left of i; product rho_i...rho_(j-1) at j>=i','unnormalized_dual_gram':'diag(1,1/(1-rho_1^2),...)','normalized_dual_gram':'identity','condition_number':'1'}
 Path(__file__).with_name('canonical-green-dual-observers.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('all_exact','observer_i','unnormalized_dual_gram','normalized_dual_gram','condition_number')},indent=2))
if __name__=='__main__':main()
