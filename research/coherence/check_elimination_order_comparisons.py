#!/usr/bin/env python3
"""Compare exact minimalization maps obtained from different adjacent-pair orders."""

import json, random
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import check_chain_skew_minimal_model as base


def inverse(A):
 n=len(A);X=[A[i][:]+base.eye(n)[i] for i in range(n)]
 for c in range(n):
  p=next(i for i in range(c,n) if X[i][c]);X[c],X[p]=X[p],X[c]
  z=X[c][c];X[c]=[x/z for x in X[c]]
  for i in range(n):
   if i!=c and X[i][c]:
    z=X[i][c];X[i]=[x-z*y for x,y in zip(X[i],X[c])]
 return [r[n:] for r in X]

def reduce_order(M,pairs):
 n=len(M);A=[r[:] for r in M];P=base.eye(n);active=set(range(n))
 for k,l in pairs:
  a=A[k][l];assert a
  for j in sorted(active-{k,l}):
   E=base.eye(n);E[k][j]=A[l][j]/a;E[l][j]=-A[k][j]/a
   A=base.mul(base.transpose(E),base.mul(A,E));P=base.mul(P,E)
  active-={k,l}
 return A,P

def det(A):
 A=[r[:] for r in A];z=Fraction(1)
 for c in range(len(A)):
  p=next(i for i in range(c,len(A)) if A[i][c]);
  if p!=c:A[c],A[p]=A[p],A[c];z=-z
  q=A[c][c];z*=q
  for i in range(c+1,len(A)):
   r=A[i][c]/q
   for j in range(c,len(A)):A[i][j]-=r*A[c][j]
 return z

def main():
 rng=random.Random(20260912);rows=[]
 for n in (4,6,8):
  gaps=[Fraction(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(n-1)];M=base.chain(gaps);pairs=[(i,i+1) for i in range(0,n,2)];normal,P0=reduce_order(M,pairs)
  for order in permutations(pairs):
   B,P=reduce_order(M,order);assert B==normal
   G=base.mul(inverse(P0),P)
   assert base.mul(base.transpose(G),base.mul(normal,G))==normal and det(G)==1
   rows.append({'size':n,'order':order,'comparison_nonidentity':G!=base.eye(n),'determinant':str(det(G))})
 assert any(r['comparison_nonidentity'] for r in rows)
 result={'schema':'marici.coherence.elimination-order-comparisons.v1','comparisons':len(rows),'all_land_in_same_normal_form':True,'all_comparisons_symplectic':True,'all_determinants_one':True,'some_comparisons_nonidentity':True,'conclusion':'minimal models agree, but elimination maps differ by nontrivial automorphisms of the hyperbolic target'}
 Path(__file__).with_name('elimination-order-comparisons.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
