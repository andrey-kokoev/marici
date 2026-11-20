"""Distinguish shortest-path, vicinity and return-to-strip incidence on the 22 alternating visits. Distances measured in the full cubic Hall incidence graph, not only along the alternating strip. Record position along the half-cycle from the fixed left vertex."""
from ramsey_tetra_swap_alternating import maps,a,b,D,M,profile
from collections import deque,Counter
from itertools import combinations
from pathlib import Path
import json
adj=[set() for _ in range(30)]
for i,d in enumerate(D):
    for j,m in enumerate(M,15):
        if d in m:adj[i].add(j);adj[j].add(i)
def distances(i):
    ds={i:0};q=deque([i]);
    while q:
        x=q.popleft()
        for y in adj[x]-ds.keys():ds[y]=ds[x]+1;q.append(y)
    return ds
dist=list(map(distances,range(30)));out=[]
for m in maps:
    n=tuple(b[m[a[i]]] for i in range(15));
    if m>=n or 22 not in profile(m,n):continue
    start=next(i for i in range(15) if a[i]==i and m[i]!=n[i]);x=start;cycle=[]
    while x not in cycle:cycle.extend([x,15+m[x]]);x=n.index(m[x])
    end=cycle[11];p=dist[start][end];views=[]
    for i,x in enumerate(cycle[1:11],1):
        y,=adj[x]-{cycle[i-1],cycle[i+1]};v=(dist[start][x],dist[end][x]);views.append(dict(position=i,dist=v,on_shortest=sum(v)==p,third_on=y in cycle,third_fixed=(a[y]==y if y<15 else b[y-15]==y-15)))
    out.append(dict(start=start,end=end,pole_distance=p,cycle=cycle,views=views))
assert len(out)==24
features=sorted({tuple(v['dist']) for r in out for v in r['views']});assert len(features)==6
assert not any(all(sum(tuple(v['dist']) in keep for v in r['views'])==3 for r in out) for k in range(7) for keep in combinations(features,k))
for r in out:
    s,t=r['start'],r['end'];bridges=[(i,j) for i in adj[s] for j in adj[t] if j in adj[i]];assert r['pole_distance']==3 and len(bridges)==1 and not set(bridges[0])&set(r['cycle']);r['bridge']=[s,*bridges[0],t]
for key in ('on_shortest','third_on','third_fixed'):print(key,Counter(tuple(v['position'] for v in r['views'] if v[key]) for r in out))
print('dist profiles',Counter(tuple(sorted(Counter(tuple(v['dist']) for v in r['views']).items())) for r in out));print('near pole',Counter(tuple(v['position'] for v in r['views'] if min(v['dist'])<=2) for r in out));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
