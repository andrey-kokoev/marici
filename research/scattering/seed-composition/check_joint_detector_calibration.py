"""Joint reference-pointer calibration with contrast, confidence and coherent-model gates."""
from fractions import Fraction as F
from itertools import product
import argparse
import json

from check_calibration_model_error_floor import audit as floor_audit
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,eye,record,digest,BASE
from check_diagonal_spin_networks import S2

DEST=BASE/'results/joint-detector-calibration.v1.json'


def sign_radical(x,radicand):
    a,b=x
    if not b:return (a>0)-(a<0)
    if not a:return (b>0)-(b<0)
    if a*b>0:return (a>0)-(a<0)
    return ((a>0)-(a<0))*((a*a>radicand*b*b)-(a*a<radicand*b*b))
def mul_radical(x,y,d):return (x[0]*y[0]+d*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def clipped(x):return min(F(1),max(F(0),x))
def interval(k,n,epsilon):
    assert isinstance(k,int) and 0<=k<=n
    return (max(F(0),F(k,n)-epsilon),min(F(1),F(k,n)+epsilon))
def pointer_interval(q,a,b):
    slope=1-a[1]-b[1]
    if slope<=0:return None
    return (clipped((q[0]-a[1])/(1-a[1]-b[0])),clipped((q[1]-a[0])/(1-a[0]-b[1])))
def nearest_count(p,n):
    x=n*p;return (2*x.numerator+x.denominator)//(2*x.denominator)


def audit():
    previous=floor_audit();epsilon=F(1,2000);total_delta=F(1,1000);allocated=total_delta/3
    m=0
    while F(2,2**m)>allocated:m+=1
    desired=F(m,2*epsilon*epsilon);n=(desired.numerator+desired.denominator-1)//desired.denominator
    tail=F(2,2**m);assert 2*n*epsilon*epsilon>=m and 3*tail<=total_delta
    assert n==26000000 and m==13 and 3*tail==F(3,4096)
    min_slope=F(19,20);max_population_width=4*epsilon/min_slope
    assert max_population_width==F(1,475)
    # New target 99.9%, preserving the inherited drift margin. Exact
    # threshold cos(acos(499/500)-rho) lies in Q(sqrt111).
    target=F(499,500);c,s=F(2499,2501),F(100,2501)
    assert c>target and c*c+s*s==1
    hthreshold=(target*c,F(3,500)*s)
    hsq=mul_radical(hthreshold,hthreshold,111)
    endpoint=(2*hsq[0]-1,2*hsq[1]);esq=mul_radical(endpoint,endpoint,111)
    assert sign_radical((1-max_population_width-esq[0],-esq[1]),111)>0
    assert sign_radical(endpoint,111)>0
    fixtures=[];enclosure_tests=0;corner_tests=0
    for a,b,p in product((F(0),F(1,100),F(1,5),F(49,100)),
                         (F(0),F(1,100),F(1,5),F(49,100)),
                         (F(0),F(1,100),F(1,99),F(1,2),F(99,100),F(1))):
        q=a+(1-a-b)*p
        counts={'known_zero_ones':nearest_count(a,n),'known_one_misses':nearest_count(b,n),'copy_pointer_ones':nearest_count(q,n)}
        aa=interval(counts['known_zero_ones'],n,epsilon);bb=interval(counts['known_one_misses'],n,epsilon);qq=interval(counts['copy_pointer_ones'],n,epsilon)
        result=pointer_interval(qq,aa,bb);assert result is not None and result[0]<=p<=result[1]
        assert aa[0]<=a<=aa[1] and bb[0]<=b<=bb[1] and qq[0]<=q<=qq[1]
        slope=1-aa[1]-bb[1];release=slope>=min_slope
        if release:assert result[1]-result[0]<=max_population_width
        for qc,ac,bc in product(qq,aa,bb):
            pc=clipped((qc-ac)/(1-ac-bc))
            assert result[0]<=pc<=result[1];corner_tests+=1
        enclosure_tests+=1
        if p in (F(0),F(1,99),F(1,2)) and a in (F(0),F(1,100),F(49,100)) and b in (F(0),F(1,100),F(49,100)):
            fixtures.append({'a':str(a),'b':str(b),'p':str(p),'q':str(q),'fixture_counts':counts,
                             'a_interval':list(map(str,aa)),'b_interval':list(map(str,bb)),'q_interval':list(map(str,qq)),
                             'certified_slope_lower_bound':str(slope),'pointer_interval':list(map(str,result)),
                             'release_999_1000_fidelity':release,'counts_are_ideal_simulated_not_observed':True})
    # The two previous indistinguishable q=1/100 models now have different
    # reference-probe populations and disjoint confidence-box p intervals.
    resolved=[]
    for model in previous['admissible_nuisance_models']:
        a=F(model['false_positive_a']);b=F(model['false_negative_b']);q=F(model['observed_population'])
        aa=interval(nearest_count(a,n),n,epsilon);bb=interval(nearest_count(b,n),n,epsilon);qq=interval(nearest_count(q,n),n,epsilon)
        pi=pointer_interval(qq,aa,bb);assert pi is not None
        resolved.append({'model':model['name'],'known_zero_population':str(a),'known_one_miss_population':str(b),
                         'pointer_interval':list(map(str,pi))})
    assert F(resolved[0]['pointer_interval'][1])<F(resolved[1]['pointer_interval'][0])
    # Honest abstention at uninformative or uncertified detector contrast.
    no_contrast=pointer_interval((F(1,2),F(1,2)),(F(1,2),F(1,2)),(F(1,2),F(1,2)))
    assert no_contrast is None
    # A coherent detector has the same known-zero/known-one populations
    # but an additional superposition cross term. This cannot be inferred
    # from those two reference streams and must not be called calibrated.
    a=b=F(1,200);z=F(1,200)
    E=((A(a),A(z)),(A(z),A(1-b)));complement=add(eye(2),scale(A(-1),E))
    assert adj(E)==E and adj(complement)==complement
    assert a*(1-b)-z*z>0 and (1-a)*b-z*z>0
    plus=((S2/2,),(S2/2,));q_observed=mm(mm(adj(plus),E),plus)[0][0]
    assert q_observed==A(F(101,200))
    aa=interval(nearest_count(a,n),n,epsilon);bb=interval(nearest_count(b,n),n,epsilon)
    qq=interval(nearest_count(F(101,200),n),n,epsilon);wrong=pointer_interval(qq,aa,bb)
    assert wrong is not None and wrong[0]>F(1,2)
    assert 1-aa[1]-bb[1]>=min_slope
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_joint_detector_calibration.py'}
    return {
        'schema':'marici.scattering.joint-detector-calibration.v1',
        'status':'joint_reference_probes_resolve_diagonal_detector_bias_with_retained_confidence_and_contrast_gate_coherent_detector_requires_more_observables',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'declared_detector_model':{'effect_one':'diag(a,1-b)','pointer_copy_population':'q=a+(1-a-b)p',
                                  'diagonal_detector_assumption_is_source_or_device_derived':False,
                                  'same_detector_parameters_across_all_streams_required':True,
                                  'reference_preparations':'separately supplied pointer |0> and |1>; not the unknown copy state',
                                  'ordered_records':['known-zero Z outcomes','known-one Z outcomes, with miss count derived','pointer-copy Z outcomes']},
        'joint_confidence':{'radius_each_stream':str(epsilon),'allocated_budget_each_stream':str(allocated),
                            'probes_each_stream':n,'total_probes':3*n,'integer_exponent':m,
                            'certified_tail_each_stream':str(tail),'joint_noncoverage_upper_bound':str(3*tail),
                            'between_stream_independence_required_for_union_bound':False,
                            'each_stream_iid_and_preparation_model_required':True,
                            'probing_stop_budget_is_reusable_without_spending':False},
        'interval_and_conditioning':{'formula':'p_low=clip((q_low-a_high)/(1-a_high-b_low)); p_high=clip((q_high-a_low)/(1-a_low-b_high))',
                                     'slope_lower':'1-a_high-b_high','uncertified_or_nonpositive_slope':'abstain; retain all records',
                                     'release_contrast_threshold':'19/20',
                                     'universal_width_bound':'4epsilon/slope_lower<=1/475',
                                     'argument':'along the interval-extreme path, clipped inverse derivatives are bounded by [delta q+(1-p)|delta a|+p delta b]/slope_lower',
                                     'enclosure_fixtures':enclosure_tests,'corner_checks':corner_tests,
                                     'retained_fixtures':fixtures},
        'residual_drift_release':{'target_Bell_undo_fidelity':'999/1000','cos_rho':'2499/2501','sin_rho':'100/2501',
                                  'control_estimate':'angular midpoint of corrected p interval',
                                  'endpoint_visibility_threshold':{'constant':str(endpoint[0]),'sqrt111':str(endpoint[1])},
                                  'width_certificate':'sqrt(1-1/475) exceeds the exact drift-aware threshold',
                                  'joint_confidence_and_contrast_release_imply_target':True,
                                  'unconditional_bad_release_bound_given_model':str(3*tail),
                                  'same_bound_conditional_on_contrast_release_automatically':False,
                                  'drift_only_9999_10000_obstruction_removed':False},
        'resolved_old_ambiguity':resolved,
        'coherent_detector_counterexample':{'effect_one':record(E),'effect_zero':record(complement),
                                           'positive_complete_POVM':True,'known_zero_population':'1/200','known_one_miss_population':'1/200',
                                           'true_plus_pointer_population':'1/2','observed_copy_population':'101/200',
                                           'diagonal_model_interval':list(map(str,wrong)),
                                           'true_pointer_excluded_even_when_all_three_population_intervals_cover':True,
                                           'certified_diagonal_contrast_would_pass':True,
                                           'diagnosis':'reference zero/one probes identify diagonals, not off-diagonal detector coherence',
                                           'actual_fidelity_violation_claimed_from_this_example':False},
        'boundary':{'new_reference_preparation_readout_and_probe_work_required':True,
                    'physical_observations_or_detector_diagonality_verified':False,
                    'all_raw_data_and_abstentions_required_records':True,
                    'physical_spin_or_preparation_admitted':False,'formal_contracts_or_outcomes_changed':False},
        'next_gate':'Test detector tomographic completeness with known superposition probes and a controlled pointer phase flip. Determine whether phase-cycled populations remove off-diagonal coherence without silently assuming diagonality; retain confidence, contrast, phase-control and deployment-drift obligations.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale joint calibration receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact joint reference/pointer intervals, simultaneous confidence and contrast-conditioned 99.9% drift-aware gate.')
    print('PASS: old diagonal nuisance models separate; coherent POVM counterexample keeps detector diagonality and tomography open.')


if __name__=='__main__':main()
