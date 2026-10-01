"""Exact static charge-response audit on the four-state carrier graph.

This is a trial scalar potential/charge interface, not Maxwell theory.
The zero-source comparison equilibrium fixes relative mismatch variances;
it contains no source-coupling or field-stiffness parameter.
"""
from fractions import Fraction as F

N=4
L=[[F(4*(i==j)-1) for j in range(N)] for i in range(N)]
# Moore-Penrose inverse on the zero-sum subspace.
G=[[F(i==j,4)-F(1,16) for j in range(N)] for i in range(N)]

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def mv(A,x): return [dot(row,x) for row in A]

assert mv(L,[F(1)]*N) == [0]*N
j=[F(1),F(-1),F(0),F(0)]
assert mv(L,mv(G,j)) == j
print('kappa | source coupling g | positive field energy for j=(1,-1,0,0)')
for kappa,g in ((F(1),F(1)),(F(1),F(2)),(F(2),F(1))):
    phi=[g*x/kappa for x in mv(G,j)]
    assert [kappa*x for x in mv(L,phi)] == [g*x for x in j]
    field_energy=kappa*dot(phi,mv(L,phi))/2
    assert field_energy == g*g/(4*kappa)
    shifted=[x+F(7) for x in phi]
    assert dot(shifted,mv(L,shifted)) == dot(phi,mv(L,phi))
    assert dot(j,shifted) == dot(j,phi)
    print(f'{kappa} | {g} | {field_energy}')
# Relative response weights are unchanged by a common readout gain.
for gain in (F(1),F(2),F(1,137)):
    variances=[gain*gain]*137
    assert all(v/sum(variances) == F(1,137) for v in variances)
# Every distinct pair has equal resistance: graph has no derived spatial1/r.
for a in range(N):
    for b in range(a+1,N):
        charge=[F((i==a)-(i==b)) for i in range(N)]
        assert dot(charge,mv(G,charge)) == F(1,2)
print('All parameter choices preserve common-potential shift symmetry and normalized comparison share1/137.')
print('Physical charge-response coefficient g^2/kappa remains free.')
print('All six distinct graph pairs have the same resistance1/2; no spatial Coulomb law is constructed.')
