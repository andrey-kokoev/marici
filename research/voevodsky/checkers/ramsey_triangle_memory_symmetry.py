"""Decompose the minimal both-phase, both-orientation triangle reader by terminal permutations and global mask complement (alphabet symmetries). Count rooted state orbits; do not assume orbit compression respects a fixed next input."""
import json
from itertools import permutations
from collections import Counter,deque
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';a=json.loads((D/'ramsey_triangle_transport_memory.json').read_text())['full'];t=a['transition'];f=a['accepting'];q=a['initial'];n=len(t);G=[]
for p in permutations(range(3)):
 for c in (0,7):
    act=[c^sum((1<<p[i]) for i in range(3) if m>>i&1) for m in range(8)];g=[None]*n;g[q]=q;todo=deque([q]);
    while todo:
        x=todo.popleft();y=g[x];assert f[x]==f[y]
        for m,j in enumerate(t[x]):
            k=t[y][act[m]]
            if g[j] is None:g[j]=k;todo.append(j)
            else:assert g[j]==k
    assert len(set(g))==n;G.append(g)
orbits={tuple(sorted({g[i] for g in G})) for i in range(n)};h=Counter(map(len,orbits));s=Counter(map(len,[o for o in orbits if f[o[0]]]));fixed=[sum(j==i for i,j in enumerate(g)) for g in G];assert sum(fixed)==len(G)*len(orbits);key={u:min(o) for o in orbits for u in o};amb=sum(any(len({key[t[x][m]] for x in o})>1 for m in range(8)) for o in orbits);sizes=dict(sorted(h.items()));dist={q:0};todo=deque([q]);
while todo:
 i=todo.popleft()
 for j in t[i]:
    if j not in dist:dist[j]=dist[i]+1;todo.append(j)
out=dict(states=n,orbits=len(orbits),size_histogram=sizes,accepting_orbits_by_size=dict(s),noncongruent_orbits_at_fixed_input=amb,states_by_shortest_history=dict(sorted(Counter(dist.values()).items())),fixed_per_action=fixed);print(out);(D/'ramsey_triangle_memory_symmetry.json').write_text(json.dumps(out,indent=2)+'\n')
