"""Try to refute even sums of nonnegative increasing and decreasing rules for each d. Columns are all prefix/suffix indicators. A dual combination nonpositive on all columns refutes arbitrary branch-specific directions. Check with Python integers."""
import sys,gzip,json,itertools
from pathlib import Path
from collections import Counter
import numpy as np
from scipy.optimize import linprog
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
rows=[];names=[]
for rec,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 A=graph6(line)
 if sum(v.bit_count() for v in A)!=66:continue
 F=independent_fives(A);D=[[j for j,b in enumerate(F) if not a&b] for a in F];K=[(len(d),sum(len(D[j]) for j in d)) for d in D];cnt=Counter(K);seen=set()
 for t,d in zip(F,D):
  c=Counter(K[j] for j in d);r=tuple((k,6*c[k]-v) for k,v in sorted(cnt.items()));
  if r not in seen:rows.append(dict(r));seen.add(r);names.append((rec,t))
K=sorted(set.union(*(set(r) for r in rows)));M=np.array([[r.get(k,0) for k in K] for r in rows]);groups=[list(g) for _,g in itertools.groupby(range(len(K)),lambda j:K[j][0])];results={}
for mode in ['both','inc','dec']:
 cols=[]
 for g in groups:
  if mode!='dec':cols.extend(M[:,g[i:]].sum(axis=1) for i in range(len(g)))
  if mode!='inc':cols.extend(M[:,g[:i+1]].sum(axis=1) for i in range(len(g)-(mode=='both')))
 B=np.column_stack(cols);n,m=B.shape
 # Seek aggregate strictly negative on every allowed indicator; weight each column by its support to condition the solver.
 scale=np.maximum(1,np.abs(B).max(axis=0));res=linprog([0]*n+[1],A_ub=np.column_stack((B.T,-scale)),b_ub=np.zeros(m),A_eq=[[1]*n+[0]],b_eq=[1],bounds=[(0,None)]*n+[(None,None)]);assert res.success;sol=res.x[:-1];use=np.where(sol>1e-12)[0];z=np.rint(sol[use]*1e10).astype('int64');upper=max(z@B[use]);print(mode,res.fun,upper,len(use),flush=True);results[mode]=dict(maxCoefficient=int(upper),verified=bool(upper<=0),multipliers=[[*names[i],int(v)] for i,v in zip(use,z)] if upper<=0 else None)
 if upper<=0:
  assert min(z)>0 and all(sum(int(v)*int(b) for v,b in zip(z,col))<=0 for col in B[use].T)
  if mode=='both':break
(root/'voevodsky/results/ramsey_37_monotone_barrier.json').write_text(json.dumps(results,indent=2)+'\n')
