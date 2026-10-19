"""Retained iid calibration confidence and exact fidelity-acceptance inequalities."""
from fractions import Fraction as F
from math import comb,factorial
import argparse
import json

from check_pointer_calibration_information import audit as calibration_audit
from check_five_cell_attachment_bridge import digest,BASE

DEST=BASE/'results/finite-calibration-gate.v1.json'


def sqrt_sum_ge(A,B,t):
    """Compare sqrt(A)+sqrt(B)>=t without floating or new radicals."""
    assert A>=0 and B>=0 and t>=0
    remainder=t*t-A-B
    return remainder<=0 or 4*A*B>=remainder*remainder


def audit():
    previous=calibration_audit();n=512;radius=F(1,10);delta=F(1,1000);eta=F(1,100)
    exponent=2*n*radius*radius
    lower_exp=sum((exponent**k/F(factorial(k)) for k in range(13)),F(0))
    certified_tail=2/lower_exp
    assert certified_tail<=delta
    # F>=1-(1-r²)(1-d_min)/2 >= (1+d_min)/2. The last
    # inequality is uniform in both source-bound inverse-filter ratios.
    threshold_visibility=1-2*eta
    endpoint_threshold=2*threshold_visibility*threshold_visibility-1
    assert threshold_visibility==F(49,50) and endpoint_threshold==F(1151,1250)
    intervals=[];accepted=[]
    for k in range(n+1):
        estimate=F(k,n);lo=max(F(0),estimate-radius);hi=min(F(1),estimate+radius)
        A=(1-lo)*(1-hi);B=lo*hi
        decision=sqrt_sum_ge(A,B,endpoint_threshold)
        assert 0<=lo<=hi<=1
        # The midpoint is in angle, not in population. Endpoint visibility
        # d_end=sqrt(A)+sqrt(B); midpoint visibility=sqrt((1+d_end)/2).
        if decision:accepted.append(k)
        intervals.append({'ones':k,'p_hat':str(estimate),'p_interval':[str(lo),str(hi)],
                          'endpoint_visibility_radicands':[str(A),str(B)],
                          'accept_fidelity_99_percent':decision})
    assert accepted and len(accepted)<n+1
    assert intervals[0]['accept_fidelity_99_percent'] and intervals[n]['accept_fidelity_99_percent']
    assert intervals[n//2]['accept_fidelity_99_percent']
    assert not intervals[51]['accept_fidelity_99_percent']
    fixtures=[]
    for p in (F(0),F(1,10),F(9,25),F(1,2),F(16,25),F(9,10),F(1)):
        total=F(0);noncoverage=F(0);accept_mass=F(0);accepted_noncoverage=F(0)
        for k,row in enumerate(intervals):
            mass=F(comb(n,k))*p**k*(1-p)**(n-k);total+=mass
            lo,hi=map(F,row['p_interval']);covered=lo<=p<=hi
            if not covered:noncoverage+=mass
            if row['accept_fidelity_99_percent']:
                accept_mass+=mass
                if not covered:accepted_noncoverage+=mass
        assert total==1 and noncoverage<=certified_tail
        assert accepted_noncoverage<=noncoverage and 0<accept_mass<=1
        conditional_noncoverage=accepted_noncoverage/accept_mass
        # This is an upper bound on fidelity failure conditioned on release,
        # not a claim that every noncovering interval violates fidelity.
        fixtures.append({'true_population_p':str(p),'total_count_mass':'1',
                         'unconditional_interval_noncoverage_probability':str(noncoverage),
                         'calibration_accept_probability':str(accept_mass),
                         'accepted_interval_noncoverage_probability':str(accepted_noncoverage),
                         'conditional_fidelity_failure_upper_bound_from_noncoverage':str(conditional_noncoverage),
                         'selected_confidence_equals_declared_delta':False})
    # Each retained probe word is analyzed by count but is not declared
    # erased. Binomial multiplicities check the entire finite word domain.
    assert sum(comb(n,k) for k in range(n+1))==2**n
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_finite_calibration_gate.py'}
    return {
        'schema':'marici.scattering.finite-calibration-gate.v1',
        'status':'finite_iid_probe_gate_certifies_conditional_interval_fidelity_with_retained_sampling_and_abstention_risk',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'declared_model':{'probes':n,'observation':'ordered independent Z-pointer outcomes from separate known-flag-one probes',
                          'population':'p=v²=sin²(beta), beta in [0,pi/2]',
                          'sampling_assumptions':['iid Bernoulli probes','one constant pointer parameter across probes and deployment','ideal population readout','independent probe preparation/reset'],
                          'observed_physical_calibration_data':False,
                          'raw_ordered_records_required_to_be_retained':True,'count_is_analysis_statistic_not_history_erasure':True,
                          'word_domain_accounting':'all 2^n ordered words via exact binomial multiplicities; no observed probe word is supplied'},
        'confidence':{'radius':str(radius),'declared_failure_budget':str(delta),
                       'interval':'[max(0,k/n-epsilon),min(1,k/n+epsilon)]',
                       'Hoeffding_bound':'P(noncoverage)<=2 exp(-2*n*epsilon²)',
                       'positive_Taylor_terms':13,'exponent':str(exponent),
                       'certified_rational_upper_bound':str(certified_tail),
                       'unconditional_confidence_at_least':'999/1000',
                       'bound_certified_without_floating_exponentials':True},
        'release_gate':{'target_Bell_undo_fidelity':'99/100',
                        'control_estimate':'beta_hat=(asin(sqrt(p_low))+asin(sqrt(p_high)))/2',
                        'endpoint_visibility':'d_end=sqrt((1-p_low)(1-p_high))+sqrt(p_low*p_high)',
                        'worst_midpoint_visibility':'sqrt((1+d_end)/2)',
                        'accept_iff':'d_end>=1151/1250, equivalent to worst midpoint visibility>=49/50',
                        'comparison':'exact rational squared-radical comparison',
                        'ratio_independent_fidelity_argument':'F>=1-(1-r²)(1-d_min)/2>=(1+d_min)/2',
                        'on_coverage_and_acceptance_fidelity_at_least':'99/100',
                        'accepted_counts':accepted,'count_domain':intervals,
                        'abstention':'do not release this guarantee for rejected counts; keep probe records and allow a separately budgeted new calibration',
                        'exact_phase_control_assumed':True},
        'statistical_scope':{'unconditional_P_accept_and_fidelity_below_target_upper_bound':str(certified_tail),
                             'same_delta_is_automatically_conditional_on_acceptance':False,
                             'generic_conditional_bound':'P(bad fidelity | accept)<=min(1,delta/P(accept)); exact fixture noncoverage ratios are recorded',
                             'coverage_failure_is_identical_to_fidelity_failure':False,
                             'repeated_calibrate_until_accept_has_same_fixed_sample_budget':False,
                             'fixture_population_tests':fixtures},
        'boundary':{'sampling_control_and_reset_resources_are_inputs':True,
                    'finite_confidence_is_exact_parameter_knowledge':False,
                    'pointer_drift_or_readout_bias_covered':False,
                    'prior_history_measurements_undone':False,'physical_platform_or_spin_admitted':False,
                    'shared_formal_contracts_changed':False,'formal_outcome_admitted':False},
        'next_gate':'Test the constant-pointer deployment assumption with explicit angular drift/readout bias. Propagate a declared drift bound into the release inequality and construct a passing-calibration/failing-deployment counterexample; keep calibration confidence distinct from control/model error.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale finite-calibration receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: certified finite iid confidence and exact interval-to-fidelity gate, including retained abstentions.')
    print('PASS: exact binomial fixtures preserve sampling and selection risks; finite confidence is not exact parameter knowledge.')


if __name__=='__main__':main()
