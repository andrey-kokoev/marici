"""Explicit CAR extension and reversible charge/rotation-compatible contact code."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
from itertools import combinations
import json
from pathlib import Path
import check_native_charge_preparation as charge

pair=charge.pair;phase=charge.phase;cm=charge.cm;x=charge.x;F=charge.F;ROOT=charge.ROOT;HOME=charge.HOME
CONTRACT=HOME/'contracts/graded-contact-vertex.v1.json'
PROOF=HOME/'GRADED-CONTACT-VERTEX.md'
RESULT=HOME/'results/graded-contact-vertex.v1.json'
mm,adj,eye=phase.mm,phase.adj,phase.eye
add,scale,sub=charge.add,charge.scale,charge.sub


def zeros(n,m):return [[F() for _ in range(m)] for _ in range(n)]
def creation(mode):
    assert mode in range(4);out=zeros(16,16)
    for mask in range(16):
        if mask&(1<<mode):continue
        out[mask|(1<<mode)][mask]=F((-1)**((mask&((1<<mode)-1)).bit_count()))
    return out

def occupied(mask):return [i for i in range(4) if mask&(1<<i)]
def exterior(A):
    assert len(A)==4 and all(len(row)==4 for row in A)
    out=zeros(16,16)
    for i in range(16):
        I=occupied(i)
        for j in range(16):
            J=occupied(j)
            if len(I)==len(J):out[i][j]=cm.determinant([[A[a][b] for b in J] for a in I])
    return out

def neutral_embedding():
    E=zeros(16,4)
    for a in range(2):
        for b in range(2):E[(1<<a)|(1<<(2+b))][2*a+b]=F(1)
    return E

def contact_channel(incoming,column):
    W=zeros(20,20)
    for j in range(16):W[16+column][j]=incoming[j][column].conjugate()
    return W

def hamiltonian(Ws,Wt,gs,gt):
    V=add(scale(gs,Ws),scale(gt,Wt))
    return add(V,adj(V))

def transition_probabilities(U,incoming,column):
    v=[row[column] for row in incoming]+[F()]*4
    out=cm.act(U,v)
    return sum((a.conjugate()*a for a in out[:16]),F()),out[16].conjugate()*out[16],sum((a.conjugate()*a for a in out[17:]),F())

def validate_contract(c):
    assert c['schema']=='marici.scattering.graded-contact-vertex.v1'
    assert c['new_postulates']==['four_charged_CAR_modes','species_swap_with_C_even_vacuum',
        'imported_relative_photon_code_modes','Hermitian_pair_conversion_vertex']
    assert c['survival_and_spectator_records_retained'] is True
    assert c['declared_total_energy_label']=='3'
    for key in ('CAR_statistics_native_derived','charge_conjugation_native_selected','native_joint_contact_licensed',
                'physical_electron_positron_preparation_bound','couplings_source_selected',
                'irreversible_annihilation_constructed','outgoing_spatial_continuum_constructed','local_field_interaction_constructed',
                'full_Fock_wavepacket_constructed','one_step_transfer_is_annihilation_rate','branching_ratio_derived',
                'live_proposition_inventory_changed','C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=charge.build();assert parent==json.loads(charge.RESULT.read_text(encoding='utf-8')),'stale charge/preparation audit'
    creators=[creation(i) for i in range(4)];annihilators=[adj(A) for A in creators]
    for i in range(4):
        for j in range(4):
            assert add(mm(annihilators[i],creators[j]),mm(creators[j],annihilators[i]))==scale(F(int(i==j)),eye(16))
            assert add(mm(creators[i],creators[j]),mm(creators[j],creators[i]))==zeros(16,16)
    species=[[F(int(i==(j+2)%4)) for j in range(4)] for i in range(4)]
    CF=exterior(species);assert mm(CF,CF)==eye(16) and CF[0][0]==F(1)
    assert all(mm(mm(CF,creators[i]),adj(CF))==creators[(i+2)%4] for i in range(4))
    QF=[[F(sum((-1 if k<2 else 1) for k in occupied(i))) if i==j else F() for j in range(16)] for i in range(16)]
    parity=[[F((-1)**len(occupied(i))) if i==j else F() for j in range(16)] for i in range(16)]
    assert mm(mm(CF,QF),adj(CF))==scale(F(-1),QF)
    E=neutral_embedding();assert mm(adj(E),E)==eye(4) and mm(QF,E)==zeros(16,4)
    swap=[[F(int((i//2,i%2)==(j%2,j//2))) for j in range(4)] for i in range(4)]
    assert mm(CF,E)==mm(E,scale(F(-1),swap))
    Csame=charge.decode(json.loads(pair.RESULT.read_text(encoding='utf-8'))['same_pair_Clebsch_Gordan_matrix'])
    incoming=mm(E,Csame);assert mm(adj(incoming),incoming)==eye(4)
    Cout=phase.blockdiag([[[F(1)]],scale(F(-1),eye(3))])
    assert mm(CF,incoming)==mm(incoming,Cout)
    Ws=contact_channel(incoming,0);Wt=zeros(20,20)
    for j in range(1,4):Wt=add(Wt,contact_channel(incoming,j))
    Hs,Ht=add(Ws,adj(Ws)),add(Wt,adj(Wt))
    Ps,Pt=mm(Hs,Hs),mm(Ht,Ht)
    assert mm(Hs,Ht)==zeros(20,20) and mm(Ps,Ps)==Ps and mm(Pt,Pt)==Pt
    assert pair.trace(Ps)==F(2) and pair.trace(Pt)==F(6)
    Ctotal=phase.blockdiag([CF,Cout]);Qtotal=phase.blockdiag([QF,zeros(4,4)])
    Ftotal=phase.blockdiag([parity,eye(4)])
    M=F(Q(c['declared_total_energy_label']))  # Not a native mass calibration.
    H0=phase.blockdiag([[[M*Q(len(occupied(i)),2) if i==j else F() for j in range(16)] for i in range(16)],scale(M,eye(4))])
    models=[hamiltonian(Ws,Wt,F(1),F(2)),hamiltonian(Ws,Wt,F(2),F(1)),
            hamiltonian(Ws,Wt,F(1)+phase.IM,F(2)-phase.IM)]
    for gs,gt in ((F(1),F(2)),(F(2),F(1)),(F(1)+phase.IM,F(2)-phase.IM)):
        assert x.positive(M*M-gs*gs.conjugate()) and x.positive(M*M-gt*gt.conjugate())
    for H in models:
        assert adj(H)==H
        assert all(mm(H,B)==mm(B,H) for B in (Ctotal,Qtotal,Ftotal,H0))
    # Explicit raw one-particle and neutral exterior embeddings.
    raw=json.loads(phase.STORE.read_text(encoding='utf-8'))
    P=[[[phase.decode(z) for z in row] for row in B] for B in raw['face_projectors']]
    Jm=scale(F(1)/phase.SQ2,[row for B in P for row in B]);Jp=scale(F(1)/phase.SQ2,[row for B in [sub(eye(2),p) for p in P] for row in B])
    B=[m+p for m,p in zip(Jm,Jp)];assert mm(adj(B),B)==eye(4)
    raw_flip=charge.decode(parent['linear_raw_flip']);assert mm(raw_flip,B)==mm(B,species)
    wedge=zeros(28,4)
    for k,(i,j) in enumerate(combinations(range(8),2)):
        for a in range(2):
            for b in range(2):wedge[k][2*a+b]=B[i][a]*B[j][2+b]-B[j][a]*B[i][2+b]
    assert mm(adj(wedge),wedge)==eye(4)
    ordered=phase.tensor(Jm,Jp);assert mm(adj(ordered),ordered)==eye(4)
    retained=sub(eye(64),mm(ordered,adj(ordered)))
    assert pair.trace(retained)==F(60) and mm(retained,ordered)==zeros(64,4)
    # The raw completion maps x -> (E ordered† x, retained x), not two copies.
    assert add(mm(ordered,adj(ordered)),retained)==eye(64)
    group,_,spin=phase.source_group();commutant_dimension=F();rotation_cases=0
    for q in sorted(group):
        U=phase.from_spin(spin,q);R=phase.spatial(U)
        one_particle=phase.blockdiag([U,U]);Gamma=exterior(one_particle)
        assert mm(adj(Gamma),Gamma)==eye(16) and mm(Gamma,CF)==mm(CF,Gamma)
        D=phase.blockdiag([[[F(1)]],R]);assert mm(Gamma,incoming)==mm(incoming,D)
        total=phase.blockdiag([Gamma,D])
        assert all(mm(H,total)==mm(total,H) for H in models)
        character=F(1)+pair.trace(R);commutant_dimension=commutant_dimension+character*character.conjugate()/24
        rotation_cases+=1
    assert commutant_dimension==F(2)
    # Exact exp(-i H pi/2) for (gs,gt)=(1,2) and (2,1), respectively.
    U12=add(sub(sub(eye(20),Ps),scale(F(2),Pt)),scale(-phase.IM,Hs))
    U21=add(sub(sub(eye(20),scale(F(2),Ps)),Pt),scale(-phase.IM,Ht))
    transfers=[]
    for label,U in (('g_s=1,g_t=2',U12),('g_s=2,g_t=1',U21)):
        assert mm(adj(U),U)==eye(20)
        assert mm(mm(U,U),mm(U,U))==eye(20)
        assert all(mm(U,A)==mm(A,U) for A in (Ctotal,Qtotal,Ftotal))
        s=transition_probabilities(U,incoming,0);t=transition_probabilities(U,incoming,1)
        assert all(sum(p,F())==F(1) for p in (s,t))
        transfers.append({'couplings':label,'time':'pi/2 in declared dimensionless units',
            'singlet_survival_two_three':[str(v.v[0]) for v in s],
            'triplet_survival_two_three':[str(v.v[0]) for v in t],
            'contact_interaction_picture_recurrence_time':'2*pi in declared dimensionless units'})
    assert transfers[0]['singlet_survival_two_three']==['0','1','0']
    assert transfers[0]['triplet_survival_two_three']==['1','0','0']
    assert transfers[1]['singlet_survival_two_three']==['1','0','0']
    assert transfers[1]['triplet_survival_two_three']==['0','0','1']
    refused=[]
    for name in ('erase_survival_or_raw_complement','claim_CAR_is_native','fix_coupling_ratio_from_symmetry',
                 'call_Rabi_transfer_annihilation_rate','claim_irreversible_decay'):
        try:
            bad=copy.deepcopy(c)
            key={'erase_survival_or_raw_complement':'survival_and_spectator_records_retained',
                 'claim_CAR_is_native':'CAR_statistics_native_derived','fix_coupling_ratio_from_symmetry':'couplings_source_selected',
                 'call_Rabi_transfer_annihilation_rate':'one_step_transfer_is_annihilation_rate',
                 'claim_irreversible_decay':'irreversible_annihilation_constructed'}[name]
            bad[key]=name!='erase_survival_or_raw_complement';validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported graded-contact promotion: '+name)
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((charge.RESULT,CONTRACT,PROOF,Path(__file__),HOME/'test_graded_contact_vertex.py'))
    return {'schema':'marici.scattering.graded-contact-vertex-receipt.v1','status':'pass',
        'scope_verdict':'postulated_CAR_and_Hermitian_finite_contact_with_recurrence_not_native_annihilation',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'fermion_modes':4,'fermion_Fock_dimension':16,'selected_photon_code_dimension':4,'contact_code_dimension':20,
        'CAR_verified':True,'vacuum_fixed_second_quantized_species_flip_constructed':True,
        'derived_neutral_pair_action_in_extension':'minus_swap','raw_neutral_exterior_embedding_isometric':True,
        'typed_Fock_spectator_dimension':12,'retained_ordered_raw_pair_complement_rank':60,
        'self_adjoint_contact_vertex_constructed':True,'charge_C_and_fermion_parity_preserved':True,
        'native_rotation_cases':rotation_cases,'complex_contact_intertwiner_dimension':2,
        'independent_contact_coefficients':['g_s','g_t'],
        'intertwiner_dimension_scope':'neutral_exactly_two_fermion_code_to_selected_photon_modes',
        'resonant_free_energy_label_commutator_verified':True,'declared_total_energy_label':'3',
        'positive_total_energy_label_trial_verified':True,'exact_recurrent_transfer_counterexamples':transfers,
        'survival_and_spectator_records_retained':True,'CAR_statistics_native_derived':False,
        'charge_conjugation_native_selected':False,'native_joint_contact_licensed':False,
        'physical_electron_positron_preparation_bound':False,'couplings_source_selected':False,
        'irreversible_annihilation_constructed':False,'outgoing_spatial_continuum_constructed':False,
        'local_field_interaction_constructed':False,
        'full_Fock_wavepacket_constructed':False,'one_step_transfer_is_annihilation_rate':False,
        'branching_ratio_derived':False,'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],
        'analytic_argument_machine_formalized':False,'new_live_proposition_admitted':False,
        'C12_protocol_renewed':False,'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale graded contact vertex'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','derived_neutral_pair_action_in_extension',
        'self_adjoint_contact_vertex_constructed','complex_contact_intertwiner_dimension',
        'retained_ordered_raw_pair_complement_rank','exact_recurrent_transfer_counterexamples',
        'irreversible_annihilation_constructed','native_joint_contact_licensed','hostile_controls_refused')}))


if __name__=='__main__':main()
