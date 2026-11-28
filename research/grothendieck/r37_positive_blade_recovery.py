"""Which positive blade observations alone identify record 2? No bound on extra blades."""
from itertools import combinations
from pysat.solvers import Solver
from r37_exchange_falsifier import a,blades,legal
X=range(6,22); E={e:i+1 for i,e in enumerate(combinations(X,2))}; B=sorted(tuple(sorted(s)) for s in blades(a)); C=[]
for (i,j),v in E.items():
    if a[i]&a[j]&63:C.append([-v])
for t in combinations(X,3):C.append([-E[e] for e in combinations(t,2)])
for k in range(1,8):
    for t in combinations(X,k):
        u=0
        for i in t:u|=a[i]&63
        if u.bit_count()<k:C.append([E[e] for e in combinations(t,2)])
C.append([-v if a[i]>>j&1 else v for (i,j),v in E.items()])
assert legal(a) and len(B)==10
with Solver(name='cadical195',bootstrap_with=C) as solver:
    wins=[]
    for k in range(11):
        for sub in combinations(range(10),k):
            units={-E[e] for i in sub for e in combinations(B[i],2)}
            if not solver.solve(assumptions=sorted(units)):wins.append(sub)
        if wins:break
    print('minimum positive count',k if wins else None,'number at minimum',len(wins),'first', [B[i] for i in wins[0]] if wins else None)
    if not wins:
        extras=[]; target=set(map(frozenset,B))
        while solver.solve(assumptions=sorted(units)):
            model=set(solver.get_model());g=a.copy()
            for (i,j),v in E.items():
                if bool(g[i]>>j&1)!=(v in model):g[i]^=1<<j;g[j]^=1<<i
            assert legal(g) and target<=blades(g);extras.append(blades(g)-target)
            solver.add_clause([-v if v in model else v for v in E.values()])
        from collections import Counter
        print('alternative extra blade counts',Counter(map(len,extras)))
        def hit(F,k):
            if not F:return []
            if not k:return None
            for s in sorted(min(F,key=len),key=lambda s:tuple(sorted(s))):
                tail=hit([f for f in F if s not in f],k-1)
                if tail is not None:return [sorted(s)]+tail
        for d in range(1,len(extras)+1):
            h=hit(extras,d)
            if h is not None:print('minimum negative selectors given all positives',d,h);break
        common=set.intersection(*extras);print('single negative selectors',len(common),'example',sorted(min(common,key=lambda s:tuple(sorted(s)))) if common else None)
