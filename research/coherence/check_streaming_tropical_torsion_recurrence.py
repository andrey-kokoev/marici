#!/usr/bin/env python3
"""Streaming two-boundary-state recurrence for all Pfaffian-divisor valuations."""

import itertools, json, random
from pathlib import Path
INF=10**9
def stream(costs):
 # zero[k]: best k-matching with latest edge absent; one[k]: latest present.
 zero=[0];one=[INF]
 for c in costs:
  m=len(zero);nz=[INF]*(m+1);no=[INF]*(m+1)
  for k in range(m+1):
   if k<m:nz[k]=min(zero[k],one[k])
   if k>0 and k-1<m:no[k]=zero[k-1]+c
  zero,one=nz,no
 return [min(a,b) for a,b in zip(zero,one)]
def brute(costs,k):
 best=INF
 for S in itertools.combinations(range(len(costs)),k):
  if all(S[i+1]>S[i]+1 for i in range(len(S)-1)):best=min(best,sum(costs[i] for i in S))
 return best
def main():
 rng=random.Random(20260927);cases=0
 for n in range(1,18):
  for _ in range(30):
   c=[rng.randrange(0,12) for _ in range(n)];vals=stream(c)
   for k in range(n//2+1):assert vals[k]==brute(c,k)
   cases+=1
 result={'schema':'marici.coherence.streaming-tropical-torsion-recurrence.v1','cases':cases,'all_exact':True,'state_per_grade':['zero_k: latest edge absent','one_k: latest edge selected'],'update':['new_zero_k=min(zero_k,one_k)','new_one_k=zero_(k-1)+edge_cost'],'full_spectrum_state_growth':'two boundary states for each k up to floor(n/2)','interpretation':'fixed torsion grade has rank two recurrence; complete integral torsion spectrum has graded unbounded size'}
 Path(__file__).with_name('streaming-tropical-torsion-recurrence.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
