"""Keep the exchanged end stars. Enumerate all disjoint invariant induced red 4-leaf stars and inspect the seven residual vertices. No route-coherence labels assumed."""
from itertools import combinations
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';g=json.loads((D/'ramsey_37_dual_stars.json').read_text());ends=json.loads((D/'ramsey_37_neutral_middle.json').read_text());E=set(map(tuple,g['red_edges']));V=set(range(22));N={u:{v for v in V if tuple(sorted((u,v))) in E} for u in V};out=[]
for d in ends:
    L,R=set(d['left']),set(d['right']);M=V-L-R;s={v:v for v in map(int,d['fixed'])}
    for a,b in d['moving_middle']:s[a]=b;s[b]=a
    choices=[]
    for c in sorted(M):
        if s[c]!=c:continue
        for leaves in combinations(sorted(N[c]&M),4):
            S={c,*leaves}
            if {s[x] for x in S}!=S:continue
            assert all(v not in N[u] for u,v in combinations(leaves,2));U=M-S;apex,=[x for x in U if x==s[x]];pairs=[(v,s[v]) for v in sorted(U) if v<s[v]];assert len(pairs)==3
            contacts={u:[len(N[u]&b) for b in [L,S,R]] for u in sorted(U)};assert contacts[apex]==[1,2,1];choices.append(dict(center=c,leaves=leaves,pairs=pairs,apex=apex,contacts=contacts,residual_red_edges=sorted(e for e in E if set(e)<=U)))
    assert len(choices)==2;out.append(dict(left=sorted(L),right=sorted(R),choices=choices))
(D/'ramsey_37_three_stars_apex.json').write_text(json.dumps(out,indent=2)+'\n');print(out[0])
