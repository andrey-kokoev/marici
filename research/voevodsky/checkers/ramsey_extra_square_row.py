"""Try an arbitrary extra shared-root support after four oriented square rows. SAT constraints: triangle-free support hitting the core part of every already saturated blue clique. Enumerated examples only (not a full catalogue)."""
import json,itertools
from pysat.solvers import Solver
from ramsey_retention_slice import D,decode,check
P=D.parent
r=json.loads((P/'ramsey_square_compose.json').read_text());out=[]
for ks,data in r.items():
 k=int(ks);a=decode(data['examples']['0']);n=len(a);f=(1<<n)-1;I=[0]
 for j,v in enumerate(a):I.extend([s|1<<j for s in I if not s&v])
 es=[(u,v) for u in range(n) for v in range(u) if a[u]>>v&1];cnf=[[-u-1,-v-1] for u,v in es];runs=[]
 for (u,w),(v,x) in itertools.combinations(es,2):
  b=a[u]|a[w];d=a[v]|a[x];U=f&~(b|d)
  if b&d or any(q.bit_count()==k-3 and not q&~U for q in I):continue
  for c in ((u,v,w,x),(u,x,w,v)):
   rows=[a[c[(j+2)%4]]|1<<c[(j+1)%4] for j in range(4)];tight=[q for q in I if q.bit_count()+sum(not q&s for s in rows)==k];
   with Solver(name='g4',bootstrap_with=cnf) as sl:
    for q in tight:sl.add_clause([j+1 for j in range(n) if q>>j&1]);
    ok=sl.solve();s=sum(1<<(v-1) for v in sl.get_model() if 0<v<=n) if ok else None
   if ok:
    g=list(a)+[0]*6
    for j,t in enumerate(rows+[s],n):
     g[j]=t|1<<(n+5);g[-1]|=1<<j
     for h in range(n):g[h]|=((t>>h)&1)<<j
    assert check(g,(1<<len(g))-1,3,k+1)
   runs.append(dict(corners=c,tight=len(tight),extra=s))
 out.append(dict(k=k,graph=data['examples']['0'],runs=runs));print(k,len(runs),sum(t['extra'] is not None for t in runs))
(P/'ramsey_extra_square_row.json').write_text(json.dumps(out)+'\n')
