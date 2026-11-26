"""Enumerate all minimum five-deletion sets. Classify surviving graphs against seven stored (3,6) types by degree partition and exact isomorphism."""
import json,itertools,collections
import networkx as nx
from pysat.card import CardEnc
from pysat.solvers import Solver
from ramsey_retention_slice import D,CAT,decode
P=D.parent;prev=json.loads((P/'ramsey_sum10_outer_overlap.json').read_text());source=(CAT/'r37_22.g6').read_text().splitlines();refs=[decode(s) for s in (CAT/'r36_17.g6').read_text().splitlines()];mask=(1<<22)-1

def G(a,p):
 g=nx.Graph();g.add_nodes_from(i for i in range(len(a)) if p>>i&1);g.add_edges_from((i,j) for i,j in itertools.combinations(g,2) if a[i]>>j&1);return g
# invariants: counts by degree and neighbor degrees
sig=lambda g:tuple(sorted((g.degree(i),tuple(sorted(g.degree(j) for j in g[i]))) for i in g));ref=[G(a,2**17-1) for a in refs];sigs=[sig(g) for g in ref];rows=[]
for r,line in zip(prev,source,strict=True):
 a=decode(line);count=collections.Counter();rows.append(count)
 if r['overlap']!=17:continue
 def six(p,q):
  if len(q)==6:yield q;return
  while p.bit_count()>=6-len(q):
   b=p&-p;p^=b;i=b.bit_length()-1;yield from six(p&~a[i],q+[i+1])
 with Solver(name='g4',bootstrap_with=list(six(mask,[]))+CardEnc.atmost(list(range(1,23)),5).clauses) as s:
  while s.solve():
   rm=[i for i in s.get_model() if 1<=i<=22];assert len(rm)==5;s.add_clause([-i for i in rm]);g=G(a,mask^sum(1<<(i-1) for i in rm));v=sig(g);t=next(j+1 for j,x in enumerate(sigs) if x==v and nx.is_isomorphic(g,ref[j]));count[t]+=1
print('type/copies/hosts',[(i,sum(r[i] for r in rows),sum(i in r for r in rows)) for i in range(1,8)]);print('distinct types per host',collections.Counter(map(len,rows)));(P/'ramsey_sum10_seed_types.json').write_text(json.dumps(rows,indent=1)+'\n')
