"""Can a single four-label region rule out an incidence pattern without degree assumptions? Also test all such regions simultaneously on one shared triangle-free graph. No solver budgets for these small clauses."""
from ramsey_incidence_first35 import P
import json,itertools,collections
from pysat.solvers import Solver
R=json.loads((P/'ramsey_incidence_orient35.json').read_text());out=[]
for si,z in enumerate(R):
 for jz,v in enumerate(z['surv']):
  m=v['m'];edges={(i,j):1+i*26+j for i,j in itertools.combinations(range(26),2) if not m[i]&m[j]};tri=[[-edges[i,j],-edges[i,k],-edges[j,k]] for i,j,k in itertools.combinations(range(26),3) if (i,j) in edges and (j,k) in edges and (i,k) in edges];full=[];failed=[]
  for labs in itertools.combinations(range(8),4):
   t=sum(1<<b for b in labs);V=[i for i,s in enumerate(m) if not s&~t];cs=[]
   for u in range(256):
    if u&~t:continue
    for q in itertools.combinations([i for i in V if not m[i]&~u],u.bit_count()+1):cs.append([edges[e] for e in itertools.combinations(q,2) if e in edges]);
   with Solver(name='g4',bootstrap_with=tri+cs) as sl:
    if not sl.solve():failed.append(t)
   full+=cs
  with Solver(name='g4',bootstrap_with=tri+full) as sl:whole=sl.solve()
  out.append(dict(skeleton=si,j=jz,bad_local=failed,triangle_plus_all_sat=whole))
print(collections.Counter((bool(x['bad_local']),x['triangle_plus_all_sat']) for x in out));(P/'ramsey_incidence_pockets.json').write_text(json.dumps(out)+'\n')
