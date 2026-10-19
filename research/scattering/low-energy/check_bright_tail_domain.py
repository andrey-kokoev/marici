"""Sharp bright-tail domain conditions and low-mass-preserving UV-damped source controls."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb,factorial
from pathlib import Path
import check_packet_weak_coupling_tail as tail

shell=tail.shell;born=tail.born;phase=tail.phase;F=tail.F;ROOT=tail.ROOT;HOME=tail.HOME
CONTRACT=HOME/'contracts/bright-tail-domain.v1.json';PROOF=HOME/'BRIGHT-TAIL-DOMAIN.md'
RESULT=HOME/'results/bright-tail-domain.v1.json'


def bright_tail_moment_finite(p,k,r,s=Q()):
    """Asymptotic bright amplitude M^-r*(log M)^-s, with nonzero leading coefficient."""
    assert p in (3,6) and isinstance(k,int) and k>=0
    r=Q(r);s=Q(s);critical=Q(p*k)+Q(1,2)
    return r>critical or (r==critical and s>Q(1,2))


def power_tail_moment(k,R,r=14):
    assert isinstance(k,int) and k>=0 and r==14 and k<2*r-1
    R=Q(R);assert R>=4
    return Q(2*r-1,2*r-k-1)*R**k


def exponential_tail_moment(k,R,rate=27):
    assert isinstance(k,int) and k>=0 and rate==27
    R=Q(R);assert R>=4
    return R**k*sum((Q(comb(k,j)*factorial(j),rate**j) for j in range(k+1)),Q())


def moment_upper_bound(k,R,scheme):
    assert scheme in ('power','exponential')
    R=Q(R);tau=tail.tail_weight(R)
    tail_moment=(power_tail_moment if scheme=='power' else exponential_tail_moment)(k,R)
    return (1-tau)*R**k+tau*tail_moment


def validate_contract(c):
    assert c['schema']=='marici.scattering.bright-tail-domain.v1'
    assert c['bright_growth_powers']=={'scalar':3,'triplet':6}
    assert c['power_tail_amplitude_exponent']==14 and c['exponential_tail_rate_times_R']==27
    assert c['comparison_start_mass']=='4' and c['critical_log_condition']=='s>1/2 at r=p*k+1/2'
    for key in ('coherent_bright_projections_before_domain_test','dark_and_photon_complements_retained',
                'low_mass_wavefunction_and_tail_norm_preserved','independent_dimensionful_couplings_retained',
                'source_damping_distinct_from_interaction_form_factor','old_band_comparison_restriction_retained'):
        assert c[key] is True,key
    for key in ('raw_spin_moments_are_necessary_for_dark_states','all_moments_imply_convergent_coupling_series',
                'Hilbert_norm_closeness_controls_Born_graph_norm','UV_preparation_source_selected',
                'interaction_form_factor_derived','local_scattering_Hamiltonian_constructed',
                'physical_rate_or_branching_derived','native_source_licensed','live_proposition_inventory_changed',
                'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=tail.build();assert parent==json.loads(tail.RESULT.read_text(encoding='utf-8')),'stale weak-coupling tail'
    cases=0;table={}
    for p in (3,6):
        table[str(p)]={}
        for k in range(4):
            critical=Q(p*k)+Q(1,2);table[str(p)][str(k)]=str(critical)
            for r,s,expected in ((critical+Q(1,4),Q(-10),True),
                                 (critical-Q(1,4),Q(10),False),
                                 (critical,Q(),False),(critical,Q(1,2),False),(critical,Q(3,4),True)):
                assert bright_tail_moment_finite(p,k,r,s)==expected;cases+=1
    assert bright_tail_moment_finite(6,2,14) and not bright_tail_moment_finite(6,3,14)
    # Global scalar-eigenvalue controls yield strong first/second-order domain theorems.
    for x in (Q(),Q(1,4),Q(1),Q(2),Q(8),Q(-1),Q(-8)):
        for eta in (0,1):
            q=x+eta*x**3
            S=(F(1)+phase.IM*F(q)/2)/(F(1)-phase.IM*F(q)/2)
            first=S-F(1);second=first-phase.IM*F(x)
            if x:
                assert born.incoming.x.positive(F(4*x*x)-first.conjugate()*first)
                assert born.incoming.x.positive(F(9*x**4)-second.conjugate()*second)
            else:assert first==second==F()
    for y in (Q(),Q(1,16),Q(1,2),Q(1),Q(2),Q(4),Q(16)):
        f0=tail.conversion(y,0);f1=tail.conversion(y,1)
        assert 0<=y-f0<=y*y/2 and abs(f1-y)<=11*y*y
    # Heavy raw S/D amplitudes may still have an identically zero bright projection.
    for M in (Q(3),Q(4),Q(8)):
        K,jS,jD=shell.vector_kernel(M,F(1))
        dark=[[-jD],[jS],[F()]]
        assert phase.mm(K,dark)==[[F()] for _ in range(3)]
        assert jS*(-jD)+jD*jS==F()
    # Two exactly normalized tail replacements preserve the entire low-mass wavefunction.
    bounds={};moment_checks=0
    for R in (Q(4),Q(8),Q(16)):
        tau=tail.tail_weight(R);assert 0<tau<1
        assert power_tail_moment(0,R)==exponential_tail_moment(0,R)==1
        assert (1-tau)+tau==1
        for k in range(1,25):
            power=power_tail_moment(k,R);expo=exponential_tail_moment(k,R)
            assert 0<expo<power;moment_checks+=1
        for M in (R,R+1,2*R):assert Q(27)/M<=Q(27)/R
        p12=moment_upper_bound(12,R,'power');p24=moment_upper_bound(24,R,'power')
        assert p12==R**12*(1+Q(4,5)*tau)
        assert p24==R**24*(1+8*tau)
        assert moment_upper_bound(12,R,'exponential')<=p12
        assert moment_upper_bound(24,R,'exponential')<=p24
        bounds[str(R)]={'discarded_original_mass_norm':str(tau),
            'scalar_quartic_moment_upper':str(p12),
            'triplet_quartic_moment_upper':str(Q(9,4)*p24),
            'input_norm_difference_squared_upper':str(2*tau),
            'uniform_conversion_strength_difference_upper':str(tau)}
    assert tail.tail_weight(Q(4))==Q(17,81)
    assert power_tail_moment(6,4)==Q(9,7)*4**6
    # h3^2 <= (9/4)*M^24, because M^2+2 <= (3/2)*M^2 for M>2.
    for M in (Q(3),Q(4),Q(8)):
        assert M*M+2<=Q(3,2)*M*M
        B=2*(M+1)**2/(3*(M*M+2))
        assert B*M**10*(M*M+2)==Q(2,3)*M**10*(M+1)**2
    for n in range(1,5):
        assert factorial(6*n)>=(3*n)**(3*n)
        assert factorial(12*n)>=(6*n)**(6*n)
    refused=[]
    for name in ('raw_spin_moments_are_necessary_for_dark_states','all_moments_imply_convergent_coupling_series',
                 'Hilbert_norm_closeness_controls_Born_graph_norm','UV_preparation_source_selected',
                 'interaction_form_factor_derived','local_scattering_Hamiltonian_constructed',
                 'physical_rate_or_branching_derived','erase_critical_log_boundary'):
        try:
            if name=='erase_critical_log_boundary':assert bright_tail_moment_finite(6,1,Q(13,2),Q(1,2))
            else:
                bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported bright-domain promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((tail.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_bright_tail_domain.py'))
    return {'schema':'marici.scattering.bright-tail-domain-receipt.v1','status':'pass',
        'scope_verdict':'sharp_imported_bright_domain_and_source_damping_controls_not_selected_physical_UV_dynamics',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'sharp_kernel_power_domain_constructed':True,'critical_power_log_cases':cases,
        'critical_amplitude_power_r_by_p_and_k':table,
        'critical_log_rule':'at equality require s>1/2; s=1/2 diverges',
        'first_strong_Born_derivative_iff':'source in D(K)',
        'second_strong_Taylor_coefficient_iff':'source in D(K^2)',
        'global_probability_error_coefficients':{'eta0':'1/2','eta1':'11'},
        'global_probability_error_bound':'coefficient*epsilon^4*integral bright_weight*h^2',
        'heavy_dark_tail_in_all_kernel_power_domains':True,
        'low_mass_preserving_source_damping_constructed':True,'exact_tail_moment_comparisons':moment_checks,
        'damped_source_bounds':bounds,'power_control_in_DK2_but_not_DK3_for_active_triplet':True,
        'pure_S_source_Born_strength_ordering':'power tail > exponential tail; same core and tail norm',
        'exponential_eta0_probability_Taylor_radius':'0',
        'general_domain_and_stochastic_order_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale bright-tail domain'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','sharp_kernel_power_domain_constructed','critical_power_log_cases',
        'low_mass_preserving_source_damping_constructed','physical_rate_or_branching_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
