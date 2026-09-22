"""Conditional quadrature tests and a 347-decimal-order cancellation regression."""
from pathlib import Path
import importlib.util,json
from decimal import Decimal,localcontext
from flint import arb,acb,ctx

s=importlib.util.spec_from_file_location('acquisition',Path(__file__).with_name('sample_finite_cubic_observer.py'))
a=importlib.util.module_from_spec(s);s.loader.exec_module(a)
o=a.receiver.Observer();sampler=a.Acquisition(o)
bounds=sampler.certify_kernel_bounds()
(a.receiver.RESULTS/'finite-cubic-acquisition-kernels.json').write_text(json.dumps(bounds,indent=2)+'\n',encoding='utf-8')
sampler.load_kernel_bounds()
ctx.prec=2048
# Mathematical fixture, not fabricated experimental measurements:
# g(u)=exp(-4u), kernel=weak_multiplier*exp(-4u).
step=arb(1)/1024;N=8192
samples=[acb((-4*(arb(j)+arb(1)/2)*step).exp()) for j in range(N)]
acquired=sampler.sample_field('weak',samples,0,step,1,1,1)
truth=a.receiver.rational(o.manifest['weak_multiplier'])/8
assert abs(acquired['value']-truth)<acquired['error']
assert acquired['error']<arb('0.1')
# A supplied exact-zero field has zero deterministic acquisition error.
z=sampler.sample_field('weak',[acb(0)],0,1,0,0,0)
assert z['error'].is_zero() and z['value'].is_zero()
feature=sampler.feature([z,z,z,z],[['0','0'],['0','0']])
tensor=sampler.tensor([(['1','0'],feature,feature)])
result=sampler.evaluate([tensor]*449)
assert result['meets_1e_minus540_budget']
for kwargs in [dict(step=0),dict(l2_bound=-1),dict(variation_bound=-1)]:
    arguments=dict(channel='weak',samples=[acb(0)],start=0,step=1,l2_bound=1,sup_bound=1,variation_bound=1)
    arguments.update(kwargs)
    try:sampler.sample_field(**arguments)
    except ValueError:pass
    else:raise AssertionError('Invalid certificate accepted')

# Two large cancelling readings differ by 10^-540, far below 192-bit relative precision.
plus=next(i for i,r in enumerate(o.manifest['rows']) if r['coefficient']=='crossed' and r['sign']==1)
minus=next(i for i,r in enumerate(o.manifest['rows']) if r['coefficient']=='crossed' and r['sign']==-1)
readings=[['0','0'] for _ in range(449)]
with localcontext() as dc:
    dc.prec=900
    readings[plus]=['1e-193','0']
    readings[minus]=[str(Decimal('1e-193')+Decimal('1e-540')),'0']
low=a.receiver.Observer(precision_bits=192).evaluate(readings,conjugate=False)
high=o.evaluate(readings,conjugate=False)
def ball(text):return arb(text.replace('[','').replace(']',''))
assert ball(low['arithmetic_radius_upper_per_w_squared'])>1
assert ball(high['arithmetic_radius_upper_per_w_squared'])<arb('1e-200')
expected=-o.coefficients['crossed']*arb('1e-540')
assert (ball(high['value_per_w_squared'])-expected).contains(0)

# Worst-case projective truncation benchmark, not a necessary horizon bound:
# 2*K/sqrt(H) <= eta for unit total response norm, before head/sampling costs.
K=max(a.receiver.rational(b['tail_prefactor']) for b in bounds['bulk'])
horizon=(2*K/arb('1e-540'))**2
report={'schema':'marici.grothendieck.sampled-cubic-acquisition-tests.v1','passed':True,
        'conditional_weak_exponential_fixture_error':str(acquired['error']),
        'low_precision_arithmetic_radius':low['arithmetic_radius_upper_per_w_squared'],
        'high_precision_arithmetic_radius':high['arithmetic_radius_upper_per_w_squared'],
        'high_precision_recovered_difference':high['value_per_w_squared'],
        'unit_response_worst_case_sufficient_tail_horizon':str(horizon),
        'scope':'Analytical fixtures and conditional acquisition inequalities, NOT a measured positive-source certificate. Generic L2 tail control is computationally unusable at the target error; stronger source-specific tail and regularity budgets are required.'}
(a.receiver.RESULTS/'sampled-cubic-acquisition-tests.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
