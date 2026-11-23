"""Clause-first encoding for the mixed 2/17 directions, independent of cycle traversal. Validate predicted two column partitions against graph metric only afterwards."""
from pathlib import Path
import json,itertools,collections,networkx as nx
D=Path(__file__).parent;g=nx.from_graph6_bytes((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()[2]);g.remove_nodes_from([1,19]);I=[frozenset()];
for v in g:I.extend([s|{v} for s in I if not s.intersection(g[v])]);
T=[s for s in I if len(s)==6];B=[s for s in I if all(t&s for t in T)];U=frozenset.union(*B);R={t&U for t in T};R={s for s in R if not any(t<s for t in R)};assert {2,4,11} in R and {10,17,18} in R and all(g.has_edge(a,b) for a,b in [(2,17),(4,18),(10,11)])
def code(s):
    if 2 in s:return '00'
    if 17 in s:return '11'
    assert ({4,10}<=s)!=({11,18}<=s);return '01' if 4 in s else '10'
G=nx.Graph();G.add_nodes_from(B);G.add_edges_from((s,t) for s,t in itertools.combinations(B,2) if len(s^t)==1);d=dict(nx.all_pairs_shortest_path_length(G));cuts=[]
for k in range(2):
    side={s for s in B if code(s)[k]=='1'};cross=[(s,t) for s in side for t in G[s] if t not in side];assert all(side=={w for w in B if d[w][s]<d[w][t]} for s,t in cross);cuts.append(dict(crossing_sites=sorted(next(iter(s^t)) for s,t in cross),side_sizes=[len(side),len(B)-len(side)]))
o=dict(projected_rows=sorted(sorted(t) for t in R),populations=dict(collections.Counter(map(code,B))),cuts=cuts);print(o);(D/'ramsey_gate_square.json').write_text(json.dumps(o,indent=2)+'\n')
