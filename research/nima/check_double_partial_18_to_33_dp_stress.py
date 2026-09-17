#!/usr/bin/env python3
"""Count-only common-triangulation stress tests for every n=18,...,33."""
import json,random,math,time
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SAMPLES=256
def count_common(beta):
 n=len(beta);pos=[0]*n
 for i,x in enumerate(beta):pos[x]=i
 prefix=[0]
 for x in range(n):prefix.append(prefix[-1]^(1<<pos[x]))
 full=(1<<n)-1;allowed=[[True]*n for _ in range(n)]
 for i in range(n):
  for j in range(i+2,n):
   if i==0 and j==n-1:continue
   m=prefix[j+1]^prefix[i+1];rot=((m<<1)&full)|(m>>(n-1))
   allowed[i][j]=allowed[j][i]=((m^rot).bit_count()==2)
 dp=[[0]*n for _ in range(n)]
 for i in range(n-1):dp[i][i+1]=1
 for gap in range(2,n):
  for i in range(n-gap):
   j=i+gap;s=0
   for k in range(i+1,j):
    if (k==i+1 or allowed[i][k]) and (k==j-1 or allowed[k][j]):s+=dp[i][k]*dp[k][j]
   dp[i][j]=s
 return dp[0][n-1]
rows=[];started=time.time();allchecks=True
for n in range(18,34):
 rng=random.Random(330000+n);identity=(0,)+tuple(range(1,n));structured={identity}
 # Random interval-block reversals preserve substantial common interval structure.
 while len(structured)<SAMPLES//2:
  cuts=sorted(rng.sample(range(2,n),rng.randint(1,min(7,n-3))));blocks=[];start=1
  for stop in cuts+[n]:
   block=list(range(start,stop))
   if rng.randrange(2):block.reverse()
   blocks.extend(block);start=stop
  b=(0,)+tuple(blocks);r=(0,)+tuple(reversed(blocks));structured.add(min(b,r))
 orders=set(structured)
 while len(orders)<SAMPLES:
  tail=list(range(1,n));rng.shuffle(tail);b=(0,)+tuple(tail);r=(0,)+tuple(reversed(tail));orders.add(min(b,r))
 counts={b:count_common(b) for b in orders};hist=Counter(counts.values());structured_hist=Counter(counts[b] for b in structured);cat=math.comb(2*(n-2),n-2)//(n-1);closed=hist[cat];nonempty=SAMPLES-hist[0];proper=[c for c in hist if 0<c<cat]
 checks={'sample_count':len(orders)==SAMPLES,'identity_catalan':count_common(tuple(range(n)))==cat,'one_sampled_full_case':closed==1};allchecks &= all(checks.values())
 rows.append({'n':n,'dimension':n-4,'samples':SAMPLES,'catalan_facets':cat,'empty':hist[0],'nonempty':nonempty,'structured_samples':len(structured),'structured_nonempty':len(structured)-structured_hist[0],'sampled_full_cases':closed,'maximum_proper_facets':max(proper) if proper else 0,'distinct_facet_counts':len(hist),'checks':checks})
out={'schema':'marici.nima.double-partial-18-to-33-dp-stress.v1','range':[18,33],'samples_per_n':SAMPLES,'total_samples':SAMPLES*16,'elapsed_seconds':round(time.time()-started,3),'results':rows,'passed':allchecks,'scope':'Count-only structured plus deterministic-random stress census; not exhaustive. Arbitrary-n orientation coherence is proved separately by ambient restriction.'}
p=ROOT/'research/nima/results/double-partial-18-to-33-dp-stress.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':out['passed'],'total_samples':out['total_samples'],'elapsed_seconds':out['elapsed_seconds'],'summary':[{'n':r['n'],'empty':r['empty'],'nonempty':r['nonempty'],'max_proper':r['maximum_proper_facets'],'catalan':r['catalan_facets']} for r in rows]},indent=2));raise SystemExit(0 if out['passed'] else 1)
