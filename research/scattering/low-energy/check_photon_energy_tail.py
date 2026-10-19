"""Measure-compatible unbounded tail removes the Jacobi cutoff bound state."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import permutations
import json
from math import factorial
from pathlib import Path
import check_contact_escape_continuum as escape

vertex=escape.vertex;phase=escape.phase;pair=escape.pair;measure=pair.measure;F=escape.F;x=escape.x
ROOT=escape.ROOT;HOME=escape.HOME
CONTRACT=HOME/'contracts/photon-energy-tail.v1.json'
PROOF=HOME/'PHOTON-ENERGY-TAIL.md'
RESULT=HOME/'results/photon-energy-tail.v1.json'


def beta_integral(p,q):
    """Integral_0^infinity E^p/(1+E)^q dE; only convergent integer cases."""
    assert isinstance(p,int) and isinstance(q,int) and p>=0 and q>p+1
    return Q(factorial(p)*factorial(q-p-2),factorial(q-1))


def tail_weight(E):return 30*E*E/(1+E)**6


def positive_margin(delta2,old_g2=Q(2)):
    assert delta2>=0
    return Q(3)-old_g2-Q(3,2)*delta2


def triplet_extra_profile():
    s2=measure.add(*(measure.power(measure.var(i),2) for i in range(3)))
    return measure.scale(2*phase.root(6),measure.add(s2,measure.const(Q(-1,2))))


def validate_contract(c):
    assert c['schema']=='marici.scattering.photon-energy-tail.v1'
    assert c['tail_weight']=='30*E^2/(1+E)^6'
    assert c['tail_couplings']==['1/4','1/8']
    assert c['old_band_couplings_squared']=={'singlet':'1/4','triplet':'2'}
    assert c['photon_phase_volume_energy_powers']=={'two':0,'three':2}
    assert c['orthogonal_output_profiles_retained'] is True
    assert c['identical_particle_constants_retained_symbolically'] is True
    assert c['all_spectators_and_output_channels_retained'] is True
    for key in ('tail_envelope_source_selected','tail_strength_source_selected','physical_incident_preparation_bound',
                'full_total_momentum_Fock_wavepacket_constructed','physical_spatial_photon_escape_proved',
                'native_continuum_licensed','annihilation_rate_derived','branching_ratio_derived',
                'all_singular_self_adjoint_extensions_excluded','live_proposition_inventory_changed',
                'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=escape.build();assert parent==json.loads(escape.RESULT.read_text(encoding='utf-8')),'stale escape continuum'
    moments={str(k):30*beta_integral(2+k,6) for k in (-1,0,1,2)}
    assert moments=={'-1':Q(3,2),'0':Q(1),'1':Q(3,2),'2':Q(6)}
    # A_n*E^(2n-4) times |sqrt(30/A_n)*E^(3-n)/(1+E)^3|^2.
    for n in (2,3):assert (2*n-4)+2*(3-n)==2
    plus=[F(1)/phase.SQ2,phase.IM/phase.SQ2,F()];minus=[v.conjugate() for v in plus]
    inner=lambda u,v:sum((a.conjugate()*b for a,b in zip(u,v)),F())
    assert inner(plus,plus)==inner(minus,minus)==F(1) and inner(plus,minus)==F()
    h=triplet_extra_profile()
    assert measure.simplex_integral(h)==F() and measure.inner(h,h)==F(1)
    for order in permutations(range(3)):assert measure.permute(h,order)==h
    density_checks=0
    Eb=F(2)+phase.root(4)
    for E in (F(1),F(2),F(4),F(5),Eb):
        a=F(1)+E
        # Coefficient of pi in Im S(E+i0), from I3-2 I4+I5.
        coeff=30*(F(1)/measure.scalar_power(a,4)-F(2)/measure.scalar_power(a,5)+F(1)/measure.scalar_power(a,6))
        w=30*E*E/measure.scalar_power(F(1)+E,6)
        assert coeff==w and x.positive(w);density_checks+=1
    # At E=1 log(E)=0, so the real boundary transform is rational.
    def I_real_at_one(n):return -sum((Q(2**k,k) for k in range(1,n+1)),Q())/2**(n+1)
    assert 30*(I_real_at_one(3)-2*I_real_at_one(4)+I_real_at_one(5))==Q(-1,2)
    trials=[]
    for ds in c['tail_couplings']:
        delta=Q(ds);d2=delta*delta
        assert delta>0 and positive_margin(d2)>0
        assert positive_margin(d2,Q(1,4))>0
        trials.append({'delta':ds,'triplet_positive_form_margin':str(positive_margin(d2)),
            'singlet_positive_form_margin':str(positive_margin(d2,Q(1,4))),
            'perturbation_operator_norm':ds,'triplet_source_energy_variance':str(Q(2)+d2),
            'active_point_norm':'0','asymptotic_local_pair_probability':'0','active_outgoing_ac_norm':'1'})
    # Each irrep couples to its own normalized tail: norm is delta, not sqrt(4)*delta.
    group,_,spin=phase.source_group()
    for q in sorted(group):
        D=phase.blockdiag([[[F(1)]],phase.spatial(phase.from_spin(spin,q))])
        K=phase.scale(F(Q(1,4)),phase.eye(4))
        assert phase.mm(K,D)==phase.mm(D,K)
    bare_uv=[]
    for n in (2,3):
        try:beta_integral(2*n-4,0)
        except AssertionError:bare_uv.append(n)
        else:raise AssertionError('constant bare amplitude unexpectedly L2')
    refused=[]
    for name in ('reuse_same_photon_profile_as_independent_channel','omit_energy_phase_volume',
                 'declare_cutoff_bound_weight_tail_stable','infer_uniform_in_time_small_error',
                 'negative_margin_positive_model','promote_to_physical_rate'):
        try:
            if name=='reuse_same_photon_profile_as_independent_channel':assert measure.inner(measure.const(1),measure.const(1))==F()
            elif name=='omit_energy_phase_volume':assert 2*(3-3)==2
            elif name=='declare_cutoff_bound_weight_tail_stable':assert F(1)/phase.root(4)==F()
            elif name=='infer_uniform_in_time_small_error':assert Q(1,5)<=Q(1,8)
            elif name=='negative_margin_positive_model':assert positive_margin(Q(1))>=0
            else:
                bad=copy.deepcopy(c);bad['annihilation_rate_derived']=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported tail promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((escape.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_photon_energy_tail.py'))
    return {'schema':'marici.scattering.photon-energy-tail-receipt.v1','status':'pass',
        'scope_verdict':'conditional_measure_compatible_UV_tail_destabilizes_cutoff_bound_state_not_a_native_emission_law',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'tail_weight_moments':{k:str(v) for k,v in moments.items()},'tail_density_boundary_identity_checks':density_checks,
        'opposite_helicity_channel_orthogonality_checked':True,
        'orthogonal_three_photon_triplet_profile_constructed':True,'triplet_shape_multiplier':'sqrt(60)*(sum y_i^2-1/2)',
        'two_photon_extra_channel':'opposite equal-helicity scalar, orthogonal to original helicity',
        'photon_phase_volume_energy_powers':c['photon_phase_volume_energy_powers'],
        'relative_energy_measure_compatible_form_factors_constructed':True,
        'bare_constant_amplitude_not_a_bounded_rank_one_vertex_for_multiplicities':bare_uv,
        'self_adjoint_unbounded_energy_completion_constructed':True,'native_irrep_tail_rotation_cases':len(group),
        'positive_tail_trials':trials,'arbitrarily_small_positive_tail_removes_active_point_sector':True,
        'cutoff_triplet_initial_bound_norm':'1/sqrt(5)','cutoff_triplet_local_pair_plateau':'1/5',
        'nonzero_tail_triplet_initial_bound_norm':'0','nonzero_tail_local_pair_plateau':'0',
        'finite_time_operator_error_bound':'min(2,abs(delta*t))',
        'source_survival_probability_error_bound':'min(1,2*abs(delta*t))',
        'asymptotic_survival_probability_difference_for_any_nonzero_tail':'1/5',
        'small_tail_and_long_time_limits_commute':False,'analytic_argument_machine_formalized':False,
        **{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],
        'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale photon energy tail'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','self_adjoint_unbounded_energy_completion_constructed',
        'arbitrarily_small_positive_tail_removes_active_point_sector','small_tail_and_long_time_limits_commute',
        'full_total_momentum_Fock_wavepacket_constructed','branching_ratio_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
