#!/usr/bin/env python3
"""Exact inverse formula for ordered Green Gram matrices."""

import json, random
from fractions import Fraction
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def gram(rs):
 n=len(rs)+1
 def k(i,j):
  z=Fraction(1)
  for r in rs[min(i,j):max(i,j)]:z*=r
  return z
 return [[k(i,j) for j in range(n)] for i in range(n)]
def precision(rs):
 n=len(rs)+1;Q=[[Fraction(0) for _ in range(n)] for _ in range(n)]
 if n==1:Q[0][0]=1;return Q
 for i,r in enumerate(rs):
  d=1-r*r
  Q[i][i]+=r*r/d;Q[i+1][i+1]+=1/d;Q[i][i+1]-=r/d;Q[i+1][i]-=r/d
 Q[0][0]+=1
 return Q
def main():
 rng=random.Random(20260919);rows=[]
 for n in range(1,13):
  rs=[Fraction(rng.randrange(1,10),10) for _ in range(n-1)];K=gram(rs);Q=precision(rs);I=mm(Q,K)
  assert all(I[i][j]==Fraction(i==j) for i in range(n) for j in range(n))
  assert all(Q[i][j]==0 for i in range(n) for j in range(n) if abs(i-j)>1)
  rows.append({'points':n,'inverse_verified':True,'precision_bandwidth':1})
 result={'schema':'marici.coherence.green-gram-tridiagonal-precision.v1','rows':rows,'all_exact':True,'off_diagonal':'-rho_i/(1-rho_i^2)','quadratic_form':'x_1^2 + sum_i (x_(i+1)-rho_i x_i)^2/(1-rho_i^2)','collision_behavior':'precision coefficients diverge as rho_i tends to one'}
 Path(__file__).with_name('green-gram-tridiagonal-precision.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
