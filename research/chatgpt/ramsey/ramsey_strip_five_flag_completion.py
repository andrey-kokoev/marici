"""Does each minimal cyclic-group certificate meet all three flag orbits? Compare orbit closure with ordinary perfect-matching completion to expose the extra C5 assumption."""
from collections import Counter
from ramsey_strip_partial_fivefold_frame import certificate_records,closures
from ramsey_strip_minimal_shared_constraints import allms
for n,o,m,G,certs in certificate_records:
 hist=Counter();sizes=Counter()
 for obs in certs:
    forced=frozenset().union(*(closures[G,e] for e in obs));sizes[len(forced)]+=1
    completions=sum(set(obs)<=M for M in allms);hist[len(forced),completions]+=1
    assert forced<=m
 print('source',n,o,'orbit closure sizes',dict(sizes),'closure size / unconstrained completions',dict(sorted(hist.items())))
