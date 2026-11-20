"""Conditional model: each port carries a set of segment identifiers.
Within each pair count the union once. Across the two pairs add the counts.
This tests local comparison counts, not distinct Ramsey addresses.
"""
from itertools import product
# ports: wa, bb, aa, wb; exchange 2 and 3
pairings=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
contributions={tuple(sum(bool(s&(1<<a|1<<b)) for a,b in pairing) for pairing in pairings) for s in range(1,16)}
assert all(3*f<=2*(u+v) for f,u,v in contributions)
reach={(0,0,0)};todo=list(reach)
while todo:
    t=todo.pop()
    for c in contributions:
        v=tuple(x+y for x,y in zip(t,c))
        if sum(v)<=20 and v not in reach:reach.add(v);todo.append(v)
print('local 8,6,6 feasible:',(8,6,6) in reach)
print('total 15, exchanged counts equal:',sorted(t for t in reach if sum(t)==15 and t[1]==t[2]))
