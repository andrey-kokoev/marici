"""Exact Boolean algebra of the three probes, learned from the verified eight outputs; report symmetries, algebraic degrees and verify reconstruction."""
from pathlib import Path
from collections import Counter,defaultdict
import json
D=Path(__file__).parent;R=json.loads((D/'ramsey_seven_all_wirings.json').read_text());S=R['address_masks'];E=list(map(tuple,R['edge_order']));code=lambda w:sum((w>>i&1)<<j for j,i in enumerate((0,4,6)));W=sorted(R['wirings'],key=code);assert list(map(code,W))==list(range(8))
def poly(T):
    a=T[:]
    for b in [1,2,4]:
        for i in range(8):
            if i&b:a[i]^=a[i^b]
    return tuple(i for i,v in enumerate(a) if v)
def fmt(p):return '+'.join(('1','x','y','xy','z','xz','yz','xyz')[i] for i in p) or '0'
def act(swaps):
    p=list(range(7))
    for u,v in swaps:p[u],p[v]=p[v],p[u]
    m=[S.index(sum(1<<p[i] for i in range(7) if s>>i&1)) for s in S];es=[E.index(tuple(sorted((m[u],m[v])))) for u,v in E];out=[sum((w>>i&1)<<v for i,v in enumerate(es)) for w in W];assert set(out)==set(W);return list(map(code,out))
gens=[act(s) for s in [[(0,1),(2,3)],[(0,1),(4,5)],[(2,4),(3,5)]]];fun=lambda perm:[fmt(poly([i>>j&1 for i in perm])) for j in range(3)];polys=[poly([w>>i&1 for w in W]) for i in range(80)];assert all(sum((sum(1 for t in p if t&k==t)%2)<<i for i,p in enumerate(polys))==W[k] for k in range(8));out=dict(generators=list(map(fun,gens)),functions=dict(Counter(map(fmt,polys))),edge_formulas=list(map(fmt,polys)));print(out['generators']);print(out['functions']);(D/'ramsey_seven_transport_algebra.json').write_text(json.dumps(out)+'\n')
