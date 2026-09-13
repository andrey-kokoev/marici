#!/usr/bin/env python3
"""Compare Pfaffian-divisor valuations with minimum ordered matching costs."""

import itertools, json, random
from functools import lru_cache
from pathlib import Path

def path(c,i,j):return sum(c[i:j])
def brute(c,k):
 n=len(c)+1
 return min(sum(path(c,a,b) for a,b in zip(S[0::2],S[1::2])) for S in itertools.combinations(range(n),2*k))
def dynamic(c,k):
 n=len(c)+1
 @lru_cache(None)
 def f(i,q):
  if q==0:return 0
  if n-i<2*q:return 10**9
  best=f(i+1,q)
  for j in range(i+1,n):best=min(best,path(c,i,j)+f(j+1,q-1))
  return best
 return f(0,k)
def main():
 rng=random.Random(20260923);rows=[]
 for n in range(2,12):
  for trial in range(20):
   costs=[rng.randrange(0,7) for _ in range(n-1)];vals=[]
   for k in range(1,n//2+1):
    b=brute(costs,k);d=dynamic(costs,k);assert b==d;vals.append(b)
   elementary=[vals[0]]+[vals[i]-vals[i-1] for i in range(1,len(vals))]
   assert all(elementary[i]<=elementary[i+1] for i in range(len(elementary)-1))
   rows.append({'points':n,'trial':trial,'gap_valuations':costs,'pfaffian_divisor_valuations':vals,'elementary_divisor_valuations':elementary})
 result={'schema':'marici.coherence.tropical-pfaffian-divisor-matching.v1','cases':len(rows),'all_brute_force_equals_dynamic_program':True,'formula':'v_p(D_k)=minimum cost of k ordered disjoint path pairs','elementary':'v_p(d_k)=v_p(D_k)-v_p(D_(k-1))','rows':rows}
 Path(__file__).with_name('tropical-pfaffian-divisor-matching.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','all_brute_force_equals_dynamic_program','formula','elementary')},indent=2))
if __name__=='__main__':main()
