"""Independent selector-SAT replay of the 112 surviving marked seams. Each of four panels chooses an allowed attachment, giving one prediction for 32 shared edge bits. Each of the 64 actual edges must agree in its two predictions. Identify single-edge switches, then check disjoint projections on each 4x4 block, before the full SAT test. Persist exact partial verdicts rather than infeasible witness claims."""
from ramsey_retention_slice import D
from pysat.solvers import Solver
import itertools,json,collections
P=D.parent;R=json.loads((P/'ramsey_k33_22_seam.json').read_text());out=[]
for z in R['locally_supported']:
 ds=z['domains'];g=z['groups'];cs=[];top=64;allow=collections.defaultdict(dict);blocks=collections.defaultdict(dict)
 for a,dom in enumerate(ds):
  ids=[];bits={};bm={}
  for row in dom:
   top+=1;ids.append(top);m={}
   for b in (range(2,4) if a<2 else range(2)):
    bl=0
    for i,s in enumerate(row):
     for j,u in enumerate(g[b]):
      l,k=(4*a+i,4*(b-2)+j) if a<2 else (4*b+j,4*(a-2)+i);v=1+8*l+k;c=(s>>u)&1;cs.append([-top,v if c else -v]);bits.setdefault(v,set()).add(c);bl|=c<<(4*(l%4)+k%4)
    bm.setdefault(tuple(sorted((a,b))),set()).add(bl)
  cs.append(ids)
  for k,v in bits.items():allow[k][a]=v
  for k,v in bm.items():blocks[k][a]=v
 assert len(allow)==64 and all(len(v)==2 for v in allow.values());cl=[k for k,v in allow.items() if not set.intersection(*v.values())];bc=[k for k,v in blocks.items() if not set.intersection(*v.values())];
 with Solver(name='cadical195',bootstrap_with=cs) as sl:ok=sl.solve();assert not ok
 out.append(dict(candidate=z['candidate'],single_conflicts=cl,block_conflicts=bc,ok=ok))
h=collections.Counter('edge' if z['single_conflicts'] else 'block' if z['block_conflicts'] else 'joint' for z in out);print(h);(P/'ramsey_k33_22_verified.json').write_text(json.dumps(dict(classification=h,checks=out))+'\n')
