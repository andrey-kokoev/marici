"""Observationally indistinguishable detector/drift models and irreducible eraser error."""
from fractions import Fraction as F
from itertools import product
import argparse
import json

from check_calibration_precision_refinement import audit as refinement_audit
from check_recycling_information_channel import qa,qn,qr,qsign,qrecord
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,eye,record,digest,BASE

DEST=BASE/'results/calibration-model-error-floor.v1.json'


def audit():
    previous=refinement_audit();bias=F(1,100);c,s=F(2499,2501),F(100,2501)
    # Valid binary detector: q=a+(1-a-b)p; a is false positive, b false
    # negative. Both examples even obey a global population-bias bound.
    model_specs=[('false_positive',bias,F(0),F(0)),('false_negative',F(0),bias,F(1,99))]
    models=[]
    for name,a,b,p in model_specs:
        assert 0<=a<=bias and 0<=b<=bias and 0<=p<=1
        slope=1-a-b;observed=a+slope*p
        assert observed==F(1,100) and abs(observed-p)<=bias
        E1=((A(a),ZERO),(ZERO,A(1-b)));E0=((A(1-a),ZERO),(ZERO,A(b)))
        assert all(E[i][i].c[0]>=0 for E in (E0,E1) for i in range(2))
        assert tuple(tuple(E0[i][j]+E1[i][j] for j in range(2)) for i in range(2))==eye(2)
        # Complete projective diagonal effects define a legitimate detector
        # POVM; no instrument or microscopic hardware is claimed.
        for ptest in (F(0),F(1,99),F(1,2),F(1)):
            q=a+slope*ptest;assert abs(q-ptest)<=bias
        models.append({'name':name,'false_positive_a':str(a),'false_negative_b':str(b),
                       'true_calibration_population':str(p),'observed_population':'1/100',
                       'detector_effect_zero':record(E0),'detector_effect_one':record(E1),
                       'globally_bounded_population_bias_argument':'q-p=a(1-p)-b*p, so |q-p|<=max(a,b)<=1/100',
                       'deployment_angle':'0' if p==0 else 'asin(sqrt(1/99))+rho',
                       'deployment_drift':'0' if p==0 else 'rho'})
    histories=[];q=F(1,100)
    for n in (1,2,4,6):
        total=F(0);entries=[]
        for word in product((0,1),repeat=n):
            ones=sum(word);likelihood=q**ones*(1-q)**(n-ones);total+=likelihood
            # Both models have the same law for every retained ordered word.
            assert likelihood>0
            entries.append({'ordered_probe_record':list(word),'both_model_likelihood':str(likelihood)})
        assert total==1
        histories.append({'independent_probes':n,'total_likelihood':'1','records':entries})
    ratio=(F(2886,1461),F(-660,1461));alpha=qa(qr(1),qn(ratio))
    assert qsign(ratio)>0 and qsign(qa(qr(F(1,50)),qn(ratio)))>0
    assert qsign(qa(alpha,qr(F(-49,50))))>0
    # Model angles differ by Delta=asin(sqrt(1/99))+rho, in (0,pi/2).
    # cos Delta=(2499 sqrt98-100)/(2501 sqrt99). Compare it strictly
    # to 2*(489/490)^2-1, using only positive rational squaring.
    threshold=2*F(489,490)**2-1
    assert threshold==F(119071,120050)
    right_coefficient=2501*threshold
    assert 2499**2*98>100**2  # positive cos gap; Delta is below pi/2
    remainder=2499**2*98-100**2-99*right_coefficient**2
    assert remainder<0 or remainder**2<4*100**2*99*right_coefficient**2
    # Hence cos(Delta/2)<489/490. At least one indistinguishable model
    # is farther than the half-gap from any common feedback angle. On the
    # source minus witness, alpha>49/50 then forces infidelity>1/1000.
    assert F(49,50)*(1-F(489,490))/2==F(1,1000)
    # Even perfect detector/source calibration cannot remove unknown drift
    # ±rho around pi/4: identical calibration laws, deployment gap 2rho.
    drift_floor_lower=F(49,50)*(1-c)/2
    assert drift_floor_lower==F(49,125050) and drift_floor_lower>F(1,10000)
    # An exact, sampling-free population interval still has nonzero width
    # under detector bias. The existing robust midpoint rule retains that
    # width and its rho margin as epsilon tends to zero.
    residual_population_interval=[F(0),F(1,50)]
    assert residual_population_interval[1]-residual_population_interval[0]==2*bias
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_calibration_model_error_floor.py'}
    return {
        'schema':'marici.scattering.calibration-model-error-floor.v1',
        'status':'identical_Z_calibration_laws_with_valid_bounded_detectors_obstruct_stricter_uniform_fidelity_even_at_infinite_sample_precision',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'admissible_nuisance_models':models,
        'observational_equivalence':{'calibration_q':'1/100','all_iid_Z_word_likelihoods_identical':True,
                                     'finite_record_checks':histories,
                                     'eraser_Y_label_laws_identical':'both 1/2, as previously verified for every actual/estimated pair',
                                     'more_allowed_records_identify_model':False,
                                     'scope':'iid Z-pointer population probes and input-independent Y eraser labels; not additional detector tomography, known-input phase probes, or coherent gate access'},
        'strict_target_obstruction':{'source_minus_ratio':qrecord(ratio),'source_minus_alpha_lower_bound':'49/50, strict',
                                     'deployment_angle_gap':'Delta=asin(sqrt(1/99))+rho',
                                     'cos_gap':'(2499*sqrt(98)-100)/(2501*sqrt(99))',
                                     'cos_gap_exact_upper_bound':'119071/120050, strict',
                                     'best_common_worst_visibility_upper_bound':'489/490, strict',
                                     'best_common_worst_Bell_infidelity_lower_bound':'1/1000, strict',
                                     'uniform_999_1000_fidelity_from_more_Z_probes_alone':False,
                                     'argument':'the same observation law produces a common control-policy distribution; the two target-good angle sets are disjoint',
                                     'randomized_policy_limit':'at least one model has success probability <=1/2 if always released',
                                     'abstaining_policy_limit':'to keep bad-release probability <=delta in both models, common release probability must be <=2delta',
                                     'for_delta_1_1000_maximum_common_release_probability':'1/500'},
        'drift_only_floor':{'ideal_detector_and_exact_calibration_population':'p=q=1/2',
                            'deployment_models':'beta=pi/4-rho or pi/4+rho, both allowed',
                            'optimal_common_worst_visibility':'cos(rho)=2499/2501',
                            'source_witness_infidelity_lower_bound':str(drift_floor_lower),
                            'uniform_9999_10000_fidelity_without_tighter_drift_or_deployment_information':False},
        'zero_sampling_radius_limit':{'population_interval_at_observed_q_1_100':['0','1/50'],
                                      'bias_and_drift_uncertainty_vanish':False,
                                      'preceding_99_100_release_certificate_invalidated':False,
                                      'reason':'99% is a weaker target and remains conditionally certified; more probes remove sampling uncertainty, not nuisance-model ambiguity'},
        'additional_information_gate':{'known_pointer_zero_probe_population':'a',
                                       'known_pointer_one_probe_population':'1-b',
                                       'same_detector_pointer_probe_population':'q=a+(1-a-b)p',
                                       'ideal_population_identification':'p=(q-a)/(1-a-b) if slope>0',
                                       'known_zero_and_one_preparation_source_supplied':False,
                                       'deployment_drift_removed_by_detector_calibration':False},
        'boundary':{'detector_POVMs_are_declared_mathematical_models_not_devices':True,
                    'records_or_models_erased':False,'all_possible_controls_or_measurements_excluded':False,
                    'physical_spin_or_platform_admitted':False,'formal_contract_or_outcome_changed':False},
        'next_gate':'Construct a retained joint detector-and-pointer calibration interval using separately supplied known-zero/known-one pointer probes. Test slope conditioning and confidence spending, then propagate its residual deployment drift; keep new preparation/readout resources distinct from native source admission.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale model-floor receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: valid globally bias-bounded detector models have identical calibration laws but incompatible stricter feedback targets.')
    print('PASS: exact bias/drift error-floor bounds do not invalidate the weaker 99% certificate; new calibration observables remain inputs.')


if __name__=='__main__':main()
