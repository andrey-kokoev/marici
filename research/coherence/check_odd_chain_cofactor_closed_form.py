#!/usr/bin/env python3
"""Verify closed alternating-product formulas for every odd-chain cofactor."""

import random, json
from fractions import Fraction
from pathlib import Path
import check_odd_chain_pfaffian_kernel as core

def prod(xs):
 z=Fraction(1)
 for x in xs:z*=x
 return z
def closed(gaps,i):
 if i%2==0:
  r=i//2
  return prod(gaps[:i:2])*prod(gaps[i+1::2])
 r=(i-1)//2
 return -prod(gaps[:i-1:2])*gaps[i-1]*gaps[i]*prod(gaps[i+2::2])
def main():
 rng=random.Random(20260926);cases=0
 for n in range(3,14,2):
  for _ in range(30):
   gaps=[Fraction(rng.randrange(1,11),rng.randrange(1,11)) for _ in range(n-1)];A=core.chain(gaps);v=[]
   for i in range(n):
    minor=[[A[r][c] for c in range(n) if c!=i] for r in range(n) if r!=i]
    actual=(1 if i%2==0 else -1)*core.pf(minor);expected=closed(gaps,i);assert actual==expected;v.append(expected)
   assert all(sum(A[i][j]*v[j] for j in range(n))==0 for i in range(n));cases+=1
 result={'schema':'marici.coherence.odd-chain-cofactor-closed-form.v1','cases':cases,'sizes':[3,5,7,9,11,13],'all_cofactors_match_closed_form':True,'all_closed_vectors_annihilated':True,'even_coordinate':'product even gaps left * product odd gaps right','odd_coordinate':'negative product even gaps left * crossing two-gap product * product odd gaps right'}
 Path(__file__).with_name('odd-chain-cofactor-closed-form.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
