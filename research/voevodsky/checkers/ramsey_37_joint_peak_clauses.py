"""Lift the 78 pair-release proofs to global peak clauses. A marker escapes a proof precisely when some interval containing it has positive aggregate margin. Try a joint model: one peak per d, weights in [0,1], monotonicity on each side; then refit and verify integer weights. A bounded numerical search is not an impossibility proof."""
import gzip,json,itertools,sys
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.optimize import linprog,milp,Bounds,LinearConstraint
from scipy.sparse import csr_matrix
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
D=root/'voevodsky/results';load=lambda s:json.loads((D/s).read_text());rows={};G={245,973,1813}
for rec,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 if rec not in G:continue
 F=independent_fives(graph6(line));ds=[[j for j,b in enumerate(F) if not a&b] for a in F];k=[(len(d),sum(len(ds[h]) for h in d)) for d in ds];cnt=Counter(k)
 for t,d in zip(F,ds):
  hit=Counter(k[j] for j in d);rows[rec,t]={v:6*hit[v]-n for v,n in cnt.items()}
K=sorted(set.union(*(set(r) for r in rows.values())));groups=[list(g) for _,g in itertools.groupby(range(len(K)),lambda j:K[j][0])];n=len(K);M=np.array(list({tuple(r.get(k,0) for k in K) for r in rows.values()}));clauses=set();npf=0
for case in load('ramsey_37_alternative_pair_release.json'):
 for pr in case['proof']:
  npf+=1;col=Counter()
  for rec,t,v in pr['dual']:
   assert v>0
   for k,w in rows[rec,t].items():col[k]+=int(v)*w
  esc=[]
  for g in groups:
   pp=[0];
   for j in g:pp.append(pp[-1]+col[K[j]])
   esc.extend(j for i,j in enumerate(g) if max(pp[i+1:])>min(pp[:i+1]))
  clauses.add(tuple(esc))
# remove redundant supersets
minimal=[]
for c in sorted(clauses,key=lambda v:(len(v),v)):
 if not any(v.issubset(c) for v in minimal):minimal.append(set(c))
S=np.array([[int(j in g) for j in range(n)] for g in groups]);C=np.array([[int(j in c) for j in range(n)] for c in minimal]);orig=load('ramsey_37_four_peaks.json')['initial'];fixed=[K.index(tuple(a)) for a,b in orig if a==b];cost=np.array([-int(j in fixed) for j in range(n)]);res=milp(cost,integrality=np.ones(n),bounds=Bounds(0,1),constraints=[LinearConstraint(S,1,1),LinearConstraint(C,1,np.inf)]);schedule=np.where(res.x>.5)[0].tolist();assert all(len(set(schedule)&set(g))==1 for g in groups) and all(set(schedule).intersection(c) for c in clauses);out=dict(proofs=npf,uniqueClauses=len(clauses),minimalClauses=len(minimal),clauseWitness=[K[j] for j in schedule],changed=len(set(fixed)-set(schedule)));print(out,flush=True)
# Directly test the clause witness; a new dual excludes it even if it satisfied every inherited clause.
prefix=np.c_[np.zeros(len(M),dtype=int),np.cumsum(M,axis=1)];B=np.stack([prefix[:,h+1]-prefix[:,l] for g,c in zip(groups,schedule) for l in range(g[0],c+1) for h in range(c,g[-1]+1)],axis=1);a=np.array([list(r.get(k,0) for k in K) for r in rows.values()]);names={tuple(r):key for r,key in zip(a,rows)};scale=np.maximum(1,np.abs(B).max(axis=0));nr=len(M);lp=linprog([0]*nr+[1],A_ub=np.c_[B.T,-scale],b_ub=np.zeros(B.shape[1]),A_eq=[[1]*nr+[0]],b_eq=[1],bounds=[(0,None)]*nr+[(None,None)]);assert lp.success;u=np.rint(lp.x[:-1]*1e10).astype('int64');upper=max(sum(int(v)*int(b) for v,b in zip(u,col) if v) for col in B.T);assert min(u)>=0 and max(u)>0 and upper<=0;out['newExclusion']=[[*names[tuple(r)],int(v)] for r,v in zip(M,u) if v];print('new exclusion',len(out['newExclusion']),upper,flush=True)
if '--iterate' in sys.argv:
 import time
 rng=np.random.default_rng(245);trace=[];ans=None;lo=time.monotonic();prior=load('ramsey_37_local_peak_barriers.json')[1]['alternative']['weights'];h0=np.array([prior.get(str(k),0) for k in K]);fav=np.zeros(n)
 for g in groups:
  # Prefer peaks which lose least of the feasible unrestricted profile when monotonized. Normalize each branch separately.
  y=h0[g]/max(1,max(h0[g]));fav[g]=[sum(abs(y[:i+1]-np.maximum.accumulate(y[:i+1])))+sum(abs(y[i:]-np.maximum.accumulate(y[i:][::-1])[::-1])) for i in range(len(g))]
 def lift(u):
  col=[sum(int(a)*int(v) for a,v in zip(u,c) if a) for c in M.T];ret=set()
  for g in groups:
   pp=[0];
   for j in g:pp.append(pp[-1]+col[j])
   ret.update(j for i,j in enumerate(g) if max(pp[i+1:])>min(pp[:i+1]))
  return ret
 def columns(sc,active):
  spans=[s for i,(g,c) in enumerate(zip(groups,sc)) for s in ([(l,h) for l in range(g[0],c+1) for h in range(c,g[-1]+1)] if i in active else [(j,j) for j in g])];ii,jj=np.array(spans).T;return spans,prefix[:,jj+1]-prefix[:,ii]
 minimal.append(lift(u));remaining=range(len(groups));
 for it in range(60):
  cc=np.array([[int(j in c) for j in range(n)] for c in minimal]);obj=fav+rng.uniform(0,.05,n);ms=milp(obj,integrality=np.ones(n),bounds=Bounds(0,1),constraints=[LinearConstraint(S,1,1),LinearConstraint(cc,1,np.inf)],options={'time_limit':4});
  if ms.x is None:break
  sc=np.where(ms.x>.5)[0].tolist();assert len(sc)==len(groups) and all(len(set(sc)&set(g))==1 for g in groups) and all(set(sc)&c for c in minimal);active=set(remaining);sp,bb=columns(sc,active);pr=linprog(np.ones(len(sp)),A_ub=-bb,b_ub=-np.ones(nr),bounds=(0,None));
  if pr.success:
   co=np.rint(pr.x*1e7).astype('int64');w=[sum(int(v) for (l,h),v in zip(sp,co) if l<=j<=h) for j in range(n)];margin=min(sum(int(a)*v for a,v in zip(row,w)) for row in M);assert margin>0 and min(w)>=0 and all(all(w[j]<=w[j+1] if j<c else w[j]>=w[j+1] for j in g[:-1]) for g,c in zip(groups,sc));ans=dict(weights={str(k):v for k,v in zip(K,w) if v},margin=margin);break
  order=rng.permutation(len(groups));
  for i in order:
   aa=active-{i};_,b=columns(sc,aa);zz=linprog(np.ones(b.shape[1]),A_ub=-b,b_ub=-np.ones(nr),bounds=(0,None));
   if zz.status==2:active=aa
  # Try the localized system first; fall back to all peaks if the rounded dual fails.
  for aa in [active,set(remaining)]:
   _,b=columns(sc,aa);scale=np.maximum(1,np.abs(b).max(axis=0));lp=linprog([0]*nr+[1],A_ub=np.c_[b.T,-scale],b_ub=np.zeros(b.shape[1]),A_eq=[[1]*nr+[0]],b_eq=[1],bounds=[(0,None)]*nr+[(None,None)]);
   if not lp.success:continue
   z=np.rint(lp.x[:-1]*1e10).astype('int64');esc=lift(z)
   if min(z)>=0 and max(z)>0 and not set(sc)&esc:break
  else:break
  assert not any(c<=esc for c in minimal);minimal=[c for c in minimal if not esc<=c]+[esc];trace.append(dict(peaks=[K[j] for j in sc],escape=[K[j] for j in sorted(esc)],dual=[[*names[tuple(r)],int(v)] for r,v in zip(M,z) if v]));
  if time.monotonic()-lo>80:break
 print('rounds',len(trace),'success',ans is not None,'cut sizes',[len(t['escape']) for t in trace]);(D/'ramsey_37_iterated_peak_clauses.json').write_text(json.dumps(dict(trace=trace,verified=ans),indent=2)+'\n');sys.exit()
# Bound indicator constants by normalizing the largest weight to <=1. Seek any positive margin, not an optimal one.
cons=[];lower=[];upper=[]
def add(row,l,h):cons.append(row);lower.append(l);upper.append(h)
for row in M:add(np.r_[row,np.zeros(n),-1],0,np.inf)
for row in S:add(np.r_[np.zeros(n),row,0],1,1)
for row in C:add(np.r_[np.zeros(n),row,0],1,np.inf)
for g in groups:
 for j in g[:-1]:
  v=np.zeros(2*n+1);v[j]=1;v[j+1]=-1;v[n+g[0]:n+j+1]=-1;add(v,-np.inf,0)
  v=np.zeros(2*n+1);v[j]=-1;v[j+1]=1;v[n+j+1:n+g[-1]+1]=-1;add(v,-np.inf,0)
cc=np.zeros(2*n+1);cc[-1]=0;lb=np.zeros(2*n+1);lb[-1]=1e-4
res=milp(cc,integrality=np.r_[np.zeros(n),np.ones(n),0],bounds=Bounds(lb,1),constraints=LinearConstraint(csr_matrix(cons),lower,upper),options={'time_limit':50});out['jointStatus']=res.message
if res.x is not None:
 w=np.rint(res.x[:n]*1e8).astype('int64');peaks=np.where(res.x[n:2*n]>.5)[0].tolist();ok=min(w)>=0 and all(len(pp:=[i for i in peaks if i in g])==1 and all(w[j]<=w[j+1] if j<pp[0] else w[j]>=w[j+1] for j in g[:-1]) for g in groups);margin=min(sum(int(a)*int(b) for a,b in zip(row,w)) for row in M)
 if ok and margin>0:out.update(verifiedMargin=margin,weights={str(k):int(v) for k,v in zip(K,w) if v},peaks=[K[i] for i in peaks]);
print(out['jointStatus'],out.get('verifiedMargin'));(D/'ramsey_37_joint_peak_clauses.json').write_text(json.dumps(out,indent=2)+'\n')
