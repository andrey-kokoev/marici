"""Unimodality feasibility, with peak position free in EVERY d branch. A valley in a relaxed LP solution splits the possible peak interval into two exhaustive ranges. Floating infeasibility is NOT a certificate. Save integer weights for feasible solutions and audit integer inequalities."""
import gzip,json,sys,time,itertools
from collections import Counter
from pathlib import Path
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,vstack
import numpy as np
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
R=[];ids=[]
for j,line in enumerate(gzip.open(p/'r36_16.g6.gz','rb'),1):
 A=graph6(line)
 if sum(v.bit_count() for v in A)!=66:continue
 F=independent_fives(A);D=[[h for h,b in enumerate(F) if not a&b] for a in F];k=[(len(d),sum(len(D[h]) for h in d)) for d in D];cnt=Counter(k);seen=set()
 for d in D:
  hits=Counter(k[j] for j in d);r=tuple((k,6*hits[k]-n) for k,n in sorted(cnt.items()));
  if r not in seen:R.append(dict(r));ids.append(j);seen.add(r)
def search(sel,limit,hint=None):
 start=time.monotonic();rr=[r for r,i in zip(R,ids) if i in sel];K=sorted(set.union(*(set(r) for r in rr)));M=np.array([[r.get(k,0) for k in K] for r in rr]);sp=csr_matrix(-M);groups=[list(g) for _,g in itertools.groupby(range(len(K)),lambda i:K[i][0])];bounds=[(g[0],g[-1]) for g in groups];calls=0;unknown=0;pruned=0;stack=[bounds];
 while stack and time.monotonic()-start<limit:
  bd=stack.pop();sg=[(j,i) for g,(l,h) in zip(groups,bd) for j in g[:-1] for i in ([1] if j<l else [-1] if j>=h else [])];n=len(sg);rows=[];cols=[];ds=[]
  for t,(j,b) in enumerate(sg):rows.extend((t,t));cols.extend((j,j+1));ds.extend((b,-b))
  a=vstack((sp,csr_matrix((ds,(rows,cols)),shape=(n,len(K)))));z=linprog(np.ones(len(K)),A_ub=a,b_ub=np.r_[-np.ones(len(M)),np.zeros(n)],bounds=(0,None));calls+=1
  if not z.success:
   if z.status==2:pruned+=1
   else:unknown+=1
   continue
  w=np.rint(z.x*1e5).astype('int64');vs=[]
  for h,(g,(l,r)) in enumerate(zip(groups,bd)):
   for j in range(l,r):
    drop=min(max(w[g[0]:j+1]),max(w[j+1:g[-1]+1]))-min(w[j],w[j+1]);
    if drop>0:vs.append((drop,h,j))
  if not vs:
   margin=min(sum(int(w[i])*int(row[i]) for i in np.flatnonzero(row)) for row in M)
   if margin<=0 or min(w)<0 or not all(all(v<=u for v,u in zip(y[:q],y[1:q+1])) and all(v>=u for v,u in zip(y[q:],y[q+1:])) for g in groups for y in [w[g]] for q in [np.argmax(y)]):unknown+=1;continue
   return dict(status='verified',calls=calls,margin=margin,weights={str(k):int(v) for k,v in zip(K,w) if v})
  _,h,j=max(vs);l,r=bd[h];b1=bd.copy();b2=bd.copy();b1[h]=(l,j);b2[h]=(j+1,r);stack.extend([b2,b1] if hint and hint.get(K[j][0],float('inf'))<=K[j][1] else [b1,b2])
 return dict(status='incomplete' if stack or unknown else 'numeric_exclusion',calls=calls,pruned=pruned,pending=len(stack),unknown=unknown)
G=sorted(set(ids));out=[]
pairs='--pairs' in sys.argv
jobs=[(list(ab),0.8) for ab in itertools.combinations(G,2)] if pairs else [([g],1) for g in G]+[(G,20)]
retry='--retry' in sys.argv;hints={}
if retry:
 import ast
 assert pairs
 previous=json.loads((root/'voevodsky/results/ramsey_37_unimodal_pairs.json').read_text());out=[z for z in previous if z['status']=='verified'];jobs=[(z['records'],30 if '--long' in sys.argv else 5) for z in previous if z['status']!='verified'];singles=json.loads((root/'voevodsky/results/ramsey_37_unimodal_search.json').read_text());rank={}
 for z in singles:
  if z['status']!='verified':continue
  g,=z['records'];rank[g]=z['calls'];w={ast.literal_eval(k):v for k,v in z['weights'].items()};hints[g]={d:max((v,s) for (i,s),v in w.items() if i==d)[1] for d,_ in w}
triple=next((list(map(int,arg.split('=')[1].split(','))) for arg in sys.argv if arg.startswith('--triple=')),None)
if triple:
 assert len(set(triple))==3 and set(triple)<=set(G) and not retry;jobs=[(triple,30)]
for ss,t in jobs:
 z=search(ss,t,hints.get((min if '--long' in sys.argv else max)(ss,key=rank.get)) if retry else None);out.append(dict(records=ss,**z));print(len(ss),ss[0],z['status'],z['calls'],flush=True)
(root/(('voevodsky/results/ramsey_37_unimodal_triple_'+'_'.join(map(str,triple))+'.json') if triple else 'voevodsky/results/ramsey_37_unimodal_pairs.json' if pairs else 'voevodsky/results/ramsey_37_unimodal_search.json')).write_text(json.dumps(out,indent=2)+'\n')
