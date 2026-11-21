"""Separate cores by sevens that do not depend on either twin's allocation."""
from ramsey_stripped_core import T,V,E,models,seed
from itertools import combinations
from collections import Counter
cores=list(models(seed,0));non_twin=V+[14];tests={}
for k in range(1,7):
    for U in combinations(non_twin,k):
        points=sorted(set('abcdef')-set(''.join(T[i] for i in U)))
        if len(points)<7-k and k!=6:continue
        # If k=6 the root always works; prefer points when possible.
        panel=points[:7-k] if len(points)>=7-k else ['root']
        clause=sum(E.get((i,j),E.get((j,i),0)) for i,j in combinations(U,2));fail=sum(1<<i for i,s in enumerate(cores) if not s&clause)
        if fail:tests.setdefault(fail,(panel,[T[i] for i in U]))
allbad=0
for f in tests:allbad|=f
print('surviving twin-free tests',len(cores)-allbad.bit_count(),'of',len(cores));print('survivor cross edges', [[(T[i],T[j]) for (i,j),b in E.items() if j<6 and i//2!=j//2 and b&s] for k,s in enumerate(cores) if not allbad>>k&1]);
assert len(cores)-allbad.bit_count()==2
for k,s in enumerate(cores):
    if allbad>>k&1:continue
    cross={e for e,b in E.items() if e[1]<6 and e[0]//2!=e[1]//2 and b&s}
    if cross:
        # b -- cd -- ab -- c -- a -- b; the two within-pair steps
        # are forced opposite by slot allocation, the other three by triangles.
        assert {(1,5),(2,4),(0,2)}<=cross
# Exact set cover on at most twenty cores, retain certificate list.
best={0:[]}
for f in tests:
    for m,path in list(best.items()):
        h=m|f
        if h not in best or len(path)+1<len(best[h]):best[h]=path+[f]
print('minimum twin-free basis',[(tests[f],f.bit_count()) for f in best[allbad]])
