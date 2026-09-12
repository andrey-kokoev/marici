#!/usr/bin/env python3
"""Exact coherence checks for nested finite Green Gram realizations."""

import json
from fractions import Fraction
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def inv(A):
 n=len(A);M=[r[:]+[Fraction(i==j) for j in range(n)] for i,r in enumerate(A)]
 for j in range(n):
  p=next(i for i in range(j,n) if M[i][j]);M[j],M[p]=M[p],M[j];q=M[j][j];M[j]=[x/q for x in M[j]]
  for i in range(n):
   if i!=j:
    q=M[i][j];M[i]=[a-q*b for a,b in zip(M[i],M[j])]
 return [r[n:] for r in M]
def gram(S,T):return [[Fraction(1,2**abs(i-j)) for j in T] for i in S]
def projection(S,T):return mm(inv(gram(S,S)),gram(S,T))
def main():
 levels=[list(range(-k,k+1)) for k in range(4)]
 rows=[]
 for a in range(len(levels)):
  for b in range(a,len(levels)):
   for c in range(b,len(levels)):
    S,T,U=levels[a],levels[b],levels[c]
    lhs=mm(projection(S,T),projection(T,U));rhs=projection(S,U);assert lhs==rhs
    rows.append({'levels':[a,b,c],'coherent':True})
 result={'schema':'marici.coherence.green-gram-pro-system.v1','levels':[len(x) for x in levels],'triple_checks':len(rows),'all_projection_triangles_commute':True,'kernel':'2^(-abs(i-j))','state_direction':'isometric inclusions E_S -> E_T','observation_direction':'orthogonal projections E_T -> E_S','limit':'dense union completes to the Green RKHS'}
 Path(__file__).with_name('green-gram-pro-system.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
