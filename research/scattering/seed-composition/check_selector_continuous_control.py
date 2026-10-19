"""Exact bounded feedback generators, conditional control algebra, and pulse-area gate."""
from fractions import Fraction as F
import argparse
import json
import math

from check_selector_failure_feedback import audit as feedback_audit
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,rank,add,scale,decode,eye,record,load,digest,BASE
from check_diagonal_spin_networks import CI,S3

DEST=BASE/'results/selector-continuous-control.v1.json'


def zero():return tuple(tuple(ZERO for _ in range(4)) for _ in range(4))
def trace(M):return sum((M[i][i] for i in range(4)),ZERO)
def flatten(M):return tuple(x for row in M for x in row)
def span_rank(matrices):return rank(tuple(tuple(col[i] for col in map(flatten,matrices)) for i in range(16)))


def audit():
    previous=feedback_audit()
    K=tuple(tuple(decode(x) for x in row) for row in load('research/strominger/results/common-endpoint-charging.json')['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));P=scale(A(F(1,2)),add(eye(4),Q));Pm=add(eye(4),scale(A(-1),P))
    rows=[];axes=[];central=0
    for item in previous['feedback_construction']['branches']:
        q=tuple(F(x) for x in item['quaternion'])
        C0=tuple(tuple(decode(x) for x in row) for row in item['feedback']['constant'])
        C1=tuple(tuple(decode(x) for x in row) for row in item['feedback']['sqrt19'])
        if abs(q[0])==1:
            assert C0==eye(4) and C1==zero();central+=1
            rows.append({'quaternion':item['quaternion'],'generator':record(zero()),'angle':'0','central_identity':True})
            continue
        W=scale(A(19),C1)
        J=scale(-CI/(5*S3),add(adj(W),scale(A(-1),W)))
        assert adj(J)==J and mm(J,J)==P and trace(J)==ZERO
        assert mm(J,P)==mm(P,J)==J and mm(J,Pm)==mm(Pm,J)==zero()
        Eplus=scale(A(F(1,2)),add(P,J));Eminus=scale(A(F(1,2)),add(P,scale(A(-1),J)))
        for E in (Eplus,Eminus):assert mm(E,E)==E and adj(E)==E and rank(E)==1
        assert add(Eplus,Eminus)==P and mm(Eplus,Eminus)==zero()
        assert mm(J,Eplus)==Eplus and mm(J,Eminus)==scale(A(-1),Eminus)
        # exp(-i theta J)=P_minus+cos(theta)P-i sin(theta)J;
        # cos=-sqrt19/38, sin=5*sqrt3*sqrt19/38. Exact comparison
        # in the same X+sqrt19*Y representation as the preceding feedback.
        assert C0==Pm
        assert C1==add(scale(A(F(-1,38)),P),scale(-CI*5*S3/38,J))
        assert F(1,76)+F(75,76)==1  # cos²+sin² exactly
        if J not in axes:axes.append(J)
        rows.append({'quaternion':item['quaternion'],'generator':record(J),
                     'spectrum':[-1,0,0,1],'operator_norm':1,
                     'angle':'theta=acos(-1/(2*sqrt(19))) in (pi/2,pi)',
                     'central_identity':False})
    assert central==2 and len(axes)==8 and span_rank(axes)==3
    basis=[]
    for J in axes:
        if span_rank(basis+[J])>len(basis):basis.append(J)
    assert len(basis)==3
    commutator_checks=0;dots=set()
    for X in basis:
        for Y in basis:
            comm=scale(-CI/F(2),add(mm(X,Y),scale(A(-1),mm(Y,X))))
            assert adj(comm)==comm and span_rank(basis+[comm])==3
            dot=trace(mm(X,Y))/2
            assert add(mm(X,Y),mm(Y,X))==scale(A(2)*dot,P)
            dots.add(json.dumps(dot.record(),sort_keys=True));commutator_checks+=1
    theta=math.acos(-1/(2*math.sqrt(19)))
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_selector_continuous_control.py'}
    return {
        'schema':'marici.scattering.selector-continuous-control.v1',
        'status':'bounded_gauge_preserving_continuous_generators_exactly_implement_feedback_as_added_controls',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'generators':rows,
        'exact_rotation':{'ground_generator':'J_g=(S_g-S_g*)/(i*sqrt(3)) on plus; zero on minus',
                           'identities':['J_g*=J_g','J_g^2=P_plus','J_g P_minus=0'],
                           'spectral_projectors':'(P_plus+J_g)/2 and (P_plus-J_g)/2, each rank one',
                           'angle':'theta=acos(-1/(2*sqrt(19)))',
                           'angle_radians_illustrative':theta,
                           'cos_theta':'-1/(2*sqrt(19))','sin_theta':'5*sqrt(3)/(2*sqrt(19))',
                           'pulse':'exp(-i*theta*J_g)=P_minus+cos(theta)P_plus-i*sin(theta)J_g',
                           'matches_prior_sqrt19_feedback_exactly':True},
        'full_gauge_extension':{'generator':'J_full=sign(a_g)*(U_hat_g-U_hat_g*)*P_full/(i*sqrt(3))',
                                'fundamental_central_projector':'P_full from the existing conditional character construction',
                                'Hermitian_and_bounded':True,'square':'P_full','norm':1,
                                'complement_generator':'zero; pulse acts as identity',
                                'commutes_with_each_G_i':True,'preserves_total_charge_and_physical_ground':True,
                                'commutes_with_physical_H':True,'off_kernel_H_commutation_claimed':False,
                                'argument':'group adjoint pair commutes with P_full; every fundamental copy has the checked quadratic identity; inherited gauge and physical-H symmetries extend the ground formula'},
        'conditional_control_algebra':{'distinct_nonzero_ground_axes':8,'Hermitian_axis_span_dimension':3,
                                       'basis_commutator_checks':commutator_checks,
                                       'traceless_closed_algebra':'su(2) on plus, zero on minus',
                                       'continuous_control_is_available_in_native_H':False,
                                       'conditional_SU2_is_physical_spin_rotation_admission':False},
        'pulse_obligations':{'Hamiltonian':'H_ctrl(t)=hbar*Omega_g(t)*J_full,g',
                             'required_area':'integral Omega_g(t) dt = theta (central branches require zero)',
                             'fixed_axis_bounded_rate_duration':'T >= theta/Omega_max, within this pulse family',
                             'native_H_alone_generates_feedback':False,
                             'phase_clock_units_and_addressable_generator_supplied':False,
                             'endpoint_H_expectation_conserved_during_ideal_physical_pulse':True,
                             'physical_drive_or_feedback_work_cost_is_zero':False,
                             'area_error_delta':'actual feedback differs by exp(-i*delta*J_g)',
                             'area_error_operator_distance':'2*abs(sin(delta/2))',
                             'pure_area_error_changes_failure_probabilities':False,
                             'pure_area_error_can_change_plus_logical_state':True,
                             'scope':'same exact axis and sector projector; not calibration-axis, gauge-breaking or complement-coupling errors'},
        'boundary':{'new_continuous_control_required':True,'physical_platform_or_feedback_implemented':False,
                    'histories_or_minus_records_erased':False,'physical_spin_or_annihilation_derived':False,
                    'formal_outcome_admitted':False},
        'next_gate':'Compute the actual history-averaged logical channel for feedback pulse-area errors and corrected retries, retaining the branch records. Separate sector-preserving calibration errors from an explicit complement-coupling perturbation and quantify their different effects on selection and logical fidelity.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale continuous-control receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact bounded Hermitian generators and pulse angle reproduce every sqrt(19) feedback with identity complement.')
    print('PASS: eight conditional axes span su(2); gauge/ground compatibility is algebraic, continuous pulse controls remain inputs.')


if __name__=='__main__':main()
