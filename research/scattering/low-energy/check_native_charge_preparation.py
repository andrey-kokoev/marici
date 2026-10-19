"""Read-only native charge/preparation audit and a resource-explicit raw flip candidate."""
import argparse
import ast
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_two_photon_helicity as two

three=two.three;pair=two.pair;measure=two.measure;phase=two.phase;cm=two.cm;x=two.x;F=two.F;ROOT=two.ROOT;HOME=two.HOME
CONTRACT=HOME/'contracts/native-charge-preparation.v1.json'
PROOF=HOME/'NATIVE-CHARGE-PREPARATION.md'
RESULT=HOME/'results/native-charge-preparation.v1.json'
PAIR_SOURCE=phase.BASE/'checkers/check_electron_pairing_coupling.py'
REV_SOURCE=phase.BASE/'checkers/check_geometric_cycle_reversal.py'
mm,adj,eye=phase.mm,phase.adj,phase.eye
add=x.add;scale=phase.scale;sub=two.sub


def vector_inner(a,b):return sum((v.conjugate()*w for v,w in zip(a,b)),F())
def projector(v):return [[a*b.conjugate() for b in v] for a in v]
def matrix_act(A,v):return cm.act(A,v)
def partial_trace(rho,keep):
    assert keep in (0,1) and len(rho)==4 and all(len(row)==4 for row in rho)
    return [[sum((rho[2*i+k][2*j+k] if keep==0 else rho[2*k+i][2*k+j] for k in range(2)),F())
             for j in range(2)] for i in range(2)]
def decode(A):return [[F(tuple(Q(v) for v in a)) for a in row] for row in A]

def validate_contract(c):
    assert c['schema']=='marici.scattering.native-charge-preparation.v1'
    assert c['audit_scope']=='inspected_native_spinor_frontier_pairing_and_geometric_reversal_sources'
    for key in ('raw_flip_native_word_licensed','Pauli_polarization_identified_with_electromagnetic_charge',
                'antiunitary_reversal_is_quantum_channel','unitary_pair_charge_conjugation_selected',
                'fermionic_statistics_source_derived','source_pair_preparation_distribution_selected',
                'photon_number_charge_parity_source_bound','physical_electron_positron_preparation_bound',
                'contact_generator_constructed','branching_ratio_derived','live_proposition_inventory_changed',
                'C12_protocol_renewed','high_energy_protocol_executed','physical_outcomes_admitted'):
        assert c[key] is False,key


def build():
    c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
    parent=two.build();assert parent==json.loads(two.RESULT.read_text(encoding='utf-8')),'stale two-photon audit'
    source_pairs=[(phase.PRODUCER,phase.OWNER),(phase.ALGEBRA,phase.BASE/'results/electron_charge_spin_frontier.json'),
                  (PAIR_SOURCE,phase.BASE/'results/electron_pairing_coupling.json'),
                  (REV_SOURCE,phase.BASE/'results/geometric_cycle_reversal.json')]
    owner_paths=[phase.STORE]+[r for _,r in source_pairs]
    before={p:p.read_bytes() for p in owner_paths}
    # Bind the existing antiunitary formula without invoking its mutating main.
    tree=ast.parse(PAIR_SOURCE.read_text(encoding='utf-8'));main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
    Cdef=next(n for n in main.body if isinstance(n,ast.FunctionDef) and n.name=='C')
    assert ast.unparse(Cdef.body[0].value)=='act(neg(E), tuple(map(gc, z)))'
    Evalue=next(n.value for n in main.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='E' for t in n.targets))
    assert ast.unparse(Evalue)=='((G0, G1), (gs(-1, G1), G0))'
    raw=json.loads(before[phase.STORE]);assert set(raw)=={'field','normals','face_projectors','arrows'}
    P=[[[phase.decode(z) for z in row] for row in B] for B in raw['face_projectors']]
    normals=[[F(Q(a))+phase.SQ3*F(Q(b)) for a,b in n] for n in raw['normals']]
    assert all(B==scale(F(Q(1,2)),sub(eye(2),phase.pauli(n))) for B,n in zip(P,normals))
    plus=[sub(eye(2),B) for B in P]
    Jm=scale(F(1)/phase.SQ2,[row for B in P for row in B])
    Jp=scale(F(1)/phase.SQ2,[row for B in plus for row in B])
    assert mm(adj(Jm),Jm)==mm(adj(Jp),Jp)==eye(2) and mm(adj(Jm),Jp)==[[F()]*2 for _ in range(2)]
    Nm,Np=mm(Jm,adj(Jm)),mm(Jp,adj(Jp));residual=sub(sub(eye(8),Nm),Np)
    H=phase.blockdiag([phase.pauli(n) for n in normals])
    assert mm(H,Jm)==scale(F(-1),Jm) and mm(H,Jp)==Jp
    flip=add(add(mm(Jp,adj(Jm)),mm(Jm,adj(Jp))),residual)
    assert adj(flip)==flip and mm(flip,flip)==eye(8)
    assert mm(flip,Jm)==Jp and mm(flip,Jp)==Jm and mm(flip,residual)==residual
    assert mm(Nm,Np)==[[F()]*8 for _ in range(8)]
    epsilon=[[F(),F(1)],[F(-1),F()]];A2=scale(F(-1),epsilon);A8=phase.blockdiag([A2]*4)
    assert mm(A8,pair.conjugate(A8))==scale(F(-1),eye(8))
    assert mm(A8,pair.conjugate(Jm))==mm(Jp,A2)
    assert mm(mm(A8,pair.conjugate(Nm)),adj(A8))==Np
    assert mm(mm(A8,pair.conjugate(H)),adj(A8))==scale(F(-1),H)
    z=[F(1),F()];theta_z=matrix_act(A2,[v.conjugate() for v in z])
    theta_iz=matrix_act(A2,[(phase.IM*v).conjugate() for v in z])
    assert theta_iz==three.times(-phase.IM,theta_z) and theta_iz!=three.times(phase.IM,theta_z)
    # Replay the already existing source Choi witness, not a new source claim.
    swap=[[F(int((i//2,i%2)==(j%2,j//2))) for j in range(4)] for i in range(4)]
    K=phase.tensor(eye(2),A2);choi=scale(F(Q(1,2)),mm(mm(K,swap),adj(K)))
    bell=[F(1)/phase.SQ2,F(),F(),F(1)/phase.SQ2]
    assert vector_inner(bell,matrix_act(choi,bell))==F(Q(-1,2))
    Csame=decode(json.loads(pair.RESULT.read_text(encoding='utf-8'))['same_pair_Clebsch_Gordan_matrix'])
    Ps=projector([row[0] for row in Csame]);Pt=sub(eye(4),Ps)
    assert swap==sub(Pt,Ps) and mm(swap,swap)==eye(4)
    # The fixed stored stages preserve the negative code; a word cannot flip it.
    L=phase.blockdiag(P)
    assert mm(L,Jm)==mm(Nm,Jm)==Jm and mm(adj(Jm),mm(flip,Jm))==[[F()]*2 for _ in range(2)]
    assert mm(L,Jp)==mm(Nm,Jp)==[[F()]*2 for _ in range(8)]
    group,_,spin=phase.source_group();rotations=0
    for q in sorted(group):
        U=phase.from_spin(spin,q);images=[mm(mm(U,B),adj(U)) for B in P];perm=[P.index(B) for B in images]
        T=[[U[i%2][j%2] if i//2==perm[j//2] else F() for j in range(8)] for i in range(8)]
        assert mm(T,Jm)==mm(Jm,U) and mm(T,Jp)==mm(Jp,U)
        assert mm(T,flip)==mm(flip,T) and mm(A8,pair.conjugate(T))==mm(T,A8)
        V=phase.tensor(U,U)
        assert mm(V,swap)==mm(swap,V)
        for charge in (-2,-1,0,1,2):
            Qraw=scale(F(charge),sub(Np,Nm))
            assert mm(T,Qraw)==mm(Qraw,T) and mm(mm(flip,Qraw),flip)==scale(F(-1),Qraw)
        rotations+=1
    signs=[]
    for eta in (1,-1):
        Cp=scale(F(eta),swap);assert mm(Cp,Cp)==eye(4)
        diag=mm(mm(adj(Csame),Cp),Csame)
        expected=phase.blockdiag([[[F(-eta)]],scale(F(eta),eye(3))]);assert diag==expected
        P2=scale(F(Q(1,2)),add(eye(4),diag));P3=sub(eye(4),P2)
        W=mm(P2,adj(Csame))+mm(P3,adj(Csame))
        Cout=phase.blockdiag([eye(4),scale(F(-1),eye(4))])
        assert mm(adj(W),W)==eye(4) and mm(W,Cp)==mm(Cout,W)
        signs.append({'pair_operation':('swap' if eta==1 else 'minus_swap'),
                      'singlet_C':str(-eta),'triplet_C':str(eta),
                      'conditional_photon_C_selection':('singlet_three_triplet_two' if eta==1 else 'singlet_two_triplet_three')})
    opposite_encoding=phase.tensor(Jm,Jp)
    assert mm(adj(opposite_encoding),opposite_encoding)==eye(4)
    logical_total=add(phase.tensor(mm(adj(Jm),mm(H,Jm)),eye(2)),phase.tensor(eye(2),mm(adj(Jp),mm(H,Jp))))
    assert logical_total==[[F()]*4 for _ in range(4)]
    preparations=[]
    for p in (Q(),Q(1,4),Q(1,2),Q(1)):
        rho=add(scale(F(p),Ps),scale(F((1-p)/3),Pt))
        assert pair.trace(rho)==F(1) and adj(rho)==rho
        assert mm(mm(adj(Csame),rho),Csame)==phase.blockdiag([[[F(p)]],scale(F((1-p)/3),eye(3))])
        for q in group:
            U=phase.from_spin(spin,q);V=phase.tensor(U,U);assert mm(V,rho)==mm(rho,V)
        assert pair.trace(mm(Ps,rho))==F(p) and mm(logical_total,rho)==logical_total
        assert partial_trace(rho,0)==partial_trace(rho,1)==scale(F(Q(1,2)),eye(2))
        assert pair.trace(mm(scale(F(Q(1,2)),sub(eye(4),swap)),rho))==F(p)
        assert pair.trace(mm(scale(F(Q(1,2)),add(eye(4),swap)),rho))==F(1-p)
        preparations.append({'singlet_weight':str(p),'minus_swap_conditional_two_weight':str(p),
                             'swap_conditional_two_weight':str(1-p)})
    refused=[]
    for name in ('antiunitary_as_deterministic_channel','raw_flip_in_fixed_protocol','select_minus_swap_from_rotations',
                 'infer_unpolarized_preparation','calibrate_Pauli_as_electric_charge'):
        try:
            if name=='antiunitary_as_deterministic_channel':
                witness=vector_inner(bell,matrix_act(choi,bell));assert witness==F() or x.positive(witness)
            else:
                bad=copy.deepcopy(c)
                key={'raw_flip_in_fixed_protocol':'raw_flip_native_word_licensed',
                     'select_minus_swap_from_rotations':'unitary_pair_charge_conjugation_selected',
                     'infer_unpolarized_preparation':'source_pair_preparation_distribution_selected',
                     'calibrate_Pauli_as_electric_charge':'Pauli_polarization_identified_with_electromagnetic_charge'}[name]
                bad[key]=True;validate_contract(bad)
        except AssertionError:refused.append(name)
        else:raise AssertionError('unsupported charge/preparation promotion: '+name)
    source_receipts=[]
    for source,receipt in source_pairs:
        old=json.loads(before[receipt]);assert old['verification_passed'] is True
        source_receipts.append({'source':source.relative_to(ROOT).as_posix(),'receipt':receipt.relative_to(ROOT).as_posix(),
            'historical_checker_pin_matches_current':old.get('checker_sha256')==hashlib.sha256(source.read_bytes()).hexdigest()})
    assert all(p.read_bytes()==b for p,b in before.items())
    paths={ROOT/relative for relative in parent['source_sha256']}
    paths.update((two.RESULT,PAIR_SOURCE,REV_SOURCE,CONTRACT,PROOF,Path(__file__),HOME/'test_native_charge_preparation.py'))
    paths.update(owner_paths)
    return {'schema':'marici.scattering.native-charge-preparation-receipt.v1','status':'pass',
        'scope_verdict':'read_only_source_audit_raw_flip_candidate_and_unfixed_pair_charge_preparation',
        'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'inspected_source_receipts':source_receipts,'stored_fixture_fields':sorted(raw),
        'native_group_cases':rotations,'positive_Pauli_code_constructed':True,'opposite_codes_orthogonal':True,
        'linear_raw_flip_unitary_constructed':True,'linear_raw_flip':x.encoded(flip),
        'raw_complement_dimension_retained':4,'raw_flip_fixed_protocol_word_excluded':True,
        'stored_negative_protocol_annihilates_positive_code':True,
        'antiunitary_pseudoreal_square':'-I','existing_source_Choi_witness_replayed':'-1/2',
        'pair_swap_sign_counterexamples':signs,'conditional_charge_selector_isometry_Grams_verified':True,
        'rotation_invariant_preparation_counterexamples':preparations,
        'opposite_Pauli_pair_logical_total_polarization':'zero_for_all_preparations',
        'raw_flip_native_word_licensed':False,'Pauli_polarization_identified_with_electromagnetic_charge':False,
        'antiunitary_reversal_is_quantum_channel':False,'unitary_pair_charge_conjugation_selected':False,
        'fermionic_statistics_source_derived':False,'source_pair_preparation_distribution_selected':False,
        'photon_number_charge_parity_source_bound':False,'physical_electron_positron_preparation_bound':False,
        'contact_generator_constructed':False,'branching_ratio_derived':False,'owner_files_unchanged':True,
        'owner_producer_hash_matches_current':parent['owner_producer_hash_matches_current'],
        'analytic_argument_machine_formalized':False,'new_live_proposition_admitted':False,
        'C12_protocol_renewed':False,'high_energy_protocol_executed':False,'physical_outcomes_admitted':False,
        'hostile_controls_refused':refused}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args();r=build()
    if args.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale native charge/preparation audit'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','linear_raw_flip_unitary_constructed','raw_flip_fixed_protocol_word_excluded',
        'existing_source_Choi_witness_replayed','pair_swap_sign_counterexamples','source_pair_preparation_distribution_selected',
        'owner_files_unchanged','owner_producer_hash_matches_current','hostile_controls_refused')}))


if __name__=='__main__':main()
