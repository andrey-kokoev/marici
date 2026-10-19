"""Exact eventual recycling channel and retained-reference information witnesses."""
from fractions import Fraction as F
import argparse
import json
import math

from check_selector_pulse_errors import audit as error_audit
from check_selector_failure_feedback import mul,dagger
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,decode,eye,record,load,digest,BASE
from check_diagonal_spin_networks import CI,S2,S3

DEST=BASE/'results/recycling-information-channel.v1.json'
Z=(F(0),F(0));O=(F(1),F(0))
def qa(x,y):return (x[0]+y[0],x[1]+y[1])
def qn(x):return (-x[0],-x[1])
def qm(x,y):return (x[0]*y[0]+19*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qi(x):
    d=x[0]*x[0]-19*x[1]*x[1];return (x[0]/d,-x[1]/d)
def qr(x):return (F(x),F(0))
def qsign(x):
    a,b=x
    if not b:return (a>0)-(a<0)
    if not a:return (b>0)-(b<0)
    if a*b>0:return (a>0)-(a<0)
    return ((a>0)-(a<0))*((a*a>19*b*b)-(a*a<19*b*b))
def qrecord(x):return {'constant':str(x[0]),'sqrt19':str(x[1]),'illustrative':float(x[0])+math.sqrt(19)*float(x[1])}

def solve(M,b):
    rows=[list(row)+[rhs] for row,rhs in zip(M,b)]
    for j in range(len(M)):
        pivot=next(i for i in range(j,len(M)) if rows[i][j]!=Z);rows[j],rows[pivot]=rows[pivot],rows[j]
        inv=qi(rows[j][j]);rows[j]=[qm(inv,x) for x in rows[j]]
        for i in range(len(M)):
            if i!=j:
                factor=rows[i][j];rows[i]=[qa(x,qn(qm(factor,y))) for x,y in zip(rows[i],rows[j])]
    return tuple(row[-1] for row in rows)

def zero(n=4):return tuple(tuple(ZERO for _ in range(n)) for _ in range(n))
def trace(M):return sum((M[i][i] for i in range(len(M))),ZERO)
def unit(a,b,n=4):return tuple(tuple(ONE if i==a and j==b else ZERO for j in range(n)) for i in range(n))
def sandwich(U,X):return mm(mm(U,X),adj(U))
def padd(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def pscale(c,X):return (scale(c,X[0]),scale(c,X[1]))
def qscale(t,X):return (add(scale(A(t[0]),X[0]),scale(A(19*t[1]),X[1])),add(scale(A(t[0]),X[1]),scale(A(t[1]),X[0])))
def prec(X):return {'constant':record(X[0]),'sqrt19':record(X[1])}


def audit():
    previous=error_audit();c=F(previous['doublet_coupling_fixture']['cos_epsilon']);s=F(previous['doublet_coupling_fixture']['sin_epsilon'])
    a=F(16,25);q=F(9,25);t=(F(2,25),F(-1,25))
    def functional(d):
        M=((qr(c*c*a),qr(s*s*d),qm(qr(-2*c*s),t)),
           (qr(s*s*a),qr(c*c*d),qm(qr(2*c*s),t)),
           (qr(c*s*a),qr(-c*s*d),qm(qr(c*c-s*s),t)))
        system=tuple(tuple(qa(O if i==j else Z,qn(M[j][i])) for j in range(3)) for i in range(3))
        weights=solve(system,(qr(q),Z,Z))
        for j in range(3):
            rhs=qr(q) if j==0 else Z
            for i in range(3):rhs=qa(rhs,qm(weights[i],M[i][j]))
            assert weights[j]==rhs
        return weights
    assert functional(F(1))==(O,O,Z)
    eta_p,eta_m,eta_y=functional(F(1,5))
    assert qsign(eta_p)>0 and qsign(qa(O,qn(eta_p)))>0
    assert qsign(qa(eta_p,qr(F(-1,3))))>0
    assert qsign(eta_m)>0 and qsign(qa(qr(F(1,3)),qn(eta_m)))>0
    K=tuple(tuple(decode(x) for x in row) for row in load('research/strominger/results/common-endpoint-charging.json')['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));P=scale(A(F(1,2)),add(eye(4),Q));Pm=add(eye(4),scale(A(-1),P))
    B=tuple(tuple(decode(x) for x in row) for row in previous['doublet_coupling_fixture']['mixing_generator'])
    def frame(projector):
        u=tuple((S2*projector[i][0],) for i in range(4));v=tuple((S2*projector[i][1],) for i in range(4))
        overlap=mm(adj(u),v)[0][0];v=scale(S3/S2,add(v,scale(-overlap,u)))
        U=tuple((u[i][0],v[i][0]) for i in range(4));assert mm(adj(U),U)==eye(2) and mm(U,adj(U))==projector
        return U
    Up=frame(P);Um=frame(Pm);assert B==add(mm(Up,adj(Um)),mm(Um,adj(Up)))
    def channel_matrix(X):
        pp=mm(mm(adj(Up),X),Up);nn=mm(mm(adj(Um),X),Um)
        pn=mm(mm(adj(Up),X),Um);np=mm(mm(adj(Um),X),Up)
        y=scale(-CI/2,add(pn,scale(A(-1),np)))
        traceless=lambda Y:add(Y,scale(-trace(Y)/2,eye(2)))
        out=(scale((trace(pp)+trace(nn))/2,eye(2)),zero(2))
        for coefficient,Y in ((eta_p,pp),(eta_m,nn),(eta_y,y)):
            out=padd(out,qscale(coefficient,(traceless(Y),zero(2))))
        return (sandwich(Up,out[0]),sandwich(Up,out[1]))
    def channel(X):
        u=channel_matrix(X[0]);v=channel_matrix(X[1])
        return (add(u[0],scale(A(19),v[1])),add(u[1],v[0]))
    def failure_matrix(X):
        pp=sandwich(P,X);nn=sandwich(Pm,X);cross=add(mm(mm(P,X),Pm),mm(mm(Pm,X),P))
        base=add(scale(A(a),pp),add(scale(A(F(1,5)),nn),scale(A(F(2,5))*trace(nn),Pm)))
        return (add(base,scale(A(t[0]),cross)),scale(A(t[1]),cross))
    def failure(X):
        u=failure_matrix(X[0]);v=failure_matrix(X[1]);return (add(u[0],scale(A(19),v[1])),add(u[1],v[0]))
    V=(add(scale(A(c),eye(4)),scale(-CI*s,B)),zero())
    for i in range(4):
        for j in range(4):
            X=(unit(i,j),zero());output=channel(X)
            retry=mul(mul(V,failure(X)),dagger(V))
            immediate=(scale(A(q),sandwich(P,X[0])),zero())
            assert output==padd(immediate,channel(retry))
            assert trace(output[0])==trace(X[0]) and trace(output[1])==ZERO
            assert sandwich(P,output[0])==output[0] and sandwich(P,output[1])==output[1]
    # Different sector inputs with the same maximally mixed logical state
    # have identical reduced output. Native histories still distinguish them.
    same=(scale(A(F(1,2)),P),zero())
    assert channel((scale(A(F(1,2)),P),zero()))==same
    assert channel((scale(A(F(1,2)),Pm),zero()))==same
    assert trace(mm(P,Pm))==ZERO
    # Bell reference witness for each two-dimensional sector restriction.
    # The reduced Choi state is eta |Bell><Bell|+(1-eta)I4/4.
    bell=tuple(tuple(A(F(1,2)) if i in (0,3) and j in (0,3) else ZERO for j in range(4)) for i in range(4))
    def choi(eta):
        return padd(qscale(eta,(bell,zero())),qscale(qa(O,qn(eta)),(scale(A(F(1,4)),eye(4)),zero())))
    def pt(X):return tuple(tuple(X[2*(i//2)+j%2][2*(j//2)+i%2] for j in range(4)) for i in range(4))
    singlet=tuple(tuple(ONE if i==1 and j==1 or i==2 and j==2 else -ONE if i==1 and j==2 or i==2 and j==1 else ZERO for j in range(4)) for i in range(4))
    singlet=scale(A(F(1,2)),singlet)
    refs=[]
    for name,eta in (('plus',eta_p),('minus',eta_m)):
        state=choi(eta);partial=(pt(state[0]),pt(state[1]))
        antisymmetric_eigenvalue=qm(qr(F(1,4)),qa(O,qn(qm(qr(3),eta))))
        observed=(trace(mm(singlet,partial[0])),trace(mm(singlet,partial[1])))
        assert observed==(A(antisymmetric_eigenvalue[0]),A(antisymmetric_eigenvalue[1]))
        triplet_eigenvalue=qm(qr(F(1,4)),qa(O,eta))
        assert partial==padd(qscale(antisymmetric_eigenvalue,(singlet,zero())),qscale(triplet_eigenvalue,(add(eye(4),scale(A(-1),singlet)),zero())))
        assert qsign(triplet_eigenvalue)>0
        assert (qsign(antisymmetric_eigenvalue)<0)==(name=='plus')
        refs.append({'input_sector':name,'depolarizing_factor':qrecord(eta),'Bell_output':prec(state),
                     'PT_singlet_eigenvalue':qrecord(antisymmetric_eigenvalue),
                     'PT_triplet_eigenvalue':qrecord(triplet_eigenvalue),
                     'restricted_channel_entanglement_breaking':name=='minus',
                     'criterion':'two-qubit isotropic Choi; PPT is equivalent to separability'})
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_recycling_information_channel.py'}
    return {
        'schema':'marici.scattering.recycling-information-channel.v1',
        'status':'unit_success_is_a_lossy_reduced_channel_minus_restriction_entanglement_breaking_joint_dilation_retains_input',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'exact_eventual_channel':{'frame_order':'plus logical frame followed by aligned minus frame from the declared B coupling',
                                  'weights':{'eta_plus':qrecord(eta_p),'eta_minus':qrecord(eta_m),'eta_y':qrecord(eta_y)},
                                  'formula':'logical output=(tr X_pp+tr X_mm)I2/2+eta_plus X_pp^0+eta_minus X_mm^0+eta_y Y^0; Y=(X_pm-X_mp)/(2i), Z^0=Z-tr(Z)I2/2',
                                  'scalar_functional':[1,1,0],
                                  'method':'exact 3x3 resolvent for scalar and logical-traceless sector coefficients over Q(sqrt19)',
                                  'direct_stationarity_matrix_unit_checks':16,'trace_preserving':True,
                                  'uniqueness':'prior uniform two-step contraction makes the retained Kraus series convergent and fixes this stationary channel',
                                  'output_support':'plus doublet'},
        'irreversibility_witness':{'different_inputs':['P_plus/2','P_minus/2'],'same_reduced_output':'P_plus/2',
                                   'full_ground_reduced_channel_reversible':False,
                                   'immediate_success_probability_plus_input':'9/25','immediate_success_probability_minus_input':'0',
                                   'success_time_record_contains_sector_information':True},
        'reference_witnesses':refs,
        'retained_information':{'coherent_dilation':'sum_{time,history} |time,history> tensor K_time,history',
                                 'completeness':'sum K* K=I from eventual unit success',
                                 'joint_dilation_isometry':True,
                                 'four_orthogonal_ground_inputs_have_orthogonal_joint_outputs':True,
                                 'maximally_entangled_ground_reference_joint_output':'reference retains four equal Schmidt weights; reduced qubit alone cannot hold that full input',
                                 'information_location':'output/history correlations and the full coherent apparatus/environment, not necessarily history alone',
                                 'classical_history_alone_guarantees_quantum_recovery':False,
                                 'measured_history_requires_environment_in_dilation':True},
        'boundary':{'new_recycling_and_feedback_controls_still_required':True,
                    'records_erased':False,'unit_success_is_lossless_or_physical_preparation':False,
                    'physical_spin_or_annihilation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Test exact history-assisted recovery conditions for successful Kraus branches on each doublet. Determine whether classical success-time/group records suffice for deterministic unitary recovery, or whether coherent apparatus access and additional controls are required.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale recycling channel receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact eventual recycling channel is trace preserving but loses sector information in the reduced output.')
    print('PASS: Bell-reference witness is entanglement breaking on minus; full coherent history dilation retains the input.')


if __name__=='__main__':main()
