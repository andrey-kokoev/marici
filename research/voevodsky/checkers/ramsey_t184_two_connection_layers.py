"""Paired inner contacts and coarse outer edges; alternative radial reading uses shortest paths in actual fine 1-skeleton from any vertex of the exit tetrahedron. No Ramsey labels used."""
from pathlib import Path
from itertools import combinations
from collections import deque
import json
D=Path(__file__).resolve().parents[1]/'results';d=json.loads((D/'esd7_explicit_analytical_census.json').read_text());coords={v['id']:tuple(v['barycentric']) for v in d['vertices']};V={x:v for v,x in coords.items()};T=d['tetrahedra'];c=set(next(t for t in T if t['id']=='T184')['vertices']);adj={v:set() for v in coords}
for e in d['edges']:
    a,b=e['vertices'];adj[a].add(b);adj[b].add(a)
def dist(starts):
    seen={v:0 for v in starts};q=deque(starts)
    while q:
        v=q.popleft()
        for w in adj[v]-seen.keys():seen[w]=seen[v]+1;q.append(w)
    return seen
inner=[];outer=[];exits=[];rad=[]
for i in range(4):
    w=V[tuple(1 if j==i else 2 for j in range(4))];o=V[tuple(7 if j==i else 0 for j in range(4))];t,=[s for s in T if s['id']!='T184' and c-{w}<=set(s['vertices'])];inner.append(w);outer.append(o);exits.append(set(t['vertices']));f=dist(exits[-1]);b=dist([o]);L=f[o];layers=[sorted(v for v in coords if f[v]==k and b[v]==L-k) for k in range(L+1)];rad.append(dict(exit=t['id'],corner=o,distance=L,shortest_path_layers=layers))
for i,j in combinations(range(4),2):
    assert exits[i]&exits[j]==c-{inner[i],inner[j]};border=sorted((v for v,x in coords.items() if x[i]+x[j]==7),key=lambda v:coords[v][j]);assert len(border)==8 and all(b in adj[a] for a,b in zip(border,border[1:]))
out=dict(pair_contacts=6,outer_chains=6,segments_per_outer_chain=7,radial=rad);print([(s['distance'],[len(l) for l in s['shortest_path_layers']]) for s in rad]);(D/'ramsey_t184_two_connection_layers.json').write_text(json.dumps(out,indent=2)+'\n')
