"""Explain the winning single transfer's next obstruction. Keep all four-label demands and exact regular degrees; test five-label regions singly and collect an inclusion-minimal contradictory subset. Save a local completion, directly validate all four-label constraints."""
from ramsey_incidence_mismatch import base,P
from pysat.card import CardEnc
from pysat.solvers import Solver
import json,itertools
z=next(z for z in json.loads((P/'ramsey_incidence_transfer35.json').read_text())['records'] if z.get('sat4')=='sat_local');m=z['m'];E,cs=base(m);n=max(E.values());
for i,s in enumerate(m):
 f=CardEnc.equals([v for e,v in E.items() if i in e],8-s.bit_count(),top_id=n);cs+=f.clauses;n=max(n,f.nv)
act={}
for labs in itertools.combinations(range(8),5):
 t=sum(1<<i for i in labs);vs=[i for i,s in enumerate(m) if not s&~t];qs=list(itertools.combinations(vs,6));
 if not qs:continue
 n+=1;act[t]=n;cs.extend([[-n]+[E[e] for e in itertools.combinations(q,2) if e in E] for q in qs])
with Solver(name='cadical195',bootstrap_with=cs) as sl:
 assert sl.solve();model=set(sl.get_model());w=[e for e,v in E.items() if v in model];single=[t for t,h in act.items() if not sl.solve(assumptions=[h])];core=list(act)
 for t in act:
  if not sl.solve(assumptions=[act[u] for u in core if u!=t]):core.remove(t)
a=[sum(1<<j for j in range(26) if tuple(sorted((i,j))) in w) for i in range(26)];assert len(w)==76 and all(a[i].bit_count()==8-s.bit_count() for i,s in enumerate(m));assert all(not a[i]&a[j] and not m[i]&m[j] for i,j in w);I=[(0,0)]
for i,v in enumerate(a):I.extend([(q|1<<i,u|m[i]) for q,u in I if not q&v]);
assert all(q.bit_count()<=u.bit_count() for q,u in I if u.bit_count()<=4)
print(len(w),len(act),len(single),core);(P/'ramsey_incidence_transfer_pivots.json').write_text(json.dumps(dict(m=m,edges=w,nonempty_regions=len(act),single_bad=single,minimal_regions=core))+'\n')
