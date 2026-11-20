"""All local distance-profile selectors of three reflected visit pairs, by DP on count vectors. Check reversal symmetry of the reference bridge separately. Input Hall graph and verified 24 strips; no Ramsey coloring input."""
from collections import Counter
from pathlib import Path
from itertools import combinations
import json
H=Path(__file__).parent;rows=json.loads((H/'ramsey_strip_fixed_views.json').read_text());ds=list(combinations(range(6),2));ms=[m for m in combinations(ds,3) if len(set(sum(m,())))==6];N=[set() for _ in range(30)]
for i,d in enumerate(ds):
    for j,m in enumerate(ms,15):
        if d in m:N[i].add(j);N[j].add(i)
D=[]
for s in range(30):
    seen={s:0};q=[s]
    for v in q:
        for w in N[v]-seen.keys():seen[w]=seen[v]+1;q.append(w)
    D.append(seen)
profiles=[]
for row in rows:
    c=row['cycle'];bs=row['bridge'];sig=lambda x:tuple(D[x][b] for b in bs);p=list(map(sig,c[1:11]));assert p==list(map(sig,c[:11:-1]));profiles.append(p)
def solve(ps):
    classes=sorted(set.union(*(set(p) for p in ps)));target=(3,)*len(ps);z=(0,)*len(ps);dp={z:(1,[()])}
    for k in classes:
        v=tuple(p.count(k) for p in ps);nd=dp.copy()
        for a,(num,examples) in dp.items():
            b=tuple(x+y for x,y in zip(a,v));
            if max(b)>3:continue
            n,ex=nd.get(b,(0,[]));nd[b]=(n+num,(ex+[e+(k,) for e in examples])[:3])
        dp=nd
    num,examples=dp.get(target,(0,[]));return dict(classes=len(classes),rules=num,examples=examples)
out={};
for name,f in [('interior',lambda k:k[1:3]),('whole',lambda k:k),('unoriented',lambda k:min(k,k[::-1]))]:out[name]=solve([[f(k) for k in p] for p in profiles]);print(name,out[name]);
out['direct']=[sum(min(k[1:3])==1 for k in p) for p in profiles];print('direct',Counter(out['direct']));(H/'ramsey_strip_bridge_profiles.json').write_text(json.dumps(out,indent=2)+'\n')
