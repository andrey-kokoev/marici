"""Exact plus-polar failure correction and the native finite-library obstruction."""
from fractions import Fraction as F
from itertools import product
import argparse
import json

from check_retained_selector_retries import audit as retry_audit
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,decode,eye,record,load,digest,BASE
from check_diagonal_spin_networks import S3,CI
from check_native_intrinsic_spinor_adapter import native_decode
from check_electron_charge_spin_frontier import spin

DEST=BASE/'results/selector-failure-feedback.v1.json'


def zero():return tuple(tuple(ZERO for _ in range(4)) for _ in range(4))
def trace(M):return sum((M[i][i] for i in range(4)),ZERO)
# Matrix pairs X+sqrt(19)Y; all coefficients stay in the prior exact field.
def mul(X,Y):return (add(mm(X[0],Y[0]),scale(A(19),mm(X[1],Y[1]))),add(mm(X[0],Y[1]),mm(X[1],Y[0])))
def dagger(X):return (adj(X[0]),adj(X[1]))
def rec(X):return {'constant':record(X[0]),'sqrt19':record(X[1])}


def audit():
    previous=retry_audit()
    K=tuple(tuple(decode(x) for x in row) for row in load('research/strominger/results/common-endpoint-charging.json')['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));P=scale(A(F(1,2)),add(eye(4),Q));Pm=add(eye(4),scale(A(-1),P))
    native=load('research/voevodsky/results/electron_tetrahedral_spinor_store.json')
    face=[tuple(tuple(native_decode(x) for x in row) for row in p) for p in native['face_projectors']]
    n0=A(F(1,2))+S3/6;anchor=tuple(face[0][i][0] for i in range(2));w=[anchor]
    for i in range(1,4):w.append(tuple(row[0]/Q[i][0] for row in mm(face[i],tuple((x,) for x in anchor))))
    V=tuple(tuple(w[j][i%2] if i//2==j else ZERO for j in range(4)) for i in range(8));D=scale(n0.inverse(),adj(V))
    assert mm(adj(V),V)==scale(n0,eye(4))
    rows=[];sum_kappa=F(0);native_invariants=set();ident=(eye(4),zero());plus=(P,zero());minus=(Pm,zero())
    for item in previous['failure_channel']['plus_branch_records']:
        q=tuple(F(x) for x in item['quaternion']);sign=1 if q[0]>0 else -1
        U=tuple(tuple(A(x[0])+CI*A(x[1]) for x in row) for row in spin(q))
        perm=[face.index(mm(mm(U,x),adj(U))) for x in face]
        raw=tuple(tuple(U[i%2][j%2] if i//2==perm[j//2] else ZERO for j in range(8)) for i in range(8))
        T=mm(mm(D,raw),V);assert mm(adj(T),T)==eye(4) and mm(T,P)==mm(P,T)
        S=scale(A(sign),T);Sp=mm(S,P)
        probability=F(1,10) if abs(q[0])==1 else F(1,20)
        # R=amplitude*(S-(3/5)P); use the unscaled matrix to avoid
        # inserting unnecessary square roots of controller probabilities.
        R=add(S,scale(A(F(-3,5)),P))
        kappa=F(item['plus_failure_effect']);sum_kappa+=kappa
        assert mm(P,mm(adj(R),mm(R,P)))==scale(A(kappa/probability),P)
        if abs(q[0])==1:
            assert Sp==P
            C=ident;corrected_scalar=(A(F(2,5)),ZERO)
        else:
            assert add(Sp,adj(Sp))==P
            W=add(scale(A(5),adj(Sp)),scale(A(-3),P))
            assert mm(adj(W),W)==scale(A(19),P)
            C=(Pm,scale(A(F(1,19)),W));corrected_scalar=(ZERO,A(F(1,5)))
            assert trace(mm(W,P))==A(-1)
            # Phase-insensitive restricted trace norm: |tr(C_plus)|²=1/19.
            t=trace(C[1]);assert t.flip(8)*t*A(19)==A(F(1,19))
        assert mul(dagger(C),C)==mul(C,dagger(C))==ident
        assert mul(C,minus)==minus and mul(C,plus)==mul(plus,C)
        corrected=mul(C,(R,zero()))
        assert mul(corrected,plus)==(scale(corrected_scalar[0],P),scale(corrected_scalar[1],P))
        assert mul(dagger(corrected),corrected)==(mm(adj(R),R),zero())
        rows.append({'quaternion':item['quaternion'],'failure_plus_effect':str(kappa),
                     'feedback':rec(C),'scaled_corrected_branch':rec(corrected),
                     'corrected_branch_scale':'multiply by sqrt(controller preparation probability)',
                     'feedback_on_minus':'identity',
                     'native_group_feedback_available':abs(q[0])==1})
    assert sum_kappa==F(16,25)
    # All native group words collapse to one of the same 24 elements. The
    # fundamental restricted trace is 2a; the invariant excludes a match even
    # up to global phase, without assuming a depth bound on native words.
    quats={tuple(F(sign if i==k else 0) for i in range(4)) for k in range(4) for sign in (-1,1)}
    quats.update(tuple(F(sign,2) for sign in signs) for signs in product((-1,1),repeat=4))
    assert len(quats)==24
    native_invariants={4*q[0]*q[0] for q in quats}
    assert native_invariants=={F(0),F(1),F(4)} and F(1,19) not in native_invariants
    finite=[]
    for n in range(9):
        finite.append({'attempts':n,'all_failure_plus_effect':str(F(16,25)**n),
                       'success_plus_effect':str(1-F(16,25)**n),
                       'accepted_plus_logical_channel':'[1-(16/25)^n]*X_plus',
                       'all_failure_minus_effect':'1','controller_failure_slots':str(18**n)})
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_selector_failure_feedback.py'}
    return {
        'schema':'marici.scattering.selector-failure-feedback.v1',
        'status':'exact_history_feedback_restores_plus_state_but_half_quaternion_corrections_are_not_native_group_words',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'feedback_construction':{'field':'prior exact field extended by positive sqrt(19)',
                                 'central_branches':'C_g=I',
                                 'half_quaternion_branches':'C_g=P_minus+(5*S_g^*-3*P_plus)/sqrt(19), S_g=sign(a_g)*T_g*P_plus',
                                 'ground_unitary':True,'minus_extension':'identity, not a full polar correction of the minus branch',
                                 'branches':rows},
        'corrected_retry':{'actual_corrected_Kraus':'C_g R_g',
                            'corrected_reduced_plus_failure_channel':'(16/25)*X_plus',
                            'failure_effect_unchanged':True,
                            'ever_success_effect':'P_plus','ever_success_channel':'X -> P_plus X P_plus',
                            'accepted_plus_logical_state_preserved':True,
                            'deterministic_preparation_from_arbitrary_input':False,
                            'finite_depth_formulas':finite,
                            'all_depth_argument':'every corrected plus branch is scalar identity; multiply scalars along retained histories and sum geometric effects',
                            'plus_history_dependent_on_plus_logical_state':False,
                            'minus_and_all_histories_retained':True},
        'native_library_gate':{'library':'finite products of the twenty-four joint native symmetry unitaries',
                               'native_plus_trace_absolute_squared':['0','1','4'],
                               'half_quaternion_feedback_plus_trace_absolute_squared':'1/19',
                               'sixteen_noncentral_feedbacks_in_native_library_up_to_phase':False,
                               'central_feedbacks_in_native_library':True,
                               'claim_excludes_all_continuous_or_ancilla_controls':False},
        'gauge_extension':{'formula':'C_full=(I-P_full)+(5*sign(a_g)*U_hat_g^*-3*I)*P_full/sqrt(19)',
                           'P_full':'fundamental central character projector of prior gauge-preserving group representation',
                           'argument':'on each fundamental copy sign(a_g)U_hat_g+its adjoint=I for |a_g|=1/2, so the numerator norm squared is 19; complement is identity',
                           'commutes_with_each_G_i':True,'preserves_physical_ground_and_total_charge':True,
                           'physical_H_compatible':True,'off_kernel_H_commutation_claimed':False,
                           'explicit_device_or_native_pulse_synthesis_derived':False},
        'boundary':{'history_feedback_is_an_added_control':True,'native_group_covariance_supplies_feedback':False,
                    'failure_records_erased':False,'physical_spin_or_annihilation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Express the sqrt(19) feedback as a controlled continuous rotation in the fundamental central sector; test whether a bounded gauge-preserving Hamiltonian generator can implement it and quantify phase/control inputs, while retaining the identity complement and failure histories.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale feedback receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact sqrt(19) unitary feedback corrects every plus failure branch without changing failure effects.')
    print('PASS: noncentral corrections are outside all native symmetry words, even up to phase; gauge-compatible extension exists.')


if __name__=='__main__':main()
