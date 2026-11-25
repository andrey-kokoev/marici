"""Cover every k-branch subset by full attachment-feasible weights, checking unimodality only where required. Harvest all additional single-peaked branches of each exact integer solution; no incompatibility inference from numerical pruning."""
import gzip,itertools,json,sys,time,math
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
D=root/'voevodsky/results';G={245,973,1813};R=set();keys=set();start=time.monotonic()
for rec,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 if rec not in G:continue
 F=independent_fives(graph6(line));ds=[[j for j,b in enumerate(F) if not a&b] for a in F];k=[(len(d),sum(len(ds[h]) for h in d)) for d in ds];cnt=Counter(k);keys.update(cnt)
 for v in ds:
  hit=Counter(k[h] for h in v);R.add(tuple(sorted((a,6*hit[a]-n) for a,n in cnt.items())))
K=sorted(keys);n=len(K);M=np.array([[dict(r).get(k,0) for k in K] for r in R]);# small triple only
branches={d:list(g) for d,g in itertools.groupby(range(n),lambda i:K[i][0])};B=sorted(branches);witnesses=[]
def solve(required):
 bd={d:(branches[d][0],branches[d][-1]) for d in required};stack=[bd];vis=0
 while stack and vis<1000 and time.monotonic()-start<95:
  b=stack.pop();vis+=1;constraints=[]
  for d,(a,h) in b.items():
   for j in branches[d][:-1]:
    if j<a or j>=h:
     v=np.zeros(n);v[j]=1 if j<a else -1;v[j+1]=-v[j];constraints.append(v)
  z=linprog(np.ones(n),A_ub=np.vstack([-M,*constraints]),b_ub=np.r_[-np.ones(len(M)),np.zeros(len(constraints))],bounds=(0,None));
  if not z.success:continue
  w=np.rint(z.x*1e5).astype('int64');good={};valleys=[]
  for d,g in branches.items():
   y=w[g];q=int(np.argmax(y));
   if all(np.diff(y[:q+1])>=0) and all(np.diff(y[q:])<=0):good[d]=K[g[q]][1]
   elif d in b:
    l,h=b[d];valleys.extend((min(max(w[g[0]:j+1]),max(w[j+1:g[-1]+1]))-min(w[j],w[j+1]),d,j) for j in range(l,h))
  if set(required)<=good.keys():
   margin=min(sum(int(x)*int(v) for x,v in zip(row,w)) for row in M)
   if margin>0 and min(w)>=0:return dict(requested=list(required),peaks=good,margin=margin,weights={str(k):int(v) for k,v in zip(K,w) if v})
  if valleys:
   _,d,j=max(valleys);l,h=b[d];a=b.copy();c=b.copy();a[d]=(l,j);c[d]=(j+1,h);stack.extend([a,c])
 return None
case=(16,17,19,24);witnesses.append(solve(case));assert witnesses[0];tested={case};summary={}
if '--resume' in sys.argv:
 prev=json.loads((D/'ramsey_37_partial_peak_coverage.json').read_text());witnesses=prev['witnesses'];
 for x in witnesses:x['peaks']={int(d):v for d,v in x['peaks'].items()}
 tested={tuple(x['requested']) for x in witnesses}
# Reuse other verified triple tables only after independent checks on this triple.
for x in [v['alternative'] for v in json.loads((D/'ramsey_37_local_peak_barriers.json').read_text())]+[v['unrestricted'] for v in json.loads((D/'ramsey_37_single_peak_release.json').read_text()) if v['unrestricted']['status']=='possible']:
 w=[x['weights'].get(str(k),0) for k in K];margin=min(sum(int(a)*b for a,b in zip(row,w)) for row in M);assert margin>0 and min(w)>=0;good={}
 for d,g in branches.items():
  y=[w[i] for i in g];q=y.index(max(y));
  if y[:q+1]==sorted(y[:q+1]) and y[q:]==sorted(y[q:],reverse=True):good[d]=K[g[q]][1]
 if all(v['peaks']!=good for v in witnesses):witnesses.append(dict(requested=[],peaks=good,margin=margin,weights=x['weights']))
for k in (4,5,6):
 subs=set(itertools.combinations(B,k));bad=subs.copy()
 for x in witnesses:bad.difference_update(itertools.combinations(sorted(x['peaks']),k))
 while time.monotonic()-start<90:
  todo=min(bad-tested,default=None)
  if todo is None:break
  tested.add(todo);x=solve(todo)
  if x:
   witnesses.append(x);bad.difference_update(itertools.combinations(sorted(x['peaks']),k))
 summary[k]=dict(total=len(subs),uncovered=len(bad));print(k,summary[k],len(witnesses),flush=True)
 if bad:break
print('first',witnesses[0]['peaks']);(D/'ramsey_37_partial_peak_coverage.json').write_text(json.dumps(dict(records=sorted(G),summary=summary,witnesses=witnesses),indent=2)+'\n')
