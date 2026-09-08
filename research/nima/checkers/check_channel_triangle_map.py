"""Formal exponent certificates for a root-free channel-to-triangle map."""
from itertools import combinations
from functools import lru_cache
from collections import Counter
from pathlib import Path
import json

@lru_cache(None)
def faces(v):
    if len(v)<3:return (frozenset(),)
    return tuple(a|b|{(v[0],v[k],v[-1])} for k in range(1,len(v)-1) for a in faces(v[:k+1]) for b in faces(v[k:]))
def vec(edges):return Counter(edges)
def plus(a,b):
    c=Counter(a)
    for e,v in b.items():c[e]+=v
    return Counter({e:v for e,v in c.items() if v})
def minus(a,b):return plus(a,{e:-v for e,v in b.items()})
records=[]
for n in range(4,10):
    boundary={tuple(sorted((i,(i+1)%n))) for i in range(n)}
    triples=list(combinations(range(n),3))
    # Increasing boundary traversal on (i,j,k) uses ij,jk; descending uses ik.
    hp={q:vec(e for e in [(q[0],q[1]),(q[1],q[2])] if e not in boundary) for q in triples}
    hm={q:vec(e for e in [(q[0],q[2])] if e not in boundary) for q in triples}
    for i,j,k in triples:
        delta=vec(e for e in [(i,j),(j,k)] if e not in boundary)
        delta=minus(delta,vec(e for e in [(i,k)] if e not in boundary))
        assert minus(hp[i,j,k],hm[i,j,k])==delta
    ts=faces(tuple(range(n)))
    for t in ts:
        expected=vec(set(e for q in t for e in combinations(q,2))-boundary)
        p=Counter();m=Counter()
        for q in t:p=plus(p,hp[q]);m=plus(m,hm[q])
        assert p==m==expected
        assert sum(expected.values())==n-3
    # Assigning both incident triangles doubles each internal-edge exponent.
    t=ts[0];wrong=Counter()
    for q in t:wrong=plus(wrong,plus(hp[q],hm[q]))
    assert set(wrong.values())=={2}
    records.append({'n':n,'triangulations':len(ts),'triangle_gauge_checks':len(triples),'wrong_double_assignment_exponent':2})
result={'status':'passed','records':records,'map':'h_plus(i,j,k)=lambda_ij lambda_jk, h_minus(i,j,k)=lambda_ik; boundary lambda=1', 'gauge':'h_plus/h_minus=delta(lambda), boundary holonomy=1', 'scope':'Formal integer channel exponents through n=9; generic proof uses cancellation of oppositely oriented internal-edge incidences. No square roots or source-normalization claims.'}
Path('research/nima/results/channel_triangle_map.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
