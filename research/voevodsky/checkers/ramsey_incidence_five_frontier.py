"""Exact five-region incompatibilities on best two-mask repair. Probe all pairs of regions, maximize #jointly feasible five-regions with exact degree/four tests, and replay best completion. Save unavoidable pairs, optimal rejected masks and surviving six-vertex obstruction sets."""
import json,itertools,collections
from ramsey_incidence_mismatch import base,P
from pysat.card import CardEnc
from pysat.solvers import Solver
rs=json.loads((P/'ramsey_incidence_release_pairs35.json').read_text())['rows'];z=next(z for z in rs if z.get('bad')==[]);m=z['m'];E,cs=base(m);top=max(E.values());
for i,s in enumerate(m):
 x=CardEnc.equals([v for e,v in E.items() if i in e],8-s.bit_count(),top_id=top);top=max(top,x.nv);cs+=x.clauses
act={};
for labs in itertools.combinations(range(8),5):
 t=sum(1<<l for l in labs);top+=1;act[t]=top;vs=[i for i,s in enumerate(m) if not s&~t];cs.extend([[-top]+[E[e] for e in itertools.combinations(q,2) if e in E] for q in itertools.combinations(vs,6)])
with Solver(name='cadical195',bootstrap_with=cs) as sl:
 pairs=[(t,u) for t,u in itertools.combinations(act,2) if not sl.solve(assumptions=[act[t],act[u]])]
print('pairs',len(pairs),flush=True)
for k in range(57):
 b=CardEnc.atmost([-v for v in act.values()],k,top_id=top)
 with Solver(name='cadical195',bootstrap_with=cs+b.clauses) as sl:
  if sl.solve():model=set(sl.get_model());break
edges=[e for e,v in E.items() if v in model];a=[sum(1<<j for j in range(26) if tuple(sorted((i,j))) in edges) for i in range(26)];assert all(v.bit_count()==8-m[i].bit_count() for i,v in enumerate(a)) and all(not a[i]&a[j] and not m[i]&m[j] for i,j in edges);I=[(0,0)]
for i,v in enumerate(a):I.extend([(q|1<<i,u|m[i]) for q,u in I if not q&v]);
bad=[(q,u) for q,u in I if q.bit_count()==6 and u.bit_count()<=5];assert not any(q.bit_count()>u.bit_count() and u.bit_count()<=4 for q,u in I);assert len(set(t for q,t in bad))==k;print(k,len(bad),sorted(set(t for q,t in bad)),pairs[:3]);(P/'ramsey_incidence_five_frontier.json').write_text(json.dumps(dict(m=m,pair_conflicts=pairs,min_bad_regions=k,edges=edges,bad_sixes=bad))+'\n')
