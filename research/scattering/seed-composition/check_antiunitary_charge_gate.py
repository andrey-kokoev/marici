"""Cycle antiunitary, whole-library scope and the charge-sector obstruction."""
from fractions import Fraction as F
import argparse
import json

from check_native_intrinsic_spinor_adapter import audit as adapter_audit, native_decode
from check_five_cell_attachment_bridge import (
    load,digest,record,A,S5,ZERO,ONE,mm,adj,rank,add,scale,decode,eye,ROOT,BASE)
from check_diagonal_spin_networks import CI

DEST=BASE/'results/antiunitary-charge-gate.v1.json'


def conjugate(M):return tuple(tuple(x.flip(8) for x in row) for row in M)
def trans(M):return tuple(zip(*M))
def block(Aa,Bb):
    return tuple(tuple(Aa[i][j] if i<2 and j<2 else Bb[i-2][j-2] if i>=2 and j>=2 else ZERO for j in range(4)) for i in range(4))
def anti_action(B,U):return mm(mm(B,conjugate(U)),adj(B))


def audit():
    previous=adapter_audit()
    X=((ZERO,ONE),(ONE,ZERO))
    epsilon=((ZERO,ONE),(-ONE,ZERO))
    assert mm(X,conjugate(X))==eye(2)
    assert mm(epsilon,conjugate(epsilon))==scale(A(-1),eye(2))
    native=load('research/voevodsky/results/electron_tetrahedral_spinor_store.json')
    projectors=[tuple(tuple(native_decode(x) for x in row) for row in P) for P in native['face_projectors']]
    from check_diagonal_spin_networks import S2
    J=tuple(tuple(x/S2 for x in row) for P in projectors for row in P)
    N=mm(J,adj(J))
    # Native raw anti-linear coefficient matrix: J X J^t K, only on im N.
    M=mm(mm(J,X),trans(J))
    assert mm(M,adj(M))==N and mm(adj(M),M)==conjugate(N)
    assert mm(M,conjugate(M))==N
    charges=[]
    for q in [-2,-1,0,1,2]:
        Q=scale(A(q),N);image=mm(mm(M,conjugate(Q)),adj(M))
        assert image==Q
        assert (image==scale(A(-1),Q))==(q==0)
        charges.append({'q':q,'antiunitary_preserves_Qq':True,'reverses_Qq':q==0})
    source=load('research/strominger/results/diagonal-spin-networks/verification.json')
    cases=[]
    for chirality in (1,-1):
        for carrier in ('constant','complementary'):
            packet=load(f'research/strominger/results/diagonal-spin-networks/chirality-{chirality}-{carrier}.json')
            P=tuple(tuple(decode(x) for x in row) for row in packet['logical_projector'])
            W=tuple(tuple(S5*row[8+j] for j in range(2)) for row in P)
            axes=[];triangle_failures=0;cycle_U=None
            for case in [c for c in source['cases'] if c['chirality']==chirality]:
                for action in case['actions']:
                    T=tuple(tuple(decode(x) for x in row) for row in action['logical_transport'])
                    U=mm(mm(adj(W),T),W)
                    assert anti_action(epsilon,U)==U  # pseudoreal SU(2), not inverse
                    axis=((U[0][1]+U[1][0])/(2*CI),
                          (U[0][1]-U[1][0])/2,
                          (U[0][0]-U[1][1])/(2*CI))
                    assert all(x.flip(8)==x for x in axis)
                    axes.append(axis)
                    if len(action['cycle'])==6:
                        assert anti_action(X,U)==adj(U)
                        assert conjugate(U)!=adj(U)
                        cycle_U=U
                    else:
                        if anti_action(X,U)!=adj(U):triangle_failures+=1
            assert rank(tuple(axes))==3 and triangle_failures>0
            # Antiunitary conjugation of Pauli observables induces an improper
            # orthogonal map O. Inverting aI+i n.sigma requires O*n=n because
            # antiunitarity flips i. Three independent axes force O=I, impossible.
            assert cycle_U is not None
            inverse=adj(cycle_U)
            D=block(cycle_U,inverse)
            swapX=tuple(tuple(X[i%2][j%2] if i//2!=j//2 else ZERO for j in range(4)) for i in range(4))
            Qdouble=block(eye(2),scale(A(-1),eye(2)))
            assert mm(swapX,conjugate(swapX))==eye(4)
            assert anti_action(swapX,D)==D
            assert anti_action(swapX,Qdouble)==scale(A(-1),Qdouble)
            cases.append({'chirality':chirality,'carrier':carrier,
                          'cycle_antiunitary':'C=X*K, X=[[0,1],[1,0]]',
                          'C_square':'+I','C_U_C_inverse':'U^-1',
                          'pseudoreal_antiunitary':'Theta=epsilon*K, epsilon=[[0,1],[-1,0]]',
                          'Theta_square':'-I','Theta_U_Theta_inverse':'U',
                          'source_library_axis_span':3,'fixed_X_triangle_failures':triangle_failures,
                          'single_antiunitary_inverts_entire_library':False,
                          'doubled_cycle':record(D),'doubled_charge':record(Qdouble),
                          'doubled_antiunitary_coefficient':record(swapX),
                          'doubled_swap_flips_assigned_charge':True})
    # Spectrum argument is stronger than this one candidate antiunitary:
    # any antiunitary within a qI logical doublet fixes qI for real q.
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_antiunitary_charge_gate.py'}
    return {
        'schema':'marici.scattering.antiunitary-charge-gate.v1',
        'status':'cycle_reversal_antiunitary_exists_but_does_not_reverse_native_scalar_charge_global_library_inversion_fails',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'cases':cases,'native_charge_tests':charges,
        'native_raw_lift':{'anti_linear_coefficient':'M=J*X*J^t; action x -> M*conjugate(x)',
                           'domain':'im native N only; rank-six residual stays separately retained',
                           'M_bar_M_equals_N':True,'M_bar_Qq_M_adj_equals_Qq':True},
        'charge_obstruction':{'any_within_doublet_antiunitary_flips_nonzero_q':False,
                              'proof':'Q_q restricts to real scalar qI; conjugation by any within-sector antiunitary fixes qI, whereas -qI has different spectrum for q!=0.',
                              'physical_external_charge_is_derived_from_qN':False},
        'library_scope':{'full_source_axis_rank':3,
                         'proof':'For U=aI+i*n.sigma an antiunitary induces improper O on Pauli observables. Inversion requires O*n=n. A rank-three axis span forces O=I, which is not improper.',
                         'seedwise_inverse_library_still_definable':True,
                         'inverse_library_is_one_universal_antiunitary':False,
                         'physical_time_reversal_identified':False},
        'conditional_doubling':{'logical_dimension':4,'sectors':'explicit +q and -q doublets',
                                'construction':'swap sectors together with X*K; blocks carry U and U^-1',
                                'charge_flip_and_tagged_cycle_covariance_verified':True,
                                'opposite_charge_sector_source_derived':False,
                                'sector_labels_are_physical_electron_positron':False},
        'boundary':{'all_antiunitary_cycle_intertwiners_excluded':False,'physical_charge_conjugation_derived':False,
                    'annihilation_or_photon_outputs_derived':False,'shared_artifacts_rewritten':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Compare the conditional doubled charge sectors with the owning external-charge/quotient-charge constructions: test whether an existing source supplies the sector swap and opposite charge operator, rather than assigning +q/-q labels to inverse seeds.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale antiunitary charge receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: X*K inverts the selected cycle but preserves qN; pseudoreal epsilon*K instead preserves SU(2) actions.')
    print('PASS: rank-three source axes obstruct one antiunitary library inverter; doubled assigned-charge swap is conditional.')
    print('Boundary: seed/representation reversal is not derived physical charge conjugation or annihilation.')


if __name__=='__main__':main()
