"""Test sign correction vs actual pole-exchange symmetry on each previously certified ring. Red flips the carried bit; traversing a triangle is a closed walk, not a new graph automorphism."""
import json
from itertools import combinations
from collections import Counter
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results'; data=json.loads((D/'ramsey_38_disk_routes_layer.json').read_text());edges=set(map(tuple,json.loads((D/'ramsey_38_root_glue.json').read_text())['witness']['plus_edges']));V=set(range(27));red=lambda x,y:int(tuple(sorted((x,y))) in edges);out=[]
for row in data:
    p,q=row['poles'];h=row['hub'];ring=row['ring'];Z=set(row['layer']);core={p,q,h}|Z;W=V-core-set(ring);assert all(red(u,v)==((u==h)^(v==h)) for u,v in combinations(core,2));part=[sum(red(k,u) for u in ring) for k in (p,q)];assert sorted(part)==[5,6]
    lifts=[(z,w) for z in sorted(Z) for w in sorted(W) if red(h,z)^red(z,w)^red(w,h)];assert all([red(h,z),red(z,w),red(w,h)]==[1,0,0] for z,w in lifts);assert lifts
    z,w=lifts[0];route=[p,h,z,w,h,q];assert sum(red(a,b) for a,b in zip(route,route[1:]))%2==1
    out.append(dict(poles=[p,q],ring=ring,hub=h,layer=sorted(Z),external_candidates=sorted(W),odd_triangle_count=len(lifts),distinct_external_vertices=len({w for _,w in lifts}),route=route,ring_part_sizes=part))
print(len(out),out[0]);print('loop range',min(t['odd_triangle_count'] for t in out),max(t['odd_triangle_count'] for t in out));(D/'ramsey_38_hub_flip.json').write_text(json.dumps(out,indent=2)+'\n')
