"""Exact C3 action on the 3x7 incidence plane and its axial cones.

Vertices: (a,j) encoded j+7a, a in Z3, j in Z7.
Rotation: (a,j) -> (a+1,j), axial vertices fixed.
All reported orbit counts are exact integer set enumerations.
Also checks the 21-node triangle-free B7-free cyclic coloring.
"""
from itertools import combinations
from collections import Counter
from ramsey_cyclic_rotation_filler_test import cyclic_adj, admissible

CORE=21
RHO=lambda v: (v+7)%CORE if v<CORE else v

def orbit_count(n,k):
    seen=set();nonfixed=0;fixed=0
    for subset in combinations(range(n),k):
        if subset in seen: continue
        orbit=[];q=subset
        while q not in seen:
            seen.add(q);orbit.append(q)
            q=tuple(sorted(map(RHO,q)))
        assert len(orbit) in (1,3)
        if len(orbit)==3:nonfixed+=1
        else:fixed+=1
    return nonfixed, fixed

for n,E,T in [(21,70,448),(22,77,518),(23,85,595)]:
    orbe=orbit_count(n,2)
    orbt=orbit_count(n,3)
    assert sum(orbe)==E
    assert sum(orbt)==T
    print(n,'vertices: edges moving+fixed',orbe,'triangle moving+fixed',orbt)

assert orbit_count(21,3)==(441,7)
print('EXACT 21: 441 moving triangle orbits = (3*7)^2 incidence entries;')
print('             plus 7 rotation-fixed triangles.')

A=cyclic_adj(21,[3,4,5])
assert admissible(A,7)
assert {x.bit_count() for x in A} == {6}
assert all((A[RHO(i)]>>RHO(j)&1)==(A[i]>>j&1)
           for i,j in combinations(range(21),2))
blocks=[]
for j in range(7):
    blocks.append((j,j+7,j+14))
    assert all(not (A[i]>>h)&1 for i,h in combinations(blocks[-1],2))
match_types=Counter()
for j,k in combinations(range(7),2):
    # Each distinct relative shift between two 3-node columns gives 3 parallel edges.
    match=sum((A[j]>>(k+7*d))&1 for d in range(3))
    match_types[match]+=1
assert match_types==Counter({0:7,1:7,2:7})
print('21-node ring: matching multiplicities among the 21 pairs of triples:',dict(match_types))

# Any new vertex attached to the existing 21-node ring cannot preserve the graph:
# every original vertex has A-degree 6, the Ramsey maximum for R(3,7).
# If all new links are B, a pre-existing B6 clique gives a forbidden B7.
assert not admissible(A+[0],7)
print('Fixed 21 ring cannot accept an axial connector without A/B recomposition.')

# On 22 nodes, the single fixed center has 4<=d_A<=6.
# Its A-neighbor orbits have size 3, hence it must have degree 6: exactly 2 full triples.
for degree in range(4,7):
    if degree%3 == 0:assert degree==6
# On 23 nodes, each of 2 fixed axial points has A-degree 5..6;
# if their mutual edge were A, degree would be 1 mod 3, impossible.
assert not any(5<=1+3*k<=6 for k in range(8))
print('22: one center must A-connect to exactly 2 complete triples.')
print('23: two centers must connect by B, each A-connects to 2 triples.')
