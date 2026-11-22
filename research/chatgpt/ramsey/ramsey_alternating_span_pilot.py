"""Operational pilot, not a definition of the operator's span. Span k = endpoints of exactly k allowed steps with repetitions, pin = choose one endpoint. On native sector graph use forward face turns or reciprocal seam steps for both spans. On stored (3,7;22) parents also test alternating red and blue graph walks. Exhaust each possible pinned start instead of choosing a lucky path. Separate ambient-size detection from threshold derivation."""
from pathlib import Path
from collections import Counter
import json,networkx as nx
D=Path(__file__).parent

def counts(neigh,k):
    out=[]
    for v in range(len(neigh)):
        s={v}
        for _ in range(k):s=set().union(*(neigh[i] for i in s))
        out.append(len(s))
    return Counter(out)
t=json.loads((D.parents[1]/'nima/results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports'];T={r['outer_arrow']:r['triangle'] for r in t};E=list(T);n=[{E.index(e[::-1]),next(i for i,h in enumerate(E) if T[h][0]==T[e][0] and h[0]==e[1])} for e in E];sector={k:counts(n,k) for k in (3,7)};point=[{j for j in range(8) if (i^j).bit_count()==1} for i in range(8)];pts={k:counts(point,k) for k in (3,7)};R=Counter();B=Counter()
for line in (D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines():
    g=nx.from_graph6_bytes(line);red=[set(g[v]) for v in range(len(g))];blue=[set(g)-{v}-s for v,s in enumerate(red)];R.update(counts(red,3));B.update(counts(blue,7))
out=dict(point_exact=pts,sector_exact=sector,red_three=R,blue_seven=B);print(out);(D/'ramsey_alternating_span_pilot.json').write_text(json.dumps(out,indent=2)+'\n')
