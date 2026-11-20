"""Does the canonical three-layer frame provide a reciprocal dictionary? Compare its half-cycle shift with endpoint-duality factorizations, recording layer mixing."""
from collections import Counter
from ramsey_strip_layer_quarter_turn import C,M,D,N,r
from ramsey_strip_seed_half_swap import action,h
from ramsey_strip_ordered_boundary_dualities import solutions,entry,exit
H=action(h);J=[H.index(i) for i in range(30)];shift=list(range(30));layer={v:k for k,L in enumerate((C,M,D)) for v in L}
for L in (C,M,D):
 for i,v in enumerate(L):shift[v]=L[(i+5)%10]
assert all({shift[y] for y in N[x]}==N[shift[x]] and shift[shift[x]]==x for x in range(30));assert shift[0]==29 and shift[29]==0
for f in solutions:
    dictionary=[f[J[i]] for i in range(30)];reciprocal=all(dictionary[dictionary[i]]==i for i in range(30));profile=[dict(Counter(layer[dictionary[v]] for v in L)) for L in (C,M,D)]
    print('port bits',exit.index(f[entry[0]]),entry.index(f[exit[0]]),'reciprocal',reciprocal,'dictionary layer destinations',profile,'endpoint map is half-cycle shift',all(f[x]==shift[x] for x in range(30)))
