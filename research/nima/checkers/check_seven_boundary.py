"""Bounded-cardinality boundary support search, no division at zeros."""
import json
from pathlib import Path
from itertools import combinations
p=json.loads(Path('research/nima/results/seven_point_fibers.json').read_text())
g=json.loads(Path('research/nima/results/seven_groebner.json').read_text())
assert p['status']=='passed' and g['status']=='complete'
T=[set(tuple(e) for e in t) for t in p['triangulations']]
bd={tuple(sorted((i,(i+1)%7))) for i in range(7)}
Q=list(combinations(range(7),3))
F=[sum(1<<j for j,q in enumerate(Q) if all(e in t|bd for e in combinations(q,2))) for t in T]
moves=[(sum(1<<i for i,e in enumerate(a) if e),sum(1<<i for i,e in enumerate(b) if e)) for a,b in g['basis']]
records=[];witness=None
for size in range(5):
    tested=admitted=0
    for ids in combinations(range(42),size):
        tested+=1;mask=sum(1<<i for i in ids)
        if not all((mask&a==a)==(mask&b==b) for a,b in moves):continue
        admitted+=1;allowed=0
        for i in ids:allowed|=F[i]
        closure=[i for i,f in enumerate(F) if f&allowed==f]
        if closure!=list(ids):
            witness={'positive_indices':ids,'forced_extra_indices':sorted(set(closure)-set(ids)),'allowed_triangle_indices':[i for i in range(35) if allowed>>i&1]};break
    records.append({'size':size,'tested':tested,'locally_admitted':admitted,'complete':witness is None})
    if witness:break
result={'status':'passed','records':records,'witness':witness,'scope':'Search through support cardinality four, stopping at first closure defect; no claim for larger supports if none found.'}
Path('research/nima/results/seven_boundary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
