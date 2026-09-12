#!/usr/bin/env python3
"""Verify restriction of an odd cofactor state after adjoining an even block."""

import json, random
from fractions import Fraction
from pathlib import Path


def pf(A):
 n=len(A)
 if n==0:return Fraction(1)
 return sum((1 if j%2 else -1)*A[0][j]*pf([[A[r][c] for c in range(n) if c not in (0,j)] for r in range(n) if r not in (0,j)]) for j in range(1,n))
def chain(gaps):
 n=len(gaps)+1;A=[[Fraction(0) for _ in range(n)] for _ in range(n)]
 for i in range(n):
  for j in range(i+1,n):
   z=Fraction(1)
   for k in range(i,j):z*=gaps[k]
   A[i][j]=z;A[j][i]=-z
 return A
def block(A,a,b):return [row[a:b] for row in A[a:b]]
def cof(A):return [(-1 if i%2 else 1)*pf([[A[r][c] for c in range(len(A)) if c!=i] for r in range(len(A)) if r!=i]) for i in range(len(A))]
def main():
 rng=random.Random(20260912);rows=[]
 for even_n in (0,2,4,6):
  for odd_n in (1,3,5,7):
   for trial in range(8):
    n=even_n+odd_n;g=[Fraction(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(n-1)];M=chain(g);w=cof(M)
    E=block(M,0,even_n);O=block(M,even_n,n);expected=[pf(E)*x for x in cof(O)]
    assert w[even_n:]==expected
    rows.append({'orientation':'even_then_odd','even_size':even_n,'odd_size':odd_n,'trial':trial,'restriction_identity':True})
    # Reverse the block parities and retain the left odd state.
    M2=chain(g); O2=block(M2,0,odd_n); E2=block(M2,odd_n,n); w2=cof(M2)
    expected2=[pf(E2)*x for x in cof(O2)]
    assert w2[:odd_n]==expected2
    rows.append({'orientation':'odd_then_even','even_size':even_n,'odd_size':odd_n,'trial':trial,'restriction_identity':True})
 result={'schema':'marici.coherence.even-odd-pfaffian-module.v1','cases':len(rows),'all_restrictions_exact':True,'identity':'restriction to the odd block of cof(E union O) equals Pf(E) cof(O), on either side','rows':rows}
 Path(__file__).with_name('even-odd-pfaffian-module.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','all_restrictions_exact','identity')},indent=2))
if __name__=='__main__':main()
