"""Hand-checkable seven witnesses and a degree count for the shared frame twins."""
from itertools import combinations
from ramsey_shared_frame_reconstruction import T,allowed,degree
X,Y=10,11
# For each label v, four companion labels (including the twins) and two points
# leave v-X or v-Y as the only way to hit this seven.
certs=[('a','ae','ace','bd'),('b','be','bdf','ac'),
       ('c','cf','ace','bd'),('d','df','bdf','ac'),
       ('ab','ae','be','cd'),('cd','cf','df','ab')]
for v,h,j,p in certs:
    U=[T.index(t) for t in (v,h,j)]+[X,Y];assert all(set(p).isdisjoint(T[i]) for i in U)
    possible={frozenset((i,k)) for i,k in combinations(U,2) if k in allowed[i]}
    assert possible=={frozenset((U[0],t)) for t in (X,Y)}
anchor=T.index('abcd');assert allowed[anchor]=={X,Y} and degree[anchor]==2
assert sum(degree[t]-1 for t in (X,Y))==len(certs)
# Four points plus two singletons and their union label force each singleton edge.
for v,w,p in [('a','b','cdef'),('c','d','abef')]:
    i,j,k=map(T.index,(v,w,v+w));assert all(set(p).isdisjoint(T[z]) for z in (i,j,k))
    assert j in allowed[i] and k not in allowed[i]|allowed[j]
print('Six separate lower bounds exhaust six twin slots; triangles split both singleton pairs. One remaining slot per twin splits ab and cd.')
