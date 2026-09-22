"""Certified finite-window, finite-mesh escape-field representation.

The field is piecewise exponential, specified by finitely many exact rational
cell coefficients and analytic recurrences. No sampled field error is used.
"""
from pathlib import Path
import json
import runpy
from flint import arb,ctx

ROOT=Path(__file__).resolve().parents[3]
# Recompute, rather than trust an old JSON cutoff certificate.
base=runpy.run_path(str(Path(__file__).with_name('certify_uniform_escape_prior_ball.py')))
assert base['result']['passed']
ctx.prec=192
P=100000
R=arb(8);S=arb(16);gamma=arb(1)
N=800;delta=R/N
eta_budget=arb('0.001')
evaluation_budget=arb('0.0005')
cutoff_budget=arb('0.72')
source_tail=(-gamma*R).exp()
mesh=delta/arb.pi()
profile_tail=2*(-S/2).exp()*(1+eta_budget)
discretization=4*(source_tail+mesh+eta_budget)+profile_tail
total=cutoff_budget+discretization+evaluation_budget
assert base['halfline_error']<cutoff_budget
assert total<arb('0.74')

# Concrete admitted receiver input: f(x)=sqrt(2/5) exp(-2x).
# Its weighted D_1 norm is exactly one; it is not a theta window or kernel.
amp=(arb(2)/5).sqrt()
assert (amp*amp*arb(5)/2).contains(1)
denominator=100000000
numerators=[];coeff=[];noise_squared=arb(0)
for j in range(N):
    exact_average=amp*((-2*j*delta).exp()-(-2*(j+1)*delta).exp())/(2*delta)
    # Floating point only PROPOSES a rational; Arb then certifies its error.
    numerator=round(float(exact_average)*denominator)
    c=arb(numerator)/denominator
    numerators.append(numerator);coeff.append(c)
    err_upper=arb(abs(exact_average-c).upper())
    noise_squared+=delta*err_upper**2
noise=noise_squared.sqrt()
assert noise<eta_budget
assert noise<arb('8.16e-9')

# Exact analytic recurrence on the mesh, enclosed by Arb.
q=(-delta/2).exp()
minus=[arb(0)]
for c in coeff:
    minus.append(q*minus[-1]+2*c*(1-q))
plus=[arb(0)]*(N+1)
for j in reversed(range(N)):
    plus[j]=q*plus[j+1]+2*coeff[j]*(1-q)

# Integrate squared exponential-polynomial differences exactly, not by sampling.
def energy(modes,length=None):
    value=arb(0)
    for c,b in modes:
        for d,e in modes:
            rate=b+e
            if length is None:
                assert rate<0
                integ=-1/rate
            elif rate.is_zero():
                integ=length
            else:
                integ=((rate*length).exp()-1)/rate
            value+=c*d*integ
    return value

em=arb(0);ep=arb(0)
for j,c in enumerate(coeff):
    x=j*delta
    # Exact J_- f minus the piecewise-exponential J_- g.
    em+=energy([(2*amp/3*(-x/2).exp()-minus[j]+2*c,-arb(1)/2),
                (-2*amp/3*(-2*x).exp(),-arb(2)),(-2*c,arb(0))],delta)
    # Exact J_+ f minus J_+ g on this same source mesh cell.
    ep+=energy([(2*amp/5*(-2*x).exp(),-arb(2)),(-2*c,arb(0)),
                (-(plus[j+1]-2*c)*q,arb(1)/2)],delta)
# J_- g retained to t=R+S, then set to zero.
em+=energy([(2*amp/3*(-R/2).exp()-minus[-1],-arb(1)/2),
            (-2*amp/3*(-2*R).exp(),-arb(2))],S)
T=R+S
em+=energy([(2*amp/3*(-T/2).exp(),-arb(1)/2),
            (-2*amp/3*(-2*T).exp(),-arb(2))])
# J_+ g retained down to -S, and identically zero above R.
p0=2*amp/5
ep+=(p0-plus[0])**2*(1-(-S).exp())+p0**2*(-S).exp()
ep+=p0**2*(-4*R).exp()/4
assert em>0 and ep>0
fixture_error=em.sqrt()+ep.sqrt()
assert fixture_error<arb('0.000091')

# The saved object specifies exact rationals and exact symbolic recurrences.
field={'schema':'marici.grothendieck.finite-escape-field.v1',
       'prime_cutoff':P,'source_mesh':{'origin':0,'step':'1/100','cells':N},
       'coefficient_denominator':denominator,'coefficient_numerators':numerators,
       'minus_profile_support':['0','24'],'plus_profile_support':['-16','8'],
       'recurrences':{'q':'exp(-1/200)',
           'A_0':'0','A_j_plus_1':'q*A_j+2*c_j*(1-q)',
           'B_800':'0','B_j':'q*B_j_plus_1+2*c_j*(1-q)'},
       'cell_formulas':{'A(j/100+s)':'exp(-s/2)*A_j+2*c_j*(1-exp(-s/2))',
           'B(j/100+s)':'exp(-(1/100-s)/2)*B_j_plus_1+2*c_j*(1-exp(-(1/100-s)/2))'},
       'tail_formulas':{'A on [8,24]':'A_800*exp(-(t-8)/2)',
                        'B on [-16,0]':'B_0*exp(t/2)'},
       'normalized_output':'A(u+log(100000))+B(u-log(100000)); zero outside listed profile supports',
       'fixture_source':'sqrt(2/5)*exp(-2*x), weighted D_1 norm exactly one',
       'interpretation':'Exact finite piecewise-exponential representation, not a sampled response vector.'}
field_path=ROOT/'research/grothendieck/results/finite-escape-field.json'
field_path.write_text(json.dumps(field,indent=2)+'\n',encoding='utf-8')
result={'schema':'marici.grothendieck.certified-finite-escape-field.v1','passed':True,
        'arithmetic':'python-flint Arb, 192 bits; exact rational coefficient proposals independently checked',
        'parameters':{'prime_cutoff':P,'receiver_gamma':1,'prior':'weighted D_1 norm <= M',
                      'source_window_R':8,'profile_tail_length_S':16,'mesh_cells':N,
                      'mesh_step':'1/100','coefficient_L2_noise_budget_per_M':'0.001',
                      'optional_additional_global_L2_error_per_M':'0.0005'},
        'rigorous_balls':{name:str(value) for name,value in {
            'source_tail_per_M':source_tail,'source_mesh_error_per_M':mesh,
            'profile_tail_budget_per_M':profile_tail,
            'total_profile_discretization_budget_per_M':discretization,
            'total_normalized_field_budget_per_M':total,
            'fixture_coefficient_noise':noise,
            'fixture_minus_profile_squared_error':em,
            'fixture_plus_profile_squared_error':ep,
            'fixture_two_profile_error_bound':fixture_error}.items()},
        'certified_claims':{'uniform_normalized_response_error_below_0_74_M':True,
                             'nonzero_trace_fixture_admitted':True,
                             'fixture_profile_error_below_0_000091':True,
                             'base_cutoff_certificate_recomputed':True},
        'finite_field_artifact':str(field_path.relative_to(ROOT)).replace('\\','/'),
        'scope':'Finite exact piecewise-exponential field and an absolute global L2 budget. Optional numerical-field error must be independently bounded in L2. No attachment, raw-kernel identification, or noisy-source existence is asserted.'}
p=ROOT/'research/grothendieck/results/certified-finite-escape-field.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
