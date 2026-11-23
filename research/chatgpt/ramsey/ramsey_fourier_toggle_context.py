"""Scoped Fourier/multiplicity pilot: complete a refused site toggle by identity to obtain a Z2 permutation representation. In the sign sector use the canonical oriented difference of each toggle pair. Test whether opposite-edge transport through commuting squares recovers the independently measured metric directions. No quantum or efficiency claim."""
from ramsey_detour_intrinsic_cube import B,C,d,D,json,nx

def run(j):
    P=[s for s in B if j not in s and s|{j} in C];M=nx.Graph();M.add_nodes_from(P)
    for s in P:
        for t in P:
            if len(s^t)==1:M.add_edge(s,t)
    classes=[list(c) for c in nx.connected_components(M)];cut=lambda s:frozenset(w for w in C if d[w][s]<d[w][s|{j}]);actual={cut(s) for s in P};assert all(len({cut(s) for s in c})==1 for c in classes);return dict(toggle_pairs=len(P),fixed=len(C)-2*len(P),plus_mult=len(C)-len(P),minus_mult=len(P),metric_cuts=len(actual),square_classes=[[sorted(s) for s in c] for c in classes],square_edges=M.number_of_edges(),exact=(len(actual)==len(classes)))
r={i:run(i) for i in sorted(set.union(*(set(s) for s in B))) if any(i not in s and s|{i} in C for s in B)};print([(i,z['toggle_pairs'],z['metric_cuts'],list(map(len,z['square_classes']))) for i,z in r.items()]);(D/'ramsey_fourier_toggle_context.json').write_text(json.dumps(r,indent=2)+'\n')
