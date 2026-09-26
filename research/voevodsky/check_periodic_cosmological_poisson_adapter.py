"""Exact 4^3 periodic Poisson adapter; supplied Newtonian perturbation model.
Uses integer fourth roots of unity and Fraction arithmetic, no FFT rounding.
The lattice and periodic boundary are declared, not derived from FRW.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

N=4
sites=list(product(range(N),repeat=3))
roots=((1,0),(0,1),(-1,0),(0,-1))
mass={x:F(0) for x in sites}
# Separate small periodic fixture, not the infinite-space 3/4-radius fixture.
mass[(1,0,0)]=F(2)
mass[(0,1,0)]=F(1)
mean=sum(mass.values())/len(sites)
delta={x:mass[x]-mean for x in sites}

def transform(f):
    out={}
    for k in sites:
        re=F(0); im=F(0)
        for x in sites:
            c,s=roots[(-sum(a*b for a,b in zip(k,x)))%N]
            re+=f[x]*c; im+=f[x]*s
        out[k]=(re,im)
    return out

def inverse_real(h):
    out={}
    for x in sites:
        re=F(0); im=F(0)
        for k,(u,v) in h.items():
            c,s=roots[sum(a*b for a,b in zip(k,x))%N]
            re+=u*c-v*s; im+=u*s+v*c
        if im:
            raise ValueError('non-real inverse transform')
        out[x]=re/len(sites)
    return out

def lap(f):
    out={}
    for x in sites:
        out[x]=-6*f[x]
        for j in range(3):
            for sign in (-1,1):
                y=list(x);y[j]=(y[j]+sign)%N
                out[x]+=f[tuple(y)]
    return out

def solve(rhs):
    if sum(rhs.values()):
        raise ValueError('periodic Poisson requires zero mean')
    hat=transform(rhs)
    eig=(0,2,4,2)  # Positive -Delta eigenvalues per coordinate.
    phat={}
    for k,(u,v) in hat.items():
        lam=sum(eig[i] for i in k)
        phat[k]=(-u/lam,-v/lam) if lam else (F(0),F(0))
    return inverse_real(phat)

phi=solve(delta)
checks={
    'total_mass_3':sum(mass.values())==3,
    'background_density_3_over_64':mean==F(3,64),
    'contrast_has_zero_mean':sum(delta.values())==0,
    'exact_fourier_roundtrip':inverse_real(transform(delta))==delta,
    'poisson_residual_zero_all_64_sites':lap(phi)==delta,
    'chosen_potential_zero_mean':sum(phi.values())==0,
    'laplacian_always_sums_zero_on_fixture':sum(lap(mass).values())==0,
    'constant_shift_preserves_poisson':lap({x:phi[x]+7 for x in sites})==delta,
    'wrong_sign_fails':lap({x:-phi[x] for x in sites})!=delta,
}
try:solve(mass)
except ValueError:checks['positive_total_source_rejected_without_background']=True
else:checks['positive_total_source_rejected_without_background']=False
# Fixed masses in fixed comoving cells: rho_phys=m/a^3, Delta_com phi=a^2 delta_rho.
a=F(2)
rho={x:mass[x]/a**3 for x in sites}
background=mean/a**3
rhs={x:a*a*(rho[x]-background) for x in sites}
phi_a=solve(rhs)
checks['proper_total_mass_preserved']=sum(v*a**3 for v in rho.values())==3
checks['fixed_comoving_sources_potential_scales_inverse_a']=all(phi_a[x]==phi[x]/a for x in sites)
checks['proper_laplacian_matches_density_contrast']=all(lap(phi_a)[x]/a**2==rho[x]-background for x in sites)
# Observable: x-directed diagonal tidal second difference in proper units.
def exx(f,x):
    lo=((x[0]-1)%N,x[1],x[2]);hi=((x[0]+1)%N,x[1],x[2])
    return f[lo]-2*f[x]+f[hi]
checks['proper_tidal_scales_inverse_a_cubed']=all(exx(phi_a,x)/a**2==exx(phi,x)/a**3 for x in sites)
# Same mass and background, different source state, different local tide.
other={x:F(0) for x in sites}
other[(0,1,0)]=F(2);other[(0,0,1)]=F(1)
other_phi=solve({x:other[x]-mean for x in sites})
checks['background_does_not_select_local_tides']=exx(phi,(0,0,0))!=exx(other_phi,(0,0,0))
packet=dict(passed=all(checks.values()),checks=checks,
    origin_phi=str(phi[(0,0,0)]),origin_xx=str(exx(phi,(0,0,0))),
    alternative_origin_xx=str(exx(other_phi,(0,0,0))),
    convention='4*pi*G=1; comoving grid spacing 1; periodic side 4; zero-mean potential',
    scope='Finite discrete model with supplied perturbative Poisson law and background split; not GR or a continuum limit.',
    checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_name('periodic-cosmological-poisson-adapter.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
