#!/usr/bin/env python3
"""Exact orthogonal innovation decomposition of ordered Green kernel sections."""

import json, random
from fractions import Fraction
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def gram(rs):
 n=len(rs)+1
 def k(i,j):
  z=Fraction(1)
  for r in rs[min(i,j):max(i,j)]:z*=r
  return z
 return [[k(i,j) for j in range(n)] for i in range(n)]
def main():
 rng=random.Random(20260918);rows=[]
 for n in range(1,11):
  rs=[Fraction(rng.randrange(1,10),10) for _ in range(n-1)];K=gram(rs)
  R=[[Fraction(0) for _ in range(n)] for _ in range(n)];R[0][0]=1
  for i,r in enumerate(rs,1):R[i][i]=1;R[i][i-1]=-r
  D=mm(mm(R,K),tr(R));expected=[Fraction(1)]+[1-r*r for r in rs]
  assert all(D[i][j]==(expected[i] if i==j else 0) for i in range(n) for j in range(n))
  rows.append({'points':n,'innovation_norms_squared':[str(x) for x in expected],'orthogonal':True})
 result={'schema':'marici.coherence.green-markov-innovation-basis.v1','rows':rows,'all_exact':True,'innovation':'r_1=k_1; r_i=k_i-rho_(i-1) k_(i-1)','gram_in_innovation_basis':'diag(1,1-rho_1^2,...,1-rho_(n-1)^2)','interpretation':'each ordered context contributes one edge-local orthogonal state line'}
 Path(__file__).with_name('green-markov-innovation-basis.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
