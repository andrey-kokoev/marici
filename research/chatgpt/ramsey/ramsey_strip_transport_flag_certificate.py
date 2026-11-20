"""How many source matching flags resolve the four group-coherent anchored transports? Test all flags and minimum subsets, not a chosen favorable example."""
from itertools import combinations
from collections import Counter
from ramsey_strip_intrinsic_fivefold_transport import records,long,action,moved
for n,o,m,S,coherent,correct in records:
    allowed={e:{p for p in coherent if moved({e},action(p))<=long} for e in m};hist=Counter(map(len,allowed.values()));print('source',n,o,'survivors after one flag',dict(sorted(hist.items())),'unique flags',sorted(e for e,v in allowed.items() if len(v)==1))
    for k in range(1,4):
        cert=[c for c in combinations(sorted(m),k) if len(set.intersection(*(allowed[e] for e in c)))==1]
        if cert:break
    print('minimum flags',k,'certificates',len(cert),'entry/exit flag counts',[(e,len(allowed[e])) for e in sorted(m) if 0 in e or 29 in e]);assert all(correct in v for v in allowed.values())
