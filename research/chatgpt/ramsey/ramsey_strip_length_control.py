"""Change only half-route length. Keep original four pole pairs, swap, frozen profile selectors and actual residual matching test. Identify a path with its reflected copy."""
from ramsey_strip_closure_control import N,r,fixed,fill,rules,dist,out
from pathlib import Path
from collections import Counter
import json
bridges={}  # keyed by ordered endpoints
for z in out:bridges[z['path'][0],z['path'][-1]]=z['bridge'][0]
records=[]
def walk(p,used):
    for y in sorted(N[p[-1]]-used):
        if len(p)==1 and y>=r[y]:continue
        if y not in fixed:
            walk(p+[y],used|{y,r[y]});continue
        bridge=bridges.get((p[0],y));
        if not bridge:continue
        counts=[sum(tuple(dist[x][i] for i in bridge) in rule for x in p[1:]) for rule in rules];closes=next(fill(set(range(30))-used-{y}),None) is not None
        records.append(dict(path=p+[y],length=len(p),counts=counts,closes=closes))
for s in sorted({s for s,t in bridges}):walk([s],{s})
assert {(tuple(z['path']),z['closes'],tuple(z['counts'])) for z in records if z['length']==11}=={(tuple(z['path']),z['closes'],tuple(map(len,z['selected']))) for z in out}
for k in sorted({z['length'] for z in records}):print(k,Counter((tuple(z['counts']),z['closes']) for z in records if z['length']==k))
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
