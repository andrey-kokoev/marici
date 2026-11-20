"""Test worst-set slack. Look for terminal conflicts of two still-live obligations."""
from collections import Counter
from itertools import combinations
from ramsey_37_blind_tie_rules import run

def diagnose(rows):
    n=len(rows);I=[0];a=[0]*n
    for j,p in enumerate(rows):
        assert p in I;I += [s|1<<j for s in I if not p&s];a[j]|=p
        for i in range(j):a[i]|=(p>>i&1)<<j
    assert max(s.bit_count() for s in I)==6
    live=sum(1<<i for i,r in enumerate(a) if r.bit_count()<6);sets=[s for s in I if s.bit_count()==6];req=[s&live for s in sets];assert not any(all(s&p for s in sets) for p in I)
    if 0 in req:return 'empty',None
    for i,j in combinations(range(len(req)),2):
        if not any(p&req[i] and p&req[j] for p in I):return 'pair',(sets[i],req[i],sets[j],req[j])
    return 'three or more',None

if __name__=='__main__':
    sizes=Counter();causes=Counter();example=False
    for seed in range(40):
        r=run('slack',seed,trace=True);c,detail=diagnose(r);sizes[len(r)]+=1;causes[c]+=1
        if detail and not example:
            print('seed,order,sets/live',seed,len(r),[[i+1 for i in range(len(r)) if p>>i&1] for p in detail]);example=True
    print(sizes,causes)
