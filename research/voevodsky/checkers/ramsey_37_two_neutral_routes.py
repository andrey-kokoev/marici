"""Compare the same six-site route test for both choices of middle center in every rotated decomposition. Same color words, not arbitrary equality of operators."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results';g=json.loads((D/'ramsey_37_dual_stars.json').read_text());N={v:set() for v in range(22)}
for u,v in g['red_edges']:N[u].add(v);N[v].add(u)
out=[]
for rec in json.loads((D/'ramsey_37_three_stars_apex.json').read_text()):
 for c in rec['choices']:
    L,R=map(set,(rec['left'],rec['right']));a,b=c['center'],c['apex'];U={v for p in c['pairs'] for v in p}|{b};l,=L&N[a];r,=R&N[a];v,w=sorted(N[b]&U);X={l,r,b};Y={v,w,a};missing=[(x,y) for x in X for y in Y if y not in N[x]];assert not any(j in N[i] for S in [X,Y] for i,j in combinations(S,2));assert (b,a) in missing
    tails=[x for x in U if len(N[x]&U)==1];assert len(tails)==2;diamonds=[]
    for t in tails:
        foot,=N[t]&U
        for end in sorted(N[t]&{l,r}):
            for via in sorted(N[foot]&N[end]&{v,w}):diamonds.append(dict(source=foot,target=end,via=[t,via]))
    if len(missing)==1:assert len(diamonds)==2 and set().union(*({x['source'],*x['via']} for x in diamonds))==U-{b}
    else:assert len(missing)==len(set(x for x,y in missing))==len(set(y for x,y in missing))==3
    out.append(dict(center=a,apex=b,sides=[sorted(X),sorted(Y)],missing=sorted(missing),side_diamonds=diamonds))
assert Counter(len(c['missing']) for c in out)=={1:5,3:5};print(out[:2]);(D/'ramsey_37_two_neutral_routes.json').write_text(json.dumps(out,indent=2)+'\n')
