# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Closed record exchange for the137 tensor-comparison slots.

16 whitened carrier coordinates plus137 scalar records. Tests stationary
joint ensembles, conserved shared coordinates, and the absence of a unique
stationary response selected by reversible record dynamics.
"""
from itertools import product
import numpy as np

G=10*np.eye(4)+np.ones((4,4))
L=np.linalg.cholesky(np.kron(G,G))
basis=np.eye(4)
edges=[(a,b) for a,b in product(range(4),repeat=2) if a!=b and (a,b)!=(0,1)]
arrows=[basis[b]-basis[a] for a,b in edges]
features=[np.kron(a,b) for a,b in product(arrows,repeat=2)]
features += [np.kron(a,b) for a,b in product(basis,repeat=2)]
U=np.array([L.T@v/np.linalg.norm(L.T@v) for v in features])
D=153
# Every comparison exchanges u_i.q with record_i. Fixed vectors satisfy
# record_i=u_i.q for all i, so W parametrizes a16-dimensional common fixed space.
W=np.vstack((np.eye(16),U))
F=W@np.linalg.solve(W.T@W,W.T)
assert np.max(np.abs(F@F-F)) < 1e-12
assert abs(np.trace(F)-16) < 1e-12
I=np.eye(D)
for name,C in [('isotropic joint ensemble',I),('isotropic plus common fixed sector',I+F)]:
    outgoing=[]; incoming=[]; errors=[]
    for i,u in enumerate(U):
        d=np.zeros(D); d[:16]=u/np.sqrt(2); d[16+i]=-1/np.sqrt(2)
        assert np.max(np.abs(d@W)) < 1e-12
        Cd=C@d
        transformed=C-2*np.outer(d,Cd)-2*np.outer(Cd,d)+4*(d@Cd)*np.outer(d,d)
        assert np.max(np.abs(transformed-C)) < 1e-12
        outgoing.append(u@C[:16,:16]@u)
        incoming.append(C[16+i,16+i])
        errors.append(2*(d@C@d))
    assert np.max(np.abs(np.array(outgoing)-incoming)) < 1e-12
    print(f'{name}: total={np.trace(C):.12g}; carrier={np.trace(C[:16,:16]):.12g}; '
          f'arrow mean={np.mean(outgoing[:121]):.12g}; state mean={np.mean(outgoing[121:]):.12g}; '
          f'exchange-difference variance range=[{min(errors):.12g},{max(errors):.12g}]')
    if name.startswith('isotropic joint'):
        assert np.max(np.abs(np.array(outgoing)-1)) < 1e-12
    else:
        assert np.ptp(outgoing) > 1e-3
# The fixed sector is invisible to exchange differences; actual update is
# proportional to record_i-u_i.q. It leaves both carrier and record unchanged.
fixed=W@np.arange(1.,17.)
assert np.max(np.abs(U@fixed[:16]-fixed[16:])) < 1e-12
# The137 reflection normals are independent (each has a unique record
# coordinate). Their nonorthogonality graph is connected.
normal_gram=(U@U.T+np.eye(137))/2
assert np.linalg.eigvalsh(normal_gram).min() > 0
seen={0}; frontier=[0]
while frontier:
    i=frontier.pop()
    for j in range(137):
        if j not in seen and abs(normal_gram[i,j]) > 1e-12:
            seen.add(j); frontier.append(j)
assert len(seen) == 137
print('137 independent reflection normals have a connected nonorthogonality graph.')
print('Symmetric covariance invariant under EVERY individual reflection is scalar on their span.')
print('Therefore all exchange-difference variances equal2*a in that strong stationary class.')
print('All137 individual exchanges preserve both distinct joint covariances.')
print('Isotropic joint preparation yields unit return and outgoing budget, with zero net external supply.')
print('Common fixed space has dimension16; a passive cycle cannot erase its initial information.')
print('Marginal slot budgets and exchange-difference responses are distinct observables.')
print('153 here counts16 coordinates+137 records; it is not the earlier mass-comparison domain.')
