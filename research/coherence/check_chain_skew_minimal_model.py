#!/usr/bin/env python3
"""Congruence-reduce chain skew kernels to adjacent 2x2 blocks and an odd residual."""

import json, random
from fractions import Fraction
from pathlib import Path


def eye(n):return [[Fraction(i==j) for j in range(n)] for i in range(n)]
def transpose(A):return [list(x) for x in zip(*A)]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def chain(gaps):
 n=len(gaps)+1;A=[[Fraction(0) for _ in range(n)] for _ in range(n)]
 for i in range(n):
  for j in range(i+1,n):
   z=Fraction(1)
   for k in range(i,j):z*=gaps[k]
   A[i][j]=z;A[j][i]=-z
 return A
def reduce_skew(A):
 n=len(A);A=[r[:] for r in A];P=eye(n);pivots=[]
 for k in range(0,n-1,2):
  a=A[k][k+1];assert a;pivots.append(a)
  for j in range(k+2,n):
   alpha=A[k+1][j]/a;beta=-A[k][j]/a
   E=eye(n);E[k][j]=alpha;E[k+1][j]=beta
   A=mul(transpose(E),mul(A,E));P=mul(P,E)
 return A,P,pivots
def main():
 rng=random.Random(20260912);rows=[]
 for n in range(2,12):
  for trial in range(10):
   gaps=[Fraction(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(n-1)];M=chain(gaps);A,P,piv=reduce_skew(M)
   assert A==mul(transpose(P),mul(M,P))
   expected=[[Fraction(0) for _ in range(n)] for _ in range(n)]
   for k,a in zip(range(0,n-1,2),gaps[::2]):expected[k][k+1]=a;expected[k+1][k]=-a
   assert A==expected
   rows.append({'size':n,'trial':trial,'blocks':len(piv),'odd_residual_dimension':n%2})
 result={'schema':'marici.coherence.chain-skew-minimal-model.v1','cases':len(rows),'all_congruences_exact':True,'minimal_model':'direct sum of adjacent 2x2 skew blocks plus one zero line at odd size','rows':rows}
 Path(__file__).with_name('chain-skew-minimal-model.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','all_congruences_exact','minimal_model')},indent=2))
if __name__=='__main__':main()
