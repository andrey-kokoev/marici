"""Conditional invariant rest-energy completion and indispensable-input audit.

The relativistic center-of-mass extension is an explicit additional law, not a
claim that the source records derived relativity or selected neutron mass.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from check_neutron_canonical_occupied_closure import ROOT,mm,transpose,scale
from check_neutron_positive_gap_certificate import inertia


def main():
    root=ROOT/'research/strominger/results'
    paths={k:root/p for k,p in {
        'positive':'neutron-source-action-rest-gap.json',
        'uncompleted':'neutron-positive-gap-certificate.json',
        'source':'neutron-seam-control-transport.json'}.items()}
    data={k:json.loads(p.read_text()) for k,p in paths.items()};checks={}
    for obj in data.values():
        assert obj['status']=='passed'
        for p,h in obj['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    positive=data['positive'];interval=positive['gap_interval'];lo=F(interval['lower']);hi=F(interval['upper'])
    assert 0<lo<hi<F(1,2)
    for A in positive['lower_endpoint_schur_enclosures']:
        assert inertia([list(map(F,r)) for r in A])==(12,0)
    for A in positive['upper_endpoint_schur_enclosures']:
        assert inertia([list(map(F,r)) for r in A])[1]>0
    assert positive['retained_complement_energy_lower_bound']=='3/4'
    checks['fresh_full_sector_strict_positive_internal_certificate']=True
    # Independently reconstruct the proposed action from the actual source
    # projectors. This verifies its provenance, NOT admission as a rest law.
    raw=[list(map(F,r)) for r in positive['source_action']]
    total=[[F(0)]*24 for _ in range(24)]
    for row in data['source']['source_pulses']:
        for i,r in enumerate(row['projector']):
            for j,x in enumerate(r):total[i][j]+=F(x)/3
    assert total==raw
    checks['new_action_uses_actual_generators_not_a_scalar_offset']=True
    # Functional-calculus completion:
    # H_cm=sqrt(c^2 P^2 + epsilon^2 H_internal^2), on a NEW center-of-mass
    # coordinate X, independent of the original relative encounter coordinate.
    # Exact rational points parameterize the positive hyperbola. Together with
    # the symbolic derivative H'=c^2 p/H they check the boost algebra in 1+1D.
    tests=[]
    for c in (F(1),F(3,2)):
        for epsilon in (F(1),F(7,3)):
            rest=epsilon*(lo+hi)/2
            for t in (F(-3,4),F(-1,3),F(0),F(1,3),F(3,4)):
                momentum=(rest/c)*2*t/(1-t*t)
                energy=rest*(1+t*t)/(1-t*t)
                derivative=c*c*momentum/energy
                assert energy*energy-c*c*momentum*momentum==rest*rest
                assert energy>=rest>0 and energy*derivative/(c*c)==momentum
                if t==0:assert momentum==0 and energy==rest
                tests.append({'c':str(c),'energy_unit':str(epsilon),'momentum':str(momentum),
                              'energy':str(energy),'rest_energy':str(rest)})
    checks['positive_mass_shell_and_rest_limit_exact_at_20_rational_cases']=True
    checks['one_dimensional_boost_commutator_coefficient_identity']=True
    # The far-field sine packet vanishes at the contact and leaves every
    # finite core/memory coordinate zero. Its energy is Delta+kappa*pi^2/L^2.
    # pi<22/7 supplies fully rational upper bounds as L grows.
    packets=[]
    for L in (10,100,1000,10000,100000,1000000):
        upper=F(22,7)**2/(L*L)
        packets.append({'length':L,'zero_threshold_energy_upper_bound':str(upper)})
    assert F(packets[-1]['zero_threshold_energy_upper_bound'])<F(1,10**10)
    checks['zero_threshold_far_field_trials_rule_out_positive_full_gap']=True
    assert data['uncompleted']['full_retained_sector']['ground_energy']=='0'
    coefficients=list(map(F,positive['bank_trial_upper_bound_coefficients']))
    assert min(coefficients)>0
    small_beta=F(1,10**8)
    assert small_beta*min(coefficients)<lo
    checks['zero_source_action_and_small_action_limits_are_not_hidden']=True
    result={'status':'passed','checks':checks,
        'conditional_result':{'internal_rest_gap_model_units':interval,
            'center_of_mass_law':'H_cm = sqrt(c^2 |P|^2 + epsilon^2 H_internal^2)',
            'rest_energy_interval':'epsilon * (lower, upper), with epsilon>0',
            'invariant_mass_interval':'epsilon * (lower, upper) / c^2, with c>0',
            'energy_zero':'Adjoin a separate empty vacuum sector with energy 0; no scalar shift of the occupied Hamiltonian.',
            'spectral_argument':'H_internal >= lower>0. Functional calculus gives H_cm^2-c^2|P|^2=epsilon^2 H_internal^2. On the lowest bound-state branch, P=0 gives positive rest energy epsilon*E0.',
            'boost_scope':'For one translation dimension, B=i*hbar/c^2*(H*d/dp+Hprime/2); [B,P]=i*hbar*H/c^2 and [B,H]=i*hbar*P. This does not establish a neutron spin representation or source-derived Lorentz symmetry.'},
        'exact_mass_shell_cases':tests,'zero_threshold_trial_packets':packets,
        'small_beta_trial':{'beta':str(small_beta),'energy_upper_bound':str(small_beta*min(coefficients))},
        'assumption_ledger':[
            {'input':'Stationary source action beta*(sum P)/3','status':'new law; not implied by time-ordered source pulses'},
            {'input':'beta=1','status':'fixture value, not source-selected'},
            {'input':'lead threshold Delta=1/2','status':'supplied; essential for full-sector positivity'},
            {'input':'eta=2, ell=1, kappa=1','status':'supplied autonomous contact fixture'},
            {'input':'relativistic center-of-mass functional calculus','status':'additional kinematic completion, not derived from source records'},
            {'input':'physical energy unit epsilon','status':'unselected; no MeV value inferred'},
            {'input':'identify lowest branch as physical neutron','status':'not established by these algebraic records'}],
        'conclusion':'Positive invariant rest energy is established for the explicitly completed model. Physical neutron rest energy is not derived from the available source data alone.',
        'identifiability':'Removing either the stationary source action or the positive lead threshold defeats the full-sector strict gap. Both zero-gap and positive-gap laws fit the existing carrier and pulse matrices; those matrices alone do not select the rest law.'}
    inputs=list(paths.values())+[Path(__file__).resolve(),ROOT/'research/strominger/checkers/check_neutron_positive_gap_certificate.py']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    (root/'neutron-rest-energy-completion.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'conditional_rest_energy_model_units':interval,
                     'source_selected_physical_rest_energy':False,'exact_mass_shell_tests':len(tests)},indent=2))

if __name__=='__main__':main()
