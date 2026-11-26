"""Observational implications among rejection tests, at fixed order 11 and degree 5. One example per induced isomorphism type from the saved cores. No converse is inferred as a law."""
import itertools,json,collections
from pathlib import Path
import networkx as nx
from pysat.solvers import Solver
P=Path(__file__).resolve().parents[1]/'results';cores=json.loads((P/'ramsey_core_capacity_36.json').read_text());groups={};cases=[]
for ci,z in enumerate(cores):
 a=z['core']
 for t in itertools.combinations(range(len(a)),11):
  G=nx.Graph();G.add_nodes_from(range(11));G.add_edges_from((i,j) for i,j in itertools.combinations(G,2) if a[t[i]]>>t[j]&1);sig=tuple(sorted((G.degree(i),tuple(sorted(G.degree(j) for j in G[i]))) for i in G));bucket=groups.setdefault(sig,[])
  if any(nx.is_isomorphic(G,H) for H in bucket):continue
  bucket.append(G);cases.append((ci,t,G))
rows=[]
for ci,t,G in cases:
 # Variables give each neighbor a red-independent support. Include only selected sizes of blue-clique constraints.
 v=lambda j,i:1+11*j+i;base=[[-v(j,i),-v(j,h)] for j in range(5) for i,h in G.edges()];by={}
 for q in range(1,5):
  by[q]=[[v(j,i) for i in u for j in J] for u in itertools.combinations(G,q) if not any(G.has_edge(i,h) for i,h in itertools.combinations(u,2)) for J in itertools.combinations(range(5),6-q)]
 r={}
 for qs in [(1,),(2,),(3,),(4,),(2,3),(2,4),(3,4),(1,2,3,4)]:
  with Solver(name='g4',bootstrap_with=base+sum((by[q] for q in qs),[])) as s:r[''.join(map(str,qs))]=not s.solve()
 rows.append(dict(parent=ci,vertices=t,reject=r))
names=r.keys();counts={x:sum(t['reject'][x] for t in rows) for x in names};pairs={x:{y:sum(t['reject'][x] and not t['reject'][y] for t in rows) for y in names} for x in names};print(len(rows),counts,pairs);(P/'ramsey_test_coincidence.json').write_text(json.dumps(dict(rows=rows,rejection_counts=counts,counterexamples=pairs),indent=1)+'\n')
