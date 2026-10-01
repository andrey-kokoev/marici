# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Local endpoint phase changes on tensor comparisons with retained records.

Tensor x_ab has phase exp(i*(chi_B[b]-chi_A[a])). Record coordinates are
chosen neutral. Gram metric and comparison features transform together.
Time-dependent endpoint phases require an additional connection term.
"""
from itertools import product
import numpy as np

G=10*np.eye(4)+np.ones((4,4))
K=np.kron(G,G).astype(complex)
basis=np.eye(4)
edges=[(a,b) for a,b in product(range(4),repeat=2) if a!=b and (a,b)!=(0,1)]
arrows=[basis[b]-basis[a] for a,b in edges]
features=[np.kron(a,b).astype(complex) for a,b in product(arrows,repeat=2)]
features += [np.kron(a,b).astype(complex) for a,b in product(basis,repeat=2)]
rng=np.random.default_rng(137)
x=rng.normal(size=16)+1j*rng.normal(size=16)
w=rng.normal(size=137)+1j*rng.normal(size=137)


def exchange(x,w,v,K,i):
    norm=float(np.vdot(v,K@v).real)
    u=v/np.sqrt(norm)
    value=np.vdot(u,K@x)
    out=x+u*(w[i]-value)
    records=w.copy(); records[i]=value
    return out,records,w[i]-value


def budget(x,w,K): return float((np.vdot(x,K@x)+np.vdot(w,w)).real)


for trial in range(12):
    ca=rng.uniform(-np.pi,np.pi,4); cb=rng.uniform(-np.pi,np.pi,4)
    phase=np.exp(1j*(cb[None,:]-ca[:,None])).reshape(16)
    transformed_K=phase[:,None]*K*phase.conj()[None,:]
    assert np.max(np.abs(transformed_K-K)) > 1
    for a,b,c in ((0,1,5),(2,7,11),(3,8,15)):
        loop=transformed_K[a,b]*transformed_K[b,c]*transformed_K[c,a]
        assert abs(loop-K[a,b]*K[b,c]*K[c,a]) < 1e-9
    assert abs(budget(phase*x,w,transformed_K)-budget(x,w,K)) < 1e-9
    # Freezing the off-diagonal metric would generally change the budget.
    if trial==0: assert abs(budget(phase*x,w,K)-budget(x,w,K)) > 1
    for i,v in enumerate(features):
        y,z,delta=exchange(x,w,v,K,i)
        ty,tz,tdelta=exchange(phase*x,w,phase*v,transformed_K,i)
        assert np.max(np.abs(ty-phase*y)) < 1e-10
        assert np.max(np.abs(tz-z)) < 1e-10
        assert abs(tdelta-delta) < 1e-10
        assert abs(budget(y,z,K)-budget(x,w,K)) < 1e-9
    # Tensor-dependent phase change preserves covariance trace budget.
    C=np.linalg.inv(K)
    transformed_C=phase[:,None]*C*phase.conj()[None,:]
    assert np.max(np.abs(transformed_K@transformed_C-np.eye(16))) < 1e-12
# The same transformation on both endpoint phase lists is redundant if constant.
common=.713
assert np.max(np.abs(np.exp(1j*((np.zeros(4)+common)[None,:]-(np.zeros(4)+common)[:,None]))-1)) < 1e-12
print('12 phase assignments x137 comparisons: metric, update, record, mismatch, and budget covariance passed.')
print('x_ab transforms with endpoint phase difference; records are neutral under this chosen adapter.')
print('Holding the Gram fixed fails the local-phase budget test; transporting it restores covariance.')
print('A time-varying frame adds i*dot(S)*S^-1 to the evolution generator.')
print('This is a covariant change of representation; field equations and charge normalization are not selected.')
