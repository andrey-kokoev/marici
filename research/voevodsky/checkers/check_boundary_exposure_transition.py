"""Sensitivity of common-vacuum energies to boundary exposure.

lambda is an electric lead conductance, not a fitted mass parameter. Outer
mode leads have conductance one on both carriers. The belt's middle modes
have conductance lambda; their electric cost is beta*E^2/(2*lambda).
Exact convex derivatives bracket the global sector minimum and its crossing.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
from check_belt_interface_response import inverse

BASE=Path(__file__).resolve().parents[1]
O=F(2386,675)
M=F(4198,675)
A=M/(O+M)
B=2*O/(O+M)


def state(t):
    y=6*M*t*t/(12*O+6*M*t*t)
    matter=12*O*M/(O+M)*(1-t)**2/(12*O+6*M*t*t)
    return y,matter


def field(y,exposure):
    return ((exposure+2)*(1-y)**2+4*y)/(48*(exposure+1))


def derivative(t,exposure,beta):
    y,_=state(t)
    return B*(1-1/t)-A*(1-t)+beta*(2*(exposure+2)*y-2*exposure)/(48*(exposure+1))


def minimum(exposure,beta,steps=65):
    # derivative increases with y, and y increases with t. Endpoint signs
    # and strict convexity certify a unique global interior density minimum.
    lo=F(0);hi=F(2)
    assert derivative(hi,exposure,beta)>0
    for _ in range(steps):
        t=(lo+hi)/2
        if derivative(t,exposure,beta)<0:lo=t
        else:hi=t
    yl,ml=state(lo);yh,mh=state(hi)
    fl=ml+beta*(field(yl,exposure)-F(1,24))
    fh=mh+beta*(field(yh,exposure)-F(1,24))
    lower=max(fl+derivative(lo,exposure,beta)*(yh-yl),fh+derivative(hi,exposure,beta)*(yl-yh))
    t=(lo+hi)/2;y,matter=state(t)
    upper=matter+beta*(field(y,exposure)-F(1,24))
    assert lower<=upper
    return lower,upper,t,y


def main():
    source_path=BASE/'results/open_flux_common_vacuum.json'
    source_raw=source_path.read_bytes();source=json.loads(source_raw)
    assert source['verification_passed'] and source['same_vacuum_admitted']
    adapter=json.loads((BASE/'results/weighted_matter_link_adapter.json').read_text())['carriers']['belt']
    weights=list(map(F,adapter['metric_weights']))
    edges=[(i,j) for i,j,_ in adapter['edges']]
    for exposure in (F(1,10),F(1,4),F(1)):
        L=[[F(0)]*18 for _ in range(18)]
        for i,j in edges:
            L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
        for i in range(18):L[i][i]+=exposure if i%3==1 else 1
        Linv=inverse(L)
        for t in (F(1,2),F(1)):
            y,_=state(t)
            rho=[y/6 if i%3==1 else (1-y)/12 for i in range(18)]
            phi=[sum(x*r for x,r in zip(row,rho)) for row in Linv]
            assert sum(r*p for r,p in zip(rho,phi))/2==field(y,exposure)
            E_internal=[phi[j]-phi[i] for i,j in edges]
            E_boundary=[(exposure if i%3==1 else 1)*phi[i] for i in range(18)]
            assert sum(E_boundary)==1
            assert (sum(e*e for e in E_internal)+sum(e*e/(exposure if i%3==1 else 1) for i,e in enumerate(E_boundary)))/2==field(y,exposure)
    # The derivative of eliminated electric energy wrt exposure is negative:
    # d field/d lambda = -(1+y)^2/[48*(1+lambda)^2]. Thus optimized belt
    # energy decreases strictly with exposure; proton energy is unchanged.
    # A coherent belt trial becomes exactly equal to the proton at lambda0.
    y0=state(F(1))[0]
    lambda0=2*y0*y0/(1+2*y0-y0*y0)
    assert field(y0,lambda0)==F(1,24)
    assert lambda0==F(4405801,17268727)
    assert y0!=lambda0/(lambda0+2)
    # At lambda0 the coherent trial is NOT stationary, so relaxation lowers
    # the energy strictly below the proton. The true crossing is below it.
    results=[]
    for beta in (F(3,5),F(1),F(6)):
        assert minimum(F(0),beta)[0]>0
        assert minimum(lambda0,beta)[1]<0
        lo=F(0);hi=lambda0
        for _ in range(45):
            exposure=(lo+hi)/2
            lower,upper,_,_=minimum(exposure,beta)
            if lower>0:lo=exposure
            elif upper<0:hi=exposure
            else:raise AssertionError('Increase rational minimum precision')
        assert minimum(lo,beta)[0]>0>minimum(hi,beta)[1]
        points=[]
        for exposure in (F(0),F(1,10),F(1,4),F(1,2),F(1)):
            lower,upper,t,y=minimum(exposure,beta)
            points.append({'exposure':str(exposure),'belt_minus_proton_interval':[str(lower),str(upper)],
                           'difference_decimal':float((lower+upper)/2),
                           'amplitude_ratio_decimal':float(t),'middle_density_fraction':float(y)})
        results.append({'beta':str(beta),'critical_exposure_interval':[str(lo),str(hi)],
                        'critical_exposure_decimal':float((lo+hi)/2),
                        'controls':points})
    report={'verification_passed':True,
            'boundary_family':'Twelve outer leads at unit conductance on each carrier; six belt middle leads at common conductance lambda>=0.',
            'electric_energy_convention':'beta/2*sum_internal E^2 + beta/2*sum_outer E^2 + beta/(2*lambda)*sum_middle E^2; middle leads omitted at lambda=0',
            'vacuum_rule_unchanged':'zero background, common exterior charge q_ext=-(Qp+Qb), exterior energy eta*q_ext^2/2 retained',
            'eliminated_field_coefficient':'[(lambda+2)*(1-y)^2+4*y]/[48*(lambda+1)]',
            'sector_difference':'min_y (sqrt(A*(1-y))-sqrt(B*y))^2 + beta*(field(y,lambda)-1/24); A=2099/3292, B=1193/1646',
            'strict_exposure_monotonicity':'d field/d lambda=-(1+y)^2/[48*(1+lambda)^2]<0',
            'unique_crossing_for_each_beta_positive':True,
            'coherent_trial_zero_exposure_exact':str(lambda0),
            'actual_critical_exposure_strictly_below_coherent_trial_threshold':True,
            'illustrative_crossings':results,
            'physical_boundary_law_selected':False,
            'no_mass_fit_or_electron_normalization':True,
            'scope':'Quantifies boundary sensitivity in the already declared classical fixed-norm model, not a quantum vacuum or physical mass prediction.',
            'source_sha256':sha256(source_raw).hexdigest()}
    (BASE/'results/boundary_exposure_transition.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='illustrative_crossings'},indent=2))
    print(json.dumps([{k:v for k,v in row.items() if k!='controls'} for row in results],indent=2))


if __name__=='__main__':main()
