"""Centered witness projector as a charge candidate; exact rational matrices.
Uses the Euclidean metric on four carrier coordinates. No physical charge
normalization or carrier-to-matter lift is supplied. Writes no artifacts.
"""
from fractions import Fraction as F
N=4
I=tuple(tuple(F(i==j) for j in range(N)) for i in range(N))
P=tuple(tuple(F(i==0 and j==0) for j in range(N)) for i in range(N))
G=tuple(tuple(F(12 if i==j else 1) for j in range(N)) for i in range(N))
Y=tuple(tuple(P[i][j]-I[i][j]/4 for j in range(N)) for i in range(N))
def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(N)) for j in range(N)) for i in range(N))
def trace(a): return sum(a[i][i] for i in range(N))
assert trace(Y)==0
assert trace(mul(Y,Y))==F(3,4)
assert mul(Y,G)!=mul(G,Y)
# H has zero witness coordinate and sum zero among other coordinates.
for h in [(0,1,-1,0),(0,1,0,-1)]:
    assert tuple(sum(Y[i][j]*h[j] for j in range(N)) for i in range(N)) == tuple(-F(x)/4 for x in h)
c2=F(1,2)
assert c2/(c2+trace(mul(Y,Y)))==F(2,5)
# Primitive integral charges: multiply by four, eigenvalues 3,-1,-1,-1.
assert c2/(c2+16*trace(mul(Y,Y)))==F(1,25)
print('Centered witness charge: spectrum (3/4,-1/4,-1/4,-1/4), trace square=3/4.')
print('Commutes with weak action on contrast plane; fails commutation with fixed Gram.')
print('Conditional mixing with fixed inverse-trace convention: centered=2/5; integral=1/25.')
print('To force 3/13 by Y -> cY requires c^2=20/9: a target-selected scale.')
assert (F(5,3)/F(3,4))==F(20,9)
print('Exact projector-charge checks passed.')
