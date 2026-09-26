"""Exact Fourier-mode reduction of a supplied linearized Einstein equation.
Independent tensor contraction, with signature (-+++), exp(i k.x).
No continuum GR limit, FRW expansion, or scalar-state averaging theorem.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

eta=(-1,1,1,1)
def zero():return [[F(0) for _ in range(4)] for _ in range(4)]
def trace(h):return sum(eta[i]*h[i][i] for i in range(4))
def einstein(h,k):
    # k is covariant. Derivatives are i*k; all quantities below are real
    # amplitudes after the two-derivative sign is included.
    k2=sum(eta[i]*k[i]**2 for i in range(4))
    div=[sum(eta[r]*k[r]*h[r][j] for r in range(4)) for j in range(4)]
    r=[[(-k[i]*div[j]-k[j]*div[i]+k2*h[i][j]+k[i]*k[j]*trace(h))/2
        for j in range(4)] for i in range(4)]
    scalar=trace(r)
    return [[r[i][j]-(eta[i]*scalar/2 if i==j else 0) for j in range(4)] for i in range(4)]
def metric(phi,psi):
    h=zero();h[0][0]=-2*phi
    for i in range(1,4):h[i][i]=-2*psi
    return h
def gauge(k,xi):return [[k[i]*xi[j]+k[j]*xi[i] for j in range(4)] for i in range(4)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(4)] for i in range(4)]
checks={}
k=(F(0),F(1),F(2),F(0));k2=F(5)
# Choose 4*pi*G=1, so 8*pi*G=2; static dust Fourier amplitude rho=3.
rho=F(3);phi=-rho/k2
h=metric(phi,phi);target=zero();target[0][0]=2*rho
checks['dust_full_ten_component_einstein_equation']=einstein(h,k)==target
checks['poisson_sign_and_normalization']=-k2*phi==rho
# Directly verify full tensor form for unequal potentials.
u,v=F(2,7),F(-3,5);gg=einstein(metric(u,v),k)
checks['00_constraint_selects_psi']=gg[0][0]==-2*k2*v
checks['spatial_stress_measures_slip']=all(
    gg[i][j]==(u-v)*(k[i]*k[j]-(k2 if i==j else 0)) for i in range(1,4) for j in range(1,4))
checks['no_stress_slip_control']=gg!=zero() and any(gg[i][j] for i in range(1,4) for j in range(1,4))
xi=(F(1),F(-2),F(3),F(4))
checks['pure_gauge_einstein_zero']=einstein(gauge(k,xi),k)==zero()
checks['gauge_preserves_sourced_equation']=einstein(add(h,gauge(k,xi)),k)==target
# R_0i0j = -1/2 d_i d_j h00 = (k_i k_j/2) h00 for static fields.
checks['electric_curvature_matches_hessian']=all(
    k[i]*k[j]*h[0][0]/2 == -k[i]*k[j]*phi for i in range(1,4) for j in range(1,4))
# A static conserved stress source (not claimed to be an arbitrary scalar state).
e=(F(0),F(2),F(-1),F(0));T=zero();T[0][0]=rho
for i in range(1,4):
    for j in range(1,4):T[i][j]=e[i]*e[j]
checks['anisotropic_source_conserved']=all(sum(eta[i]*k[i]*T[i][j] for i in range(4))==0 for j in range(4))
# Harmonic equation k^2 hbar =16*pi*G T=4 T.
hbar=[[4*T[i][j]/k2 for j in range(4)] for i in range(4)]
th=trace(hbar)
hs=[[hbar[i][j]-(eta[i]*th/2 if i==j else 0) for j in range(4)] for i in range(4)]
checks['stressed_full_einstein_solution']=einstein(hs,k)==[[2*x for x in row] for row in T]
phi_stress=-hs[0][0]/2
checks['active_static_source_includes_stress_trace']=-k2*phi_stress==rho+sum(T[i][i] for i in range(1,4))
checks['density_only_prediction_rejected']=phi_stress!=phi
# Homogeneous free massive scalar at two phases: same rho, different stress.
# mu=1, amplitude=2, V=phi_scalar^2/2; gradients zero.
def scalar_state(field,velocity):
    potential=field*field/2
    return velocity*velocity/2+potential, velocity*velocity/2-potential
r1,p1=scalar_state(F(2),F(0));r2,p2=scalar_state(F(0),F(2))
checks['scalar_energy_does_not_fix_pressure']=r1==r2==2 and p1==-2 and p2==2
# Exact analytic cycle moments cos^2=sin^2=1/2, entered as known moments.
avg_velocity_squared=F(2);avg_potential=F(1)
checks['homogeneous_oscillator_average_pressure_zero']=avg_velocity_squared/2-avg_potential==0
checks['homogeneous_oscillator_average_density']=avg_velocity_squared/2+avg_potential==2
# Scalar field with potential only is not static dust.
checks['potential_dominated_scalar_not_dust']=p1!=0
paths=[Path(__file__),Path(__file__).resolve().parents[1]/'nima/checkers/check_machian_linearized_source_boundary_map.py']
packet=dict(passed=all(checks.values()),checks=checks,
    dust_phi=str(phi),stressed_phi=str(phi_stress),
    scope='Exact finite Fourier amplitudes of supplied linearized GR; homogeneous scalar moments are not a localized cosmological dust limit.',
    source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
Path(__file__).with_name('linearized-einstein-poisson-reduction.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
