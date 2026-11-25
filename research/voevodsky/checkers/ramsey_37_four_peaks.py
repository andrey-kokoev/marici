"""Hold single-peak locations from the verified 13-branch table; leave the peak on every other branch free. Bisect ranges; prune ONLY with an exact integer dual against all intervals intersecting the allowed peak ranges. Otherwise find an integer profile or report unresolved."""
import json,gzip,itertools,sys,math
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
D=root/'voevodsky/results';G={245,973,1813};R=[];names=[]
for rec,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 if rec not in G:continue
 F=independent_fives(graph6(line));ds=[[j for j,b in enumerate(F) if not a&b] for a in F];k=[(len(d),sum(len(ds[j]) for j in d)) for d in ds];c=Counter(k);seen=set()
 for t,d in zip(F,ds):
  hit=Counter(k[h] for h in d);r=tuple(sorted((v,6*hit[v]-n) for v,n in c.items()));
  if r not in seen:seen.add(r);R.append(dict(r));names.append((rec,t))
K=sorted(set.union(*(set(r) for r in R)));M=np.array([[r.get(k,0) for k in K] for r in R]);groups=[list(g) for _,g in itertools.groupby(range(len(K)),lambda i:K[i][0])];base=json.loads((D/'ramsey_37_local_peak_barriers.json').read_text())[1]['alternative']['weights'];near='--near15' in sys.argv
if near:base=max(json.loads((D/'ramsey_37_partial_peak_coverage.json').read_text())['witnesses'],key=lambda x:len(x['peaks']))['weights']
w0=[base.get(str(k),0) for k in K];bounds=[];free=[]
for g in groups:
 y=[w0[i] for i in g];j=y.index(max(y));ok=y[:j+1]==sorted(y[:j+1]) and y[j:]==sorted(y[j:],reverse=True);bounds.append((g[j],g[j]) if ok else (g[0],g[-1]));
 if not ok:free.append(len(bounds)-1)
assert len(free)==(2 if near else 4)
m,n=M.shape;pre=np.column_stack([np.zeros(m,dtype=int),np.cumsum(M,axis=1)]);certs=[];unknown=[];remaining=[bounds];result=None;tested=0
if any(k in sys.argv for k in ('--release','--pair-release','--alternative-pair','--one-more','--two-bands')):
 records=[];target=next(i for i,g in enumerate(groups) if K[g[0]][0]==19)
 def attempt(release,relocate):
  unrestricted=set(free)-{target};bd0=bounds.copy();axes=[target]
  for i in (release if isinstance(release,tuple) else (release,)):
   g=groups[i];bd0[i]=(g[0],g[-1])
   if relocate:axes.append(i);unrestricted.discard(i)
   else:unrestricted.add(i)
  stack=[bd0];proof=[];unknown=0;tested=0
  while stack:
   bd=stack.pop();tested+=1;spans=[span for i,(g,(lo,hi)) in enumerate(zip(groups,bd)) for span in ([(j,j) for j in g] if i in unrestricted else [(j,k) for j in range(g[0],hi+1) for k in range(max(j,lo),g[-1]+1)])];ii,jj=np.array(spans).T;B=pre[:,jj+1]-pre[:,ii];z=linprog(np.ones(B.shape[1]),A_ub=-B,b_ub=-np.ones(m),bounds=(0,None))
   if z.success:
    coef=np.rint(z.x*10**6).astype('int64');w=[sum(int(c) for (a,b),c in zip(spans,coef) if a<=j<=b) for j in range(n)];margin=min(sum(r.get(k,0)*v for k,v in zip(K,w)) for r in R);shape={}
    for i,(g,(a,b)) in enumerate(zip(groups,bd)):
     if i in unrestricted:continue
     y=[w[j] for j in g];shape[i]=next((j for j in range(a,b+1) if y[:j-g[0]+1]==sorted(y[:j-g[0]+1]) and y[j-g[0]:]==sorted(y[j-g[0]:],reverse=True)),None)
    if min(w)>=0 and margin>0 and None not in shape.values():return dict(status='possible',tested=tested,peaks=[K[j] for j in shape.values()],margin=margin,weights={str(k):v for k,v in zip(K,w) if v})
   else:
    scales=np.maximum(1,np.abs(B).max(axis=0));lp=linprog([0]*m+[1],A_ub=np.column_stack((B.T,-scales)),b_ub=np.zeros(B.shape[1]),A_eq=[[1]*m+[0]],b_eq=[1],bounds=[(0,None)]*m+[(None,None)]);u=np.rint(lp.x[:-1]*10**11).astype('int64') if lp.success else None
    if u is not None and min(u)>=0 and max(u)>0 and m*int(max(u))*int(np.abs(B).max())<2**63 and max(u@B)<=0:proof.append(dict(ranges=[(K[bd[i][0]],K[bd[i][1]]) for i in axes],dual=[[*name,int(v)] for name,v in zip(names,u) if v]));continue
   i=max(axes,key=lambda i:bd[i][1]-bd[i][0]);a,b=bd[i];mid=(a+b)//2
   if a==b:unknown+=1;continue
   l=bd.copy();h=bd.copy();l[i]=(a,mid);h[i]=(mid+1,b);stack.extend([l,h])
  return dict(status='unresolved' if unknown else 'excluded',tested=tested,proof=proof)
 if '--two-bands' in sys.argv:
  prior=json.loads((D/'ramsey_37_near15_one_more.json').read_text())['11'];fixed=dict(prior['peaks']);orig=groups.copy();idx=next(i for i,g in enumerate(orig) if K[g[0]][0]==16);full=orig[idx];tests=[]
  for cut in sorted(range(1,len(full)),key=lambda i:abs(i-len(full)/2)):
   groups=orig[:idx]+[full[:cut],full[cut:]]+orig[idx+1:];bounds=[]
   for g in groups:
    d=K[g[0]][0];j=next((j for j in g if K[j][1]==fixed.get(d)),None);bounds.append((g[0],g[-1]) if d==16 else (j,j))
   free=[idx,idx+1];target=idx;z=attempt((idx+1,),True);tests.append(dict(cutAfter=K[full[cut-1]][1],**z));print(cut,z['status'],z['tested'],flush=True)
   if z['status']=='possible':break
  (D/'ramsey_37_two_band_exception.json').write_text(json.dumps(tests,indent=2)+'\n')
  # Construct a tighter upper bound by penalizing changes along d=16. Reweighted TV proposes profiles; only integer verification and actual peak counts are used.
  t=len(full)-1;ineq=[];rhs=[]
  for g in orig:
   d=K[g[0]][0]
   if d==16:continue
   for j in g[:-1]:
    b=1 if K[j][1]<fixed[d] else -1;v=np.zeros(n+t);v[j]=b;v[j+1]=-b;ineq.append(v);rhs.append(0)
  for a,j in enumerate(full[:-1]):
   for b in [-1,1]:
    v=np.zeros(n+t);v[j]=b;v[j+1]=-b;v[n+a]=-1;ineq.append(v);rhs.append(0)
  mat=np.vstack([np.c_[-M,np.zeros((m,t))],ineq]);rr=np.r_[-np.ones(m),rhs];rng=np.random.default_rng(16);best=None
  for it in range(120):
   if it%4==0:pen=np.exp(rng.uniform(-2,2,t))
   else:pen=1/(.01+z.x[n:]);
   z=linprog(np.r_[np.full(n,.0001),pen],A_ub=mat,b_ub=rr,bounds=(0,None));assert z.success;w=np.rint(z.x[:n]*1e6).astype('int64');margin=min(sum(row.get(k,0)*int(v) for k,v in zip(K,w)) for row in R);assert margin>0 and min(w)>=0 and all((w[j]<=w[j+1] if K[j][1]<fixed[K[g[0]][0]] else w[j]>=w[j+1]) for g in orig if g!=full for j in g[:-1]);blocks=[(u,list(js)) for u,js in itertools.groupby(full,key=lambda j:int(w[j]))];peaks=[(K[js[0]][1],K[js[-1]][1]) for i,(u,js) in enumerate(blocks) if u>(blocks[i-1][0] if i else -1) and u>(blocks[i+1][0] if i+1<len(blocks) else -1)]
   if best is None or len(peaks)<len(best['peaks']):best=dict(peaks=peaks,margin=margin,weights={str(k):int(v) for k,v in zip(K,w) if v})
   if len(peaks)<=3:break
  print('upper',best['peaks'],best['margin']);(D/'ramsey_37_band_exception_upper.json').write_text(json.dumps(best,indent=2)+'\n');sys.exit()
 if '--one-more' in sys.argv:
  assert near;one={}
  for target in free:
   d=K[groups[target][0]][0];one[d]=attempt((),True);print(d,one[d]['status'],one[d].get('peaks'),flush=True)
  (D/'ramsey_37_near15_one_more.json').write_text(json.dumps(one,indent=2)+'\n');sys.exit()
 if '--alternative-pair' in sys.argv:
  checked=[];candidates=[i for i in range(len(groups)) if i not in free];pairs=sorted(itertools.combinations(candidates,2),key=lambda pair:(not any(K[groups[i][0]][0] in (16,17) for i in pair),pair));
  for pair in pairs:
   ds=[K[groups[i][0]][0] for i in pair];z=attempt(pair,True);checked.append(dict(degrees=ds,**z));print(ds,z['status'],flush=True)
   if z['status']=='possible':break
  (D/'ramsey_37_alternative_pair_release.json').write_text(json.dumps(checked,indent=2)+'\n');sys.exit()
 if '--pair-release' in sys.argv:
  pair=tuple(i for i,g in enumerate(groups) if K[g[0]][0] in (16,17));z=attempt(pair,True);print(z['status'],z['tested'],z.get('peaks'),len(z.get('proof',[])));(D/'ramsey_37_pair_peak_release.json').write_text(json.dumps(z,indent=2)+'\n');sys.exit()
 for i,(a,b) in enumerate(bounds):
  if i in free:continue
  x=attempt(i,False);y=attempt(i,True) if x['status']=='possible' else None;records.append(dict(fixed=K[a],unrestricted=x,relocated=y));print(K[a],x['status'],y and y['status'],flush=True)
 (D/'ramsey_37_single_peak_release.json').write_text(json.dumps(records,indent=2)+'\n');sys.exit()
while remaining and tested<150:
 bd=remaining.pop();tested+=1;spans=[(i,j) for g,(lo,hi) in zip(groups,bd) for i in range(g[0],hi+1) for j in range(max(i,lo),g[-1]+1)];ii,jj=np.array(spans).T;B=pre[:,jj+1]-pre[:,ii];z=linprog(np.ones(B.shape[1]),A_ub=-B,b_ub=-np.ones(m),bounds=(0,None))
 if not z.success:
  scales=np.maximum(1,np.abs(B).max(axis=0));lp=linprog([0]*m+[1],A_ub=np.column_stack((B.T,-scales)),b_ub=np.zeros(B.shape[1]),A_eq=[[1]*m+[0]],b_eq=[1],bounds=[(0,None)]*m+[(None,None)]);u=np.rint(lp.x[:-1]*10**11).astype('int64') if lp.success else None
  if u is not None and min(u)>=0 and max(u)>0 and m*int(max(u))*int(np.abs(B).max())<2**63 and max(u@B)<=0:
   certs.append(dict(ranges=[(K[a],K[b]) for a,b in bd],dual=[[*name,int(v)] for name,v in zip(names,u) if v]));continue
 else:
  co=np.rint(z.x*10**5).astype('int64');w=[sum(int(c) for c,(a,b) in zip(co,spans) if a<=j<=b) for j in range(n)];margin=min(sum(r.get(k,0)*v for k,v in zip(K,w)) for r in R);shape=True
  for g,(a,b) in zip(groups,bd):
   y=[w[i] for i in g];shape &= any(y[:j+1]==sorted(y[:j+1]) and y[j:]==sorted(y[j:],reverse=True) for j in range(a-g[0],b-g[0]+1))
  if margin>0 and shape and min(w)>=0:result=dict(weights={str(k):v for k,v in zip(K,w) if v},margin=margin);break
 i=max(free,key=lambda i:bd[i][1]-bd[i][0]);l,h=bd[i];
 if l==h:unknown.append(bd);continue
 mid=(l+h)//2;A=bd.copy();C=bd.copy();A[i]=(l,mid);C[i]=(mid+1,h);remaining.extend([A,C])
size=lambda bd:math.prod(b-a+1 for a,b in bd);print(tested,size(bounds),len(certs),len(remaining),len(unknown),bool(result));out=dict(initial=[(K[a],K[b]) for a,b in bounds],schedules=size(bounds),tested=tested,certs=certs,remaining=sum(map(size,remaining+unknown)),verified=result);(D/('ramsey_37_near15_peaks.json' if near else 'ramsey_37_four_peaks.json')).write_text(json.dumps(out,indent=2)+'\n')
