"""Generate order-11 (3,5) cores by canonical one-vertex augmentation. Exclude the original 16 before testing. Record first counterexample if present; exhaustive otherwise."""
import json,time,itertools,igraph as ig
from pathlib import Path
from pysat.solvers import Solver
from ramsey_retention_slice import has,check
P=Path(__file__).resolve().parents[1]/'results';src=json.loads((P/'ramsey_test_coincidence.json').read_text())['rows'];parents=json.loads((P/'ramsey_core_capacity_36.json').read_text());
def key(a):
 n=len(a);G=ig.Graph(n,[(i,j) for i,j in itertools.combinations(range(n),2) if a[i]>>j&1]);return tuple(sorted(tuple(sorted(e)) for e in G.permute_vertices(G.canonical_permutation()).get_edgelist()))
known=set()
for r in src:
 t=r['vertices'];g=parents[r['parent']]['core'];known.add(key([sum(1<<j for j,y in enumerate(t) if g[x]>>y&1) for x in t]))
assert len(known)==16;layer=[[]];counts=[]
for n in range(11):
 nxt={};p=(1<<n)-1
 for a in layer:
  b=[~v for v in a]
  for s in range(p+1):
   if has(a,s,2) or has(b,p^s,4):continue
   h=[v|((s>>j&1)<<n) for j,v in enumerate(a)]+[s];nxt.setdefault(key(h),h)
 layer=list(nxt.values());counts.append(len(layer));print(n+1,len(layer),flush=True)
assert known<=set(nxt);rows=[]
for kt,g in nxt.items():
 if kt in known:continue
 cs={k:[] for k in range(5)};v=lambda j,i:1+11*j+i;cs[0]=[[-v(j,i),-v(j,h)] for j in range(5) for i,h in itertools.combinations(range(11),2) if g[i]>>h&1]
 for t in range(1,2048):
  if has(g,t,2):continue
  k=t.bit_count();cs[k].extend([[v(j,i) for i in range(11) if t>>i&1 for j in js] for js in itertools.combinations(range(5),6-k)])
 row={'g':g}
 for name in ('34','1234'):
  start=time.perf_counter();c=cs[0]+sum((cs[int(k)] for k in name),[])
  with Solver(name='g4',bootstrap_with=c,with_proof=True) as sl:
   ok=sl.solve();row[name]=[ok,time.perf_counter()-start];
   if name=='34' and ok:row['supports']=[sum(1<<i for i in range(11) if v(j,i) in set(sl.get_model())) for j in range(5)]
   if name=='1234' and not ok and row['34'][0]:row['proof']=sl.get_proof()
 rows.append(row)
 # Do not stop on a counterexample: measure the error rate on the full held-out census.
out=dict(counts=counts,excluded=len(known),tested=len(rows),counterexample=any(r['34'][0]!=r['1234'][0] for r in rows),rows=rows);print(out['tested'],out['counterexample']);(P/'ramsey_distill_unseen.json').write_text(json.dumps(out)+'\n')
