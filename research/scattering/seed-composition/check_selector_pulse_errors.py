"""Area-error retry channels versus a retained doublet-coupling error fixture."""
from fractions import Fraction as F
import argparse
import json

from check_selector_continuous_control import audit as control_audit
from check_selector_failure_feedback import mul,dagger
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,decode,eye,record,load,digest,BASE
from check_diagonal_spin_networks import S2,S3,CI
from check_native_intrinsic_spinor_adapter import native_decode
from check_electron_charge_spin_frontier import spin

DEST=BASE/'results/selector-pulse-errors.v1.json'


def zero():return tuple(tuple(ZERO for _ in range(4)) for _ in range(4))
def trace(M):return sum((M[i][i] for i in range(4)),ZERO)
def pluspair(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def scalepair(c,X):return (scale(c,X[0]),scale(c,X[1]))
def unit(a,b):return tuple(tuple(ONE if i==a and j==b else ZERO for j in range(4)) for i in range(4))
def sandwich(R,X):return mm(mm(R,X),adj(R))
def encode(X):return {'constant':record(X[0]),'sqrt19':record(X[1])}


def audit():
    previous=control_audit()
    K=tuple(tuple(decode(x) for x in row) for row in load('research/strominger/results/common-endpoint-charging.json')['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));P=scale(A(F(1,2)),add(eye(4),Q));Pm=add(eye(4),scale(A(-1),P))
    axes=[tuple(tuple(decode(x) for x in row) for row in item['generator']) for item in previous['generators'] if not item['central_identity']]
    assert len(axes)==16
    total=zero()
    for J in axes:total=add(total,J)
    assert total==zero()
    # Direct exact axis second moment proves the common-area-error channel.
    for a in range(4):
        for b in range(4):
            X=sandwich(P,unit(a,b));Y=zero()
            for J in axes:Y=add(Y,scale(A(F(1,16)),sandwich(J,X)))
            assert Y==scale(A(F(1,3)),add(scale(A(2)*trace(X),P),scale(A(-1),X)))
    area_fixtures=[]
    for c,s in [(F(1),F(0)),(F(3,5),F(4,5)),(F(12,13),F(5,13))]:
        assert c*c+s*s==1
        coefficient=F(16,25)-F(304,375)*s*s
        beta=F(152,375)*s*s
        for a in range(4):
            for b in range(4):
                X=sandwich(P,unit(a,b));actual=scale(A(F(4,125)),X)
                for J in axes:
                    U=add(scale(A(c),P),scale(-CI*s,J))
                    actual=add(actual,scale(A(F(19,500)),sandwich(U,X)))
                assert actual==add(scale(A(coefficient),X),scale(A(beta)*trace(X),P))
        lam=1-F(19,15)*s*s;pooled=F(135)/(135+304*s*s)
        area_fixtures.append({'cos_delta':str(c),'sin_delta':str(s),'normalized_failure_Bloch_factor':str(lam),
                              'eventual_success_Bloch_factor':str(pooled),'pure_input_pooled_fidelity':str((1+pooled)/2)})

    # Reconstruct native S on both doublets to check the corrected failure
    # channel's cross-sector term, rather than dephasing sectors implicitly.
    native=load('research/voevodsky/results/electron_tetrahedral_spinor_store.json')
    face=[tuple(tuple(native_decode(x) for x in row) for row in p) for p in native['face_projectors']]
    n0=A(F(1,2))+S3/6;anchor=tuple(face[0][i][0] for i in range(2));w=[anchor]
    for i in range(1,4):w.append(tuple(row[0]/Q[i][0] for row in mm(face[i],tuple((x,) for x in anchor))))
    V=tuple(tuple(w[j][i%2] if i//2==j else ZERO for j in range(4)) for i in range(8));D=scale(n0.inverse(),adj(V))
    branches=[]
    for item in previous['generators']:
        q=tuple(F(x) for x in item['quaternion']);sign=1 if q[0]>0 else -1
        U=tuple(tuple(A(x[0])+CI*A(x[1]) for x in row) for row in spin(q))
        perm=[face.index(mm(mm(U,x),adj(U))) for x in face]
        raw=tuple(tuple(U[i%2][j%2] if i//2==perm[j//2] else ZERO for j in range(8)) for i in range(8))
        S=scale(A(sign),mm(mm(D,raw),V))
        if abs(q[0])==1:branches.append((F(1,10),(add(S,scale(A(F(-3,5)),P)),zero())))
        else:branches.append((F(1,20),(mm(Pm,S),scale(A(F(1,5)),P))))
    def phi_matrix(X):
        xp=sandwich(P,X);xm=sandwich(Pm,X);cross=add(mm(mm(P,X),Pm),mm(mm(Pm,X),P))
        constant=add(add(scale(A(F(16,25)),xp),scale(A(F(1,5)),xm)),scale(A(F(2,5))*trace(xm),Pm))
        return (add(constant,scale(A(F(2,25)),cross)),scale(A(F(-1,25)),cross))
    def phi(X):
        y=phi_matrix(X[0]);z=phi_matrix(X[1])
        return (add(y[0],scale(A(19),z[1])),add(y[1],z[0]))
    for a in range(4):
        for b in range(4):
            X=(unit(a,b),zero());Y=(zero(),zero())
            for probability,R in branches:Y=pluspair(Y,scalepair(A(probability),mul(mul(R,X),dagger(R))))
            assert Y==phi(X)
    I=(eye(4),zero());Pi=(P,zero());Pmi=(Pm,zero())
    assert phi(I)==(add(scale(A(F(16,25)),P),Pm),zero())

    # An explicit Hermitian unitary swaps the two logical doublets, staying
    # inside the four-dimensional ground. This is not excited-state leakage.
    def frame(projector):
        col=lambda i:tuple((S2*projector[j][i],) for j in range(4))
        u=col(0);v=col(1);overlap=mm(adj(u),v)[0][0]
        orth=scale(S3/S2,add(v,scale(-overlap,u)))
        result=tuple((u[i][0],orth[i][0]) for i in range(4));assert mm(adj(result),result)==eye(2)
        assert mm(result,adj(result))==projector
        return result
    Up=frame(P);Um=frame(Pm);B=add(mm(Up,adj(Um)),mm(Um,adj(Up)))
    assert adj(B)==B and mm(B,B)==eye(4) and add(mm(B,Q),mm(Q,B))==zero()
    c,s=F(99,101),F(20,101);assert c*c+s*s==1
    Vmix=(add(scale(A(c),eye(4)),scale(-CI*s,B)),zero())
    assert mul(dagger(Vmix),Vmix)==I
    # Phi is self-adjoint as a superoperator; the mixed retry dual is
    # Phi(Vmix* X Vmix). No intermediate sector measurement is inserted.
    dual=lambda X:phi(mul(mul(dagger(Vmix),X),Vmix))
    q=F(9,25);first=(scale(A(q),P),zero());failure=I;cumulative=(zero(),zero());mix_depth=[]
    Z=scale(CI,add(mm(B,P),scale(A(-1),mm(P,B))))
    assert adj(Z)==Z and mm(Z,Z)==eye(4)
    diagonal_two=add(scale(A(1+F(16,25)*c*c),P),scale(A(s*s),Pm))
    two_step=(scale(A(q),add(diagonal_two,scale(A(F(2,25)*c*s),Z))),scale(A(-q*c*s/25),Z))
    assert pluspair(first,dual(first))==two_step
    for n in range(6):
        assert pluspair(failure,cumulative)==I
        minus_success=mul(mul(Pmi,cumulative),Pmi)
        plus_success=mul(mul(Pi,cumulative),Pi)
        mix_depth.append({'attempts':n,'success_effect':encode(cumulative),
                          'maximally_mixed_minus_success_probability':{'constant':(trace(minus_success[0])/2).record(),'sqrt19':(trace(minus_success[1])/2).record()},
                          'maximally_mixed_plus_success_probability':{'constant':(trace(plus_success[0])/2).record(),'sqrt19':(trace(plus_success[1])/2).record()}})
        if n==2:assert minus_success==(scale(A(q*s*s),Pm),zero())
        cumulative=pluspair(cumulative,first);first=dual(first);failure=dual(failure)
    # For t=(2-sqrt19)/25, |t|<1/10. Two-step success is
    # q[(1+16c²/25)P+s²Pm+i*c*s*t*(BP-PB)]. Its off-diagonal
    # norm <= c*s/10, giving success >= kappa*I for this fixture.
    assert F(4)<19<F(81,4)  # 2<sqrt19<9/2
    kappa=q*(s*s-c*s/10);assert kappa>0
    assert 1+F(16,25)*c*c>=s*s
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_selector_pulse_errors.py'}
    return {
        'schema':'marici.scattering.selector-pulse-errors.v1',
        'status':'area_error_preserves_selection_but_disturbs_logical_state_doublet_coupling_changes_retry_selection',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'area_error':{'model':'same area error delta on all sixteen noncentral feedbacks; central feedback remains identity; fresh histories retained',
                       'axis_first_moment':'zero','axis_second_moment':'mean J_g X_plus J_g=(2 tr(X_plus)P_plus-X_plus)/3',
                       'failure_plus_channel':'[16/25-(304/375)sin²(delta)]X_plus+(152/375)sin²(delta)tr(X_plus)P_plus',
                       'conditional_failure_Bloch_factor':'1-(19/15)sin²(delta)',
                       'eventual_success_Bloch_factor':'135/[135+304 sin²(delta)]',
                       'ever_success_probability':'initial plus weight, unchanged',
                       'pure_plus_success_fidelity':'[1+135/(135+304 sin²(delta))]/2',
                       'small_error_infidelity':'(152/135)delta²+O(delta^4)',
                       'fixtures':area_fixtures,'reduced_statistics_destroy_joint_history':False},
        'corrected_full_failure_channel':{'plus_block':'(16/25)X_plus','minus_block':'(1/5)X_minus+(2/5)tr(X_minus)P_minus',
                                          'cross_block_factor':'(2-sqrt(19))/25','direct_operator_basis_checks':16,
                                          'sector_dephasing_silently_inserted':False},
        'doublet_coupling_fixture':{'mixing_generator':record(B),'identities':['B*=B','B²=I','BQ+QB=0'],
                                    'unitary':'V_epsilon=cos(epsilon)I-i sin(epsilon)B, applied after every corrected failure',
                                    'cos_epsilon':str(c),'sin_epsilon':str(s),'coupled_complement':'minus doublet inside the retained ground; not the excited twelve-dimensional complement',
                                    'one_step_failure_effect_unchanged':True,'retry_effects_change':True,
                                    'minus_success_at_attempt_two':'(9/25)sin²(epsilon)',
                                    'finite_depths':mix_depth,
                                    'two_step_success_lower_bound':str(kappa),
                                    'all_failure_after_2n_upper_bound':'(1-kappa)^n I',
                                    'ever_success_effect':'I for this fixture, by the uniform bound',
                                    'ever_success_preserves_arbitrary_input_logical_state':False,
                                    'coupling_is_native_source_interaction':False,
                                    'gauge_extension':'extend the ground unitary by identity on its orthogonal physical complement and gauge sectors; this is an added control, not a pulse synthesis'},
        'boundary':{'controls_from_predecessors_still_required':True,'failure_and_controller_records_retained':True,
                    'calibration_fixture_is_physical_noise_measurement':False,
                    'physical_spin_or_annihilation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Compute the retained input-to-success channel of the explicit doublet-coupling recycling fixture, including a reference-system witness. Test whether eventual unit success preserves encoded information or instead gives a lossy preparation, and identify where the distinguishing input/history records reside.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale pulse-error receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact area-error channel and pooled retry fidelity; sector selection unchanged with histories retained.')
    print('PASS: actual coherent doublet-coupling retries change selection; a two-step bound proves unit eventual success, not lossless encoding.')


if __name__=='__main__':main()
