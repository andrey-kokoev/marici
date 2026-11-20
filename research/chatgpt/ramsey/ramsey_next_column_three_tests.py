"""Three next-column tests on the same labeled 20-address prefix. Requires SciPy."""
from itertools import combinations
from collections import Counter
from functools import lru_cache
import numpy as np
from scipy.optimize import linprog
from ramsey_37_pair_rotation_rule import build
from ramsey_delayed_address_move import moves

n=20; full=(1<<n)-1; rows=[r&full for r in build()[:n]]
_,_,legal=moves(rows)
ids=lambda m:[i for i in range(n) if (m>>i)&1]
sixes=[sum(1<<i for i in s) for s in combinations(range(n),6) if all(not(rows[i]>>j&1) for i,j in combinations(s,2))]
assert len(sixes)==74 and len(legal)==5
D=min((r^p).bit_count() for r in rows for p in legal)
print('minimum edits',D)
for i,r in enumerate(rows):
    for p in legal:
        if (r^p).bit_count()==D: print('row',i,'remove',ids(r&~p),'add',ids(p&~r),'previously missed',len([s for s in sixes if not s&r]))
@lru_cache(None)
def greedy(p):
    missed=[s for s in sixes if not s&p];eligible=[i for i in range(n) if not ((rows[i]|(1<<i))&p)]
    if not missed or not eligible:
        assert bool(not missed)==(p in legal);return Counter({(p,not missed):1})
    gain={i:sum((s>>i)&1 for s in missed) for i in eligible};best=max(gain.values());out=Counter()
    for i in eligible:
        if gain[i]==best:out.update(greedy(p|1<<i))
    return out
out=greedy(0);print('greedy terminal sets and path counts',[(ids(p),ok,v) for (p,ok),v in out.items()]);
A=np.array([[r>>j&1 for j in range(n)] for r in rows]);w,V=np.linalg.eigh(A);assert min(np.diff(w))>1e-8
hits=Counter();pairs=set()
for i,j in combinations(range(n),2):
    X=np.column_stack((V[:,i],V[:,j],np.ones(n)))
    for p in legal:
        y=np.array([1 if p>>v&1 else -1 for v in range(n)])
        sol=linprog(np.zeros(3),A_ub=-y[:,None]*X,b_ub=-np.ones(n),bounds=(None,None),method='highs')
        if sol.success:
            assert min(y*(X@sol.x))>.99;hits[p]+=1;pairs.add((i,j))
        else:assert sol.status==2
print('eigenvector pairs with successes',len(pairs),'separated columns',len(hits),'counts',[hits[p] for p in legal])
