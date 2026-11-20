"""Input k only: greedy cycle construction and complete cyclic-class audit for (3,k).
No catalogues or saved matrices. Standard library. Output CSV is an audit witness.
"""
import sys
from itertools import combinations
from math import comb
from pathlib import Path
from pauli_realization_audit import triangle_free, independent_witness


def audit(k):
    bound=comb(k+1,2)-1  # elementary Ramsey recurrence R(3,k)<=binom(k+1,2)
    greedy_best=best=0;stats={}
    for n in range(1,bound+1):
        full=(1<<n)-1
        def rot(m,d):return ((m<<d)|(m>>(n-d)))&full
        def jumps(ds):return {v for d in ds for v in (d,n-d)}
        def ok(S):return not any((x+y)%n in S for x in S for y in S)
        def witness(S):
            m=sum(1<<s for s in S);rows=[rot(m,i) for i in range(n)]
            # By translation any independent k-set can be moved to contain zero.
            if independent_witness(rows,k-1,full&~(m|1)) is not None:return None
            assert triangle_free(rows) and independent_witness(rows,k) is None
            return rows
        g=set()
        for d in range(1,n//2+1):
            s=g|jumps([d]);
            if len(s)<k and ok(s):g=s
        if witness(g) is not None:greedy_best=n;greedy_jumps=sorted(s for s in g if s<=n//2)
        checked=valid=0; first=None
        for anti in ([False,True] if n%2==0 else [False]):
            for r in range(min((n-1)//2,(k-1-int(anti))//2)+1):
                for ds in combinations(range(1,(n+1)//2),r):
                    S=jumps(ds)
                    if anti:S.add(n//2)
                    if not ok(S):continue
                    checked+=1;rows=witness(S)
                    if rows is not None:
                        valid+=1
                        if first is None:first=(sorted(s for s in S if s<=n//2),rows)
        stats[n]=(checked,valid)
        if first:best=n;offsets,bestrows=first
    path=Path(__file__).with_name(f'ramsey_3_{k}_target_only_cyclic_{best}.csv');path.write_text(''.join(','.join(str(row>>i&1) for i in range(best))+'\n' for row in bestrows))
    print('greedy',greedy_best,greedy_jumps,'best across cyclic class',best,offsets,'upper scan bound',bound)
    print('n: (triangle-free tables within degree cap, valid tables)',{n:c for n,c in stats.items() if n>=best-1})

if __name__=='__main__':audit(int(sys.argv[1]) if len(sys.argv)>1 else 10)
