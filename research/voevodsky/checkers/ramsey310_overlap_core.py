"""Find small red-only obstructions inside red neighborhoods of the stored parent."""
from itertools import combinations
from ramsey310_six_set_parent_test import base

# S of size r needs a common blue set of size 10-r. Use known R(3,10-r).
R={2:28,3:23,4:18,5:14,6:9,7:6,8:3,9:1}
best=None
for a in base:
    N=[i for i in range(39) if a>>i&1]
    for r in range(2,len(N)+1):
        need=10*r+R[r]-40
        for S in combinations(N,r):
            m=sum(1<<i for i in S)
            T=sorted(((x&m).bit_count()-1,i) for i,x in enumerate(base) if (x&m).bit_count()>=2)[::-1]
            kept=[];bonus=0
            for gain,i in T:
                kept.append(i);bonus+=gain
                if bonus>=need:break
            if bonus<need:continue
            assert any(base[i]&m==m for i in kept)
            key=(r+len(kept),sum((base[i]&m).bit_count() for i in kept),S,tuple(kept))
            if best is None or key<best:best=key
print(best)
if best:
    _,_,S,T=best
    print([(i,[j for j in S if base[i]>>j&1]) for i in T])
