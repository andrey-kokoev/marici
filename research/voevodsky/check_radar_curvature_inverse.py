"""Exact polarization, temporal-difference and noise-budget controls.
No claim that finite radar samples stably determine arbitrary curvature.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

def quad(g,v):return sum(v[i]*g[i][j]*v[j] for i in range(2) for j in range(2))
e1=(F(1),F(0));e2=(F(0),F(1));e12=(F(1),F(1))
checks={}
for i,g in enumerate((((F(2),F(1,3)),(F(1,3),F(1))),((F(1),F(-2,5)),(F(-2,5),F(3))))):
    q1,q2,q12=(quad(g,v) for v in (e1,e2,e12))
    recovered=((q1,(q12-q1-q2)/2),((q12-q1-q2)/2,q2))
    checks[str(i)+'_three_labelled_probes_reconstruct_metric']=recovered==g
    checks[str(i)+'_unlabelled_axis_swap_changes_result']=((q2,recovered[0][1]),(recovered[1][0],q1))!=g
    checks[str(i)+'_positive_metric']=g[0][0]>0 and g[0][0]*g[1][1]>g[0][1]**2
# Central second differences at a declared clock step, not an inverse oracle.
for h in (F(1,2),F(1,4),F(1,8)):
    d2=lambda fm,f0,fp:(fp-2*f0+fm)/(h*h)
    label=str(h)
    checks[label+'_constant_killed']=d2(F(3),F(3),F(3))==0
    checks[label+'_linear_killed']=d2(-h,F(0),h)==0
    checks[label+'_quadratic_recovered']=d2(h*h,F(0),h*h)==2
    checks[label+'_cubic_killed']=d2(-h**3,F(0),h**3)==0
    checks[label+'_quartic_bias_matches_bound']=d2(h**4,F(0),h**4)==2*h*h
    noise=F(1,1000)
    checks[label+'_adversarial_noise_amplification']=d2(noise,-noise,noise)==4*noise/(h*h)
# Exact Taylor coefficients of 2(1-cos z)/z^2: 1-z^2/12+z^4/360+...
checks['high_frequency_transfer_taylor']=(-2*F(-1,2),-2*F(1,24),-2*F(-1,720))==(F(1),F(-1,12),F(1,360))
# In the analytic proof cos(2*pi*m)=1 makes the transfer zero, while beta''(0)=1.
checks['period_alias_numerator_zero']=2*(1-F(1))==0
schedules=[]
for t in (F(1,2),F(1,4),F(1,8),F(1,16)):
    sigma=t**8;epsilon=t**4;h=t
    budget=(epsilon+sigma/epsilon)/(h*h)+h*h
    schedules.append(dict(t=str(t),distance_noise=str(sigma),baseline=str(epsilon),clock_step=str(h),leading_budget=str(budget)))
checks['conditional_resolution_schedule']=all(F(r['leading_budget'])==3*F(r['t'])**2 for r in schedules)
ratios=[F(1,2)/F(8,n*n) for n in (4,8,16,32)]
checks['hostile_required_inverse_constants_grow']=ratios==[F(1),F(4),F(16),F(64)]
root=Path(__file__).resolve().parents[2]
paths=[Path(__file__),root/'research/voevodsky/causal-radar-readout-is-c0-stable-in-the-plane-wave-sector.md',root/'research/voevodsky/tidal-readout-needs-second-jet-completion.md']
packet=dict(passed=all(checks.values()),checks=checks,schedules=schedules,
    scope='Finite exact inverse-algebra/stencil controls. Small-baseline theorem, instability and conditional error bound are written proofs. No admitted instrument bandwidth or empirical noise model.',
    source_sha256={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
Path(__file__).with_name('radar-curvature-inverse.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
