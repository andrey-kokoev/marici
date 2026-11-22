"""cells control: verify the missing around-corner relation on every actual sector. Independent of the walk-length schedule and any Ramsey graph."""
from pathlib import Path
import json
D=Path(__file__).parent;T={t['outer_arrow']:t['triangle'] for t in json.loads((D.parents[1]/'nima/results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports']};E=sorted(T);F={e:next(k for k,v in T.items() if v[0]==T[e][0] and k[0]==e[1]) for e in E}
def act(e,word):
    for w in word:e=F[e] if w=='F' else e[::-1]
    return e
for w in ('FFF','SS','SFSFSF'):assert all(act(e,w)==e for e in E)
todo=[''];perms={};
while todo:
    w=todo.pop(0);p=tuple(act(e,w) for e in E)
    if p not in perms:perms[p]=w;todo.extend((w+'F',w+'S'))
assert len(perms)==len({p[0] for p in perms})==12;r=dict(relations=['F^3','S^2','(SF)^3'],permutation_group=len(perms),orbit=12,representatives=list(perms.values()));print(r);(D/'ramsey_sector_gluing_relations.json').write_text(json.dumps(r)+'\n')
