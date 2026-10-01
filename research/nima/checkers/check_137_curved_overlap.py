# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Curved phase-dressed overlap family and comparison equilibrium audit.

Hermitian four-probe Gram has diagonal11 and off-diagonal unit modulus.
Arbitrary edge phases remain positive by strict diagonal dominance (bound8).
No field action or electromagnetic normalization is inferred from this family.
"""
from itertools import combinations, product
import numpy as np

edges6=list(combinations(range(4),2))
basis=np.eye(4)
edges12=[(a,b) for a,b in product(range(4),repeat=2) if a!=b and (a,b)!=(0,1)]
arrows=[basis[b]-basis[a] for a,b in edges12]
features=[np.kron(a,b).astype(complex) for a,b in product(arrows,repeat=2)]
features += [np.kron(a,b).astype(complex) for a,b in product(basis,repeat=2)]


def gram(phases):
    G=11*np.eye(4,dtype=complex)
    for (a,b),theta in zip(edges6,phases):
        G[a,b]=np.exp(1j*theta); G[b,a]=np.exp(-1j*theta)
    return G


rng=np.random.default_rng(137)
x=rng.normal(size=16)+1j*rng.normal(size=16)
print('edge phase | triangle phase | min tensor eigenvalue | exchange directions | normalized variance')
for theta in (0.,.2,.7,1.4,np.pi):
    pa=np.array([theta,0.,0.,0.,0.,0.])
    pb=np.array([0.,.3*theta,0.,0.,0.,0.])
    GA,GB=gram(pa),gram(pb)
    K=np.kron(GA.conj(),GB)
    assert np.linalg.eigvalsh(GA).min() >= 8-1e-12
    assert np.linalg.eigvalsh(K).min() >= 64-1e-10
    factor=np.linalg.cholesky(K)
    U=np.array([factor.conj().T@v/np.sqrt(np.vdot(v,K@v).real) for v in features])
    # Columns d_i are complex unit reflection normals for carrier/record swap.
    D=np.vstack((U.T,-np.eye(137)))/np.sqrt(2)
    N=D.conj().T@D
    assert np.linalg.eigvalsh(N).min() > .49
    seen={0}; stack=[0]
    while stack:
        i=stack.pop()
        for j in range(137):
            if j not in seen and abs(N[i,j])>1e-10:
                seen.add(j); stack.append(j)
    assert len(seen)==137
    # Active orthogonal projector; covariance a*A is a common stationary choice.
    A=D@np.linalg.solve(N,D.conj().T)
    assert np.max(np.abs(A@A-A))<1e-10
    variances=2*np.real(np.sum(D.conj()*(A@D),axis=0))
    assert np.max(np.abs(variances/variances.sum()-1/137)) < 1e-12
    loop=GA[0,1]*GA[1,2]*GA[2,0]
    assert abs(loop-np.exp(1j*theta))<1e-12
    print(f'{theta:.6g} | {np.angle(loop):.6g} | {np.linalg.eigvalsh(K).min():.10g} | 137 | 1/137')
    # Analytic derivative of K for pa[0]=theta, pb[1]=.3theta.
    dGA=np.zeros((4,4),complex); dGA[0,1]=1j*GA[0,1]; dGA[1,0]=-1j*GA[1,0]
    dGB=np.zeros((4,4),complex); dGB[0,2]=.3j*GB[0,2]; dGB[2,0]=-.3j*GB[2,0]
    dK=np.kron(dGA.conj(),GB)+np.kron(GA.conj(),dGB)
    velocity=-.5*np.linalg.solve(K,dK@x)
    balance=2*np.vdot(x,K@velocity).real+np.vdot(x,dK@x).real
    assert abs(balance)<1e-9
print('Independent loop phases preserve positivity and the conditional137-response normalization.')
print('Metric-compatible transport xdot=-K^-1*Kdot*x/2 conserves the quadratic norm instantaneously.')
print('Curvature evolution, additional skew transport, and field coefficients remain unspecified.')
