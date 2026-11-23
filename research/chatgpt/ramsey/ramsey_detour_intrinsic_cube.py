"""Independent replay on saved core. Test abstract partial cube separately from failure in incidence coordinates. Edge semicubes defined by graph distance are necessary cuts for EVERY isometric cube embedding; all distinct cuts together attaining graph distances suffice."""
from pathlib import Path
import json,networkx as nx
from itertools import combinations
D=Path(__file__).parent;r=json.loads((D/'ramsey_support_detour.json').read_text());g=nx.from_graph6_bytes((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()[r['record']-1]);g.remove_nodes_from(r['deleted']);I=[frozenset()];
for i in g:I.extend([s|{i} for s in I if not s.intersection(g[i])]);
T=[s for s in I if len(s)==6];B=[s for s in I if all(s&t for t in T)];G=nx.Graph();G.add_nodes_from(B);G.add_edges_from((a,b) for a,b in combinations(B,2) if len(a^b)==1);a,b=map(frozenset,(r['start'],r['target']));C=G.subgraph(nx.node_connected_component(G,a));d=dict(nx.all_pairs_shortest_path_length(C));cuts=set();per_axis={};assert nx.is_bipartite(C)
for u,v in C.edges:
    S=frozenset(w for w in C if d[w][u]<d[w][v]);cut=S if a not in S else frozenset(C)-S;cuts.add(cut);axis,=u^v;per_axis.setdefault(axis,set()).add(cut)
err=sum(sum((u in s)!=(v in s) for s in cuts)!=d[u][v] for u,v in combinations(C,2));unavoidable=[v for v in g if v not in a|b and not nx.has_path(G.subgraph([s for s in B if v not in s]),a,b)];out=dict(component_sizes=sorted(map(len,nx.connected_components(G))),edges=C.number_of_edges(),cuts=len(cuts),distance_mismatches=err,abstract_partial_cube=not err,unavoidable_auxiliaries=unavoidable,metric_cuts_per_site={v:len(c) for v,c in sorted(per_axis.items())},available_first_moves=[sorted(s^a) for s in G.neighbors(a)]);print(out);(D/'ramsey_detour_intrinsic_cube.json').write_text(json.dumps(out,indent=2)+'\n')
