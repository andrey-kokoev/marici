"""Formal certificates for flip context changes, without triangle weights."""
from functools import lru_cache
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

@lru_cache(None)
def ts(v):
    if len(v)<3:return (frozenset(),)
    out=[]
    for k in range(1,len(v)-1):
        extra=set()
        if k>1:extra.add(tuple(sorted((v[0],v[k]))))
        if k<len(v)-2:extra.add(tuple(sorted((v[k],v[-1]))))
        for a in ts(v[:k+1]):
            for b in ts(v[k:]):out.append(a|b|extra)
    return tuple(out)

def vector(terms):
    c=Counter()
    for t,s in terms:c[tuple(sorted(t))]+=s
    return {t:s for t,s in c.items() if s}
records=[]
for n in range(6,9):
    all_t=set(ts(tuple(range(n))));count=0;example=None
    for i in range(n):
        for j in range(i+2,n):
            if i==0 and j==n-1:continue
            cut=(i,j)
            a=ts(tuple(range(i,j+1)))
            b=ts(tuple(range(j,n))+tuple(range(i+1)))
            for left,right in [(a,b),(b,a)]:
                flips=[(x,y) for x,y in combinations(left,2) if len(x^y)==2]
                contexts=[(x,y) for x,y in combinations(right,2) if len(x^y)==2]
                for l0,l1 in flips:
                    for r0,r1 in contexts:
                        t00=l0|r0|{cut};t10=l1|r0|{cut}
                        t01=l0|r1|{cut};t11=l1|r1|{cut}
                        assert all(t in all_t for t in [t00,t10,t01,t11])
                        # (f11-f01)-(f10-f00) equals the facet mixed minor.
                        change=vector([(t11,1),(t01,-1),(t10,-1),(t00,1)])
                        minor=vector([(t00,1),(t11,1),(t10,-1),(t01,-1)])
                        assert change==minor and len(change)==4
                        count+=1
                        if example is None:
                            # f is a Kronecker function on t11, not triangle-additive input.
                            residual=change[tuple(sorted(t11))]
                            assert residual==1
                            example={'cut':cut,'terms':[{'triangulation':t,'coefficient':s} for t,s in minor.items()], 'kronecker_context_residual':residual}
    assert count>0
    records.append({'n':n,'certificates':count,'example':example})
result={'status':'passed','records':records,'scope':'All pairs of regional flips across every cut for n=6..8; integer formal identities, no coefficient ansatz.', 'identity':'context increment difference equals one signed facet minor'}
Path('research/nima/results/flip_context.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
