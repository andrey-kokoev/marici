"""An old-link path parity rule. Degrees select a candidate, not a required completion."""
from itertools import combinations
from collections import Counter
from ramsey_37_pair_rotation_rule import build
from ramsey_difference_next_round import add
from pauli_realization_audit import triangle_free, independent_witness

def propose(r):
    d=[x.bit_count() for x in r];V=range(len(r));S={i for i in V if d[i]==5}
    if not S or set(d)-{4,5,6}:return
    stack=[min(S)];side={stack[0]:0}; deg={i:sum(r[i]>>j&1 for j in S) for i in S}
    while stack:
        i=stack.pop()
        for j in S:
            if not r[i]>>j&1:continue
            if j in side:
                if side[i]==side[j]:return
            else:side[j]=1-side[i];stack.append(j)
    if set(side)!=S:return
    halves=[{i for i in S if side[i]==b} for b in (0,1)]
    halves.sort(key=lambda h:sum(deg[i]==1 for i in h),reverse=True)
    if sum(deg[i]==1 for i in halves[0])==sum(deg[i]==1 for i in halves[1]):return
    common={i for i in V if d[i]==4};p,q=[sum(1<<i for i in h|common) for h in halves];return p,q,halves

if __name__=='__main__':
    g=build();counts=Counter()
    for u,v in combinations(range(22),2):
        L=[i for i in range(22) if i not in (u,v)];proj=lambda r:sum((r>>j&1)<<i for i,j in enumerate(L));r=[proj(g[i]) for i in L];result=propose(r)
        if result is None:counts['no prediction']+=1;continue
        p,q,H=result;valid=[]
        for e in (0,1):
            child=add(add(r,p),q|(e<<20));
            if triangle_free(child) and independent_witness(child,7) is None:valid.append(e)
        counts['valid' if valid else 'invalid']+=1
        if (u,v)==(20,21):print('10,01:',[sorted(h) for h in H],'allowed mutual bits',valid)
    print(counts)
