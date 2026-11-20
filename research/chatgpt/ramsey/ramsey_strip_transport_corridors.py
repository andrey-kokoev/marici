"""Explain the gate+middle recognition test by splitting at the middle edge. Count locally possible reflected-compatible paired corridors (not assumed reflected inside), before checking collisions across left and right corridors."""
from collections import defaultdict,Counter
from ramsey_strip_transport_recognition import paths,r,s,t
K=(1,5,6,10);pool=defaultdict(set)
for p in paths:pool[tuple(p[i] for i in K)].add(p)
H=Counter();mixed=Counter();example=None
for k,S in pool.items():
 mirror=tuple(r[v] for v in k)
 if k>=mirror or mirror not in pool or any(x==r[x] for x in k):continue
 # use both paths in first-sheet coordinates; disjointness across copies is checked explicitly
 A={p[1:6] for p in S};B={p[6:11] for p in S}
 def legal(X):return [(x,y) for x in X for y in X if set(x).isdisjoint(r[v] for v in y)]
 L=legal(A);R=legal(B)
 for a,c in L:
    for b,d in R:
        P=(s,)+a+b+(t,);Q=(s,)+c+d+(t,);diag=(a==c,b==d)
        if P not in S or Q not in S:why='own path repeats'
        elif not set(a+b).isdisjoint(r[v] for v in c+d):why='opposite corridors collide'
        else:why='valid';assert all(diag)
        H[diag,why]+=1
        if not all(diag) and example is None:example=(k,a,c,b,d,why)
 if L and R:mixed[(len(L),len(R))]+=1
print('corridor pair classes',H,'local sizes',mixed,'example',example)
