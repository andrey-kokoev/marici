"""Exact projective eraser-basis classification and phase-feedback calibration fixtures."""
from fractions import Fraction as F
import argparse
import json

from check_retained_quantum_eraser import audit as eraser_audit
from check_inverse_flag_dilation import Radicals
from check_recycling_information_channel import qa,qn,qm as qmul,qr,qrecord
from check_selector_failure_feedback import mul
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,eye,record,digest,BASE
from check_diagonal_spin_networks import S2,CI

DEST=BASE/'results/eraser-basis-calibration.v1.json'


def zero():return ((ZERO,ZERO),(ZERO,ZERO))
def pair(X):return (X,zero())
def scalar(X):return (F(X['constant']),F(X['sqrt19']))
def padd(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def qscale(c,X):return (add(scale(A(c[0]),X[0]),scale(A(19*c[1]),X[1])),add(scale(A(c[0]),X[1]),scale(A(c[1]),X[0])))
def trace(X):return X[0][0]+X[1][1]
def conjugate(x):return x.flip(8)
def rational(x):
    assert all(v==0 for v in x.c[1:]);return x.c[0]
def unit(a,b):return tuple(tuple(ONE if i==a and j==b else ZERO for j in range(2)) for i in range(2))


def audit():
    previous=eraser_audit();I=pair(eye(2));H=pair(((ZERO,ZERO),(ZERO,ONE)));Low=pair(((ONE,ZERO),(ZERO,ZERO)))
    fixtures=[('balanced_real',S2/2,S2/2,ONE,ONE),
              ('balanced_i_compensated',S2/2,S2/2,CI,-CI),
              ('balanced_rational_phase_compensated',S2/2,S2/2,(A(3)+4*CI)/5,(A(3)-4*CI)/5),
              ('imbalanced_compensated',A(F(3,5)),A(F(4,5)),CI,-CI),
              ('balanced_quarter_turn_error',S2/2,S2/2,CI,ONE),
              ('balanced_rational_phase_error',S2/2,S2/2,ONE,(A(3)+4*CI)/5),
              ('imbalanced_phase_error',A(F(3,5)),A(F(4,5)),ONE,CI),
              ('which_outcome_basis',ONE,ZERO,ONE,ONE)]
    cases=[]
    for case in previous['retained_tests']:
        pending=next(x for x in case['configurations'] if x['copied_pointers']==1 and x['X_basis_readouts']==0)
        ratio=scalar(pending['reduced_undo_coherence']);alpha=qa(qr(1),qn(ratio));R=Radicals((ratio,alpha));tests=[]
        for name,a,b,p,f in fixtures:
            readout=((a,b*p),(b,-a*p));assert mm(adj(readout),readout)==mm(readout,adj(readout))==eye(2)
            assert conjugate(f)*f==ONE and conjugate(p)*p==ONE
            balanced=a*a==b*b
            residual=p*f;correct_phase=residual==ONE
            amplitudes=((a,b*residual),(b,a*residual))
            z=sum((u*conjugate(w) for u,w in amplitudes),ZERO)
            real_z=rational((z+conjugate(z))/2)
            visibility=rational(2*a*b);distinguishability=abs(rational(a*a-b*b))
            assert visibility*visibility+distinguishability*distinguishability==1
            assert z==2*a*b*conjugate(residual)
            coherence=padd(qscale(ratio,pair(((ONE,ZERO),(ZERO,ONE)))),qscale(alpha,pair(scale(z,eye(2)))))
            maps=[];labels=[];complete={}
            for y,(u,w) in enumerate(amplitudes):
                # After phase correction and W*: terminal flag zero amplitude
                # u*Low+(u*r²+w*s²)H, terminal flag one rs*(w-u)H.
                A0=padd((scale(u,Low[0]),zero()),padd(qscale(ratio,pair(scale(u,H[0]))),qscale(alpha,pair(scale(w,H[0])))))
                A1=pair(scale(w-u,H[0]));branches=({0:A0},R.clean({3:A1}))
                effect=R.add(R.mul(R.adj(branches[0]),branches[0]),R.mul(R.adj(branches[1]),branches[1]))
                expected=padd(pair(scale(u*u,Low[0])),padd(qscale(ratio,pair(scale(u*u,H[0]))),qscale(alpha,pair(scale(conjugate(w)*w,H[0])))))
                assert effect==R.clean({0:expected})
                is_scalar=all(add(M,scale(-trace(M)/2,eye(2)))==zero() for M in expected)
                assert is_scalar==balanced
                exact=branches[0]=={0:pair(scale(u,eye(2)))} and not branches[1]
                assert exact==(balanced and correct_phase)
                complete=R.add(complete,effect);maps.extend(branches)
                labels.append({'label':y,'feedback_flag_one_phase':(f if y==0 else -f).record(),
                               'effect':{'constant':record(expected[0]),'sqrt19':record(expected[1])},
                               'input_independent':is_scalar,'exact_restoration':exact,
                               'terminal_flag_maps':[R.record(M) for M in branches]})
            assert complete=={0:I}
            for i in range(2):
                for j in range(2):
                    X=pair(unit(i,j));actual={}
                    for M in maps:actual=R.add(actual,R.mul(R.mul(M,{0:X}),R.adj(M)))
                    base=padd(mul(mul(Low,X),Low),mul(mul(H,X),H))
                    cross0=mul(mul(Low,X),H);cross1=mul(mul(H,X),Low)
                    cross=padd(cross0,cross1)
                    phasecross=padd((scale(z,cross0[0]),scale(z,cross0[1])),(scale(conjugate(z),cross1[0]),scale(conjugate(z),cross1[1])))
                    expected=padd(base,padd(qscale(ratio,cross),qscale(alpha,phasecross)))
                    assert actual==R.clean({0:expected})
            terminal=qmul(qr(2*(1-real_z)),qmul(ratio,alpha))
            observed={}
            for index in (1,3):observed=R.add(observed,R.mul(R.adj(maps[index]),maps[index]))
            assert observed==R.clean({0:qscale(terminal,H)})
            fidelity=qa(qr(1),qn(qmul(alpha,qr((1-real_z)/2))))
            if balanced and correct_phase:assert fidelity==qr(1)
            else:assert fidelity!=qr(1)
            tests.append({'fixture':name,'readout_basis':record(readout),'label_tests':labels,
                          'amplitude_balanced':balanced,'relative_phase_compensated':correct_phase,
                          'original_flag_distribution_distinguishability':str(distinguishability),
                          'phase_corrected_visibility_limit':str(visibility),
                          'cross_coherence':{'constant':coherence[0][0][0].record(),'sqrt19':coherence[1][0][0].record()},
                          'Bell_undo_fidelity':qrecord(fidelity),'terminal_flag_one_coefficient':qrecord(terminal),
                          'all_records_and_terminal_outcomes_retained':True})
        cases.append({'code':case['code'],'spectral_frame':'logical output low eigenvector then high eigenvector',
                      'ratio':qrecord(ratio),'fixtures':tests})
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_eraser_basis_calibration.py'}
    return {
        'schema':'marici.scattering.eraser-basis-calibration.v1',
        'status':'unbiased_readout_and_matched_relative_phase_are_required_uniform_labels_alone_do_not_certify_recovery',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'classification':{'scope':'single orthogonal pointer, rank-one two-outcome projective readout, flag phase feedback and W*; no outstanding copies',
                           'basis':'rows (a,b*p), (b,-a*p), a,b>=0, a²+b²=1, |p|=1; outcome/row phases may be relabelled',
                           'feedback':'flag-one phases f and -f; residual relative phase e=p*f',
                           'deterministic_reference_recovery':'a=b=1/sqrt(2) and e=1',
                           'label_input_independence':'a²=b², irrespective of relative phase error',
                           'generality':'this covers projective qubit bases up to row phases and outcome relabelling, not arbitrary POVMs or coherent global controls'},
        'error_channel':{'maximal_phase_compensated_visibility':'2ab=sqrt(1-|a²-b²|²)',
                         'residual_readout_factor':'z=2ab*conjugate(e)',
                         'system_low_high_coherence':'kappa=r²+(1-r²)z',
                         'Bell_undo_fidelity':'1-(1-r²)(1-Re(z))/2',
                         'terminal_flag_one_effect':'2r²(1-r²)(1-Re(z))Pi_high',
                         'amplitude_imbalance':'classical label leaks input information and phase-only feedback cannot restore exact unknown state',
                         'phase_mismatch':'labels can remain uniform while the actual channel still disturbs reference coherence'},
        'retained_tests':cases,
        'boundary':{'prior_outcome_copies_assumed_addressed':True,'earlier_history_measurements_undone':False,
                    'readout_basis_and_phase_controls_are_native_H':False,'physical_noise_or_feedback_derived':False,
                    'records_erased':False,'formal_outcome_admitted':False},
        'next_gate':'Extend the eraser to the nonorthogonal pointer states of the partial-copy model. Construct a readout unbiased relative to that actual pointer pair, with exact flag-phase feedback, and test reference recovery and input-independent labels rather than assuming the orthogonal X basis still works.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale eraser calibration receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: projective eraser basis classification and exact readout/feedback error channels on both witnessed cases.')
    print('PASS: amplitude imbalance leaks labels; phase errors disturb recovery even with uniform labels; every outcome retained.')


if __name__=='__main__':main()
