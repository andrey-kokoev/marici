#!/usr/bin/env python3
"""Reduce tropical principal-Pfaffian optimization to path k-matching."""

import itertools, json, random
from functools import lru_cache
from pathlib import Path

def interval_brute(c,k):
 n=len(c)+1
 def path(i,j):return sum(c[i:j])
 return min(sum(path(a,b) for a,b in zip(S[0::2],S[1::2])) for S in itertools.combinations(range(n),2*k))
def edge_dp(c,k):
 @lru_cache(None)
 def f(i,q):
  if q==0:return 0
  if len(c)-i<2*q-1:return 10**9
  return min(f(i+1,q),c[i]+f(i+2,q-1))
 return f(0,k)
def main():
 rng=random.Random(20260924);rows=[]
 for n in range(2,14):
  for trial in range(25):
   c=[rng.randrange(0,9) for _ in range(n-1)]
   vals=[]
   for k in range(1,n//2+1):
    a=interval_brute(c,k);b=edge_dp(c,k);assert a==b;vals.append(a)
   rows.append({'points':n,'trial':trial,'gap_costs':c,'minimum_k_matching_costs':vals})
 result={'schema':'marici.coherence.pfaffian-divisor-path-matching-reduction.v1','cases':len(rows),'all_exact':True,'closed_reduction':'v_p(D_k) is minimum weight k-matching on the adjacent-edge path','recurrence':'F(i,k)=min(F(i+1,k),c_i+F(i+2,k-1))','complexity':'O(nk)','rows':rows}
 Path(__file__).with_name('pfaffian-divisor-path-matching-reduction.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','all_exact','closed_reduction','recurrence','complexity')},indent=2))
if __name__=='__main__':main()
