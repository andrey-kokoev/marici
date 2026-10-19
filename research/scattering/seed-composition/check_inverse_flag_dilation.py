"""Exact inverse-filter flag dilation and the effect of measured versus coherent flags."""
from fractions import Fraction as F
import argparse
import json

from check_heralded_history_inverse import audit as inverse_audit,inverse2
from check_recycling_information_channel import qa,qn,qm as qmul,qr,qi,qsign,qrecord
from check_selector_failure_feedback import mul,dagger
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,decode,eye,record,digest,BASE

DEST=BASE/'results/inverse-flag-dilation.v1.json'


def zero(n):return tuple(tuple(ZERO for _ in range(n)) for _ in range(n))
def padd(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def pscale(c,X):return (scale(c,X[0]),scale(c,X[1]))
def qscale(c,X):return (add(scale(A(c[0]),X[0]),scale(A(19*c[1]),X[1])),add(scale(A(c[0]),X[1]),scale(A(c[1]),X[0])))
def decodepair(X):return tuple(tuple(tuple(decode(x) for x in row) for row in X[part]) for part in ('constant','sqrt19'))
def encode(X):return {'constant':record(X[0]),'sqrt19':record(X[1])}
def scalar(X):return (F(X['constant']),F(X['sqrt19']))


class Radicals:
    """Formal positive roots r,s,u with exact squared values in Q(sqrt19)."""
    def __init__(self,squares):self.squares=squares
    def clean(self,X):return {k:v for k,v in X.items() if any(x!=ZERO for M in v for row in M for x in row)}
    def add(self,X,Y):
        out=dict(X)
        for k,v in Y.items():out[k]=padd(out[k],v) if k in out else v
        return self.clean(out)
    def scale(self,c,X):return self.clean({k:pscale(c,v) for k,v in X.items()})
    def adj(self,X):return {k:dagger(v) for k,v in X.items()}
    def mul(self,X,Y):
        out={}
        for i,x in X.items():
            for j,y in Y.items():
                factor=qr(1)
                for bit,square in enumerate(self.squares):
                    if i&j&(1<<bit):factor=qmul(factor,square)
                k=i^j;value=qscale(factor,mul(x,y));out[k]=padd(out[k],value) if k in out else value
        return self.clean(out)
    def record(self,X):
        return [{'positive_root_mask':k,'coefficient':encode(v)} for k,v in sorted(X.items())]


def blocks(*entries):
    out={}
    for block,X in enumerate(entries):
        br,bc=divmod(block,2)
        for mask,pair in X.items():
            if mask not in out:out[mask]=[[[ZERO]*4 for _ in range(4)] for _ in range(2)]
            for part in range(2):
                for i in range(2):
                    for j in range(2):out[mask][part][2*br+i][2*bc+j]=pair[part][i][j]
    return {k:tuple(tuple(tuple(row) for row in M) for M in pair) for k,pair in out.items()}


def audit():
    previous=inverse_audit();rows=[]
    I=(eye(2),zero(2));I4={0:(eye(4),zero(4))}
    for item in previous['filters']:
        L=decodepair(item['unscaled_history_map']);Linv=inverse2(L)
        weight=F(item['history_scale_squared']);G=qscale(qr(weight),mul(dagger(L),L))
        # Recover the output spectral projectors directly from the witnessed
        # complete filter: F=sqrt(alpha)*Pi_high.
        H=decodepair(item['inverse_failure_Kraus']['matrix_projector']);Low=padd(I,pscale(A(-1),H))
        alpha=scalar(item['inverse_failure_Kraus']['positive_prefactor_squared']);ratio=qa(qr(1),qn(alpha))
        low_unscaled=scalar(item['inverse_success_Kraus']['positive_prefactor_squared'])
        assert qsign(ratio)>0 and qsign(alpha)>0 and qsign(low_unscaled)>0
        low=qmul(qr(weight),low_unscaled);high=qmul(low,qi(ratio))
        E_low=qscale(qmul(qr(weight),qi(low)),mul(mul(dagger(L),Low),L))
        E_high=qscale(qmul(qr(weight),qi(high)),mul(mul(dagger(L),H),L))
        assert padd(E_low,E_high)==I
        R=Radicals((ratio,alpha,low_unscaled))
        # r=sqrt(ratio), s=sqrt(alpha), u=sqrt(low_unscaled).
        # Polar unitary U=L(E_low+r E_high)/u, with 1/u=u/u².
        U={4:qscale(qi(low_unscaled),mul(L,E_low)),5:qscale(qi(low_unscaled),mul(L,E_high))}
        U=R.clean(U);identity={0:I}
        assert R.mul(R.adj(U),U)==R.mul(U,R.adj(U))==identity
        D=R.clean({0:Low,1:H});T=R.clean({2:H})
        N=R.clean({4:Linv})
        assert R.mul(R.adj(U),D)==N
        assert R.add(R.mul(D,D),R.mul(T,T))==identity
        assert R.mul(D,T)==R.mul(T,D)
        # Flag-first ordering: rotation [[D,-T],[T,D]], followed by
        # polar undoing on flag zero only.
        rotation=R.clean(blocks(D,R.scale(A(-1),T),T,D))
        controlled=R.clean(blocks(R.adj(U),{}, {},identity))
        W=R.mul(controlled,rotation)
        assert R.mul(R.adj(rotation),rotation)==R.mul(rotation,R.adj(rotation))==I4
        assert R.mul(R.adj(W),W)==R.mul(W,R.adj(W))==I4
        assert W==R.clean(blocks(N,R.scale(A(-1),R.mul(R.adj(U),T)),T,D))
        # Measure the flag after W, then apply W*. Conditional polar factors
        # cancel, but lost flag coherence does not. Four retained Kraus maps
        # are indexed by measured flag and terminal flag.
        maps=(R.mul(D,D),R.mul(T,T),R.scale(A(-1),R.mul(T,D)),R.mul(D,T))
        complete={}
        for M in maps:complete=R.add(complete,R.mul(R.adj(M),M))
        assert complete==identity
        for a in range(2):
            for b in range(2):
                X=(tuple(tuple(ONE if i==a and j==b else ZERO for j in range(2)) for i in range(2)),zero(2));actual={}
                for M in maps:actual=R.add(actual,R.mul(R.mul(M,{0:X}),R.adj(M)))
                expected=padd(mul(mul(Low,X),Low),mul(mul(H,X),H))
                cross=padd(mul(mul(Low,X),H),mul(mul(H,X),Low))
                expected=padd(expected,qscale(ratio,cross))
                assert actual==R.clean({0:expected})
        terminal_failure=qmul(qr(2),qmul(ratio,alpha))
        observed=R.add(R.mul(R.adj(maps[2]),maps[2]),R.mul(R.adj(maps[3]),maps[3]))
        assert observed==R.clean({0:qscale(terminal_failure,H)})
        fidelity=qmul(qr(F(1,2)),qa(qr(1),ratio))
        assert qsign(qa(qr(1),qn(fidelity)))>0
        rows.append({'code':item['code'],'root_squares':{'r_squared':qrecord(ratio),'s_squared':qrecord(alpha),'u_squared':qrecord(low_unscaled)},
                     'flag_angle':'phi=acos(sqrt(lambda_min/lambda_max)), 0<phi<pi/2',
                     'output_high_projector':encode(H),'polar_unitary':R.record(U),
                     'flag_rotation':R.record(rotation),'full_filter_unitary':R.record(W),
                     'two_sided_unitarity_verified':True,
                     'flag_zero_Kraus':'N=u*L_inverse','flag_one_Kraus':'F=s*Pi_output,high',
                     'measured_then_undo_Kraus':[R.record(M) for M in maps],
                     'measured_then_undo_reduced_channel':'Pi_low X Pi_low+Pi_high X Pi_high+r²(Pi_low X Pi_high+Pi_high X Pi_low)',
                     'retained_terminal_flag_one_effect':encode(qscale(terminal_failure,H)),
                     'Bell_reference_fidelity_after_measuring_then_undoing':qrecord(fidelity),
                     'Bell_input_terminal_flag_one_probability':qrecord(qmul(ratio,alpha))})
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_inverse_flag_dilation.py'}
    return {
        'schema':'marici.scattering.inverse-flag-dilation.v1',
        'status':'explicit_unitary_flag_dilation_is_coherently_reversible_flag_measurement_obstructs_local_uncomputation',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'dilations':rows,
        'factorization':{'flag_rotation':'exp(-i phi sigma_y,flag tensor Pi_output,high)',
                          'success_polar_undoing':'|0><0| tensor U* + |1><1| tensor I',
                          'full_unitary_blocks':'[[U* D,-U* F],[F,D]], D=Pi_low+r Pi_high, F=s Pi_high',
                          'first_column':'optimal inverse success and retained failure',
                          'polynomial_verification':'positive root masks r,s,u, squares in Q(sqrt19); all matrix identities reduced exactly'},
        'access_gate':{'coherent_W_then_W_adjoint_restores_system_flag_reference':True,
                       'measurement_then_W_adjoint_same_operation':False,
                       'measured_and_terminal_flags_retained':True,
                       'classical_flag_allows_missing_coherences_to_be_recreated_for_unknown_input':False,
                       'global_measurement_apparatus_coherent_access_could_change_result':True,
                       'scope':'the flag dilation reverses the inverse-filter interaction, not the earlier state-dependent successful-history measurement'},
        'gauge_and_control':{'flag_charge':'neutral supplied ancilla',
                             'high_projector':'embedded in the physical dressed ground, zero outside; hence commutes with Gauss and physical H',
                             'known_code_polar_extension':'unitary on the output/target code frames; extend on retained ground complement and other gauge sectors',
                             'additional_inputs':['rank-one ground-projector control','neutral coherent flag','pulse area phi and phase','success-controlled polar unitary','apparatus access for coherent readout undoing'],
                             'native_H_provides_dilation':False,'physical_hardware_or_work_cost_derived':False},
        'boundary':{'inverse_failure_erased':False,'flag_measurement_is_coherent_uncomputation':False,
                    'physical_preparation_spin_or_annihilation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Model an explicit flag-to-apparatus copying interaction and partial decoherence. Quantify how apparatus overlap controls undo fidelity, and test whether preserving an accessible outcome record is compatible with exact recovery of an unknown reference-entangled input.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale flag-dilation receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact two-sided unitary inverse-filter dilation, with coherent success/failure flag and polar undoing.')
    print('PASS: measured-flag uncomputation retains residual dephasing and terminal flag failure; apparatus access remains explicit.')


if __name__=='__main__':main()
