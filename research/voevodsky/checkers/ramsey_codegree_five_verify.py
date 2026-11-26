"""Independent SAT cross-check; no panel enumeration/symmetry pruning. Use igraph to enumerate independent 5/6-sets. Exactly prescribed H-neighbor counts, triangle clauses, and blue-set hitting clauses for the two trios. Also replay arbitrary-vertex codegree distribution on the known witness as a sharpness control."""
from ramsey_retention_slice import CAT,D,decode
from pysat.solvers import Solver
from pysat.card import CardEnc
import json,itertools,collections,igraph as ig
P=D.parent;res=[];pairs=itertools.combinations
for i,l in enumerate((CAT/'r37_22.g6').read_text().splitlines()):
 a=decode(l);es=[(v,w) for v,w in pairs(range(22),2) if a[v]>>w&1];k=len(es)-52
 if k>9:continue
 assert k in (8,9);g=ig.Graph(22,es);sets={n:g.independent_vertex_sets(n,n) for n in (5,6)};V=lambda u,j:1+22*u+j;cs=[];top=132
 for u in range(6):
  b=CardEnc.equals([V(u,j) for j in range(22)],4+int(k==8 and u%3==2),top_id=top);cs+=b.clauses;top=max(top,b.nv);cs.extend([[-V(u,j),-V(u,h)] for j,h in es])
 for side in ((0,1,2),(3,4,5)):
  for n,t in [(6,2),(5,3)]:
   for us in pairs(side,t):cs.extend([[V(u,j) for u in us for j in q] for q in sets[n]])
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  separate=sl.solve();
  for u,v in itertools.product(range(3),range(3,6)):
   if k==8 and (u,v)==(2,5):continue
   for j in range(22):sl.add_clause([-V(u,j),-V(v,j)])
  joint=sl.solve();assert not joint and separate==(k==8);res.append(dict(i=i,independent_sides=separate,with_cross_edges=joint));print(i,separate,joint,flush=True)
z=decode(json.loads((P/'ramsey_incidence35_endpoint.json').read_text())['graph6']);hist=collections.Counter((z[i]&z[j]).bit_count() for i,j in pairs(range(35),2) if not z[i]>>j&1);assert max(hist)==4;print(hist);(P/'ramsey_codegree_five_verify.json').write_text(json.dumps(dict(checks=res,known_blue_pair_codegrees=hist))+'\n')
