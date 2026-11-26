"""Forget one entire support of the cube (label 7), retain the other seven. No constraints on unknown row except size, disjoint-red and endpoint conditions. Core graph completely free. Relaxed SAT includes the forbidden blue-clique subsets with unions of at most 4/5/6 known labels; enumeration blocks only mask choices, never just the core. Exhaustion at relaxed level is an upper bound on full completions. Cubic choices certified by relabeling equal residual masks."""
import itertools,json,collections,sys
from pysat.card import CardEnc,ITotalizer
from pysat.solvers import Solver
from ramsey_incidence_first35 import P
# Build cube independently: nonempty proper coordinate subcubes in {0,1}^3.
m=[sum(1<<i for i in range(8) if i&mask==v) for mask in range(1,8) for v in range(8) if not v&~mask];h=[t&127 for t in m];target=sum((t>>7)<<i for i,t in enumerate(m));assert len(m)==26 and target.bit_count()==7
E={(i,j):k+27 for k,(i,j) in enumerate(itertools.combinations(range(26),2)) if not h[i]&h[j]};cs=[];top=max(E.values());var=lambda i:i+1
for i,j,k in itertools.combinations(range(26),3):
 if (i,j) in E and (i,k) in E and (j,k) in E:cs.append([-E[i,j],-E[i,k],-E[j,k]])
for (i,j),e in E.items():cs.append([-e,-var(i),-var(j)])
for i,s in enumerate(h):
 c=CardEnc.equals([v for e,v in E.items() if i in e]+[var(i)],8-s.bit_count(),top_id=top);cs+=c.clauses;top=max(top,c.nv)
c=CardEnc.equals(list(map(var,range(26))),7,top_id=top);cs+=c.clauses;stage=int(sys.argv[1]);cset=set()
for t in range(128):
 if t.bit_count()>stage:continue
 vs=[i for i,s in enumerate(h) if not s&~t];k=t.bit_count()
 for size,require_hit in ((k+1,True),(min(8,k+2),False)):
  for q in itertools.combinations(vs,size):
   clause=[E[e] for e in itertools.combinations(q,2) if e in E];
   if require_hit:clause.extend(map(var,q))
   cset.add(tuple(clause))
print('stage',stage,'clauses',len(cset),flush=True);cs+=list(cset);out=[];groups={s:[i for i,t in enumerate(h) if t==s] for s in set(h)};print('row equivalent choices',__import__('math').prod(__import__('math').comb(len(g),sum(target>>i&1 for i in g)) for g in groups.values()),flush=True)
with Solver(name='cadical195',bootstrap_with=cs) as sl:
 while sl.solve():
  model=set(sl.get_model());s=sum(1<<i for i in range(26) if var(i) in model);out.append(s);sl.add_clause([-var(i) for i in range(26) if s>>i&1])
 assert target in out
is_cube=lambda s:all(sum(s>>i&1 for i in g)==sum(target>>i&1 for i in g) for g in groups.values());print('admitted',len(out),'canonical residual orbit',sum(map(is_cube,out)));(P/f'ramsey_cube_missing_label_{stage}.json').write_text(json.dumps(dict(partial=h,cube=target,rows=sorted(out)))+'\n')
