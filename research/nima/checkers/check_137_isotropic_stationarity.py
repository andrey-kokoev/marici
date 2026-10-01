# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Stationary covariance audit for 137 normalized comparison projections.

Whitened carrier metric; independent zero-mean injection each step.
Compare rank-one normal refresh with equality-preserving tangent injection.
All strengths and schedule are declared trial choices.
"""
from itertools import product
import numpy as np

G = 10*np.eye(4)+np.ones((4,4))
K = np.kron(G,G)
L = np.linalg.cholesky(K)
basis = np.eye(4)
edges = [(a,b) for a,b in product(range(4),repeat=2) if a!=b and (a,b)!=(0,1)]
arrows = [basis[b]-basis[a] for a,b in edges]
features = [('arrow',np.kron(a,b)) for a,b in product(arrows,repeat=2)]
features += [('state',np.kron(a,b)) for a,b in product(basis,repeat=2)]
I = np.eye(16)
projectors = []
for kind,v in features:
    u = L.T@v; u /= np.linalg.norm(u)
    Q = np.outer(u,u); P = I-Q
    projectors.append((kind,u,Q,P))
    # Necessary independent additive covariance for target C=I:
    # N=I-PIP=Q. Tangent noise cannot restore variance along u.
    assert np.max(np.abs(I-P@I@P-Q)) < 1e-12
    assert abs(u@(P@I@P+P/15)@u) < 1e-12


def sweep(C,mode):
    losses=[]
    for kind,u,Q,P in projectors:
        loss=float(u@C@u)
        N=Q if mode=='normal' else P/15
        before=float(np.trace(C))
        C=P@C@P+N
        assert abs(np.trace(C)-(before-loss+1)) < 1e-10
        losses.append(loss)
        if mode=='tangent': assert abs(u@C@u) < 1e-10
    return C,np.array(losses)


for mode in ('normal','tangent'):
    C=np.zeros((16,16))
    for iteration in range(1,501):
        nxt,_=sweep(C,mode)
        change=np.max(np.abs(nxt-C))
        C=nxt
        if change < 1e-12: break
    else: raise AssertionError('no periodic covariance convergence')
    nxt,losses=sweep(C,mode)
    assert np.max(np.abs(nxt-C)) < 1e-10
    assert abs(losses.sum()-137) < 1e-9
    assert np.linalg.eigvalsh(C).min() > -1e-10
    if mode=='normal':
        assert np.max(np.abs(C-I)) < 1e-10
        assert np.max(np.abs(losses-1)) < 1e-10
    else:
        assert np.max(np.abs(C-I)) > .1
        assert np.ptp(losses) > .1
    print(f'{mode}: converged in{iteration} sweeps; total={np.trace(C):.12g}; '
          f'loss range=[{losses.min():.12g},{losses.max():.12g}]; '
          f'arrow mean={losses[:121].mean():.12g}; state mean={losses[121:].mean():.12g}; '
          f'sweep removed={losses.sum():.12g}')
for _,u,Q,P in projectors:
    assert np.max(np.abs(P@(0.5*I)@P+0.5*Q-0.5*I)) < 1e-12
    assert np.count_nonzero(P@np.zeros((16,16))@P) == 0
print('Both stationary programmes inject137 units per sweep at the declared strength1.')
print('Normal refresh preserves isotropy and equal losses but reopens the just-tested direction.')
print('Tangent injection preserves the current equality but yields unequal per-slot losses.')
print('Zero strength and zero input remain zero; absolute refresh strength is an input.')
