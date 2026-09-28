"""Finite construction of the proposed 12*(12^2+3^2) slot domain.

Counts only: no proton/electron identification or energy operator assumed.
Carriers have identified labels 0..3 and shared reference label 0.
Writes no files.
"""
from itertools import permutations, product
from fractions import Fraction as F

X=tuple(range(4))
E=tuple((i,j) for i in X for j in X if i!=j)
remaining=tuple(i for i in X if i!=0)
slots=[('arrow',a,b) for a,b in product(E,E)]
slots += [('state',a,b) for a,b in product(remaining,remaining)]
assert len(E)==12 and len(slots)==153 and len(set(slots))==153
expanded=list(product(E,slots))
assert len(expanded)==1836 and len(set(expanded))==1836

def orbit(edge, group):
    return {(p[edge[0]],p[edge[1]]) for p in group}

full=list(permutations(X))
rooted=[p for p in full if p[0]==0]
assert len(orbit((0,1),full))==12
outgoing=orbit((0,1),rooted)
incoming=orbit((1,0),rooted)
internal=orbit((1,2),rooted)
assert (len(outgoing),len(incoming),len(internal))==(3,3,6)
assert outgoing|incoming|internal==set(E)
assert not(outgoing&incoming or outgoing&internal or incoming&internal)
# Symmetry allows unequal weights on the three rooted edge orbits.
def total(a,b,c): return 153*(3*a+3*b+6*c)
assert total(F(1),F(1),F(1))==1836
assert total(F(1),F(1),F(2))==2754
print('One shared-reference comparison: 144 arrow pairs + 9 remaining-state pairs =153.')
print('Twelve labelled outer directed relationships: 1836 slots.')
print('Fixed-reference stabilizer orbits: outgoing=3, incoming=3, internal=6.')
print('Weighted sum=153*(3*w_out+3*w_in+6*w_internal).')
print('Uniform weights give1836; rooted symmetry alone permits unequal weights.')
print('Exact slot and orbit checks passed. Particle/energy assignment remains unspecified.')
