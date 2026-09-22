"""Fixed-prior next-observation certificate; no physical acquisition claimed."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import json
from flint import arb

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('task',HERE/'certify_noisy_attachment_task.py')
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
A=t.A


def main():
    eta=12;budget=Q(40);bc=Q(1,100);vr=Q(1,1000)
    K={a:t.c.scaled_residual(a) for a in (2,12,20)}
    E0=K[2]*K[12]*(-arb.pi()*148).exp()/5
    Ex=K[2]*K[20]*(-arb.pi()*404).exp()/5
    m0=Q(str(E0.mid().fmpq()));mx=Q(str(Ex.mid().fmpq()))
    z0=(m0,m0/10);zx=(Q(0),mx/100)
    amin=t.endpoints(t.interval(*z0)/E0)[0]
    cmax=t.endpoints(t.interval(*zx)/Ex)[1]
    bmin=bc-vr;B=budget-32*amin-8*bmin
    q3=Q(3,2)**eta;q4=Q(2)**eta
    mu={a:t.r.moments(a) for a in (2,4,12,60)}
    s0=(mu[4]-mu[2])*(mu[60]-mu[12])/18
    sx=-(mu[2]-t.c.L)*(mu[60]-t.c.L)/18
    R=t.endpoints((1+arb(3).log())**2/(32*A(q3)))[1]
    sl=t.endpoints(s0)[0];xl=t.endpoints(sx)[0]
    cross=min(cmax,B/32) if xl+32*R<0 else Q(0)
    residual_lower=sl*amin+xl*cross-R*(B-32*cross)
    assert residual_lower>0
    eps=Q(1,1000)
    assert 8*q3*eps<B
    vacuum_lower=bmin-eps-(B-8*q3*eps)/(8*q4)
    assert vacuum_lower>0
    radius_threshold=(bmin-B/(8*q4))/(1-q3/q4)
    assert eps<radius_threshold and radius_threshold<B/(8*q3)
    # Positive witness: a0=1, ax=0, b2=.01; all unacquired coefficients zero.
    assert abs(E0-A(m0))<=A(m0/10)
    assert 32+8*bc<budget
    # Actual old negative witness, robustly compatible with all calibration values.
    el,eh=t.endpoints(E0)
    alo=(m0-m0/10)/el;ahi=(m0+m0/10)/eh
    a=alo+(ahi-alo)/1000;b=bmin+2*vr/1000
    assert abs(A(a)*E0-A(m0))<=A(m0/10) and abs(b-bc)<=vr
    tail=-(budget-32*a-8*b)/(8*q3)
    assert 32*a+8*b+8*q3*abs(tail)==budget
    assert b+tail<0 and abs(tail)>eps and abs(tail)<Q(1,50)
    result={'passed':True,'prior':'sum_A (A/2)^12 p(x_A)<=40',
        'background_domain':'integer arithmetic backgrounds A>=2',
        'baseline_raw_inputs':{'z0':list(map(str,z0)),'zx':list(map(str,zx)),
                               'u2':['1/100','1/1000']},
        'recommended_conditional_acquisition':{'background':3,'channel':'unit vacuum',
            'returned_interval':['-1/1000','1/1000'],'status':'SUFFICIENT_PLAN',
            'vacuum_sum_lower_bound':t.decimal_bounds(A(vacuum_lower))['lower'],
            'normalized_residual_sum_lower_bound':t.decimal_bounds(A(residual_lower))['lower']},
        'zero_centered_radius_sufficient_threshold':str(radius_threshold),
        'threshold_decimal_enclosure':t.decimal_bounds(A(radius_threshold)),
        'negative_source_witness':{'a0_at_2':str(a),'b_at_2':str(b),'b_at_3':str(tail)},
        'negative_source_vacuum_sum':t.decimal_bounds(A(b+tail)),
        'controls':{'A3_interval_plus_minus_1_over_50':'AMBIGUOUS: both witnesses remain compatible',
                    'A4_interval_plus_minus_1_over_1000':'AMBIGUOUS: both witnesses have b4=0'},
        'scope':'Conditional on the newly acquired interval containing the true scalar value, including all acquisition errors. A3 vacuum acquisition does not determine its residual coordinates. No source prior is strengthened; no experimental reading is asserted.'}
    out=HERE.parent/'results/next-vacuum-acquisition.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('passed','prior','recommended_conditional_acquisition',
        'threshold_decimal_enclosure','negative_source_vacuum_sum','controls')},indent=2))


if __name__=='__main__':main()
