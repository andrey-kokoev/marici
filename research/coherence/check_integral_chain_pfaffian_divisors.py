#!/usr/bin/env python3
"""Compute all Pfaffian determinantal divisors of integral chain kernels."""

import itertools, json, math, random
from pathlib import Path

def path(gaps,i,j):
 z=1
 for x in gaps[i:j]:z*=x
 return z
def principal_pf(gaps,subset):
 z=1
 for a,b in zip(subset[0::2],subset[1::2]):z*=path(gaps,a,b)
 return z
def invariants(gaps):
 n=len(gaps)+1;Ds=[1];ds=[]
 for k in range(1,n//2+1):
  vals=[principal_pf(gaps,S) for S in itertools.combinations(range(n),2*k)]
  D=0
  for v in vals:D=math.gcd(D,abs(v))
  assert D%Ds[-1]==0
  ds.append(D//Ds[-1]);Ds.append(D)
  if len(ds)>1:assert ds[-1]%ds[-2]==0
 return Ds,ds
def main():
 rng=random.Random(20260922);rows=[]
 for n in range(2,10):
  for trial in range(10):
   gaps=[rng.randrange(1,13) for _ in range(n-1)];Ds,ds=invariants(gaps)
   if n%2==0:
    adjacent=1
    for x in gaps[0::2]:adjacent*=x
    assert Ds[-1]==abs(adjacent)
   rows.append({'points':n,'trial':trial,'pfaffian_divisors':Ds,'alternating_elementary_divisors':ds})
 result={'schema':'marici.coherence.integral-chain-pfaffian-divisors.v1','cases':len(rows),'all_divisibility_chains_valid':True,'formula':'D_k = gcd over 2k-subsets of products of path weights on adjacent selected pairs','elementary_divisors':'d_k=D_k/D_(k-1)','full_even_pfaffian':'D_m=abs(product of even-indexed gaps)','rows':rows}
 Path(__file__).with_name('integral-chain-pfaffian-divisors.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','all_divisibility_chains_valid','formula','elementary_divisors','full_even_pfaffian')},indent=2))
if __name__=='__main__':main()
