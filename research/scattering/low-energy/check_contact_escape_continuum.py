"""Self-adjoint Jacobi escape completion: weak release and positive bound trapping."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_graded_contact_vertex as vertex

charge=vertex.charge;pair=vertex.pair;phase=vertex.phase;cm=vertex.cm;x=vertex.x;F=vertex.F;ROOT=vertex.ROOT;HOME=vertex.HOME
CONTRACT=HOME/'contracts/contact-escape-continuum.v1.json'
PROOF=HOME/'CONTACT-ESCAPE-CONTINUUM.md'
RESULT=HOME/'results/contact-escape-continuum.v1.json'


def spectral_classification(epsilon,g2):
    assert 0<epsilon<4 and g2>=0
    if g2==0:return {'decoupled_embedded_source':True,'below_band':0,'above_band':0,
                     'lower_threshold_resonance':False,'upper_threshold_resonance':False,'pure_ac':False}
    below=int(g2>epsilon);above=int(g2>4-epsilon)
    return {'decoupled_embedded_source':False,'below_band':below,'above_band':above,
            'lower_threshold_resonance':g2==epsilon,'upper_threshold_resonance':g2==4-epsilon,
            'pure_ac':not (below or above)}

def density_denominator(epsilon,g2):
    a0=epsilon-g2;a1=g2/2-1
    return [a0*a0,2*a0*a1+g2*g2,1-g2]

def bound_certificate(epsilon,g,r):
    assert r==r.conjugate() and r!=F() and x.positive(F(1)-r*r)
    E=F(2)-r-F(1)/r;g2=g*g
    assert (F(1)-g2)*r*r+(epsilon-2)*r+F(1)==F()
    assert epsilon-E-g2*r==F()
    def u(n):return F(1) if n==0 else g*pair.measure.scalar_power(r,n)
    assert (epsilon-E)*u(0)-g*u(1)==F()
    assert (F(2)-E)*u(1)-g*u(0)-u(2)==F()
    for n in range(2,9):assert (F(2)-E)*u(n)-u(n-1)-u(n+1)==F()
    norm=F(1)+g2*r*r/(F(1)-r*r);Z=F(1)/norm
    for N in (0,1,4,8):
        partial=sum((u(n)*u(n).conjugate() for n in range(N+1)),F())
        tail=g2*pair.measure.scalar_power(r,2*(N+1))/(F(1)-r*r)
        assert partial+tail==norm
    return E,Z

def validate_contract(c):
    assert c['schema']=='marici.scattering.contact-escape-continuum.v1'
    assert c['new_postulates']==['semi_infinite_Jacobi_escape_coordinate','onsite_2_hopping_minus_1',
        'bare_source_energy_3','boundary_coupling_per_irrep']
    assert c['weak_couplings']=={'singlet':'1/2','triplet':'1/3'}
    assert c['all_spectator_and_bound_components_retained'] is True
    for key in ('lead_dispersion_identified_with_physical_photon_dispersion','native_continuum_licensed',
                'continuum_form_factors_source_selected','weak_couplings_source_selected',
                'bound_trapping_identified_with_physical_capture','all_source_preparations_escape',
                'physical_electron_positron_preparation_bound','full_Fock_wavepacket_constructed',
                'branching_ratio_derived','live_proposition_inventory_changed','C12_protocol_renewed',
                'high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=vertex.build();assert parent==json.loads(vertex.RESULT.read_text(encoding='utf-8')),'stale graded vertex'
    epsilon=Q(3);cases={};density_checks=0
    for name,g2 in (('weak_singlet',Q(1,4)),('weak_triplet',Q(1,9)),('upper_threshold',Q(1)),
                    ('positive_bound_triplet',Q(2)),('decoupled',Q()),('too_strong_negative_energy',Q(4))):
        status=spectral_classification(epsilon,g2);coef=density_denominator(epsilon,g2)
        cases[name]={'coupling_squared':str(g2),'bare_source_total_energy_variance':str(g2),
                     **status,'density_denominator_coefficients':[str(v) for v in coef]}
        if g2>0:
            for E,d in ((F(1),phase.SQ3),(F(2),F(2)),(F(3),phase.SQ3)):
                m=(F(2)-E+phase.IM*d)/2
                assert m*m-(F(2)-E)*m+F(1)==F()
                G=F(1)/(F(epsilon)-E-F(g2)*m)
                imaginary=(G-G.conjugate())/(2*phase.IM)
                denominator=F(coef[0])+F(coef[1])*E+F(coef[2])*E*E
                assert imaginary==F(g2)*d/(2*denominator) and x.positive(imaginary)
                density_checks+=1
    assert cases['weak_singlet']['pure_ac'] and cases['weak_triplet']['pure_ac']
    assert cases['upper_threshold']['pure_ac'] and cases['upper_threshold']['upper_threshold_resonance']
    assert not cases['decoupled']['pure_ac'] and cases['decoupled']['decoupled_embedded_source']
    assert cases['positive_bound_triplet']['above_band']==1 and cases['positive_bound_triplet']['below_band']==0
    assert cases['too_strong_negative_energy']['below_band']==cases['too_strong_negative_energy']['above_band']==1
    sqrt5=phase.root(4);r=(F(1)-sqrt5)/2
    E,Z=bound_certificate(F(3),phase.SQ2,r)
    assert E==F(2)+sqrt5 and x.positive(E-F(4)) and Z==F(1)/sqrt5
    local=Z*Z;cloud=Z-local;outgoing=F(1)-Z
    assert local==F(Q(1,5)) and x.positive(cloud) and local+cloud+outgoing==F(1)
    # Positive quadratic form: |b1-g*a|^2+(epsilon-g^2)|a|^2+sum |b[n+1]-b[n]|^2.
    for g2 in (Q(1,4),Q(1,9),Q(2)):assert epsilon-g2>0
    g2=F(2);a=F(1)+phase.IM;b1=F(2)-phase.IM;b2=phase.IM
    left=F(3)*a.conjugate()*a+2*b1.conjugate()*b1+2*b2.conjugate()*b2
    left=left-phase.SQ2*(a.conjugate()*b1+b1.conjugate()*a)-(b1.conjugate()*b2+b2.conjugate()*b1)
    t=b1-phase.SQ2*a;u=b2-b1
    right=t.conjugate()*t+(F(3)-g2)*a.conjugate()*a+u.conjugate()*u+b2.conjugate()*b2
    assert left==right
    group,_,spin=phase.source_group();rotation_cases=0
    boundary=[[F() for _ in range(4)] for _ in range(4)]
    boundary[0][0]=F(Q(1,2))
    for i in range(1,4):boundary[i][i]=F(Q(1,3))
    for q in sorted(group):
        U=phase.from_spin(spin,q);D=phase.blockdiag([[[F(1)]],phase.spatial(U)])
        assert phase.mm(D,boundary)==phase.mm(boundary,D);rotation_cases+=1
    # Conditional late-time norm accounting; p is not selected by the source.
    mixtures=[]
    for p in (Q(),Q(1,4),Q(1,2),Q(1)):
        two=F(p);three=F(1-p)*outgoing;bound=F(1-p)*Z;pair_local=F(1-p)*local
        assert two+three+bound==F(1)
        mixtures.append({'singlet_weight':str(p),'weak_outgoing_two_three':[str(p),str(1-p)],
            'strong_triplet_outgoing_two':two.encoded(),'strong_triplet_outgoing_three':three.encoded(),
            'strong_triplet_retained_bound_norm':bound.encoded(),'strong_triplet_local_pair_probability':pair_local.encoded()})
    refused=[]
    for name in ('zero_coupling_complete_escape','threshold_tail_is_bound','erase_bound_cloud',
                 'negative_energy_positive_model','identify_lead_with_photon_dispersion','declare_all_raw_preparations_escape'):
        try:
            if name=='zero_coupling_complete_escape':assert spectral_classification(Q(3),Q())['pure_ac']
            elif name=='threshold_tail_is_bound':bound_certificate(F(3),F(1),F(-1))
            elif name=='erase_bound_cloud':assert F(1)-local==outgoing
            elif name=='negative_energy_positive_model':assert epsilon-Q(4)>=0
            else:
                bad=copy.deepcopy(c)
                key={'identify_lead_with_photon_dispersion':'lead_dispersion_identified_with_physical_photon_dispersion',
                     'declare_all_raw_preparations_escape':'all_source_preparations_escape'}[name]
                bad[key]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported continuum promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((vertex.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_contact_escape_continuum.py'))
    return {'schema':'marici.scattering.contact-escape-continuum-receipt.v1','status':'pass',
        'scope_verdict':'declared_self_adjoint_Jacobi_escape_and_retained_bound_cloud_not_physical_photon_dispersion',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'self_adjoint_infinite_escape_completion_constructed':True,'bare_source_energy':'3','lead_band':['0','4'],
        'spectral_cases':cases,'source_density_boundary_checks':density_checks,'native_irrep_boundary_rotation_cases':rotation_cases,
        'weak_model_initial_encoded_pair_complete_local_release_proved':True,
        'weak_model_complete_outgoing_wave_operator_on_active_ac_space':True,
        'positive_bound_example':{'coupling_squared':'2','tail_ratio':r.encoded(),'energy':E.encoded(),
            'initial_source_bound_norm':Z.encoded(),'asymptotic_local_pair_probability':local.encoded(),
            'bound_lead_cloud_norm':cloud.encoded(),'outgoing_ac_norm':outgoing.encoded(),
            'source_bound_norm_formula':'1/sqrt(5)','local_pair_probability_formula':'1/5',
            'outgoing_ac_norm_formula':'1-1/sqrt(5)'},
        'preparation_norm_accounting_examples':mixtures,'all_spectator_and_bound_components_retained':True,
        'lead_dispersion_identified_with_physical_photon_dispersion':False,'native_continuum_licensed':False,
        'continuum_form_factors_source_selected':False,'weak_couplings_source_selected':False,
        'bound_trapping_identified_with_physical_capture':False,'all_source_preparations_escape':False,
        'physical_electron_positron_preparation_bound':False,'initial_contact_source_is_sharp_total_energy':False,
        'full_Fock_wavepacket_constructed':False,
        'branching_ratio_derived':False,'analytic_argument_machine_formalized':False,
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],
        'new_live_proposition_admitted':False,'C12_protocol_renewed':False,'high_energy_protocol_executed':False,
        'physical_outcomes_admitted':False,'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale contact escape continuum'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','self_adjoint_infinite_escape_completion_constructed',
        'weak_model_initial_encoded_pair_complete_local_release_proved','native_irrep_boundary_rotation_cases',
        'lead_dispersion_identified_with_physical_photon_dispersion','branching_ratio_derived','hostile_controls_refused')}))


if __name__=='__main__':main()
