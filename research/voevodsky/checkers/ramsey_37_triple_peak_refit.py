"""Fix branch peaks before refitting all weights on the 245/973/1813 triple. If the three inherited peak schedules fail, try their branchwise combinations and coordinate descent. Only integer-verified success establishes feasibility."""
import ast,itertools,json,sys,gzip,random
from pathlib import Path
from collections import Counter
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack,vstack,eye
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
D=root/'voevodsky/results';G={245,973,1813};addresses={};rows=[];rowIds=[]
for j,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 if j not in G:continue
 A=graph6(line);F=independent_fives(A);ds=[[h for h,b in enumerate(F) if not a&b] for a in F];k=[(len(d),sum(len(ds[h]) for h in d)) for d in ds];cnt=Counter(k);addresses[j]=set(k);seen=set()
 for mask,d in zip(F,ds):
  hit=Counter(k[h] for h in d);v=tuple(sorted((k,6*hit[k]-n) for k,n in cnt.items()));
  if v not in seen:rows.append(dict(v));rowIds.append((j,mask));seen.add(v)
K=sorted(set.union(*addresses.values()));M=np.array([[r.get(k,0) for k in K] for r in rows]);groups=[list(g) for _,g in itertools.groupby(range(len(K)),lambda j:K[j][0])];n=len(K);m=len(M);rng=random.Random(245);memory={};result={};schedules=[];record=[]
for z in json.loads((D/'ramsey_37_unimodal_pairs.json').read_text()):
 if not set(z['records'])<=G:continue
 w={ast.literal_eval(k):v for k,v in z['weights'].items()};old=set.union(*(addresses[i] for i in z['records']));schedule=[]
 for g in groups:
  v=[j for j in g if K[j] in old];peaks=[j for j in v if w.get(K[j],0)==max(w.get(K[i],0) for i in v)];schedule.append(peaks[len(peaks)//2] if peaks else g[len(g)//2]);
 schedules.append(schedule);record.append(z['records'])
if '--localize' in sys.argv:
 def constraints(peaks,active):
  vs=[(j,1 if j<peaks[i] else -1) for i in active for j in groups[i][:-1]];u=np.zeros((len(vs),n),dtype=int)
  for t,(j,b) in enumerate(vs):u[t,j]=b;u[t,j+1]=-b
  return u
 def test_fixed(peaks,active):
  shape=constraints(peaks,active);return linprog(np.ones(n),A_ub=np.vstack([-M,shape]),b_ub=np.r_[-np.ones(m),np.zeros(len(shape))],bounds=(0,None))
 cores=[]
 for peaks in schedules:
  active=list(range(len(groups)))
  for i in sorted(active,key=lambda h:-len(groups[h])):
   trial=[j for j in active if j!=i];z=test_fixed(peaks,trial)
   if z.status==2:active=trial
  # Unrestricted branches use singleton indicators. Restricted branches use all intervals containing the specified peak.
  B=np.column_stack([col for i,(g,c) in enumerate(zip(groups,peaks)) for col in ([M[:,j] for j in g] if i not in active else [M[:,l:h+1].sum(axis=1) for l in range(g[0],c+1) for h in range(c,g[-1]+1)])]);scale=np.maximum(1,np.abs(B).max(axis=0));lp=linprog([0]*m+[1],A_ub=np.column_stack((B.T,-scale)),b_ub=np.zeros(B.shape[1]),A_eq=[[1]*m+[0]],b_eq=[1],bounds=[(0,None)]*m+[(None,None)]);assert lp.success;u=np.rint(lp.x[:-1]*10**9).astype('int64');upper=int(max(u@B));assert upper<=0 and max(u)>0 and min(u)>=0
  # Test whether those same branches admit any jointly valid peak schedule when the others remain unrestricted.
  found=None;tested=0
  candidates=[tuple(groups[i][0] for i in active),tuple(groups[i][-1] for i in active)]+[tuple(rng.choice(groups[i]) for i in active) for _ in range(400)]
  for choices in candidates:
   pp=peaks.copy();tested+=1
   for i,j in zip(active,choices):pp[i]=j
   z=test_fixed(pp,active)
   if not z.success:continue
   w=np.rint(z.x*1e6).astype('int64');margin=int(min(M@w));assert max(constraints(pp,active)@w)<=0 and margin>0 and min(w)>=0;found=dict(peaks=[K[pp[i]] for i in active],margin=margin,weights={str(k):int(v) for k,v in zip(K,w) if v});break
  cores.append(dict(fixed=[K[peaks[i]] for i in active],upper=upper,multipliers=[[*rowIds[i],int(v)] for i,v in enumerate(u) if v],alternative=found,tested=tested));print(cores[-1]['fixed'],tested,found['peaks'] if found else None,flush=True)
 (D/'ramsey_37_local_peak_barriers.json').write_text(json.dumps(cores,indent=2)+'\n');sys.exit()
base=hstack([-csr_matrix(M),-eye(m)]);cost=np.r_[np.zeros(n),np.ones(m)];rhs=np.r_[-np.ones(m),np.zeros(n-len(groups))]
def test(peaks):
 key=tuple(peaks)
 if key in memory:return memory[key]
 sg=[(j,1 if j<h else -1) for g,h in zip(groups,peaks) for j in g[:-1]];rr=np.repeat(np.arange(len(sg)),2);cc=[i for j,_ in sg for i in (j,j+1)];val=[v for _,b in sg for v in (b,-b)];sh=csr_matrix((val,(rr,cc)),shape=(len(sg),n+m));z=linprog(cost,A_ub=vstack([base,sh]),b_ub=rhs,bounds=(0,None));loss=z.fun if z.success else float('inf');memory[key]=loss
 if loss<1e-7:
  w=np.rint(z.x[:n]*1e6).astype('int64');margin=min(sum(int(w[j])*int(row[j]) for j in np.flatnonzero(row)) for row in M);assert min(w)>=0 and margin>0 and all(int(w[j]-w[j+1])*b<=0 for j,b in sg);result.update(margin=margin,peaks=[K[j] for j in peaks],weights={str(k):int(v) for k,v in zip(K,w) if v});return 0
 return loss
fixedProof=[]
for peaks in schedules:
 B=np.column_stack([M[:,l:h+1].sum(axis=1) for g,c in zip(groups,peaks) for l in range(g[0],c+1) for h in range(c,g[-1]+1)]);scale=np.maximum(1,np.abs(B).max(axis=0));lp=linprog([0]*m+[1],A_ub=np.column_stack((B.T,-scale)),b_ub=np.zeros(B.shape[1]),A_eq=[[1]*m+[0]],b_eq=[1],bounds=[(0,None)]*m+[(None,None)]);assert lp.success;u=np.rint(lp.x[:-1]*10**9).astype('int64');assert min(u)>=0 and max(u)>0 and max(u@B)<=0;fixedProof.append(dict(peaks=[K[i] for i in peaks],upper=int(max(u@B)),multipliers=[[*rowIds[i],int(v)] for i,v in enumerate(u) if v]))
initial=[test(x) for x in schedules];print('initial',initial,flush=True);order=list(range(len(groups)));r=0
while not result and r<(0 if '--fixed-only' in sys.argv else 10):
 peaks=list(min(schedules,key=test)) if not r else [rng.choice([s[i] for s in schedules]) for i in order];r+=1
 for epoch in range(4):
  before=test(peaks);scan=order.copy();rng.shuffle(scan)
  for i in scan:
   cs=list(dict.fromkeys([peaks[i]]+[s[i] for s in schedules]+groups[i][::max(1,len(groups[i])//6)]));rng.shuffle(cs);v=min(cs,key=lambda x:test(peaks[:i]+[x]+peaks[i+1:]));peaks[i]=v
   if result:break
  if result or test(peaks)>=before-1e-7:break
print('tested',len(memory),'verified',bool(result),'best slack',min(memory.values()));(D/'ramsey_37_triple_peak_refit.json').write_text(json.dumps(dict(records=sorted(G),initial=list(zip(record,initial)),tested=len(memory),fixedProof=fixedProof,bestSearchSlack=min(memory.values()),**result),indent=2)+'\n')
