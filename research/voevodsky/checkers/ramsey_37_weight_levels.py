"""Compress shared weight table. Sort keys by fitted weights; merge into contiguous bins. Optimize bin weights with LP, verifying rounded candidates exactly. No claim of global minimum."""
import sys,json,gzip,itertools
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
D=root/'voevodsky/results';prior=json.loads((D/'ramsey_37_degree_walk2.json').read_text())['weights'];rows=[]
for line in gzip.open(p/'r36_16.g6.gz','rb'):
 A=graph6(line)
 if sum(v.bit_count() for v in A)!=66:continue
 F=independent_fives(A);ds=[[j for j,b in enumerate(F) if not a&b] for a in F];k=[(len(d),sum(len(ds[j]) for j in d)) for d in ds];C=Counter(k);seen=set()
 for d in ds:
  c=Counter(k[j] for j in d);v=tuple((i,6*c[i]-n) for i,n in sorted(C.items()));
  if v not in seen:rows.append(dict(v));seen.add(v)
K=sorted(set.union(*(set(v) for v in rows)),key=lambda k:(prior.get(str(k),0),k));M=np.array([[v.get(k,0) for k in K] for v in rows]);old=np.array([prior.get(str(k),0) for k in K]);assert min(M@old)>0;best=None
for scale in range(1,151):
 for fn in (np.log1p,np.sqrt,lambda x:x):
  t=fn(old/1e6);bins=np.unique(np.rint(scale*t/max(t)).astype(int),return_inverse=True)[1];a=np.stack([M[:,bins==j].sum(axis=1) for j in range(max(bins)+1)],axis=1);res=linprog(np.ones(a.shape[1]),A_ub=-a,b_ub=-np.ones(len(a)),bounds=(0,None));
  if not res.success:continue
  for factor in [1,2,4,8,16,64,1024,10**6]:
   w=np.rint(res.x*factor).astype('int64')[bins];m=int(min(M@w));
   if m>0:
    z=len(set(w));
    if best is None or z<best['levels']:best=dict(levels=z,alphabet=sorted(set(map(int,w))),margin=m,scale=scale,binner=fn.__name__,weights={str(k):int(v) for k,v in zip(K,w) if v})
    break
 if best and scale>=best['scale']+6:break
assert best
while True:
 v=np.array([best['weights'].get(str(k),0) for k in K]);lev=sorted(set(v));changed=False
 for i in sorted(range(len(lev)-1),key=lambda j:lev[j+1]-lev[j]):
  bins=np.unique(np.where(v==lev[i+1],lev[i],v),return_inverse=True)[1];a=np.stack([M[:,bins==j].sum(axis=1) for j in range(max(bins)+1)],axis=1);res=linprog(np.ones(a.shape[1]),A_ub=-a,b_ub=-np.ones(len(a)),bounds=(0,None));
  if not res.success:continue
  for factor in [1,2,4,8,16,64,1024,10**6]:
   w=np.rint(res.x*factor).astype('int64')[bins];m=int(min(M@w));
   if m>0:break
  if m<=0:continue
  best.update(levels=len(set(w)),alphabet=sorted(set(map(int,w))),margin=m,weights={str(k):int(t) for k,t in zip(K,w) if t});changed=True;break
 if not changed:break
print({k:v for k,v in best.items() if k!='weights'});(D/'ramsey_37_weight_levels.json').write_text(json.dumps(best,indent=2)+'\n')
