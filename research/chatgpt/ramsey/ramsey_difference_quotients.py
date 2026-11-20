"""Compare fixed, label-independent partitions. Search legal unions on quotient directly."""
from collections import defaultdict
from itertools import combinations
from ramsey_37_pair_rotation_rule import build
from ramsey_delayed_address_move import moves

if __name__=='__main__':
 n=20; V=range(n); full=(1<<n)-1; rows=[r&full for r in build()[:n]]; d=[r.bit_count() for r in rows]; legal=set(moves(rows)[2]); assert len(legal)==5
 N=[[j for j in V if r>>j&1] for r in rows]; six=[sum(1<<j for j in t) for t in combinations(V,6) if all(not(rows[i]>>j&1) for i,j in combinations(t,2))]
 diff=[[d[i]-d[j] for j in N[i]] for i in V]; hist=[tuple(sorted(x*x for x in ds)) for ds in diff]; energy=[sum(h) for h in hist]; twostep=[sum((energy[i]-energy[j])**2 for j in N[i]) for i in V]
 for name,keys in [('sum of squares',energy),('square of sum',[sum(ds)**2 for ds in diff]),('sorted squares',hist),('sorted signed differences',[tuple(sorted(ds)) for ds in diff]),('two rounds',list(zip(energy,twostep)))]:
    buckets=defaultdict(int)
    for i,key in enumerate(keys):buckets[key]|=1<<i
    hits=[]; tested=0
    def visit(items,p):
        global tested
        if not items:
            tested+=1
            if all(p&s for s in six):hits.append(p)
            return
        g,*rest=items;visit(rest,p)
        if all(not(rows[i]&(p|g)) for i in V if g>>i&1):visit(rest,p|g)
    visit(list(buckets.values()),0)
    assert set(hits)=={p for p in legal if all(p&g in (0,g) for g in buckets.values())}
    print(name,len(buckets),tested,len(hits),[[i for i in V if p>>i&1] for p in hits[:1]])
