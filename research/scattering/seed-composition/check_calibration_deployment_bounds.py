"""Exact bias/drift-aware release gate and passing-calibration counterexamples."""
from fractions import Fraction as F
from math import comb
import argparse
import json

from check_finite_calibration_gate import audit as finite_audit,sqrt_sum_ge
from check_recycling_information_channel import qa,qn,qm as qmul,qr,qsign,qrecord
from check_five_cell_attachment_bridge import A as Coefficient,ONE,digest,BASE
from check_diagonal_spin_networks import S2

DEST=BASE/'results/calibration-deployment-bounds.v1.json'


def a11(x,y):return (x[0]+y[0],x[1]+y[1])
def m11(x,y):return (x[0]*y[0]+11*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def s11(x):
    a,b=x
    if not b:return (a>0)-(a<0)
    if not a:return (b>0)-(b<0)
    if a*b>0:return (a>0)-(a<0)
    return ((a>0)-(a<0))*((a*a>11*b*b)-(a*a<11*b*b))
def sqrt_sum_ge11(A,B,t):
    assert A>=0 and B>=0 and s11(t)>0
    t2=m11(t,t);remainder=(t2[0]-A-B,t2[1])
    if s11(remainder)<=0:return True
    squared=m11(remainder,remainder)
    return s11((4*A*B-squared[0],-squared[1]))>=0

def audit():
    previous=finite_audit();n=previous['declared_model']['probes'];epsilon=F(previous['confidence']['radius'])
    tail=F(previous['confidence']['certified_rational_upper_bound']);bias=F(1,100)
    cos_drift,sin_drift=F(2499,2501),F(100,2501);target=F(49,50)
    assert cos_drift*cos_drift+sin_drift*sin_drift==1 and cos_drift>target
    # cos(acos(49/50)-rho) = a+b sqrt11, since sin(acos(49/50))=3sqrt11/50.
    half_threshold=(target*cos_drift,F(3,50)*sin_drift)
    square=m11(half_threshold,half_threshold)
    endpoint_threshold=(2*square[0]-1,2*square[1])
    intervals=[];accepted=[]
    for old in previous['release_gate']['count_domain']:
        k=old['ones'];p_hat=F(k,n);lo=max(F(0),p_hat-epsilon-bias);hi=min(F(1),p_hat+epsilon+bias)
        A=(1-lo)*(1-hi);B=lo*hi
        decision=sqrt_sum_ge11(A,B,endpoint_threshold)
        # Expanded calibration interval and nonzero drift can only tighten
        # the original release decision under the same raw probe word.
        assert not decision or old['accept_fidelity_99_percent']
        if decision:accepted.append(k)
        intervals.append({'ones':k,'bias_expanded_p_interval':[str(lo),str(hi)],
                          'accept_with_bias_and_drift':decision,
                          'original_gate_accept':old['accept_fidelity_99_percent']})
    assert accepted and len(accepted)<len(previous['release_gate']['accepted_counts'])
    assert intervals[n//2]['accept_with_bias_and_drift']
    # Exact sampling validation concerns observed q, not true p. Widening
    # the population interval absorbs a known |q-p| bound without changing
    # the iid concentration budget for q.
    fixtures=[]
    for p,q in ((F(0),bias),(F(9,25),F(37,100)),(F(1,2),F(51,100)),(F(16,25),F(63,100)),(F(1),1-bias)):
        assert abs(p-q)<=bias
        total=F(0);noncoverage=F(0);accepted_noncoverage=F(0)
        for k,row in enumerate(intervals):
            mass=F(comb(n,k))*q**k*(1-q)**(n-k);total+=mass
            lo,hi=map(F,row['bias_expanded_p_interval'])
            if not lo<=p<=hi:
                noncoverage+=mass
                if row['accept_with_bias_and_drift']:accepted_noncoverage+=mass
        assert total==1 and accepted_noncoverage<=noncoverage<=tail
        fixtures.append({'true_pointer_population':str(p),'observed_population':str(q),
                         'bias':str(q-p),'exact_noncoverage_probability':str(noncoverage),
                         'exact_accepted_noncoverage_probability':str(accepted_noncoverage)})
    # The source-bound witnessed minus filter has k=sqrt19/5 and
    # lambda_min/lambda_max=(1-k)^2/(1+k^2+k).
    ratio=(F(2886,1461),F(-660,1461));alpha=qa(qr(1),qn(ratio))
    assert qsign(ratio)>0 and qsign(qa(qr(F(1,50)),qn(ratio)))>0
    # A small allowed population bias can invalidate the old gate even on
    # an observed-population coverage event; the new gate abstains.
    k=26;hat=F(k,n);q=hat+epsilon;p=q+bias
    assert previous['release_gate']['count_domain'][k]['accept_fidelity_99_percent']
    assert not intervals[k]['accept_with_bias_and_drift']
    oldlo,oldhi=map(F,previous['release_gate']['count_domain'][k]['p_interval'])
    assert oldlo==0 and oldhi==q and abs(q-p)==bias
    # beta_hat=asin(sqrt(q))/2, beta_true=asin(sqrt(p)), p<1/2.
    # cos(2*(beta_true-beta_hat))=sqrt(A)+sqrt(B).
    A=(1-2*p)**2*(1-q);B=4*p*(1-p)*q
    assert p<F(1,2) and p>q
    assert not sqrt_sum_ge(A,B,F(2207,2401))
    # Therefore actual visibility d<48/49. With alpha>49/50,
    # infidelity alpha*(1-d)/2>1/100, strictly below target fidelity.
    assert qsign(qa(alpha,qr(F(-49,50))))>0
    # Passing calibration with deployment-only drift: population 1/2 then
    # deployed population 1. The midpoint is pi/4, visibility 1/sqrt2.
    assert previous['release_gate']['count_domain'][n//2]['accept_fidelity_99_percent']
    fidelity_constant=ONE-Coefficient(alpha[0])*(ONE-S2/2)/2
    fidelity_sqrt19=-Coefficient(alpha[1])*(ONE-S2/2)/2
    assert F(2)>F(16,9)  # 1/sqrt2<3/4, so F<1-(49/50)/8=351/400.
    assert F(351,400)<F(99,100)
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_calibration_deployment_bounds.py'}
    return {
        'schema':'marici.scattering.calibration-deployment-bounds.v1',
        'status':'sampling_confidence_does_not_cover_bias_or_drift_declared_bounds_tighten_release_exact_counterexamples_retained',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'declared_bounds':{'readout_bias':'|q_observed-p_calibration|<=1/100',
                            'deployment_angle_drift':'|beta_deploy-beta_calibration|<=rho',
                            'cos_rho':str(cos_drift),'sin_rho':str(sin_drift),
                            'within_calibration_iid_observed_q':True,'exact_feedback_phase_assumed':True,
                            'these_bounds_measured_or_source_derived':False},
        'robust_gate':{'population_interval':'[max(0,k/n-epsilon-bias),min(1,k/n+epsilon+bias)]',
                        'feedback':'midpoint of expanded calibration angular interval',
                        'worst_angle':'h+rho, h=(beta_high-beta_low)/2; conservative even when deployment interval clips at endpoints',
                        'release':'cos(h+rho)>=49/50',
                        'equivalent_endpoint_threshold':{'constant':str(endpoint_threshold[0]),'sqrt11':str(endpoint_threshold[1])},
                        'comparison':'exact sign tests in Q(sqrt11), with positive squared-radical reduction',
                        'accepted_counts':accepted,'count_domain':intervals,
                        'guaranteed_Bell_fidelity_on_coverage_and_declared_bounds':'99/100',
                        'sampling_noncoverage_budget_unchanged':str(tail),
                        'model_or_drift_bound_violation_included_in_sampling_budget':False,
                        'population_fixtures':fixtures},
        'counterexamples':{'small_bias':{'count':k,'observed_q':str(q),'true_p':str(p),'readout_bias':str(q-p),
                                        'observed_q_inside_original_interval':True,'old_release':True,'new_release':False,
                                        'source_minus_ratio':qrecord(ratio),
                                        'actual_visibility_upper_bound':'48/49, strict',
                                        'actual_Bell_fidelity':'strictly below 99/100 by exact rational/radical inequalities',
                                        'assumption_breaking_old_gate':'ideal unbiased population readout; new declared bias bound is respected'},
                           'deployment_drift':{'count':n//2,'calibration_p':'1/2','deployment_p':'1','old_release':True,
                                                'deployment_visibility':'1/sqrt2',
                                                'exact_Bell_fidelity':{'constant':fidelity_constant.record(),'sqrt19':fidelity_sqrt19.record()},
                                                'strict_fidelity_upper_bound':'351/400 < 99/100',
                                                'assumption_breaking':'constant parameter; this large drift is outside the new declared rho bound'}},
        'risk_accounting':{'all_probe_count_and_abstention_records_retained':True,
                           'unconditional_P_release_and_bad_fidelity':'<=sampling tail only if bias/drift/control assumptions hold',
                           'conditional_on_release_same_confidence_automatically':False,
                           'earlier_history_or_pointer_records_erased':False},
        'boundary':{'bias_drift_control_supply_are_inputs':True,'physical_noise_or_platform_verified':False,
                    'formal_contract_or_outcome_admitted':False},
        'next_gate':'Construct a finite repeated-calibration confidence-spending schedule under these bounds. Test stopping at first release without reusing the single-window failure budget, retaining all rejected probe windows and the deployment/control assumptions.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale deployment receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact bias/drift-aware release gate preserves the sampling budget only under declared model bounds.')
    print('PASS: passing old calibration can fail deployment fidelity; small-bias and drift counterexamples retain all assumptions and outcomes.')


if __name__=='__main__':main()
