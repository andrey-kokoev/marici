"""Finite first-release confidence spending with all rejected windows retained."""
from fractions import Fraction as F
from math import comb,factorial
import argparse
import json

from check_calibration_deployment_bounds import audit as deployment_audit,sqrt_sum_ge11
from check_five_cell_attachment_bridge import digest,BASE

DEST=BASE/'results/repeated-calibration-budget.v1.json'


def runs(values):
    out=[]
    for x in values:
        if out and out[-1][1]+1==x:out[-1][1]=x
        else:out.append([x,x])
    return out


def audit():
    previous=deployment_audit();horizon=20;total_delta=F(1,1000);epsilon=F(1,10);bias=F(1,100)
    threshold=previous['robust_gate']['equivalent_endpoint_threshold'];threshold=(F(threshold['constant']),F(threshold['sqrt11']))
    windows=[];total_spend=F(0);total_certified=F(0);probe_cost=0
    for t in range(1,horizon+1):
        n=512+128*(t-1);delta_t=total_delta/F(t*(t+1));exponent=2*n*epsilon*epsilon
        lower_exp=sum((exponent**j/F(factorial(j)) for j in range(13)),F(0));tail=2/lower_exp
        assert tail<=delta_t
        accepted=[];rejected=[]
        for k in range(n+1):
            lo=max(F(0),F(k,n)-epsilon-bias);hi=min(F(1),F(k,n)+epsilon+bias)
            decision=sqrt_sum_ge11((1-lo)*(1-hi),lo*hi,threshold)
            (accepted if decision else rejected).append(k)
        accept_runs=runs(accepted);reject_runs=runs(rejected)
        assert sum(hi-lo+1 for lo,hi in accept_runs+reject_runs)==n+1
        assert set(accepted).isdisjoint(rejected)
        assert accepted and len(accepted)<n+1
        assert n//2 in accepted and 0 not in accepted and n not in accepted
        total_spend+=delta_t;total_certified+=tail;probe_cost+=n
        windows.append({'window':t,'new_probes':n,'radius':str(epsilon),
                        'allocated_failure_budget':str(delta_t),'certified_rational_sampling_tail':str(tail),
                        'accept_count_runs':accept_runs,'reject_count_runs':reject_runs,
                        'count_domain_completely_partitioned':True,
                        'rejected_raw_probe_word_required_to_be_retained':True})
    assert total_spend==total_delta*F(horizon,horizon+1) and total_certified<=total_spend<total_delta
    assert probe_cost==34560
    # Naive repeated-release counterexample for the interval-confidence
    # claim. At p=q=1/100, every accepted first-window interval misses p.
    # Release remains possible, but no exact guarantee follows from waiting.
    n=512;p=F(1,100);accept=F(0);reject=F(0);bad=F(0)
    for row in previous['robust_gate']['count_domain']:
        k=row['ones'];mass=F(comb(n,k))*p**k*(1-p)**(n-k)
        if row['accept_with_bias_and_drift']:
            lo,hi=map(F,row['bias_expanded_p_interval']);assert not lo<=p<=hi
            accept+=mass;bad+=mass
        else:reject+=mass
    assert 0<accept<1 and reject+accept==1 and bad==accept
    # Exact probabilities retain a reconstructible rational base and powers
    # rather than printing enormous expanded numerators at every depth.
    stop_mass=F(0);prefixes=[]
    for t in range(1,horizon+1):
        first=reject**(t-1)*accept;stop_mass+=first
        assert stop_mass+reject**t==1
        prefixes.append({'window':t,'first_release_probability_expression':f'(1-a)^{t-1}*a',
                         'no_release_probability_expression':f'(1-a)^{t}',
                         'first_release_interval_noncoverage_probability_equals_first_release':True,
                         'censored_terminal_record_retained':True})
    finite_bad_horizon=(accept.denominator+accept.numerator-1)//accept.numerator
    assert finite_bad_horizon*accept>=1
    # (1-a)^H<=exp(-aH)<=exp(-1)<1/2; exp(1)>1+1+1/2>2.
    assert F(1)+F(1)+F(1,2)>2
    # The budgeted policy itself can abstain with high probability for a
    # benign endpoint-near population because radius never decreases.
    # This is not a promise of eventual release or a model failure.
    abstention_population=F(1,100)
    for window in windows:
        n=window['new_probes']
        for lo,hi in window['accept_count_runs']:
            assert F(lo,n)-epsilon-bias>abstention_population
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_repeated_calibration_budget.py'}
    return {
        'schema':'marici.scattering.repeated-calibration-budget.v1',
        'status':'finite_first_release_policy_has_explicit_confidence_spending_naive_unbounded_retry_does_not_and_fixed_radius_can_abstain',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'policy':{'maximum_windows':horizon,'stop':'first bias/drift-aware accepted count, otherwise terminal no-release record',
                  'N_t':'512+128*(t-1)','epsilon':'1/10','delta_t':'(1/1000)/(t*(t+1))',
                  'schedule_chosen_before_window_data':True,
                  'retain':['ordered raw probe words in every window','counts','release/abstention decisions','first-release time or censored no-release record'],
                  'physical_observations_supplied':False,'windows':windows},
        'risk_certificate':{'allocated_sum':str(total_spend),'certified_tail_sum':str(total_certified),
                             'total_budget':'1/1000','union_bound_applies_at_first_release':True,
                             'bad_release_event':'release with fidelity below target while declared bias/drift/phase bounds hold',
                             'argument':'bad release is contained in the union of window noncoverage events; conditional iid concentration and predetermined spending bound each event, independently of the stopping rule',
                             'between_window_independence_required_for_union_bound':False,
                             'within_window_conditionally_iid_observed_population_required':True,
                             'bias_drift_control_violation_included':False,
                             'conditional_on_release_same_budget_automatically':False},
        'resource_accounting':{'maximum_independent_probes':probe_cost,'release_is_guaranteed':False,
                               'raw_records_actually_measured':False,'source_supplies_probe_reset_or_work':False,
                               'no_release_when_coverage_holds_at_p_1_100':True,
                               'reason':'fixed radius cannot resolve this population sufficiently for the robust angular target; increased N only reduces tail probability'},
        'naive_retry_witness':{'model':'independent repeated copies of the original 512-probe robust gate, p=q=1/100, no bias/drift violation',
                               'a_exact_single_window_release_probability':str(accept),
                               'every_released_interval_misses_p':True,
                               'first_release_conditional_noncoverage':'1',
                               'finite_prefixes':prefixes,
                               'finite_horizon_H':str(finite_bad_horizon),
                               'finite_H_bad_interval_release_probability':'1-(1-a)^H > 1/2',
                               'proof':'aH>=1 and exp(1)>2',
                               'single_window_tail_reuse_valid':False,
                               'noncoverage_is_identical_to_actual_fidelity_failure_claimed':False},
        'boundary':{'sampling_and_control_resources_are_inputs':True,'confidence_is_exact_parameter_knowledge':False,
                    'records_or_rejected_windows_erased':False,'physical_platform_or_spin_admitted':False,
                    'formal_contract_or_outcome_changed':False},
        'next_gate':'Construct a confidence-spent precision-refinement schedule that shrinks the population radius as probe cost grows. Test whether it releases on covered endpoint-near populations within a finite budget while preserving bias/drift margins and all abstention records.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale repeated-calibration receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: twenty-window confidence spending bounds first release and retains all rejected/censored records.')
    print('PASS: naive indefinite budget reuse fails interval confidence; fixed-radius spending can validly abstain without release.')


if __name__=='__main__':main()
