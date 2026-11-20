"""Enumerate all mixed-cube exchanges without row constraints or named-port anchoring. Classify temporal orbits to test port-free nonreturn."""
from itertools import permutations
from collections import Counter
from ramsey_strip_mixed_cube_exchange import U,V,E,F,cross,r
isos=[]
for dest in permutations(V):
 g=dict(zip(U,dest))
 if all(bool(E(x,y))==bool(F(g[x],g[y])) for x in U for y in U):isos.append(g)
counts=Counter();maps=[]
for g in isos:
 for h in isos:
    a=g|{v:u for u,v in h.items()}
    if not all(cross(x,y)==cross(a[y],a[x]) for x in U for y in V):continue
    todo=set(a);sizes=[]
    while todo:
        x=min(todo);p=[]
        while x not in p:p.append(x);x=a[x]
        assert x==p[0];todo-=set(p);sizes.append(len(p))
    counts[tuple(sorted(sizes))]+=1;maps.append(a)
nonreturn=[a for a in maps if all(a[a[x]]!=x for x in a)];roots=[a for a in maps if all(a[a[x]]==r[x] for x in a)]
print('all cube isometries',len(isos),'full incidence exchanges',len(maps),'orbit types',counts);print('port-free no-two-step-return',len(nonreturn),'exact row-swap roots',len(roots),'same set',nonreturn==roots)
print('no-return maps satisfying directed row flag',sum(a[16]==7 for a in nonreturn))
