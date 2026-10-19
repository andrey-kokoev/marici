"""Explicit partial flag copying, retained apparatus, and the record/undo tradeoff."""
from fractions import Fraction as F
import argparse
import json

from check_inverse_flag_dilation import audit as dilation_audit,Radicals
from check_selector_failure_feedback import mul
from check_recycling_information_channel import qa,qn,qm as qmul,qr,qsign,qrecord
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,decode,eye,record,digest,BASE

DEST=BASE/'results/apparatus-record-tradeoff.v1.json'


def zero(n=2):return tuple(tuple(ZERO for _ in range(n)) for _ in range(n))
def trace(X):return sum((X[i][i] for i in range(len(X))),ZERO)
def padd(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def qscale(c,X):return (add(scale(A(c[0]),X[0]),scale(A(19*c[1]),X[1])),add(scale(A(c[0]),X[1]),scale(A(c[1]),X[0])))
def decodepair(X):return tuple(tuple(tuple(decode(x) for x in row) for row in X[part]) for part in ('constant','sqrt19'))
def scalar(X):return (F(X['constant']),F(X['sqrt19']))
def encode(X):return {'constant':record(X[0]),'sqrt19':record(X[1])}


def audit():
    previous=dilation_audit();rows=[];I=(eye(2),zero())
    for case in previous['dilations']:
        ratio=scalar(case['root_squares']['r_squared']);alpha=scalar(case['root_squares']['s_squared'])
        assert qa(ratio,alpha)==qr(1)
        R=Radicals((ratio,alpha));H=decodepair(case['output_high_projector'])
        Low=padd(I,(scale(A(-1),H[0]),scale(A(-1),H[1])))
        D={0:Low,1:H};T={2:H};D=R.clean(D);T=R.clean(T)
        fixtures=[]
        for gamma,v in ((F(0),F(1)),(F(3,5),F(4,5)),(F(4,5),F(3,5)),(F(1),F(0))):
            assert gamma*gamma+v*v==1
            pointer_rotation=((A(gamma),A(-v)),(A(v),A(gamma)))
            assert mm(adj(pointer_rotation),pointer_rotation)==mm(pointer_rotation,adj(pointer_rotation))==eye(2)
            # First rotate the inverse flag. Copy flag basis 0 -> e0=|0>,
            # 1 -> e1=gamma|0>+v|1>. Then coherently undo the flag rotation.
            # Success-controlled polar factors commute with the copy and
            # cancel under undoing, so this is also the full W-copy-W* test.
            maps=(R.add(R.mul(D,D),R.scale(A(gamma),R.mul(T,T))),
                  R.scale(A(v),R.mul(T,T)),
                  R.scale(A(gamma-1),R.mul(D,T)),
                  R.scale(A(v),R.mul(D,T)))  # (flag,apparatus)=(0,0),(0,1),(1,0),(1,1)
            coherence=qa(ratio,qmul(qr(gamma),alpha))
            expected0=padd(Low,qscale(coherence,H))
            assert maps[0]==R.clean({0:expected0})
            assert maps[1]==R.clean({0:qscale(qmul(qr(v),alpha),H)})
            assert maps[2]==R.clean({3:(scale(A(gamma-1),H[0]),scale(A(gamma-1),H[1]))})
            assert maps[3]==R.clean({3:(scale(A(v),H[0]),scale(A(v),H[1]))})
            complete={}
            for M in maps:complete=R.add(complete,R.mul(R.adj(M),M))
            assert complete=={0:I}
            for a in range(2):
                for b in range(2):
                    X=(tuple(tuple(ONE if i==a and j==b else ZERO for j in range(2)) for i in range(2)),zero());actual={}
                    for M in maps:actual=R.add(actual,R.mul(R.mul(M,{0:X}),R.adj(M)))
                    expected=padd(mul(mul(Low,X),Low),mul(mul(H,X),H))
                    cross=padd(mul(mul(Low,X),H),mul(mul(H,X),Low))
                    assert actual==R.clean({0:padd(expected,qscale(coherence,cross))})
            terminal=qmul(qr(2*(1-gamma)),qmul(ratio,alpha))
            terminal_effect=R.add(R.mul(R.adj(maps[2]),maps[2]),R.mul(R.adj(maps[3]),maps[3]))
            assert terminal_effect==R.clean({0:qscale(terminal,H)})
            # Reduced apparatus states, explicitly traced from the retained
            # joint flag/apparatus map, distinguish logical low/high input.
            E0=(((ONE,ZERO),(ZERO,ZERO)),zero())
            E1=(((A(gamma*gamma),A(gamma*v)),(A(gamma*v),A(v*v))),zero())
            for input_projector,target in ((Low,E0),(H,padd(qscale(ratio,E0),qscale(alpha,E1)))):
                actual_parts=[[[ZERO]*2 for _ in range(2)] for _ in range(2)]
                for a in range(2):
                    for b in range(2):
                        entry={}
                        for f in range(2):entry=R.add(entry,R.mul(R.mul(maps[2*f+a],{0:input_projector}),R.adj(maps[2*f+b])))
                        traced={k:(trace(pair[0]),trace(pair[1])) for k,pair in entry.items()}
                        traced={k:x for k,x in traced.items() if x!=(ZERO,ZERO)}
                        assert all(k==0 for k in traced)
                        for part in range(2):actual_parts[part][a][b]=traced.get(0,(ZERO,ZERO))[part]
                actual=tuple(tuple(tuple(row) for row in M) for M in actual_parts)
                assert actual==target
            # Reading the apparatus in its pointer-coordinate basis has a
            # non-scalar outcome-one effect whenever v>0, even if the flag
            # is subsequently uncomputed and retained.
            record_one=R.add(R.mul(R.adj(maps[1]),maps[1]),R.mul(R.adj(maps[3]),maps[3]))
            record_effect=qmul(qr(v*v),alpha)
            assert record_one==R.clean({0:qscale(record_effect,H)})
            fidelity=qmul(qr(F(1,2)),qa(qr(1),coherence))
            if gamma<1:assert qsign(qa(qr(1),qn(fidelity)))>0 and qsign(record_effect)>0
            else:assert fidelity==qr(1) and not record_one
            fixtures.append({'apparatus_overlap':str(gamma),'pointer_distinguishability':str(v),
                             'copy_rotation':record(pointer_rotation),
                             'joint_output_maps':[R.record(M) for M in maps],
                             'joint_flag_apparatus_map_isometry':True,
                             'reduced_undo_coherence':qrecord(coherence),
                             'Bell_undo_fidelity':qrecord(fidelity),
                             'terminal_flag_one_effect':encode(qscale(terminal,H)),
                             'logical_low_high_apparatus_trace_distance':qrecord(qmul(qr(v),alpha)),
                             'apparatus_pointer_basis_outcome_one_effect':encode(qscale(record_effect,H))})
        rows.append({'code':case['code'],'ratio':qrecord(ratio),'fixtures':fixtures})
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_apparatus_record_tradeoff.py'}
    return {
        'schema':'marici.scattering.apparatus-record-tradeoff.v1',
        'status':'explicit_pointer_records_trade_distinguishability_for_local_undo_fidelity_coherent_records_remain_retained',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'copy_model':{'apparatus':'supplied neutral two-state pointer initially |0>',
                       'flag_controlled_copy':'flag 0 leaves pointer |e0>=|0>; flag 1 applies [[gamma,-v],[v,gamma]] giving |e1>=gamma|0>+v|1>',
                       'parameters':'0<=gamma<=1, v=sqrt(1-gamma²); real nonnegative overlap, or known relative pointer phase compensated',
                       'flag_controlled_polar_factors_commute_with_copy':True,
                       'unitary_copy_and_joint_isometry':True,'apparatus_not_silently_discarded':True},
        'tradeoff':{'r_squared':'lambda_min/lambda_max, from each optimal inverse filter',
                    'reduced_local_undo_coherence':'lambda=r²+(1-r²)gamma',
                    'Bell_undo_fidelity':'F=(1+lambda)/2',
                    'terminal_flag_one_effect':'2r²(1-r²)(1-gamma)Pi_high',
                    'pointer_equal_prior_trace_distance':'D=sqrt(1-gamma²)',
                    'pointer_equal_prior_optimal_guess_probability':'(1+D)/2',
                    'logical_low_high_apparatus_trace_distance':'(1-r²)D',
                    'phase_compensated_fidelity_vs_distinguishability':'F=1-(1-r²)[1-sqrt(1-D²)]/2',
                    'limits':{'gamma_one':'perfect local undo; pointer states identical, no useful which-flag information',
                              'gamma_zero':'orthogonal which-flag pointer; recovers previous measured-flag disturbance'},
                    'verified_fixtures_each_code':4},
        'retained_models':rows,
        'recovery_gate':{'pointer_coordinate_readout_outcome_one_effect':'(1-r²)v² Pi_high, non-scalar for gamma<1',
                          'deterministic_recovery_with_that_classical_pointer_record':False,
                          'exact_unknown_input_recovery_and_nontrivial_which_outcome_record_compatible':False,
                          'argument':'the apparatus marginal distinguishes low/high logical inputs; exact reference-preserving recovery requires its complementary record to be input independent',
                          'every_possible_classical_record_precludes_recovery':False,
                          'scope':'which-outcome information; an input-independent eraser-basis label is a different record',
                          'coherent_inverse_copy_then_inverse_filter_restores_input':True,
                          'coherent_inverse_copy_retains_useful_which_outcome_record':False},
        'boundary':{'new_pointer_and_copy_controls_required':True,'measured_noise_or_hardware_derived':False,
                    'earlier_history_measurement_undone_by_this_test':False,
                    'physical_spin_or_annihilation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Construct an apparatus quantum-eraser readout with flag-phase feedback for the orthogonal-pointer fixture. Test exact reference recovery while retaining the eraser label, and verify that label is input independent and is not a preserved which-outcome record.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale apparatus receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: explicit pointer-copy unitary and retained joint isometry give exact distinguishability/undo-fidelity tradeoff.')
    print('PASS: which-outcome records obstruct deterministic local recovery; input-independent eraser labels remain a distinct open gate.')


if __name__=='__main__':main()
