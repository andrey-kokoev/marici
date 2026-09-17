#!/usr/bin/env python3
"""O(n^3) dynamic-programming stress census of common triangulation counts at n=17."""
import json,random,math
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];N=17;SAMPLES=10000
def beta_interval(i,j,pos):
 # Alpha diagonal (i,j), labels 0..n-1; one split side is i+1..j.
 S=set(range(i+1,j+1));bits=[False]*N
 for x in S:bits[pos[x]]=True
 return sum(bits[t]!=bits[(t+1)%N] for t in range(N))==2
def count_common(beta):
 pos={x:i for i,x in enumerate(beta)};allowed=[[True]*N for _ in range(N)]
 for i in range(N):
  for j in range(i+2,N):
   if i==0 and j==N-1:continue
   allowed[i][j]=allowed[j][i]=beta_interval(i,j,pos)
 dp=[[0]*N for _ in range(N)]
 for i in range(N-1):dp[i][i+1]=1
 for gap in range(2,N):
  for i in range(N-gap):
   j=i+gap;s=0
   for k in range(i+1,j):
    left=(k==i+1 or allowed[i][k]);right=(k==j-1 or allowed[k][j])
    if left and right:s+=dp[i][k]*dp[k][j]
   dp[i][j]=s
 return dp[0][N-1]
rng=random.Random(170017);orders={(0,)+tuple(range(1,N))}
# Structured reversals/block patterns plus deterministic random dihedral representatives.
orders.add((0,)+tuple(range(1,N,2))+tuple(range(2,N,2)))
orders.add((0,)+tuple(range(2,N,2))+tuple(range(1,N,2)))
while len(orders)<SAMPLES:
 tail=list(range(1,N));rng.shuffle(tail);b=(0,)+tuple(tail);r=(0,)+tuple(reversed(tail));orders.add(min(b,r))
hist=Counter();nonempty=[]
for b in orders:
 c=count_common(b);hist[c]+=1
 if c:nonempty.append((c,b))
catalan=math.comb(2*(N-2),N-2)//(N-1);mx=max(c for c,b in nonempty);closed=sum(c==catalan for c,b in nonempty)
checks={'ten_thousand_distinct_orbits':len(orders)==SAMPLES,'identity_has_full_catalan_count':count_common(tuple(range(N)))==catalan,'counts_nonnegative':all(c>=0 for c in hist),'unique_sampled_full_case':closed==1}
out={'schema':'marici.nima.double-partial-seventeen-point-dp-stress.v1','n':N,'dimension':N-4,'samples':len(orders),'full_associahedral_facets':catalan,'empty_samples':hist[0],'nonempty_samples':len(nonempty),'sampled_full_cases':closed,'maximum_proper_sampled_facets':max(c for c,b in nonempty if c<catalan) if len(nonempty)>closed else 0,'count_histogram':dict(sorted(hist.items())),'largest_proper_examples':[{'facets':c,'beta':list(b)} for c,b in sorted((x for x in nonempty if x[0]<catalan),reverse=True)[:10]],'checks':checks,'passed':all(checks.values()),'scope':'Count-only deterministic stress test. Orientation coherence at n=17 follows symbolically by restriction of the ambient oriented associahedral sphere, not from this sample.'}
p=ROOT/'research/nima/results/double-partial-seventeen-point-dp-stress.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'samples':len(orders),'catalan':catalan,'empty':hist[0],'nonempty':len(nonempty),'closed':closed,'max_proper':out['maximum_proper_sampled_facets']},indent=2));raise SystemExit(0 if out['passed'] else 1)
