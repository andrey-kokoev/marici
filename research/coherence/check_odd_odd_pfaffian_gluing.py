#!/usr/bin/env python3
"""Test odd-state contraction against the even Pfaffian under contiguous sewing."""

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
def cof(A):
 return [(-1 if i%2 else 1)*pf([[A[r][c] for c in range(len(A)) if c!=i] for r in range(len(A)) if r!=i]) for i in range(len(A))]
def main():
 rng=random.Random(20260912);rows=[];ratios=set()
 for left_n,right_n in ((1,1),(1,3),(3,1),(3,3),(3,5),(5,3),(5,5)):
  for trial in range(12):
   n=left_n+right_n;g=[Fraction(rng.randrange(1,10),rng.randrange(1,10)) for _ in range(n-1)];M=chain(g)
   A=[row[:left_n] for row in M[:left_n]];C=[row[left_n:] for row in M[left_n:]];B=[row[left_n:] for row in M[:left_n]]
   u,v=cof(A),cof(C);pair=sum(u[i]*B[i][j]*v[j] for i in range(left_n) for j in range(right_n));whole=pf(M)
   assert pair
   ratio=whole/pair;ratios.add(ratio);rows.append({'left':left_n,'right':right_n,'ratio':str(ratio),'cross_block_rank_one':all(B[i][j]*B[0][0]==B[i][0]*B[0][j] for i in range(left_n) for j in range(right_n))})
 assert len(ratios)==1 and all(r['cross_block_rank_one'] for r in rows)
 result={'schema':'marici.coherence.odd-odd-pfaffian-gluing.v1','cases':len(rows),'universal_gluing_sign':str(next(iter(ratios))),'all_cross_blocks_rank_one':True,'identity':'Pf([[A,B],[-B^T,C]]) = sign * cof(A)^T B cof(C)','rows':rows}
 Path(__file__).with_name('odd-odd-pfaffian-gluing.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','universal_gluing_sign','all_cross_blocks_rank_one','identity')},indent=2))
if __name__=='__main__':main()
