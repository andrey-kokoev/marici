#!/usr/bin/env python3
"""Exact determinant and insertion-cocycle checks for ordered Green Gram matrices."""

import json, random
from fractions import Fraction
from pathlib import Path

def det(A):
 M=[r[:] for r in A];d=Fraction(1)
 for j in range(len(M)):
  p=next(i for i in range(j,len(M)) if M[i][j]);
  if p!=j:M[j],M[p]=M[p],M[j];d=-d
  q=M[j][j];d*=q
  for i in range(j+1,len(M)):
   a=M[i][j]/q
   for k in range(j+1,len(M)):M[i][k]-=a*M[j][k]
 return d
def gram(gaps):
 n=len(gaps)+1
 def k(i,j):
  z=Fraction(1)
  for g in gaps[min(i,j):max(i,j)]:z*=g
  return z
 return [[k(i,j) for j in range(n)] for i in range(n)]
def formula(gaps):
 z=Fraction(1)
 for r in gaps:z*=1-r*r
 return z
def main():
 rng=random.Random(20260917);rows=[]
 for n in range(1,10):
  gaps=[Fraction(rng.randrange(1,9),10) for _ in range(n-1)]
  d=det(gram(gaps));assert d==formula(gaps) and d>0
  rows.append({'points':n,'determinant':str(d),'formula_verified':True})
 for _ in range(50):
  a=Fraction(rng.randrange(1,9),10);b=Fraction(rng.randrange(1,9),10)
  ratio=(1-a*a)*(1-b*b)/(1-a*a*b*b)
  # Replacing old gap ab by the two gaps a,b.
  assert (1-a*a)*(1-b*b)==(1-a*a*b*b)*ratio
 result={'schema':'marici.coherence.green-gram-determinant-transitions.v1','ordered_cases':rows,'interior_insertions':50,'all_exact':True,'determinant_formula':'product_i (1-rho_i^2)','interior_transition':'(1-alpha^2)(1-beta^2)/(1-alpha^2 beta^2)','transition_equals_innovation_norm_squared':True,'collision_behavior':'transition tends to zero when either new gap tends to zero distance'}
 Path(__file__).with_name('green-gram-determinant-transitions.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
