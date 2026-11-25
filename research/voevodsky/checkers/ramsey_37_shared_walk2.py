"""One shared nonnegative weight per two-step count. Float LP discovers certificate; integer arithmetic checks it. If infeasible, reduce graphs greedily and seek strictly negative aggregate, rationalizing a boundary solution by exact elimination if necessary."""
import gzip,sys,json,math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
rows=[];keys=[];ids=[];capacities={};by_capacity='--capacity' in sys.argv;by_degree='--degree' in sys.argv;assert not(by_capacity and by_degree)
for j,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 A=graph6(line)
 if sum(v.bit_count() for v in A)!=66:continue
 F=independent_fives(A);D=[[h for h,b in enumerate(F) if not a&b] for a in F];s=[sum(len(D[h]) for h in d) for d in D];capacities[j]=len(F);s=[(len(F),v) for v in s] if by_capacity else [(len(d),v) for d,v in zip(D,s)] if by_degree else s;counts=Counter(s);seen=set()
 for t,d in zip(F,D):
  cover=Counter(s[h] for h in d);v={k:6*cover[k]-n for k,n in counts.items()};k=tuple(sorted(v.items()))
  if k in seen:continue
  seen.add(k);rows.append(v);keys.append((j,t));ids.append(j)
K=sorted(set.union(*(set(v) for v in rows)));M=np.array([[v.get(k,0) for k in K] for v in rows]);ids=np.array(ids)
def solve(a):return linprog(np.ones(len(K)),A_ub=-a,b_ub=-np.ones(len(a)),bounds=(0,None))
res=solve(M);out=dict(classes=len(K),constraints=len(M),capacityGroups=dict(Counter(capacities.values())) if by_capacity else None)
if by_degree:
 old=json.loads((root/'voevodsky/results/ramsey_37_capacity_walk2.json').read_text());core=sorted({t[0] for t in old['dual']});a=M[np.isin(ids,core)];z=solve(a);out['priorCore']=core
 if z.success:
  ww=np.rint(z.x*10**6).astype('int64');assert min(a@ww)>0;out['priorCoreMargin']=int(min(a@ww))
if by_capacity:
 out['byCapacity']={}
 for f in sorted(set(capacities.values())):
  a=M[np.isin(ids,[j for j,v in capacities.items() if v==f])];z=solve(a)
  if z.success:
   ww=np.rint(z.x*10**6).astype('int64');assert min(a@ww)>0;out['byCapacity'][f]={'weights':{str(k[1]):int(v) for k,v in zip(K,ww) if v},'margin':int(min(a@ww))}
  else:out['byCapacity'][f]={'solverStatus':z.status}
 print('group weights verified:',[f for f,v in out['byCapacity'].items() if 'margin' in v]);
if res.success:
 w=np.rint(res.x*10**6).astype('int64');assert min(M@w)>0;out.update(weights={str(k):int(v) for k,v in zip(K,w) if v},margin=int(min(M@w)))
else:
 assert res.status==2;G=set(ids.tolist());
 for j in sorted(G):
  trial=G-{j};z=solve(M[np.isin(ids,list(trial))]) # Unknown numeric status: retain graph; exact final dual is decisive.
  if z.status==2:G=trial
 ix=np.where(np.isin(ids,list(G)))[0];a=M[ix];a=a[:,np.any(a!=0,axis=0)];L=len(a);res=linprog([0]*L+[1],A_ub=np.column_stack((a.T,-np.ones(a.shape[1]))),b_ub=np.zeros(a.shape[1]),A_eq=[[1]*L+[0]],b_eq=[1],bounds=[(0,None)]*L+[(None,None)]);assert res.success
 use=np.where(res.x[:-1]>1e-10)[0];aa=a[use];w=np.rint(res.x[use]*10**8).astype('int64');print('core',G,'dual margin',res.fun,'round max',max(w@aa),flush=True)
 if max(w@aa)>0:
  # exact rational values on the dual LP vertex, including its objective
  eq=[[Q(1)]*len(use)+[Q(0),Q(1)]]+[[Q(int(v)) for v in col]+[Q(-1),Q(0)] for col in aa.T if abs(res.x[use]@col-res.fun)<1e-8];n=len(use)+1
  for col in range(n):
   h=next(i for i in range(col,len(eq)) if eq[i][col]);eq[col],eq[h]=eq[h],eq[col];u=eq[col]=[x/eq[col][col] for x in eq[col]]
   for i,v in enumerate(eq):
    if i!=col and v[col]:eq[i]=[x-v[col]*y for x,y in zip(v,u)]
  f=[eq[i][-1] for i in range(len(use))];den=math.lcm(*(v.denominator for v in f));w=[int(v*den) for v in f]
 w=list(map(int,w));assert min(w)>0 and all(sum(x*int(v) for x,v in zip(w,col))<=0 for col in M[ix[use]].T);out.update(core=sorted(G),dual=[[*keys[i],v] for i,v in zip(ix[use],w)])
print({k:(len(v) if k in ('dual','weights','byCapacity') else v) for k,v in out.items()});(root/('voevodsky/results/ramsey_37_capacity_walk2.json' if by_capacity else 'voevodsky/results/ramsey_37_degree_walk2.json' if by_degree else 'voevodsky/results/ramsey_37_shared_walk2.json')).write_text(json.dumps(out,indent=2)+'\n')
