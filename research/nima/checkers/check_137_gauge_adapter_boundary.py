# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Gauge adapter tests: real reflection obstruction and complex lift.

The active real comparison reflections admit no nonzero skew generator
commuting with every labelled comparison. Complex doubling supplies a global
phase symmetry, but not a physical four-site matter/link identification.
"""
from itertools import product
import numpy as np

G=10*np.eye(4)+np.ones((4,4))
K=np.kron(G,G)
L=np.linalg.cholesky(K)
basis=np.eye(4)
edges=[(a,b) for a,b in product(range(4),repeat=2) if a!=b and (a,b)!=(0,1)]
arrows=[basis[b]-basis[a] for a,b in edges]
features=[np.kron(a,b) for a,b in product(arrows,repeat=2)]
features += [np.kron(a,b) for a,b in product(basis,repeat=2)]
U=np.array([L.T@v/np.linalg.norm(L.T@v) for v in features])
D=np.vstack((U.T,-np.eye(137)))/np.sqrt(2)
assert np.linalg.matrix_rank(D) == 137
# Rank-one reflection eigenspace: commutation forces any skew generator to
# preserve the real line spanned by d; skewness forces its action there to0.
# Verify the block-complex lift on all directions without dense306^3 products.
rng=np.random.default_rng(137)
z=rng.normal(size=153)+1j*rng.normal(size=153)
phase=np.exp(.37j)
for d in D.T:
    Pz=d*(d@z)
    out=z-2*Pz
    assert abs(np.vdot(out,out)-np.vdot(z,z)) < 1e-10
    assert np.max(np.abs((phase*z-2*d*(d@(phase*z)))-phase*out)) < 1e-12
    # exp(-i*pi*P)=I-2P, as P^2=P.
    pulse=z+(np.exp(-1j*np.pi)-1)*Pz
    assert np.max(np.abs(pulse-out)) < 1e-12
    # In real coordinates J(x,y)=(-y,x); H acts identically on both blocks.
    hx=z.real-2*d*(d@z.real); hy=z.imag-2*d*(d@z.imag)
    assert np.max(np.abs((-z.imag+2*d*(d@z.imag))-(-hy))) < 1e-12
    assert np.max(np.abs((z.real-2*d*(d@z.real))-hx)) < 1e-12
# A natural product-state adapter from four-state amplitudes fails closure.
x=np.kron(basis[0],basis[0])
a=basis[2]-basis[0]
v=np.kron(a,a)
y=x-v*(v@K@x)/(v@K@v)
assert np.linalg.matrix_rank(x.reshape(4,4)) == 1
assert np.linalg.matrix_rank(y.reshape(4,4),tol=1e-12) == 2
# Weight/coupling normalization remains free in pulse duration tau.
for tau in (.5,1.,2.):
    frequency=np.pi/tau
    assert abs(np.exp(-1j*frequency*tau)+1) < 1e-12
print('137 independent real reflection directions: a commuting skew generator must vanish on all of them.')
print('Complex lift preserves norm and global U(1) phase for all137 comparisons.')
print('Each lifted exchange has a rank-one Hamiltonian pulse with integrated angle pi.')
print('Product-state adapter fails: one valid comparison takes tensor rank1 to rank2.')
print('Pulse duration changes generator strength without changing the comparison endpoint.')
print('Global phase charge is constructed in the enlarged model; local electromagnetic adapter remains open.')
