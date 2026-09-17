#!/usr/bin/env python3
"""Classify all sharp proper Catalan cases through n=9 using O(n^3) counting."""
import itertools,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def count_common(beta):
 n=len(beta);pos=[0]*n
 for i,x in enumerate(beta):pos[x]=i
 prefix=[0]
 for x in range(n):prefix.append(prefix[-1]^(1<<pos[x]))
 full=(1<<n)-1;ok=[[True]*n for _ in range(n)]
 for i in range(n):
  for j in range(i+2,n):
   if i==0 and j==n-1:continue
   m=prefix[j+1]^prefix[i+1];rot=((m<<1)&full)|(m>>(n-1));ok[i][j]=ok[j][i]=(m^rot).bit_count()==2
 dp=[[0]*n for _ in range(n)]
 for i in range(n-1):dp[i][i+1]=1
 for g in range(2,n):
  for i in range(n-g):
   j=i+g;dp[i][j]=sum(dp[i][k]*dp[k][j] for k in range(i+1,j) if (k==i+1 or ok[i][k]) and (k==j-1 or ok[k][j]))
 return dp[0][n-1]
def normalize(c):
 n=len(c);i=c.index(0);r=c[i:]+c[:i];z=(0,)+tuple(reversed(r[1:]));return min(tuple(r),z)
def adjacent_swaps(n):
 a=list(range(n));out=set()
 for i in range(n):
  b=a[:];j=(i+1)%n;b[i],b[j]=b[j],b[i];out.add(normalize(tuple(b)))
 return out
rows=[];fails=[]
for n in range(4,10):
 target=math.comb(2*(n-3),n-3)//(n-2);sharp=[];maximum=0
 for tail in itertools.permutations(range(1,n)):
  b=(0,)+tail;r=(0,)+tuple(reversed(tail))
  if b>r:continue
  c=count_common(b)
  if c<math.comb(2*(n-2),n-2)//(n-1):maximum=max(maximum,c)
  if c==target:sharp.append(b)
 expected=adjacent_swaps(n);actual=set(sharp);ok=actual==expected
 if not ok:fails.append({'n':n,'missing':[list(x) for x in expected-actual],'extra':[list(x) for x in actual-expected]})
 rows.append({'n':n,'proper_maximum':maximum,'catalan_bound':target,'sharp_order_orbits':len(actual),'adjacent_swap_orbits':len(expected),'sharp_cases_exactly_adjacent_swaps':ok})
out={'schema':'marici.nima.catalan-extremizer-classification.v1','range':[4,9],'results':rows,'failures':fails,'passed':not fails,'scope':'Exhaustive over cyclic orders modulo reversal with alpha fixed.'}
p=ROOT/'research/nima/results/catalan-extremizer-classification.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
