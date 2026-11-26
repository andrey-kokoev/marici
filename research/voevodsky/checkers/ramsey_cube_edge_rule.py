"""Extract and verify orbit rule in cube coordinates, then classify completions without assuming those symmetries. Fixed cube incidences, exact degrees, triangle and blue-clique constraints. No endpoint data in the completion solver."""
import json,itertools,collections
from ramsey_incidence_mismatch import base,P
from ramsey_retention_slice import check
from pysat.card import CardEnc
from pysat.solvers import Solver
z=json.loads((P/'ramsey_incidence35_endpoint.json').read_text());xyz=z['cube_coordinates'];m=z['masks'];cores=z['red_core_edges'];cells=lambda s:frozenset(xyz[i] for i in range(8) if s>>i&1);cs=[cells(s) for s in m];diag=next((list(cs[i])[0],list(cs[j])[0]) for i,j in cores if len(cs[i])==len(cs[j])==1 and list(cs[i])[0]^list(cs[j])[0]==7);cs=[frozenset(u^diag[0] for u in cell) for cell in cs];name=lambda cell:''.join(str(next(iter(bits))) if len(bits)==1 else '*' for k in [2,1,0] for bits in [{(u>>k)&1 for u in cell}]);names=list(map(name,cs));edge=lambda u,v:tuple(sorted((u,v)));red=frozenset(edge(names[i],names[j]) for i,j in cores);syms=[]
for p in itertools.permutations(range(3)):
 for x in range(8):
  def f(u):return x^sum(((u>>p[k])&1)<<k for k in range(3))
  syms.append({n:name(frozenset(map(f,c))) for n,c in zip(names,cs)})
def move(s,e):return edge(s[e[0]],s[e[1]])
orb={frozenset(move(s,e) for e in red) for s in syms};stab=[s for s in syms if all(move(s,e) in red for e in red)];fixed=set.intersection(*map(set,orb));seeds=[];left=set(red)
while left:
 e=min(left);o={move(s,e) for s in stab};seeds.append((e,len(o)));left-=o
print('diag',diag,'stabilizer',len(stab),'orbit',len(orb),'common',len(fixed),'seeds',seeds,flush=True);print('stabilizer basis images',[(s['000'],s['001'],s['010'],s['100']) for s in stab],flush=True)
# Enumerate with no symmetry assumption; seed one blocking clause per known orbit member. For each new four-region completion either replay as legal, or cut its violated blue sets.
E,cnf=base(m);top=max(E.values());
for i,s in enumerate(m):
 b=CardEnc.equals([v for e,v in E.items() if i in e],8-s.bit_count(),top_id=top);top=max(top,b.nv);cnf+=b.clauses
for t in range(256):
 if t.bit_count() not in (5,6):continue
 for q in itertools.combinations([i for i,s in enumerate(m) if not s&~t],t.bit_count()+1):cnf.append([E[e] for e in itertools.combinations(q,2) if e in E])
extra=[];rejected=0
with Solver(name='cadical195',bootstrap_with=cnf) as sl:
 for variant in orb:sl.add_clause([-v for (i,j),v in E.items() if edge(names[i],names[j]) in variant]);
 while sl.solve():
  sol=set(sl.get_model());edges=[e for e,v in E.items() if v in sol];a=[sum(1<<j for j in range(26) if edge(i,j) in edges) for i in range(26)];I=[(0,0)]
  for i,v in enumerate(a):I.extend([(q|1<<i,u|m[i]) for q,u in I if not q&v]);
  bad=[q for q,u in I if q.bit_count()>min(7,u.bit_count())];
  if not bad:extra.append(edges);sl.add_clause([-E[e] for e in edges])
  else:
   rejected+=1
   for q in bad:sl.add_clause([v for (i,j),v in E.items() if q>>i&1 and q>>j&1])
print('extra',len(extra),'rejected',rejected);(P/'ramsey_cube_edge_rule.json').write_text(json.dumps(dict(diagonal=diag,labels=names,seeds=seeds,group=[(s['000'],s['001'],s['010'],s['100']) for s in stab],orbit=len(orb),common=sorted(fixed),extra=extra,rejected=rejected))+'\n')
