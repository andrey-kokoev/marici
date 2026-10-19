"""Exact rational interval certificate; supplied bounds, no measurements."""
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]

def positive_interval(x):
    if len(x)!=2 or not 0<x[0]<=x[1]:raise ValueError('invalid positive interval')
def posterior_bounds(shape,rate,factor):
    positive_interval(rate)
    if shape<=0 or not 0<=factor[0]<=factor[1]<=1:raise ValueError('invalid posterior bounds')
    return (factor[0]*shape/rate[1],factor[1]*shape/rate[0],factor[1]**2*shape/rate[0]**2)

def certificate(shapes,rates,factors,q_bounds,h,epsilon,delta):
    if not 0<=q_bounds[0]<=q_bounds[1]<=1 or h<0 or epsilon<=0 or not 0<delta<1:raise ValueError('invalid task/control bounds')
    if any(len(x)!=2 for x in (shapes,rates,factors)):raise ValueError('two-mode context required')
    lo=hi=variance=F(0)
    for i,(k,r,f) in enumerate(zip(shapes,rates,factors)):
        mlo,mhi,vhi=posterior_bounds(k,r,f)
        exponent=2 if i==0 else 4
        lo+=q_bounds[0]**exponent*mlo
        hi+=q_bounds[1]**exponent*mhi
        variance+=q_bounds[1]**(2*exponent)*vhi
    bias=max(abs(lo-h),abs(hi-h))
    bound=None if bias>=epsilon else min(F(1),variance/(epsilon-bias)**2)
    return {'mean_interval':(lo,hi),'variance_upper':variance,'bias_upper':bias,
            'tail_bound':bound,'status':'certified' if bound is not None and bound<=delta else 'abstain'}

K=F(100000);rates=[(K*F(999,1000),K*F(1001,1000))]*2
factors=[(F(1),F(1))]*2
h=F(5,16);epsilon=h/4;delta=F(1,20)
tight=certificate([K,K],rates,factors,(F(499,1000),F(501,1000)),h,epsilon,delta)
wide=certificate([K,K],rates,factors,(F(2,5),F(3,5)),h,epsilon,delta)
checks={'tight_declared_regime_certifies':tight['status']=='certified',
        'wide_gain_bounds_abstain':wide['status']=='abstain',
        'systematic_bias_not_zero':tight['bias_upper']>0}
corner_checks=[]
for r1,r2,q in itertools.product(rates[0],rates[1],(F(499,1000),F(501,1000))):
    mean=q*q*K/r1+q**4*K/r2
    var=q**4*K/r1**2+q**8*K/r2**2
    corner_checks.append(tight['mean_interval'][0]<=mean<=tight['mean_interval'][1] and var<=tight['variance_upper'])
checks['all_corner_moments_enclosed']=all(corner_checks)
# Exposure bounds for uncertain detector efficiency/tap/preceding signal factor.
eta=(F(3,4),F(4,5));tau=(F(1,5),F(1,4));factor=(F(1,2),F(3,4))
exposure=(eta[0]*tau[0]*factor[0],eta[1]*tau[1]*factor[1])
checks['efficiency_exposure_enclosure']=all(exposure[0]<=e*t*f<=exposure[1] for e,t,f in itertools.product(eta,tau,factor))
checks['tap_survival_interval']=(1-tau[1])*factor[0]<=(1-tau[0])*factor[1]
invalid=False
try:posterior_bounds(K,(F(0),F(1)),(F(1),F(1)))
except ValueError:invalid=True
checks['zero_rate_bound_rejected']=invalid
out={'schema':'marici.sontag.optical-calibration-bounds.v1','passed':all(checks.values()),
 'scope':'conditional Gamma/coherent preparation-mean risk, independently supplied interval assumptions',
 'checks':checks,'tight':tight,'wide':wide,
 'empirical_calibration_supplied':False,'counts_precision_certified':False}
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
p=ROOT/'research/sontag/results/optical-calibration-bounds-v1.json'
p.write_text(json.dumps(encode(out),indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':out['passed'],'checks':len(checks),'tight':tight['status'],'wide':wide['status']},indent=2))
raise SystemExit(0 if out['passed'] else 1)
