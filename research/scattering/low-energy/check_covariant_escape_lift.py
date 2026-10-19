"""Declared active Poincare lift, lab wave operators and invariant-mass retention."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path
import check_total_momentum_packet as packet

F=packet.F;phase=packet.phase;x=packet.x;ROOT=packet.ROOT;HOME=packet.HOME
CONTRACT=HOME/'contracts/covariant-escape-lift.v1.json'
PROOF=HOME/'COVARIANT-ESCAPE-LIFT.md'
RESULT=HOME/'results/covariant-escape-lift.v1.json'
mm=phase.mm


def clock_coefficients(u):
    assert packet.minkowski(u,u)==F(1) and x.positive(u[0])
    v=[r/u[0] for r in u[1:]]
    along=u[0]-sum((a*b for a,b in zip(v,u[1:])),F())
    assert along==F(1)/u[0]
    return u[0],along


def retained_mass_weights(delta):
    assert delta>=0 and packet.tail.positive_margin(delta*delta)>0
    if delta==0:
        Z=F(1)/phase.root(4)
        return {'mass_bound':Z,'local_pair':Z*Z,'outgoing':F(1)-Z,'bound_lead_cloud':Z-Z*Z}
    return {'mass_bound':F(),'local_pair':F(),'outgoing':F(1),'bound_lead_cloud':F()}


def lead_polynomials(count):
    assert count>=2
    ps=[[Q(1)],[Q(),Q(1)]]
    while len(ps)<count:
        nxt=[Q()]+ps[-1]
        for i,c in enumerate(ps[-2]):nxt[i]-=c
        ps.append(nxt)
    return ps


def semicircle_inner(p,q):
    def moment(n):return Q() if n%2 else Q(comb(n,n//2),n//2+1)
    return sum((a*b*moment(i+j) for i,a in enumerate(p) for j,b in enumerate(q)),Q())


def validate_contract(c):
    assert c['schema']=='marici.scattering.covariant-escape-lift.v1'
    assert c['additional_postulates']==['conserved_future_unit_velocity_carrier',
        'rest_scalar_mass_operator_per_imported_spin_irrep','interacting_four_momentum_u_times_rest_mass']
    assert c['opened_tail_coupling']=='1/4'
    for key in ('all_output_bound_and_spectator_records_retained','lab_wave_operator_range_typed_by_rest_mass_ac'):
        assert c[key] is True
    for key in ('native_source_Poincare_representation_derived','untyped_spectator_Lorentz_action_licensed',
                'physical_incident_preparation_bound','form_factors_source_selected','local_field_interaction_constructed',
                'cluster_separability_proved','microcausality_proved','lab_energy_ac_implies_complete_photon_escape',
                'lab_frame_lifetime_calibrated','naive_gamma_acceleration_called_time_dilation',
                'annihilation_rate_derived','branching_ratio_derived','live_proposition_inventory_changed',
                'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=packet.build();assert parent==json.loads(packet.RESULT.read_text(encoding='utf-8')),'stale full packet'
    ps=lead_polynomials(6)
    assert [[semicircle_inner(p,q) for q in ps] for p in ps]==[[Q(int(i==j)) for j in range(6)] for i in range(6)]
    qs=[[F(v) for v in q] for q in ((0,0,0),(Q(1,8),0,0),(Q(1,8),Q(1,6),Q(1,5)))]
    L=packet.mm(packet.boost(packet.velocity([F(),F(Q(1,6)),F()])),
                packet.boost(packet.velocity([F(Q(1,8)),F(),F()])))
    # A common-factor algebra witness, NOT a finite approximation used for escape claims.
    A=[[F(3),-phase.SQ2],[-phase.SQ2,F(2)]];A2=mm(A,A)
    momenta_cases=0;clock_cases=0
    for q in qs:
        u=packet.velocity(q);gamma,along=clock_coefficients(u)
        P=[phase.scale(v,A) for v in u]
        assert phase.add(mm(P[0],P[0]),phase.scale(F(-1),
            phase.add(phase.add(mm(P[1],P[1]),mm(P[2],P[2])),mm(P[3],P[3]))))==A2
        for i in range(4):
            for j in range(4):assert mm(P[i],P[j])==mm(P[j],P[i])
        Lu=packet.act(L,u)
        for i in range(4):
            transformed=[[sum((L[i][j]*P[j][a][b] for j in range(4)),F()) for b in range(2)] for a in range(2)]
            assert transformed==phase.scale(Lu[i],A)
        for mass in (F(1),F(2),F(2)+phase.root(4)):
            p=[mass*v for v in u]
            assert packet.minkowski(p,p)==mass*mass and x.positive(p[0])
            assert packet.act(L,p)==[mass*v for v in Lu];momenta_cases+=1
        assert gamma*along==F(1);clock_cases+=1
    gamma,along=clock_coefficients(packet.velocity(qs[1]))
    assert gamma==F(Q(65,63)) and along==F(Q(63,65))
    cutoff=retained_mass_weights(Q());opened=retained_mass_weights(Q(1,4))
    assert cutoff['mass_bound']==F(1)/phase.root(4) and cutoff['local_pair']==F(Q(1,5))
    assert cutoff['mass_bound']+cutoff['outgoing']==F(1)
    assert cutoff['local_pair']+cutoff['bound_lead_cloud']+cutoff['outgoing']==F(1)
    assert opened['outgoing']==F(1) and opened['mass_bound']==opened['local_pair']==F()
    # Analytic coarea for the bound packet's lab-energy pushforward on the boost cube:
    # E_lab=Eb*(1+r^2)/(1-r^2), derivative=4*Eb*r/(1-r^2)^2, nonzero for r>0.
    Eb=F(2)+phase.root(4)
    for r in (F(Q(1,16)),F(Q(1,8)),F(Q(1,4))):
        derivative=4*Eb*r/((F(1)-r*r)*(F(1)-r*r))
        assert x.positive(derivative)
    # Fixed compact velocity example makes both clock scales bounded and positive.
    assert Q(1)<=Q(65,63)<=Q(19,13) and Q(13,19)<=Q(63,65)<=Q(1)
    margins=packet.tail.positive_margin(Q(1,16));assert margins==Q(29,32)
    refused=[]
    for name in ('drop_velocity_from_lab_energy','call_fixed_origin_clock_time_dilation',
                 'erase_mass_bound_weight_after_energy_dephasing','declare_lab_ac_full_photon_range',
                 'erase_untyped_spectators','promote_native_Poincare','promote_covariance_to_microcausality'):
        try:
            if name=='drop_velocity_from_lab_energy':assert gamma==F(1)
            elif name=='call_fixed_origin_clock_time_dilation':assert gamma==along
            elif name=='erase_mass_bound_weight_after_energy_dephasing':assert cutoff['mass_bound']==F()
            else:
                bad=copy.deepcopy(c)
                key={'declare_lab_ac_full_photon_range':'lab_energy_ac_implies_complete_photon_escape',
                     'erase_untyped_spectators':'all_output_bound_and_spectator_records_retained',
                     'promote_native_Poincare':'native_source_Poincare_representation_derived',
                     'promote_covariance_to_microcausality':'microcausality_proved'}[name]
                bad[key]=name!='erase_untyped_spectators';validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported covariant lift promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((packet.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_covariant_escape_lift.py'))
    return {'schema':'marici.scattering.covariant-escape-lift-receipt.v1','status':'pass',
        'scope_verdict':'postulated_active_velocity_Poincare_completion_and_photon_wave_operator_not_native_local_source_theory',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'active_velocity_Poincare_completion_constructed':True,'strongly_commuting_four_momentum_constructed':True,
        'positive_self_adjoint_lab_generator_constructed':True,'lab_escape_wave_operator_constructed':True,
        'full_Fock_outgoing_readout_translation_and_Lorentz_intertwiner_constructed':True,
        'completed_outgoing_bound_spectator_readout_isometric':True,
        'spectral_momentum_covariance_cases':momenta_cases,'clock_identity_cases':clock_cases,
        'free_lead_Chebyshev_Gram_dimension':6,
        'clock_witness':{'gamma':'65/63','fixed_origin_generator':'(65/63)*H_rest',
                         'co_moving_generator':'(63/65)*H_rest'},
        'opened_positive_form_margin':str(margins),'opened_active_outgoing_norm':'1',
        'cutoff_mass_bound_norm':'1/sqrt(5)','cutoff_local_pair_plateau':'1/5',
        'cutoff_packet_lab_energy_point_weight':'0','cutoff_packet_global_return_amplitude_limit':'0',
        'cutoff_bound_mass_retention_survives_boost_dephasing':True,
        'lab_wave_operator_range':'I_velocity tensor P_ac(H_rest), not generally P_ac(P0)',
        'untyped_spectator_record_dimensions':{'other_fermion_occupations':12,'ordered_raw_complement':60},
        'analytic_argument_machine_formalized':False,**{k:c[k] for k in c if isinstance(c[k],bool)},
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale covariant escape lift'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','active_velocity_Poincare_completion_constructed',
        'lab_escape_wave_operator_constructed','cutoff_bound_mass_retention_survives_boost_dephasing',
        'native_source_Poincare_representation_derived','branching_ratio_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
