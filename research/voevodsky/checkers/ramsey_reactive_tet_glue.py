"""Candidate center composition: union named directed comparisons, final absence OR."""
from itertools import combinations,product
from pathlib import Path
import json

# Incidence keys (direction, labeled R,B slots). Gluing overlapping regions
# identifies a comparison by key. A center returns a function, not a snapshot.
def center(region):
    return lambda other: center(region|other) if other is not None else lambda net: resolve(region,net)

def resolve(region,net):
    hits={side for key in region if net(key) for side in [key[0]]}
    return ('R' not in hits) or ('B' not in hits)

def subsets(xs):return [frozenset(p) for k in range(len(xs)+1) for p in combinations(xs,k)]

def run():
    keys=[(s,i,j) for s in 'RB' for i,j in ((0,0),(1,1))];regions=subsets(keys);tested=0
    for left,right,on in product(regions,repeat=3):
        calls=[]
        def net(key):calls.append(key);return key in on
        got=center(left)(right)(None)(net);assert set(calls)==left|right and len(calls)==len(set(calls));assert got==resolve(left|right,lambda k:k in on);tested+=1
    # Abstract terminal cases: every directional support subset is realizable;
    # contexts can supply neither, just R, just B, or both. No clock/order.
    cases=subsets('RB');rows={''.join(sorted(a)) or 'none':[len(a|c)<2 for c in cases] for a in cases};assert len({tuple(v) for v in rows.values()})==4
    out=dict(scope='presence of a positive response; union of incidence keys; fixed terminal net when comparing restrictions; contexts can supply either direction separately',checks=tested,context_order=['none','R','B','RB'],terminal_OR_by_local_support=rows);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_reactive_tet_glue.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
