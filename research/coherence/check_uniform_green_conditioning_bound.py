#!/usr/bin/env python3
"""Exact infinity-norm conditioning bounds for uniform Green contexts."""

import json
from fractions import Fraction
from pathlib import Path

def norm_inf(A):return max(sum(abs(x) for x in r) for r in A)
def gram(n,r):return [[r**abs(i-j) for j in range(n)] for i in range(n)]
def precision(n,r):
 if n==1:return [[Fraction(1)]]
 d=1-r*r;Q=[[Fraction(0) for _ in range(n)] for _ in range(n)]
 for i in range(n-1):Q[i][i]+=r*r/d;Q[i+1][i+1]+=1/d;Q[i][i+1]-=r/d;Q[i+1][i]-=r/d
 Q[0][0]+=1;return Q
def main():
 rows=[]
 for r in (Fraction(1,2),Fraction(3,4),Fraction(9,10),Fraction(99,100)):
  bound=((1+r)/(1-r))**2
  for n in (2,4,8,16):
   kappa=norm_inf(gram(n,r))*norm_inf(precision(n,r));assert kappa<=bound
   rows.append({'rho':str(r),'points':n,'kappa_infinity':str(kappa),'bound':str(bound)})
 result={'schema':'marici.coherence.uniform-green-conditioning-bound.v1','cases':len(rows),'all_exact':True,'bound':'kappa_infinity(K_n) <= ((1+rho)/(1-rho))^2','small_spacing':'rho=exp(-h) gives bound asymptotic to 4/h^2','fixed_interval_refinement':'h=L/(n-1) gives O(n^2) upper bound'}
 Path(__file__).with_name('uniform-green-conditioning-bound.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
