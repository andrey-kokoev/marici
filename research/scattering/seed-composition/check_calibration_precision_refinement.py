"""Predetermined confidence-spent precision refinement with finite model release."""
from fractions import Fraction as F
import argparse
import json

from check_repeated_calibration_budget import audit as repeated_audit,runs
from check_calibration_deployment_bounds import m11,s11,sqrt_sum_ge11
from check_five_cell_attachment_bridge import digest,BASE

DEST=BASE/'results/calibration-precision-refinement.v1.json'


def ceiling(x):return (x.numerator+x.denominator-1)//x.denominator


def audit():
    previous=repeated_audit();horizon=previous['policy']['maximum_windows'];delta=F(previous['risk_certificate']['total_budget'])
    bias=F(1,100);c,s=F(2499,2501),F(100,2501);target=F(49,50)
    half_threshold=(target*c,F(3,50)*s);sq=m11(half_threshold,half_threshold)
    endpoint_threshold=(2*sq[0]-1,2*sq[1]);threshold_squared=m11(endpoint_threshold,endpoint_threshold)
    windows=[];certified_spend=F(0);allocated_spend=F(0);cost=0;universal_window=None;universal_cost=None
    for t in range(1,horizon+1):
        epsilon=F(1,t+9);delta_t=delta/F(t*(t+1));m=0
        while F(2,2**m)>delta_t:m+=1
        n=ceiling(F(m,2*epsilon*epsilon));exponent=2*n*epsilon*epsilon
        assert exponent>=m and F(2,2**m)<=delta_t
        # exp(1)>2 implies 2 exp(-exponent)<2/2^m, without
        # logarithms or floating exponentials. Plans precede observations.
        tail=F(2,2**m);certified_spend+=tail;allocated_spend+=delta_t;cost+=n
        radius=epsilon+bias
        accepted=[];rejected=[]
        for k in range(n+1):
            lo=max(F(0),F(k,n)-radius);hi=min(F(1),F(k,n)+radius)
            decision=sqrt_sum_ge11((1-lo)*(1-hi),lo*hi,endpoint_threshold)
            (accepted if decision else rejected).append(k)
        assert len(accepted)+len(rejected)==n+1 and n//2 in accepted
        # A clipped population interval has width <=2*radius. Its maximum
        # angular width occurs at an endpoint, with cosine sqrt(1-2*radius).
        # This sufficient universal certificate covers even non-grid counts.
        assert 0<2*radius<1
        universal=s11((1-2*radius-threshold_squared[0],-threshold_squared[1]))>=0
        if universal:assert len(accepted)==n+1
        if universal and universal_window is None:universal_window=t;universal_cost=cost
        windows.append({'window':t,'new_probes':n,'radius':str(epsilon),
                        'allocated_failure_budget':str(delta_t),'integer_exponent_certificate':m,
                        'certified_sampling_tail':str(tail),'Hoeffding_exponent':str(exponent),
                        'accept_count_runs':runs(accepted),'reject_count_runs':runs(rejected),
                        'all_counts_partitioned':True,'universal_angular_width_certificate':universal,
                        'all_counts_release':len(accepted)==n+1,'cumulative_probe_cost':cost,
                        'ordered_raw_words_and_rejected_window_required_records':True})
    assert universal_window==17 and universal_cost is not None
    assert certified_spend<=allocated_spend<delta
    assert windows[0]['reject_count_runs'] and windows[universal_window-1]['reject_count_runs']==[]
    spent_at_release=sum((F(x['certified_sampling_tail']) for x in windows[:universal_window]),F(0))
    assert spent_at_release<delta
    # Endpoint-near and arbitrary populations need no special exemption at
    # the certified window: every possible count passes its fixed predicate.
    t=universal_window;last=windows[t-1];n=last['new_probes'];epsilon=F(last['radius'])
    fixtures=[]
    for p,q in ((F(0),bias),(F(1,100),F(1,100)),(F(1,100),F(0)),(F(1,2),F(51,100)),(F(1),1-bias)):
        assert abs(q-p)<=bias
        # Retain the exact count range representing observed-q coverage.
        lo_k=max(0,ceiling(n*(q-epsilon)));hi_value=n*(q+epsilon);hi_k=min(n,hi_value.numerator//hi_value.denominator)
        assert 0<=lo_k<=hi_k<=n
        assert last['accept_count_runs']==[[0,n]]
        fixtures.append({'true_population':str(p),'observed_population':str(q),
                         'coverage_count_range':[lo_k,hi_k],'every_count_including_covered_counts_releases':True})
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_calibration_precision_refinement.py'}
    return {
        'schema':'marici.scattering.calibration-precision-refinement.v1',
        'status':'shrinking_radius_spending_guarantees_finite_model_release_under_declared_bias_drift_and_control_bounds',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'predetermined_schedule':{'planned_maximum_windows':horizon,'epsilon_t':'1/(t+9)',
                                  'delta_t':'(1/1000)/(t(t+1))','m_t':'smallest integer with 2/2^m_t<=delta_t',
                                  'N_t':'ceil(m_t/(2 epsilon_t²))','first_release_stopping':True,
                                  'tail_certificate':'2 exp(-2N_t epsilon_t²)<2/2^m_t<=delta_t, because exp(1)>2',
                                  'allocated_total':str(allocated_spend),'certified_total':str(certified_spend),
                                  'planned_probe_cost':cost,'windows':windows},
        'finite_release_certificate':{'guaranteed_model_release_by_window':universal_window,
                                      'maximum_probes_before_release':universal_cost,
                                      'last_window_probes':last['new_probes'],'last_window_radius':last['radius'],
                                      'universal_count_runs':last['accept_count_runs'],
                                      'analytic_argument':'maximum angular width of a population interval of length 2(epsilon+bias) is asin(sqrt(2(epsilon+bias))); its endpoint visibility passes the exact drift-aware threshold',
                                      'first_release_bad_fidelity_probability_bound':str(spent_at_release),
                                      'target_Bell_fidelity':'99/100',
                                      'model_release_probability':1,
                                      'conditional_on_release_matches_unconditional_within_this_model':True,
                                      'scope':'complete valid probe windows and ideal specified controls; physical aborts or extra acceptance filters can change release probability',
                                      'population_fixtures':fixtures},
        'assumptions_and_records':{'within_window_conditionally_iid_observed_population':True,
                                   'population_bias_bound':'1/100','angle_drift_cos':'2499/2501','angle_drift_sin':'100/2501',
                                   'exact_phase_midpoint_control_required':True,
                                   'real_nonnegative_pointer_family_and_ideal_Y_readout_required':True,
                                   'all_distinguishing_outcome_copies_addressed':True,
                                   'ordered_raw_probe_words_counts_and_decisions_required':True,
                                   'physical_data_or_device_supplied':False,
                                   'invalid_missing_windows_require_explicit_abort_record':True,
                                   'model_bound_violations_included_in_sampling_budget':False},
        'comparison':{'fixed_radius_schedule_can_abstain_on_covered_endpoint_near_population':True,
                      'refinement_uses_more_probes_and_smaller_intervals_not_budget_reuse':True,
                      'finite_release_is_exact_parameter_knowledge':False,
                      'finite_release_is_physical_preparation_or_spin_admission':False},
        'boundary':{'shared_contracts_or_outcomes_changed':False,'rejected_records_erased':False,
                    'control_work_or_hardware_derived':False},
        'next_gate':'Quantify the irreducible bias/drift error floor as probe radius tends to zero. Construct observationally indistinguishable nuisance models and test whether stricter fidelity targets can be guaranteed by more iid Z probes alone or require tighter source/control bounds.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale refinement receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact shrinking-radius confidence spending and drift-aware count partitions.')
    print('PASS: a universal width certificate guarantees finite model release by window seventeen; resources and assumptions remain explicit.')


if __name__=='__main__':main()
