"""Exact relative-scale and power-class certificates for rational weights."""
import json
from pathlib import Path
from fractions import Fraction as F
from math import prod
p=json.loads(Path('research/nima/results/local_global_torus_lattice.json').read_text())
assert p['status']=='passed'
T=[frozenset(tuple(e) for e in t) for t in p['triangulations']]
C=sorted(set().union(*T))
flips=[]
for i,a in enumerate(T):
    for j in range(i+1,len(T)):
        b=T[j]
        if len(a^b)==2:flips.append((i,j,next(iter(a-b)),next(iter(b-a))))
def recover(w,root,reverse=False):
    r={root:F(1)}
    edges=list(reversed(flips)) if reverse else flips
    while True:
        size=len(r)
        for i,j,x,y in edges:
            ratio=w[j]/w[i]
            if x in r and y not in r:r[y]=r[x]*ratio
            if y in r and x not in r:r[x]=r[y]/ratio
        if len(r)==size:break
    assert len(r)==len(C)
    residuals=[w[j]/w[i]-r[y]/r[x] for i,j,x,y in flips]
    if any(residuals):return None
    a=[w[i]/prod(r[e] for e in t) for i,t in enumerate(T)]
    assert len(set(a))==1
    return r,a[0]
scales={c:F(i+2) for i,c in enumerate(C)}
w=[prod(scales[e] for e in t) for t in T]
records=[]
for multiplier in [1,2]:
    values=[multiplier*x for x in w]
    for root in C:
        r,a=recover(values,root)
        assert recover(values,root,True)==(r,a)
        assert r=={c:scales[c]/scales[root] for c in C}
        assert a==multiplier*scales[root]**3
    records.append({'multiplier':multiplier,'power_class_representative':multiplier,'roots_checked':len(C),'rational_recoverable':multiplier==1})
# A local triangle-factor input need not pass the crossing-graph consistency test.
q=(0,1,3)
boundary={tuple(sorted((i,(i+1)%6))) for i in range(6)}
from itertools import combinations
bad=[F(2) if all(e in t|boundary for e in combinations(q,2)) else F(1) for t in T]
assert recover(bad,C[0]) is None
result={'status':'passed','cases':records,'local_triangle_input_rejected':True,'criterion':'all flip ratios admit relative channel potentials, then a is an (n-3)rd power in the coefficient field','scope':'Six-point rational examples; path-order and root checks; multiplier two fails by v_2 modulo three.'}
Path('research/nima/results/field_channel_recovery.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
