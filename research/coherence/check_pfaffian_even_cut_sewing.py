#!/usr/bin/env python3
"""Verify exact factorization at every contiguous even cut of a chain kernel."""

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
def principal(A,start,end):return [row[start:end] for row in A[start:end]]
def main():
 rng=random.Random(20260912);rows=[]
 for n in (4,6,8,10,12):
  for trial in range(12):
   gaps=[Fraction(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(n-1)];M=chain(gaps);whole=pf(M)
   for cut in range(2,n,2):
    left=pf(principal(M,0,cut));right=pf(principal(M,cut,n));assert whole==left*right
    rows.append({'size':n,'cut':cut,'trial':trial,'factorization':True})
 result={'schema':'marici.coherence.pfaffian-even-cut-sewing.v1','cases':len(rows),'all_even_cuts_factor_exactly':True,'identity':'Pf(M_[0,n))=Pf(M_[0,2k)) Pf(M_[2k,n))','consequence':'iterated sewing across contiguous even blocks is independent of parenthesization'}
 Path(__file__).with_name('pfaffian-even-cut-sewing.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
