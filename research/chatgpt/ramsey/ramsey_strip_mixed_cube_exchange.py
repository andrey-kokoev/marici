"""Enumerate type-exchanging symmetries of the two literal cubes plus their cross-incidences. Outward and return cube identifications are chosen independently; reciprocity is not assumed."""
from itertools import permutations
from collections import Counter
from ramsey_strip_mixed_cube_incidence import P,T
from ramsey_strip_matching_restart import r
U=[i for i,d in enumerate(P) if len(set(d)&set(P[0]))==1];V=[j+15 for j,t in enumerate(T) if not T[14]&t];E=lambda i,j:not set(P[i])&set(P[j]);F=lambda i,j:len(T[i-15]&T[j-15])==1;cross=lambda i,j:P[i] in T[j-15]
isos=[]
for dest in permutations(V):
 g=dict(zip(U,dest))
 if all(E(i,j)==F(g[i],g[j]) for i in U for j in U) and all(g[r[i]]==r[g[i]] for i in U):isos.append(g)
ans=[]
for g in isos:
 for h in isos:
    inv={v:u for u,v in h.items()};a=g|inv
    if not all(cross(i,j)==cross(a[j],a[i]) for i in U for j in V):continue
    assert all(a[a[x]]==x for x in a) or all(a[a[x]]==r[x] for x in a)
    ans.append(a)
print('cube maps commuting with row swap',len(isos),'mixed incidence exchanges',len(ans));print('with directed boundary 16 -> 7',Counter('identity' if all(a[a[x]]==x for x in a) else 'row swap' for a in ans if a[16]==7));print('port actions',[tuple(a[i] for i in (16,17,4,7)) for a in ans])
