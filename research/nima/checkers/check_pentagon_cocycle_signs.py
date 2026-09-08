"""Exact oriented pentagon and simplex contraction identities on six labels."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

def add(a,b,scale=1):
    out=Counter(a)
    for k,v in b.items(): out[k]+=scale*v
    return Counter({k:v for k,v in out.items() if v})

def delta(c,face):
    out=Counter()
    for i in range(len(face)):
        out=add(out,c[face[:i]+face[i+1:]],(-1)**i)
    return out

vertices=tuple(range(6))
h={t:Counter({t:1}) for t in combinations(vertices,3)}
g={q:delta(h,q) for q in combinations(vertices,4)}
assert all(not delta(g,p) for p in combinations(vertices,5))
contracted={t:(Counter() if 0 in t else g[(0,)+t]) for t in h}
assert all(delta(contracted,q)==g[q] for q in g)

def crossing(a,b):
    i,j=a;k,l=b
    return i<k<j<l or k<i<l<j
records=[]
for p in combinations(vertices,5):
    boundary={tuple(sorted((p[i],p[(i+1)%5]))) for i in range(5)}
    ds=[e for e in combinations(p,2) if e not in boundary]
    ts=sorted(tuple(sorted((a,b))) for a,b in combinations(ds,2) if not crossing(a,b))
    assert len(ts)==5
    neighbors={t:[u for u in ts if len(set(t)^set(u))==2] for t in ts}
    assert all(len(v)==2 for v in neighbors.values())
    cycle=[ts[0],neighbors[ts[0]][0]]
    while len(cycle)<5:
        cycle.append(next(u for u in neighbors[cycle[-1]] if u!=cycle[-2]))
    assert cycle[0] in neighbors[cycle[-1]] and len(set(cycle))==5
    coefficients=Counter(); increments=[]
    for t,u in zip(cycle,cycle[1:]+cycle[:1]):
        old=next(iter(set(t)-set(u)));new=next(iter(set(u)-set(t)))
        q=tuple(sorted(set(old)|set(new)))
        sign=1 if old==(q[0],q[2]) else -1
        coefficients[q]+=sign;increments.append((q,sign))
    expected={p[:i]+p[i+1:]:(-1)**i for i in range(5)}
    overall=coefficients[next(iter(expected))]*expected[next(iter(expected))]
    assert all(coefficients[q]==overall*v for q,v in expected.items())
    total=Counter()
    for q,sign in increments: total=add(total,g[q],sign)
    assert not total
    q,sign=increments[0]
    defect=add(total,g[q],-2*sign)
    assert defect and set(abs(v) for v in defect.values())=={2}
    records.append({'vertices':p,'cycle_orientation':overall,'flipped_sign_residual_coefficients':list(defect.values())})
result={'status':'passed','pentagons':records,'contraction_quadruples':len(g),
 'identity':'delta(sg)=g for closed g, with (sg)(i,j,k)=g(0,i,j,k) off the root',
 'convention':'g_abcd is the increment from diagonal ac to bd; g=delta h',
 'boundary':'Integer symbolic identities on six labels; proof uses relabelling, not a census of arbitrary source data. The sign-error test is invisible in characteristic two.'}
Path('research/nima/results/pentagon_cocycle_signs.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
