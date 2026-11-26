"""Relax exact copy anchors at fixed endpoint order 17. Enumerate every core in the predecessor-only 12-layer and the 13-layer; no use of order-17 endpoints to select cores. Exact anchors in specified slots, arbitrary independent rows elsewhere."""
import json,itertools,collections
from pysat.solvers import Solver
from ramsey_retention_slice import CAT,D,decode,check
P=D.parent
def run(a):
 n=len(a);d=16-n;I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not v&s])
 assert max(t.bit_count() for t in I)==4
 var=lambda j,i:1+n*j+i;cs=[[-var(j,i),-var(j,h)] for j in range(d) for i,h in itertools.combinations(range(n),2) if a[i]>>h&1]
 for q in I:
  for slots in itertools.combinations(range(d),6-q.bit_count()):cs.append([var(j,i) for j in slots for i in range(n) if q>>i&1])
 best=None;calls={}
 with Solver(name='g4',bootstrap_with=cs) as sl:
  for size in ([1,0] if n==13 else range(d,-1,-1)):
   tried=0;wins=[]
   for subset in itertools.combinations(range(n),size):
    tried+=1
    if sl.solve(assumptions=[var(j,i)*(1 if a[v]>>i&1 else -1) for j,v in enumerate(subset) for i in range(n)]):
     pos=set(sl.get_model());w=[sum(1<<i for i in range(n) if var(j,i) in pos) for j in range(d)];g=list(a)+[0]*(d+1)
     for j,t in enumerate(w,n):
      g[j]=t|1<<16;g[16]|=1<<j
      for i in range(n):g[i]|=((t>>i)&1)<<j
     assert check(g,(1<<17)-1,3,6);wins.append(subset)
     if best is None:best=dict(anchors=subset,supports=w)
   calls[size]=[tried,len(wins)]
   if wins:break
 fours=[q for q in I if q.bit_count()==4];return dict(core=a,d=d,calls=calls,best=best,fours=len(fours),max_four_hits=max(sum(bool(s&q) for q in fours) for s in I))
layers=[decode(s) for s in (CAT/'r35_13.g6').read_text().splitlines()]+[list(t) for t in sorted({tuple(r['core']) for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==12})];rs=[run(a) for a in layers];print(rs[0]);print('12',collections.Counter(len(r['best']['anchors']) if r['best'] else -1 for r in rs[1:]));(P/'ramsey_anchor_release36.json').write_text(json.dumps(rs)+'\n')
