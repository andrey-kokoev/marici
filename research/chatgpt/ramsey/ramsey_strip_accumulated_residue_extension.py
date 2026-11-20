"""Can accumulated shared residues be preserved by any Hall matching, even outside the five-strip family? Full perfect matching search and Hall-deficit certificates."""
from itertools import combinations
from ramsey_strip_residue_progress import C,ids
from ramsey_strip_matching_restart import P,T
N={i:{j for j,t in enumerate(T,15) if p in t} for i,p in enumerate(P)}
def test(chosen):
    fixed=set.union(*(set(C[i]) for i in chosen));used={v for e in fixed for v in e};left=set(range(15))-used;right=set(range(15,30))-used
    def count(L,R):
        if not L:return 1
        i=min(L,key=lambda i:len(N[i]&R));return sum(count(L-{i},R-{j}) for j in N[i]&R)
    n=count(left,right);witness=None
    if not n:
        for k in range(1,len(left)+1):
            for S in combinations(sorted(left),k):
                reach=set.union(*(N[i]&right for i in S))
                if len(reach)<k:witness=(S,sorted(reach));break
            if witness:break
        assert witness
    print('preserve tracks',chosen,'fixed links',len(fixed),'full matching completions',n,'deficit witness',witness)
    return n
for k in (1,2,3):
    for chosen in combinations(ids,k):test(chosen)
