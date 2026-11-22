"""Test two intrinsic edge readings for distinct triple intersections in Euclidean 3-space. Line model: exactly three independent assigned planes per point, edges iff sharing two planes (three fixed-direction families suffice). Two-distance model: one distance per color. Witness obstructions are local and do not require fitting coordinates."""
from itertools import product
from pathlib import Path
import json,networkx as nx
D=Path(__file__).parent
# Literal positive control: x=a, y=b, z=ab. All six squared distances coincide.
pts=[(a,b,a*b) for a,b in product((-1,1),repeat=2)];dist={sum((x-y)**2 for x,y in zip(p,q)) for i,p in enumerate(pts) for q in pts[:i]};assert dist=={8}
counts={};mins={};example=None
for index,line in enumerate((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines(),1):
    g=nx.from_graph6_bytes(line);v=max(g,key=g.degree);N=list(g[v]);assert len(g)==22 and all(not g.has_edge(x,y) for i,x in enumerate(N) for y in N[:i]);assert len(N)>4;counts[len(N)]=counts.get(len(N),0)+1
    d=min(v for _,v in g.degree());mins[d]=mins.get(d,0)+1
    if example is None:example=dict(record=index,center=v,independent_neighbors=N)
r=dict(tetrahedron=pts,squared_distance=8,max_degree_histogram=counts,min_degree_histogram=mins,example=example);print(r);Path(__file__).with_suffix('.json').write_text(json.dumps(r)+'\n')
