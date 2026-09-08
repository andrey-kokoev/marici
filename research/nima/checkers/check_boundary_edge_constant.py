"""Division-free constant triangle weights; exact finite verification."""
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path
import json

@lru_cache(None)
def faces(v):
    if len(v)<3: return (frozenset(),)
    out=[]
    for k in range(1,len(v)-1):
        for a in faces(v[:k+1]):
            for b in faces(v[k:]):
                out.append(a|b|{(v[0],v[k],v[-1])})
    return tuple(out)

stages=[]
for n in range(4,10):
    ts=faces(tuple(range(n)))
    assert len(ts)==comb(2*(n-2),n-2)//(n-1)
    for t in ts:
        assert len(t)==n-2
        for i in range(n):
            edge={i,(i+1)%n}
            assert sum(edge<=set(triangle) for triangle in t)==1
    stages.append({'n':n,'triangulations':len(ts),'boundary_edge_checks':n*len(ts)})
# Uniform triangle weights cannot represent constant 1 when p divides n-2.
failures=[]
for n,p in [(4,2),(5,3),(7,5)]:
    assert (n-2)%p==0
    assert all(((n-2)*a)%p==0 for a in range(p))
    failures.append({'n':n,'p':p,'uniform_constant_obstruction':1})
result={'status':'passed','stages':stages,'deliberate_failures':failures,
        'theorem':'A fixed boundary-edge indicator represents constant 1 over any coefficient ring.',
        'scope':'Finite tests verify the constant correction, not a formal verification of the full converse proof.'}
Path('research/nima/results/boundary_edge_constant.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
