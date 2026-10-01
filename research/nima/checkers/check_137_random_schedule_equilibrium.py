# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Covariance mixing under a declared lazy random comparison schedule.

With probability1/2 wait; otherwise choose one of137 exchanges uniformly.
Every realized exchange is orthogonal. The covariance channel averages over
unobserved schedule histories. It introduces no amplitude noise or energy input.
"""
from itertools import product
import numpy as np

G=10*np.eye(4)+np.ones((4,4))
L=np.linalg.cholesky(np.kron(G,G))
e=np.eye(4)
edges=[(a,b) for a,b in product(range(4),repeat=2) if a!=b and (a,b)!=(0,1)]
arrows=[e[b]-e[a] for a,b in edges]
features=[np.kron(a,b) for a,b in product(arrows,repeat=2)]
features += [np.kron(a,b) for a,b in product(e,repeat=2)]
U=np.array([L.T@v/np.linalg.norm(L.T@v) for v in features])
D=np.vstack((U.T,-np.eye(137)))/np.sqrt(2)
S=D@D.T
W=np.vstack((np.eye(16),U))
F=W@np.linalg.solve(W.T@W,W.T)
A=np.eye(153)-F
initial=np.zeros((153,153)); initial[:16,:16]=np.eye(16)
active=float(np.trace(A@initial))
a=active/137
limit=F@initial@F+a*A

def channel(C):
    CD=C@D
    diagonal=np.sum(D*CD,axis=0)
    return C-(S@C+C@S)/137+2*(D*diagonal)@D.T/137

assert np.max(np.abs(channel(limit)-limit)) < 1e-12
assert abs(np.trace(limit)-16) < 1e-10
variance=2*np.sum(D*(limit@D),axis=0)
assert np.max(np.abs(variance-2*a)) < 1e-12
assert np.max(np.abs(variance/variance.sum()-1/137)) < 1e-12
# Unequal positive scheduling weights retain the same equilibrium.
weights=np.arange(1.,138.); weights/=weights.sum()
weighted_S=(D*weights)@D.T
CD=limit@D
weighted=limit-weighted_S@limit-limit@weighted_S+2*(D*(weights*np.sum(D*CD,axis=0)))@D.T
assert np.max(np.abs(weighted-limit)) < 1e-12
C=initial.copy()
old_error=np.linalg.norm(C-limit)
start_error=old_error
for step in range(1,2001):
    C=channel(C)
    error=np.linalg.norm(C-limit)
    assert error <= old_error+1e-11
    old_error=error
    assert abs(np.trace(C)-16) < 1e-9
    if step in (1,137,1000,2000):
        print(f'Step{step}: covariance error={error:.12g}; carrier budget={np.trace(C[:16,:16]):.12g}')
assert old_error < start_error/100
assert np.max(np.abs(F@C@F-F@initial@F)) < 1e-9
print(f'Initial active budget={active:.12g}; limiting variance per comparison={2*a:.12g}')
print(f'Predicted limiting carrier budget={np.trace(limit[:16,:16]):.12g}; total16.')
print('Limiting normalized mismatch variance is1/137 for both uniform and unequal positive scheduling weights.')
print('Convergence concerns schedule-averaged covariance; each realized history remains reversible.')
