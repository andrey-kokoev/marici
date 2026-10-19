"""Subtracted scalar response: exact spectral moments, Ward-compatible freedom, and UV bounds."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb,factorial
from pathlib import Path
import check_complex_mass_analyticity as analytic

ROOT=analytic.ROOT;HOME=analytic.HOME
CONTRACT=HOME/'contracts/scalar-dispersive-response.v1.json';PROOF=HOME/'SCALAR-DISPERSIVE-RESPONSE.md'
RESULT=HOME/'results/scalar-dispersive-response.v1.json'


def convergent_subtractions(density_power,n):
    assert isinstance(density_power,int) and density_power>=0 and isinstance(n,int) and n>=0
    return density_power-n-1 < -1


def coefficient(n):
    assert isinstance(n,int) and n>=0
    return Q(factorial(n)*factorial(n+1),factorial(2*n+3))


def integrated_coefficient(n,u0=Q()):
    assert isinstance(n,int) and n>=0 and 0<=u0<1
    return sum((Q((-1)**j*comb(n,j),2*j+3)*(1-u0**(2*j+3)) for j in range(n+1)),Q())/(2*4**n)


def series_box(s,n=32,u0=Q()):
    s=Q(s);u0=Q(u0);assert 0<=s<4 and n>=1 and 0<=u0<1
    a=lambda k:coefficient(k) if not u0 else integrated_coefficient(k,u0)
    lo=sum((a(k)*s**k for k in range(n)),Q())
    ratio=s*(1-u0*u0)/4
    hi=lo+a(n)*s**n/(1-ratio)
    assert lo<=hi
    return lo,hi


def log_ratio_box(x,n=24):
    x=Q(x);assert 0<x<1 and n>=1
    lo=2*sum((x**(2*j+1)/Q(2*j+1) for j in range(n)),Q())
    hi=lo+2*x**(2*n+1)/(Q(2*n+1)*(1-x*x))
    return lo,hi


def validate_contract(c):
    assert c['schema']=='marici.scattering.scalar-dispersive-response.v1'
    assert c['cut_threshold']==4 and c['mass_unit']==1
    assert c['spectral_density']=='sigma(t)=t^3*sqrt(1-4/t);t>=4'
    assert c['normalization']=='T_gamma_gamma_leading=(epsilon2^2/2)*R(s)'
    assert c['minimum_subtractions']=={'full_response':4,'Ward_factored_response':2}
    assert c['free_local_subtraction_degrees']==[2,3]
    assert c['spectral_model']=='right_hand_cut_only_contact_density_extrapolated_to_infinity'
    for key in ('charged_pair_absorptive_cut_matched','Ward_regular_local_subtractions_retained',
                'independent_dimensionful_couplings_retained','free_real_subtraction_data_retained',
                'UV_spectral_comparisons_distinct_from_source_packet_damping','second_order_Hermitian_loss_retained'):
        assert c[key] is True,key
    for key in ('contact_spectral_density_UV_extrapolation_source_licensed','crossed_channel_input_derived',
                'crossing_complete_four_photon_amplitude_constructed','zero_second_order_forward_phase_preserved',
                'positive_cut_fixes_sign_of_s2_subtraction','subtraction_constants_source_selected',
                'all_UV_spectral_changes_obey_damping_bound','exact_unitary_scattering_constructed',
                'eta1_higher_order_contractivity_failure_repaired','interaction_UV_form_factor_derived',
                'local_QFT_loop_renormalization_completed','native_source_licensed','physical_rates_or_branching_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=analytic.build();assert parent==json.loads(analytic.RESULT.read_text(encoding='utf-8')),'stale complex-mass audit'
    assert not convergent_subtractions(3,3) and convergent_subtractions(3,4)
    assert not convergent_subtractions(1,1) and convergent_subtractions(1,2)
    moments=[]
    for n in range(12):
        a=coefficient(n);assert a==integrated_coefficient(n)>0
        assert coefficient(n+1)/a==Q(n+1,2*(2*n+5))<Q(1,4)
        moments.append(str(a))
    transforms=0
    for s in (Q(-2),Q(),Q(1),Q(2),Q(3)):
        for u in (Q(),Q(1,4),Q(1,2),Q(3,4)):
            t=4/(1-u*u);dt=8*u/(1-u*u)**2
            assert u*u==1-4/t
            assert u*dt/(t*(t-s))==2*u*u/(4-s+s*u*u);transforms+=1
    jlo,jhi=series_box(2)
    pi_lo=4*(1-jhi);pi_hi=4*(1-jlo)
    assert 3<pi_lo<pi_hi<Q(22,7)
    sub={}
    for s in (Q(),Q(1,2),Q(1),Q(2),Q(3)):
        lo,hi=series_box(s)
        Rlo=s**4*lo/pi_hi;Rhi=s**4*hi/pi_lo
        assert 0<=Rlo<=Rhi
        sub[str(s)]={'J_lower':str(lo),'J_upper':str(hi),'zero_subtraction_R_lower':str(Rlo),'zero_subtraction_R_upper':str(Rhi)}
    # Same positive cut and Ward scaling permit both signs of the s^2 coefficient.
    rlo=Q(sub['1']['zero_subtraction_R_lower']);rhi=Q(sub['1']['zero_subtraction_R_upper'])
    assert 0<rlo<=rhi<1
    assert -1+rhi<0<1+rlo
    # Above threshold Re R0=s^3/pi*(2-beta*log((1+beta)/(1-beta))).
    phases={}
    for beta in (Q(1,2),Q(7,8)):
        s=4/(1-beta*beta);llo,lhi=log_ratio_box(beta)
        lo=2-beta*lhi;hi=2-beta*llo
        assert s**4*(beta/s)==s**3*beta  # Imaginary part after the 1/pi dispersion factor.
        if beta==Q(1,2):assert lo>0
        else:assert hi<0
        phases[str(beta)]={'s':str(s),'Re_R0_times_pi_over_s3_lower':str(lo),'Re_R0_times_pi_over_s3_upper':str(hi),
            'absorptive_density':str(s**3*beta)}
    uv={};tail_checks=0
    for u0 in (Q(1,2),Q(3,4),Q(7,8)):
        cutoff=4/(1-u0*u0);uv[str(cutoff)]={}
        for n in range(12):
            a=integrated_coefficient(n,u0)
            assert 0<a<coefficient(n)
            assert integrated_coefficient(n+1,u0)<=a/cutoff;tail_checks+=1
        assert integrated_coefficient(0,u0)<=1/cutoff
        for s in (Q(1),Q(2),Q(3)):
            lo,hi=series_box(s,u0=u0)
            assert 0<lo<=hi<=1/(cutoff-s)
            uv[str(cutoff)][str(s)]={'pi_scaled_response_change_upper':str(s**4/(cutoff-s))}
    refused=[]
    for name in ('positive_cut_fixes_sign_of_s2_subtraction','subtraction_constants_source_selected',
                 'crossing_complete_four_photon_amplitude_constructed','exact_unitary_scattering_constructed',
                 'eta1_higher_order_contractivity_failure_repaired','contact_spectral_density_UV_extrapolation_source_licensed',
                 'all_UV_spectral_changes_obey_damping_bound','local_QFT_loop_renormalization_completed'):
        try:
            bad=copy.deepcopy(c);bad[name]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported dispersive promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((analytic.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_scalar_dispersive_response.py'))
    return {'schema':'marici.scattering.scalar-dispersive-response-receipt.v1','status':'pass',
        'scope_verdict':'conditional_right_cut_dispersive_control_with_free_Ward_subtractions_not_a_selected_unitary_local_QFT',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'minimum_subtractions':c['minimum_subtractions'],'free_local_subtraction_degrees':c['free_local_subtraction_degrees'],
        'exact_J_Taylor_coefficients':moments,'J_series_radius_in_s':'4','rational_change_of_variable_checks':transforms,
        'pi_from_J2_identity_box':{'lower':str(pi_lo),'upper':str(pi_hi)},'subthreshold_series_boxes':sub,
        'above_cut_zero_subtraction_phase_boxes':phases,'UV_spectral_damping_bounds':uv,'exact_tail_moment_checks':tail_checks,
        'same_cut_s2_subtraction_sign_controls':['-1','1'],'general_dispersion_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale scalar dispersive response'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','minimum_subtractions','free_local_subtraction_degrees',
        'charged_pair_absorptive_cut_matched','exact_unitary_scattering_constructed','hostile_controls_refused')}))


if __name__=='__main__':main()
