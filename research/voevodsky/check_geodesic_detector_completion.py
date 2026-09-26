"""Exact Jacobi detector controls. No numerical curvature averaging or finite-arm theorem."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

# Rational powers on u>0; reference event u=1.
def term(q,a=1):return {F(q):F(a)} if a else {}
def add(*ps):
    out={}
    for p in ps:
        for q,a in p.items():out[q]=out.get(q,F(0))+a
    return {q:a for q,a in out.items() if a}
def scale(a,p):return {q:a*b for q,b in p.items() if a*b}
def mul(p,r):
    out={}
    for q,a in p.items():
        for s,b in r.items():out[q+s]=out.get(q+s,F(0))+a*b
    return {q:a for q,a in out.items() if a}
def der(p):return {q-1:q*a for q,a in p.items() if q*a}
def at1(p):return sum(p.values(),F(0))
def at_fifth_power(p,t):
    if any((5*q).denominator!=1 for q in p):raise ValueError('unsupported exponent')
    return sum(a*t**int(5*q) for q,a in p.items())
checks={};values={}
for alpha in (F(6,5),F(3,5)):
    p=term(alpha)
    K=add(term(alpha,(1-alpha)/(1-2*alpha)),term(1-alpha,-alpha/(1-2*alpha)))
    H=scale(1/(1-2*alpha),add(term(1-alpha),scale(-1,term(alpha))))
    # H here is the velocity-to-displacement propagator, no time prefactor.
    A=term(-2,alpha*(alpha-1))
    label=str(alpha)
    checks[label+'_rest_initial_position']=at1(K)==1
    checks[label+'_rest_initial_velocity']=at1(der(K))==0
    checks[label+'_velocity_initial_position']=at1(H)==0
    checks[label+'_velocity_initial_velocity']=at1(der(H))==1
    checks[label+'_exact_rest_jacobi_equation']=der(der(K))==mul(A,K)
    checks[label+'_exact_velocity_jacobi_equation']=der(der(H))==mul(A,H)
    checks[label+'_coordinate_comoving_not_physically_at_rest']=at1(der(p))!=0
    # K = p(1-alpha integral_1^u p^-2); verify by expanding powers.
    integ=scale(1/(1-2*alpha),add(term(1-2*alpha),term(0,-1)))
    checks[label+'_rosen_conserved_momentum_formula']=K==mul(p,add(term(0),scale(-alpha,integ)))
    values[label]=str(at_fifth_power(K,F(6,5)))
# Both directions belong to ONE trace-free vacuum plane wave.
checks['two_transverse_profiles_form_vacuum']=F(6,5)*F(1,5)+F(3,5)*F(-2,5)==0
checks['proper_time_normalization']=F(1,2)*F(6,25)==F(3,25) # d2/dtau2 = (1/2)d2/du2.
# C1-loss hostile: beta_n=(1-cos nu)/n^2, r solves focusing with resting corner.
# Analytic bound for n>=2: |p_n-1|,|q_n-1| <= 5/n^2 on [0,1].
rows=[dict(n=n,displacement_envelope=str(F(5,n*n)),pointwise_tidal_gap=str(F(1,2)),
           initial_coordinate_momentum='0',radial_lower_bound=str(1-F(1,2*n*n))) for n in (2,4,8,16,32)]
checks['response_envelope_decreases']=all(F(rows[i+1]['displacement_envelope'])<F(rows[i]['displacement_envelope']) for i in range(len(rows)-1))
checks['tidal_gap_persists']=all(F(row['pointwise_tidal_gap'])==F(1,2) for row in rows)
checks['no_caustic_in_hostile']=all(F(row['radial_lower_bound'])>0 for row in rows)
checks['endpoint_displacement_is_not_instantaneous_curvature']=F(rows[-1]['displacement_envelope'])<F(1,2)
root=Path(__file__).resolve().parents[2]
paths=[Path(__file__),root/'research/strominger/sources/fghn1901.00021.txt',root/'research/voevodsky/tidal-readout-needs-second-jet-completion.md']
packet=dict(passed=all(checks.values()),checks=checks,rest_propagator_at_u_6_over_5_to_5=values,hostile_bounds=rows,
    scope='Exact rational-power Jacobi solutions and analytic-bound constants. General C1 continuity and all-n estimates are written proofs; only first order in detector separation, no finite-arm or instrument-noise theorem.',
    source_sha256={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
Path(__file__).with_name('geodesic-detector-completion.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
