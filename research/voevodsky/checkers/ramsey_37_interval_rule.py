"""Generate interval indicators 1[d=a and lo<=s<=hi] by LP pricing. Start without any fitted table. Superpose nonnegative indicators, then translate into disjoint constant intervals. Exact integer margin check on success, no optimality claim for rule length."""
import sys,json,gzip,itertools
from pathlib import Path
from collections import Counter
import numpy as np
from scipy.optimize import linprog
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
rows=[]
for line in gzip.open(p/'r36_16.g6.gz','rb'):
 A=graph6(line)
 if sum(v.bit_count() for v in A)!=66:continue
 F=independent_fives(A);D=[[j for j,b in enumerate(F) if not a&b] for a in F];K=[(len(d),sum(len(D[j]) for j in d)) for d in D];cnt=Counter(K);seen=set()
 for d in D:
  c=Counter(K[j] for j in d);r=tuple((k,6*c[k]-v) for k,v in sorted(cnt.items()));
  if r not in seen:rows.append(dict(r));seen.add(r)
K=sorted(set.union(*(set(r) for r in rows)));M=np.array([[r.get(k,0) for k in K] for r in rows]);ranges=[list(g) for _,g in itertools.groupby(range(len(K)),lambda j:K[j][0])];cols=[np.ones(len(M))];spans=[]
for iteration in range(200):
 mat=np.column_stack(cols);res=linprog([1]+[1e-6]*len(spans),A_ub=-mat,b_ub=-np.ones(len(M)),bounds=(0,None));assert res.success
 if res.x[0]<.99 and spans:
  x=np.rint(res.x[1:]*1e7).astype('int64');w=np.zeros(len(K),dtype='int64');
  for (i,j),v in zip(spans,x):w[i:j+1]+=v
  if min(M@w)>0:break
 score=(-res.ineqlin.marginals)@M;offers=[]
 for g in ranges:
  # maximum subarray along ordered s for each d
  start=g[0];v=0;best=(-1,None)
  for j in g:
   if v<=0:start=j;v=0
   v+=score[j];best=max(best,(v,(start,j))) if v>best[0] else best
  if best[0]>1.001e-6 and best[1] not in spans:offers.append(best)
 assert offers
 for _,(i,j) in sorted(offers,reverse=True)[:8]:spans.append((i,j));cols.append(M[:,i:j+1].sum(axis=1))
else:raise ArithmeticError('iteration cap')
intervals=[]
for g in ranges:
 for v,js in itertools.groupby(g,lambda j:int(w[j])):
  js=list(js)
  if v:intervals.append([K[js[0]][0],K[js[0]][1],K[js[-1]][1],v])
assert all(sum(v for a,l,h,v in intervals if d==a and l<=s<=h)==t for (d,s),t in zip(K,w));out=dict(keys=len(K),degreeBranches=len(ranges),rounds=iteration,nonzeroIntervals=intervals,margin=int(min(M@w)));print(len(intervals),out['degreeBranches'],iteration,out['margin'],sum(w>0));(root/'voevodsky/results/ramsey_37_interval_rule.json').write_text(json.dumps(out,indent=2)+'\n')
