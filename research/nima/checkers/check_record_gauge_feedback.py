# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Closed finite U(1) matter/link Hamiltonian trial in temporal gauge.

Four vertices, six oriented links, four triangular loops. A static neutralizing
background makes Gauss compatible with positive matter norm on a closed graph.
Uses exact subflows and a symmetric second-order composition.
"""
from itertools import combinations
import numpy as np

edges=list(combinations(range(4),2))
B=np.array([[int(v==b)-int(v==a) for a,b in edges] for v in range(4)],float)
C=np.zeros((4,6))
for row,(a,b,c) in enumerate(combinations(range(4),3)):
    for edge,sign in (((a,b),1),((b,c),1),((a,c),-1)):
        C[row,edges.index(edge)]=sign
assert np.max(np.abs(B@C.T)) == 0
hopping=np.array([1.,.8,1.1,.9,1.2,.7])
beta=.6
magnetic=.4
psi0=np.array([1+.2j,.4-.3j,-.2+.6j,.7+.1j])
A0=np.array([.1,-.2,.3,.2,-.1,.4])
rho0=np.abs(psi0)**2
background=np.full(4,rho0.sum()/4)
E0=B.T@(rho0-background)/4


def gauss(psi,E): return B@E-(np.abs(psi)**2-background)

def energy(psi,A,E):
    matter=sum(k*abs(psi[b]-np.exp(1j*A[i])*psi[a])**2
               for i,((a,b),k) in enumerate(zip(edges,hopping)))
    return matter+beta*(E@E)/2+magnetic*np.sum(1-np.cos(C@A))


def current(psi,A):
    return np.array([2*k*(psi[b].conjugate()*np.exp(1j*A[i])*psi[a]).imag
                     for i,((a,b),k) in enumerate(zip(edges,hopping))])


def hop(psi,A,E,i,dt):
    a,b=edges[i]; u=np.exp(1j*A[i]); k=hopping[i]
    old_b=abs(psi[b])**2
    x,y=psi[a],psi[b]
    phase=np.exp(-2j*k*dt)-1
    psi[a]=x+phase*(x-u.conjugate()*y)/2
    psi[b]=y+phase*(y-u*x)/2
    E[i] += abs(psi[b])**2-old_b


def advance(psi,A,E,dt):
    A += dt*beta*E/2
    E -= dt*magnetic*(C.T@np.sin(C@A))/2
    for i in range(6): hop(psi,A,E,i,dt/2)
    for i in reversed(range(6)): hop(psi,A,E,i,dt/2)
    E -= dt*magnetic*(C.T@np.sin(C@A))/2
    A += dt*beta*E/2


assert np.max(np.abs(gauss(psi0,E0))) < 1e-12
# Hamiltonian link force matches matter current plus magnetic loop force.
epsilon=1e-6
for i in range(6):
    delta=np.eye(6)[i]*epsilon
    derivative=(energy(psi0,A0+delta,E0)-energy(psi0,A0-delta,E0))/(2*epsilon)
    expected=current(psi0,A0)[i]+magnetic*(C.T@np.sin(C@A0))[i]
    assert abs(derivative-expected)<1e-8


def run(dt,chi=None):
    psi=psi0.copy(); A=A0.copy(); E=E0.copy()
    if chi is not None:
        psi*=np.exp(1j*chi); A+=B.T@chi
    H=energy(psi,A,E); max_error=0.
    for _ in range(round(1/dt)):
        advance(psi,A,E,dt)
        assert np.max(np.abs(gauss(psi,E))) < 1e-10
        assert abs(np.sum(np.abs(psi)**2)-rho0.sum()) < 1e-10
        max_error=max(max_error,abs(energy(psi,A,E)-H))
    return psi,A,E,max_error

coarse=run(.01); fine=run(.005)
assert fine[3] < coarse[3]/3
chi=np.array([.17,-.43,.81,.29])
gauged=run(.01,chi)
assert np.max(np.abs(gauged[0]-np.exp(1j*chi)*coarse[0])) < 1e-10
assert np.max(np.abs(gauged[1]-coarse[1]-B.T@chi)) < 1e-10
assert np.max(np.abs(gauged[2]-coarse[2])) < 1e-10
# Reverse the complete numerical history using negative time steps.
psi,A,E=(x.copy() for x in coarse[:3])
for _ in range(100): advance(psi,A,E,-.01)
assert max(np.max(np.abs(psi-psi0)),np.max(np.abs(A-A0)),np.max(np.abs(E-E0))) < 1e-10
assert np.linalg.norm(coarse[2]-E0) > .01
assert np.linalg.norm(coarse[1]-A0) > .01
print('Closed loop: matter current changes E; E changes link phases; phases change matter transport.')
print('Gauss constraint, total matter norm, time reversal, and local gauge covariance passed.')
print(f'Max energy error: dt=.01 -> {coarse[3]:.12g}; dt=.005 -> {fine[3]:.12g}')
print(f'Field changes after unit model time: |delta E|={np.linalg.norm(coarse[2]-E0):.12g}, '
      f'|delta A|={np.linalg.norm(coarse[1]-A0):.12g}')
print('Background, hopping, electric/magnetic coefficients, and model time are declared trial inputs.')
print('No137-comparison adapter or physical electromagnetic normalization is supplied by this test.')
