"""Replay all 17 unweighted support interval contradictions with integer arithmetic."""
from ramsey310_joint_separators import instances,D,json
from collections import Counter
certs={tuple(r['case']):r['cert'] for r in json.loads((D/'ramsey310_joint_small_sets.json').read_text())};sizes=Counter();directions=Counter()
for k,d,C in instances():
    r=certs.pop(k);U=r['vertices'];mask=sum(1<<v for v in U);loads=sorted((s&mask).bit_count() for s in C);a,b=sum(loads[:6]),sum(loads[-6:]);need=sum(d[v] for v in U)
    assert (need,a,b)==(r['need'],r['lo'],r['hi']) and not a<=need<=b
    sizes[len(U)]+=1;directions['over' if need>b else 'under']+=1
assert not certs and sum(sizes.values())==17
print(dict(sorted(sizes.items())),dict(directions))
