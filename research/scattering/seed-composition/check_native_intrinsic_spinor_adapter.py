"""Exact native face adapter, residual-preserving global embedding and inverse-action distinction."""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json

from check_five_cell_attachment_bridge import (
    audit as bridge_audit, load, digest, dense, record, A,S5,ZERO,ONE,mm,adj,rank,
    add,scale,decode,recover,smul,sadj,sparse,eye,power,ROOT,BASE)
from check_diagonal_spin_networks import S2

DEST=BASE/'results/native-intrinsic-spinor-adapter.v1.json'


def native_decode(x):
    coefficients=[F(0)]*16
    for k,v in [(0,x[0][0]),(2,x[0][1]),(8,x[1][0]),(10,x[1][1])]:coefficients[k]=F(v)
    return A(tuple(coefficients))


def audit():
    previous=bridge_audit()
    path='research/voevodsky/results/electron_tetrahedral_spinor_store.json'
    native=load(path);receipt_path='research/voevodsky/results/electron_tetrahedral_spinor.json';receipt=load(receipt_path)
    assert receipt['verification_passed']
    producer='research/voevodsky/checkers/check_electron_tetrahedral_spinor.py'
    prerequisite='research/voevodsky/results/electron_charge_spin_frontier.json'
    assert digest(prerequisite)==receipt['source_sha256']
    producer_hash_matches=digest(producer)==receipt['checker_sha256']
    # Do not repair or silently trust a stale producer receipt. All adapter and
    # stage identities below are recomputed from the current stored matrices.
    projectors=[tuple(tuple(native_decode(x) for x in row) for row in P) for P in native['face_projectors']]
    native_J=tuple(tuple(x/S2 for x in row) for P in projectors for row in P)
    assert mm(adj(native_J),native_J)==eye(2)
    operators={name:{} for name in ('L','G','N')}
    for arrow in native['arrows']:operators[arrow['stage']][arrow['target'],arrow['source']]=native_decode(arrow['weight'])
    Ln=dense(operators['L'],8,8);Nn=dense(operators['N'],8,8);Gn=dense(operators['G'],8,8)
    assert Nn==Gn==mm(native_J,adj(native_J))
    assert mm(Ln,native_J)==native_J
    assert [len(operators[k]) for k in ('L','G','N')]==[16,64,64]
    remainder=add(eye(8),scale(A(-1),Nn));assert rank(remainder)==6
    # Intrinsic cell-4 directed faces have reverse native face order, with the
    # same two-component Pauli frame. No fitted per-face unitary is necessary.
    perm=[6,7,4,5,2,3,0,1]
    S=tuple(tuple(ONE if i==perm[j] else ZERO for j in range(8)) for i in range(8))
    assert mm(adj(S),S)==eye(8)
    global_receipt=load('research/strominger/results/diagonal-spin-networks/verification.json')
    rows=[]
    for bridge in previous['bridges']:
        ch=bridge['chirality']
        local=tuple(tuple(decode(x) for x in row) for row in bridge['local_face_encoding'])
        assert local==mm(S,native_J)
        local_P=[scale(S2,tuple(local[2*i:2*i+2])) for i in range(4)]
        Li=tuple(tuple(local_P[i//2][i%2][j%2] if i//2==j//2 else ZERO for j in range(8)) for i in range(8))
        Ni=mm(local,adj(local))
        assert mm(S,Ln)==mm(Li,S) and mm(S,Nn)==mm(Ni,S)
        for carrier in ('constant','complementary'):
            packet=load(f'research/strominger/results/diagonal-spin-networks/chirality-{ch}-{carrier}.json')
            P=tuple(tuple(decode(x) for x in row) for row in packet['logical_projector'])
            W=tuple(tuple(S5*row[8+j] for j in range(2)) for row in P)
            J=recover(packet['encoding']);global_frame=smul(J,sparse(W))
            Fmap=smul(global_frame,sparse(adj(native_J)))
            Fdense=dense(Fmap,40,8)
            assert smul(sadj(Fmap),Fmap)==operators['N']
            for stage in ('L','G','N'):
                assert smul(Fmap,operators[stage])==smul(recover(packet['operators'][stage]),Fmap)
            # Full native input is not squeezed into a rank-two output: retain
            # the six-dimensional rejected complement as a separate record.
            assert add(mm(adj(Fdense),Fdense),mm(adj(remainder),remainder))==eye(8)
            assert mm(Fdense,remainder)==tuple(tuple(ZERO for _ in range(8)) for _ in range(40))
            case=next(case for case in global_receipt['cases'] if case['chirality']==ch)
            action=next(a for a in case['actions'] if len(a['cycle'])==6)
            T=tuple(tuple(decode(x) for x in row) for row in action['logical_transport'])
            U=mm(mm(adj(W),T),W)
            assert mm(T,W)==mm(W,U) and mm(adj(U),U)==eye(2)
            assert power(U,5)==scale(A(-1),eye(2)) and power(U,10)==eye(2)
            assert power(U,2)!=eye(2) and U!=eye(2)
            conjugate=tuple(tuple(x.flip(8) for x in row) for row in U)
            assert adj(U)!=conjugate
            # A conditional extension to the native raw carrier, not an element
            # newly inferred inside the native binary-tetrahedral source group.
            Un=add(mm(mm(native_J,U),adj(native_J)),remainder)
            assert mm(adj(Un),Un)==eye(8) and mm(Un,native_J)==mm(native_J,U)
            rows.append({'chirality':ch,'carrier':carrier,'face_adapter_permutation':perm,
                         'local_encoding_equals_S_native_J':True,'local_L_G_N_intertwining':True,
                         'global_map_rank':2,'global_map_isometry_domain':'im(native N)',
                         'global_L_G_N_intertwining':True,'residual_rank':rank(remainder),
                         'combined_map_isometry_on_all_native_inputs':True,
                         'decoder':'F* global_record + residual_record',
                         'logical_five_cycle':record(U),'logical_inverse':record(adj(U)),
                         'logical_entrywise_conjugate':record(conjugate),
                         'logical_lift_order':10,'inverse_equals_entrywise_conjugate':False,
                         'native_raw_conditional_lift_unitary':True})
    dependencies=set(previous['source_sha256'])|{path,receipt_path,producer,prerequisite,
        'research/scattering/seed-composition/check_native_intrinsic_spinor_adapter.py'}
    return {
        'schema':'marici.scattering.native-intrinsic-spinor-adapter.v1',
        'status':'exact_local_frame_and_conditional_global_protocol_bridge_inverse_lift_not_entrywise_conjugation',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'native_protocol':{'raw_coordinates':8,'logical_rank':2,'stage_supports':[16,64,64],'transfers':144},
        'receipt_freshness':{'prerequisite_hash_matches':True,'producer_hash_matches_historical_receipt':producer_hash_matches,
                            'historical_receipt_claimed_as_fresh_producer_replay':False,
                            'adapter_and_stage_algebra_recomputed_from_store':True,
                            'shared_receipt_repaired':False},
        'adapter_cases':rows,
        'selection_boundary':{'two_global_doublets_still_possible':True,'face_adapter_selects_global_doublet':False,
                               'global_3120_protocol_replaces_native_144':False},
        'operation_boundary':{'source_geometric_cycle_order':5,'displayed_spin_lift_order':10,
                               'native_binary_tetrahedral_group_order':24,
                               'displayed_order_ten_lift_in_native_group':False,
                               'reason':'an element order divides finite group order; ten does not divide twenty-four',
                               'inverse_operation':'unitary adjoint, not entrywise coefficient conjugation in this adapter frame',
                               'frame_dependent_conjugation_comparison':True,
                               'all_antiunitary_intertwiners_excluded':False},
        'boundary':{'physical_charge_conjugation_derived':False,'native_stage_transport_is_physical_energy_transport':False,
                    'source_library_enlargement_authorized':False,'shared_artifacts_rewritten':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Test a frame-explicit antiunitary intertwiner for the transported five-cycle and its reverse, retaining the native charge family Q_q=qN. Determine whether that intertwiner reverses the charge operator or only the seed/representation action.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale native/intrinsic adapter receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: reverse face-order adapter exactly matches native and intrinsic Pauli encodings and L/G/N stages.')
    print('PASS: four global embeddings retain rank-six native residuals; lifted cycle has order ten and inverse differs from entrywise conjugation.')
    print('Boundary: conditional source-library extension, not derived physical charge conjugation or doublet selection.')


if __name__=='__main__':main()
