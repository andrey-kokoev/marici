"""First interval-closure failure radius per candidate bit, exact 12-state control. Radius two includes the square-completion test."""
import networkx as nx,json,itertools
from pathlib import Path
D=Path(__file__).parent;g=nx.from_graph6_bytes((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()[9]);g.remove_nodes_from([17,21]);I=[frozenset()];
for v in g:I.extend([s|{v} for s in I if not s.intersection(g[v])]);
T=[s for s in I if len(s)==6];B=[s for s in I if all(s&t for t in T)];G=nx.Graph();G.add_nodes_from(B);G.add_edges_from((s,t) for s,t in itertools.combinations(B,2) if len(s^t)==1);d=dict(nx.all_pairs_shortest_path_length(G));code=lambda s:0 if 7 in s else 3 if 9 in s else 1 if 1 in s else 2
out={}
for bit in [2,1]:
 bad=[(s,t,z) for s,t in itertools.combinations(B,2) for z in B if not ((code(s)^code(t))&bit) and (code(s)^code(z))&bit and d[s][t]==d[s][z]+d[z][t]];w=min(bad,key=lambda v:d[v[0]][v[1]]) if bad else None;out[bit]=dict(first_failed_radius=d[w[0]][w[1]] if w else None,witness=list(map(sorted,w)) if w else None)
print(out);(D/'ramsey_gate_closure_radius.json').write_text(json.dumps(out,indent=2)+'\n')
