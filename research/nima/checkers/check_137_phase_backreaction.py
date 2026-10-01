# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Variational phase backreaction from the actual137 comparison mismatches.

One overlap phase theta and conjugate p; complex16 carrier+137 records.
Chosen canonical whitened frame, simultaneous comparison penalty, and rotor
storage. A scalar-mode trial, not a full local gauge-field derivation.
"""
from itertools import product
from functools import lru_cache
import numpy as np

G0=10*np.eye(4)+np.ones((4,4))
e=np.eye(4)
edges=[(a,b) for a,b in product(range(4),repeat=2) if a!=b and (a,b)!=(0,1)]
arrows=[e[b]-e[a] for a,b in edges]
features=np.array([np.kron(a,b) for a,b in product(arrows,repeat=2)] +
                  [np.kron(a,b) for a,b in product(e,repeat=2)],complex)
kappa=.3
beta=.7
mu=.2

@lru_cache(maxsize=4096)
def directions(theta):
    G=G0.astype(complex).copy()
    G[0,1]=np.exp(1j*theta); G[1,0]=np.exp(-1j*theta)
    K=np.kron(G.conj(),G0)
    values,V=np.linalg.eigh(K)
    root=(V*np.sqrt(values))@V.conj().T
    U=(root@features.T).T
    U/=np.linalg.norm(U,axis=1)[:,None]
    return U


def unpack(y): return y[:16],y[16:153],float(y[153].real),float(y[154].real)

def energy(y):
    q,w,theta,p=unpack(y)
    delta=w-directions(theta).conj()@q
    return kappa*np.vdot(delta,delta).real/2+beta*p*p/2+mu*(1-np.cos(theta))

def rhs(y,parts=False):
    q,w,theta,p=unpack(y)
    U=directions(theta)
    eps=1e-5
    dU=(directions(theta+eps)-directions(theta-eps))/(2*eps)
    delta=w-U.conj()@q
    # Hamiltonian gradient: H=kappa/2*sum|w-u^dagger q|^2.
    dq=1j*kappa*(U.T@delta)/2
    dw=-1j*kappa*delta/2
    matter_force=kappa*np.vdot(delta,dU.conj()@q).real
    field_force=-mu*np.sin(theta)
    if parts: return matter_force,field_force
    return np.r_[dq,dw,complex(beta*p),complex(matter_force+field_force)]

def step(y,dt):
    a=rhs(y); b=rhs(y+dt*a/2); c=rhs(y+dt*b/2); d=rhs(y+dt*c)
    return y+dt*(a+2*b+2*c+d)/6

rng=np.random.default_rng(137)
y0=np.r_[.1*(rng.normal(size=16)+1j*rng.normal(size=16)),np.zeros(137,complex),.4+0j,.1+0j]
# Independently check phase force against the total energy derivative.
eps=2e-5
shift=np.zeros(155,complex); shift[153]=eps
force=sum(rhs(y0,parts=True))
assert abs(force+(energy(y0+shift)-energy(y0-shift))/(2*eps)) < 1e-8
# Canonical global norm conservation is exact in the differential equations.
assert abs(2*np.vdot(y0[:153],rhs(y0)[:153]).real) < 1e-12


def run(dt):
    y=y0.copy(); H=energy(y); norm=np.vdot(y[:153],y[:153]).real
    err=0.; normerr=0.
    for _ in range(round(1/dt)):
        y=step(y,dt)
        err=max(err,abs(energy(y)-H))
        normerr=max(normerr,abs(np.vdot(y[:153],y[:153]).real-norm))
    assert err < 1e-6 and normerr < 1e-6
    return y,err,normerr

coarse=run(.02); fine=run(.01)
assert fine[1] < coarse[1]/4
assert fine[2] < coarse[2]/4
assert abs(fine[0][153]-y0[153]) > .01
assert np.linalg.norm(fine[0][16:153]) > .01
# A constant global phase transforms the full complex comparison state.
gauge=y0.copy(); gauge[:153]*=np.exp(.7j)
assert abs(energy(gauge)-energy(y0)) < 1e-12
assert np.max(np.abs(rhs(gauge)[:153]-np.exp(.7j)*rhs(y0)[:153])) < 1e-10
print(f'Initial comparison force={rhs(y0,parts=True)[0]:.12g}; rotor force={rhs(y0,parts=True)[1]:.12g}')
print(f'Final theta={fine[0][153].real:.12g}; p={fine[0][154].real:.12g}; record norm={np.linalg.norm(fine[0][16:153]):.12g}')
print(f'Max energy error dt .02/.01: {coarse[1]:.12g} / {fine[1]:.12g}')
print(f'Max global norm error dt .02/.01: {coarse[2]:.12g} / {fine[2]:.12g}')
print('Phase force is the derivative of137-slot mismatch storage; state and phase evolve together.')
print('Action, canonical frame, scalar reduction, and kappa/beta/mu remain declared model choices.')
