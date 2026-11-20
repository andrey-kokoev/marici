"""Pilot n=3+t, shared pole-edge tetra fan. Ring vertex has one red pole and one blue pole. Test simple alternating red rings, allowing exactly one same-side blue seam for odd n. No induced-cycle condition. Count qualifying pole pairs, not all rings."""
import json
from pathlib import Path
from itertools import combinations
D=Path(__file__).resolve().parents[1]/'results';out=[]
for t,N,file in [(7,22,'ramsey_37_dual_stars'),(8,27,'ramsey_38_root_glue'),(9,35,'ramsey_39_glue_vs_circle')]:
    d=json.loads((D/(file+'.json')).read_text());d=d.get('witness',d);E={tuple(sorted(e)) for e in d.get('red_edges',d.get('plus_edges'))};V=set(range(N));red=lambda a,b:tuple(sorted((a,b))) in E; adj=[{v for v in V if red(u,v)} for u in range(N)];n=t+3; examples=[]
    for p,q in combinations(range(N),2):
        L=(adj[p]-adj[q])-{q};R=(adj[q]-adj[p])-{p};A=L|R
        if min(len(L),len(R))<n//2 or max(len(L),len(R))<(n+1)//2:continue
        def walk(path):
            if len(path)==n:
                same=(path[0] in L)==(path[-1] in L)
                if same==bool(n%2) and red(path[-1],path[0])==bool(not(n%2)):return path
            else:
                for v in sorted((adj[path[-1]]&A)-set(path)):
                    hit=walk(path+[v]);
                    if hit:return hit
        for start in sorted(A):
            ring=walk([start]);
            if ring:
                assert all((v in L)!=(w in L) for v,w in zip(ring,ring[1:]));examples.append(dict(poles=[p,q],ring=ring,pole_edge_red=red(p,q)));break
    row=dict(t=t,n=n,source=file,qualifying_pairs=len(examples),example=examples[0] if examples else None);out.append(row);print(row,flush=True)
(D/'ramsey_three_case_tet_ring.json').write_text(json.dumps(out,indent=2)+'\n')
