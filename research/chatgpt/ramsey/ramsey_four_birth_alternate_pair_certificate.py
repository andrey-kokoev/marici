"""An exact 10+11 pair-obstruction normal form for four square-pair births.

No Ramsey catalogues, optimizers, or third-party libraries.
The 4-birth arrangement is fixed; two newborns are B-connected.
"""
from itertools import combinations
from ramsey_contact_normal_form_theorem import graph

PAIRS=((0,1),(2,3),(4,6),(5,7))
SELECTED=(0,2)
E,PORTS,_=graph(PAIRS)
I={3,5,8,9,15,16,22,23,26,28}
assert len(I)==10
assert {v^31 for v in I}==I
J={32+v for v in range(32) if v.bit_count()%2==0 and v not in I}
assert len(J)==11
W=I|J
assert len(W)==21
assert all(tuple(sorted((u,v)))not in E for u,v in combinations(W,2))
assert all(not(W&PORTS[b]) for b in SELECTED)
B23=sorted(W|{64,66})
assert len(B23)==23
assert all(tuple(sorted((u,v)))not in E for u,v in combinations(W,2))
print('Fixed oriented births:',PAIRS)
print('Pair of newborns B-connected:',SELECTED)
print('Lower antipodal witness:',sorted(I))
print('Upper parity witness:',sorted(J))
print('Forbidden B23:',B23)
print('Certificate: old 21-vertex common B-link, two new B-vertices, no A-edges.')
