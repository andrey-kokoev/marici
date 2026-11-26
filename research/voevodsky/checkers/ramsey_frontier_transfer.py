"""Frozen frontier rule from order 11 degree 5. Independent canonical augmentation; test adjacent orders and degree 4 with unchanged scores. Time selection separately from SAT."""
import json,time,itertools,collections,igraph as ig
from pysat.solvers import Solver
from ramsey_retention_slice import D,has
P=D.parent;layer=[[]];out=[]
for m in range(12):
 nxt={};n=m+1;p=(1<<m)-1
 for a in layer:
  b=[~v for v in a]
  for s in range(p+1):
   if has(a,s,2) or has(b,p^s,4):continue
   h=[v|((s>>j&1)<<m) for j,v in enumerate(a)]+[s];G=ig.Graph(n,[(i,j) for i,j in itertools.combinations(range(n),2) if h[i]>>j&1]);key=tuple(sorted(tuple(sorted(e)) for e in G.permute_vertices(G.canonical_permutation()).get_edgelist()));nxt.setdefault(key,h)
 layer=list(nxt.values())
 if n<10:continue
 for a in layer:
  Q=[q for q in range(1,1<<n) if not has(a,q,2)];start=time.perf_counter();S=[s for s in Q if not any(s!=u and s&u==s for u in Q)];T=[q for q in Q if q.bit_count()==4];sel=[]
  for k in [1,2]:
   scores={q:(sum(bool(s&q) for s in S),sum(q&t==q for t in T)) for q in Q if q.bit_count()==k};sel.extend(q for q,(h,f) in scores.items() if not any(i<=h and j<=f and (i,j)!=(h,f) for i,j in scores.values()))
  prep=time.perf_counter()-start
  for d in ([4] if n==11 else [4,5]):
   v=lambda j,i:1+n*j+i;base=[[-v(j,i),-v(j,h)] for i,h in itertools.combinations(range(n),2) if a[i]>>h&1 for j in range(d)];rec=dict(n=n,d=d,core=a,prep=prep)
   for name in ['34','frontier','full']:
    start=time.perf_counter();cs=base.copy()
    for q in Q:
     if q.bit_count()<3 and name!='full' and not(name=='frontier' and q in sel):continue
     cs.extend([[v(j,i) for i in range(n) if q>>i&1 for j in J] for J in itertools.combinations(range(d),6-q.bit_count())]);
    with Solver(name='g4',bootstrap_with=cs) as sl:rec[name]=sl.solve()
    rec[name+'_seconds']=time.perf_counter()-start
   assert rec['34']>=rec['frontier']>=rec['full'];out.append(rec)
 print(n,len(layer),flush=True)
for key in sorted({(r['n'],r['d']) for r in out}):
 z=[r for r in out if (r['n'],r['d'])==key];print(key,len(z),[sum(r[s] for r in z) for s in ('34','frontier','full')],round(sum(r['prep']+r['frontier_seconds'] for r in z),2),round(sum(r['full_seconds'] for r in z),2))
(P/'ramsey_frontier_transfer.json').write_text(json.dumps(out)+'\n')
