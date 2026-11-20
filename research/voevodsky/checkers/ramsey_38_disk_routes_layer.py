"""Test Z2 transport on the actual colored cone and the hub's unused red neighbors as a first layer. Count distinct pole pairs separately from boundary paths."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results';g=json.loads((D/'ramsey_38_root_glue.json').read_text())['witness'];V=set(range(27));E=set(map(tuple,g['plus_edges']));N=[{v for v in V if tuple(sorted((u,v))) in E} for u in range(27)];out=[]
for p,q in combinations(range(27),2):
    l=N[p]-N[q]-{q};r=N[q]-N[p]-{p};A=l|r
    for side,opp in ((l,r),(r,l)):
        if len(side)<6 or len(opp)<5:continue
        def paths(s):
            if len(s)==11:
                if s[0]<s[-1]:yield s
            else:
                for v in sorted((A&N[s[-1]])-set(s)):yield from paths(s+[v])
        for s0 in sorted(side):
            for s in paths([s0]):
                h,=N[p]&N[q];Z=N[h]-{p,q};assert not (Z & (A|{p,q,h}));assert all(v not in N[u] for u,v in combinations(Z,2));S=[v in l for v in s];B=[int(v in N[u]) for u,v in zip(s,s[1:]+s[:1])];assert B==[int(a!=b) for a,b in zip(S,S[1:]+S[:1])];assert sum(B)==10
                # With red=1 and blue=0, a flat extension to a cone requires radial bits to differ by B along its boundary. Compare actual spoke bits vs the two candidate assignments.
                assert all(v not in N[h] for v in s);fits=[u for u in V-set(s) if all(((x in N[u])!=(y in N[u]))==bool(b) for x,y,b in zip(s,s[1:]+s[:1],B))];assert {p,q}<=set(fits)
                extras=[len(Z&N[v]) for v in s];out.append(dict(poles=[p,q],ring=s,hub=h,layer=sorted(Z),flat_cone_centers=sorted(fits),extra_two_red_routes=extras))
assert len(out)==35
for key in ['layer','flat_cone_centers','extra_two_red_routes']:
 print(key,Counter(len(x[key]) if key!='extra_two_red_routes' else x[key].count(0) for x in out))
print(out[0]);(D/'ramsey_38_disk_routes_layer.json').write_text(json.dumps(out,indent=2)+'\n')
