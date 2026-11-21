"""Exact SAT attachment test for the five deletion distances surviving capacity."""
from itertools import combinations
from pysat.solvers import Solver
from ramsey_mutual_repair_conjecture import sevens
A=[sum(1<<z for z in {(v+s*d)%38 for s in (1,-1) for d in (1,3,5,12,19)}) for v in range(38)]
for d in (1,2,5,7,19):
    keep=[v for v in range(38) if v not in (0,d)];B=[sum(1<<j for j,v in enumerate(keep) if A[u]>>v&1) for u in keep]+[0]*3;E=list((i,j) for j in range(36,39) for i in range(j) if i>=36 or B[i].bit_count()<9);ids={e:k+1 for k,e in enumerate(E)}
    with Solver(name='cadical195') as s:
        for i in range(36):
            opts=[k for (a,b),k in ids.items() if a==i];
            for sub in combinations(opts,10-B[i].bit_count()):s.add_clause([-x for x in sub])
        for U in combinations(range(39),3):
            es=list(combinations(U,2))
            if all(e in ids or B[e[0]]>>e[1]&1 for e in es):s.add_clause([-ids[e] for e in es if e in ids])
        for I in sevens(B[:36],k=9):
            for j in range(36,39):s.add_clause([k for (a,b),k in ids.items() if b==j and I>>a&1])
        count=0
        while s.solve():
            pos=set(s.get_model());C=B[:]
            for (a,b),k in ids.items():
                if k in pos:C[a]|=1<<b;C[b]|=1<<a
            bad=next(sevens(C,k=10),None)
            if bad is None:print('witness',d,C);break
            s.add_clause([k for (a,b),k in ids.items() if bad>>a&bad>>b&1]);count+=1
        else:print('excluded',d,'extra ten cuts',count)
