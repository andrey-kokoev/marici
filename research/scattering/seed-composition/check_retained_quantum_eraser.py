"""Retained eraser-basis labels, exact reference recovery, and outstanding-copy obstruction."""
from fractions import Fraction as F
from itertools import product
import argparse
import json

from check_apparatus_record_tradeoff import audit as apparatus_audit
from check_inverse_flag_dilation import Radicals,blocks
from check_recycling_information_channel import qa,qn,qm as qmul,qr,qi,qrecord
from check_selector_failure_feedback import mul
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,decode,eye,record,digest,BASE
from check_diagonal_spin_networks import S2

DEST=BASE/'results/retained-quantum-eraser.v1.json'


def zero(n=2,m=None):return tuple(tuple(ZERO for _ in range(n if m is None else m)) for _ in range(n))
def pair(X):return (X,zero(len(X),len(X[0])))
def decodepoly(X):return {item['positive_root_mask']:tuple(tuple(tuple(decode(x) for x in row) for row in item['coefficient'][part]) for part in ('constant','sqrt19')) for item in X}
def padd(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def qscale(c,X):return (add(scale(A(c[0]),X[0]),scale(A(19*c[1]),X[1])),add(scale(A(c[0]),X[1]),scale(A(c[1]),X[0])))
def scalar(X):return (F(X['constant']),F(X['sqrt19']))


def audit():
    previous=apparatus_audit();rows=[];I=pair(eye(2))
    readout=((S2/2,S2/2),(S2/2,-S2/2))
    assert mm(adj(readout),readout)==eye(2)
    input_zero=pair(tuple(tuple(ONE if i==j else ZERO for j in range(2)) for i in range(4)))
    for case in previous['retained_models']:
        ratio=scalar(case['ratio']);alpha=qa(qr(1),qn(ratio));R=Radicals((ratio,alpha))
        orth=next(item for item in case['fixtures'] if item['apparatus_overlap']=='0')
        # The freshly computed gamma=0 output maps include alpha*H in
        # flag-zero/apparatus-one. Recover H from that exact map.
        base_maps=[decodepoly(X) for X in orth['joint_output_maps']]
        assert set(base_maps[1])=={0}
        H=qscale(qi(alpha),base_maps[1][0]);Low=padd(I,(scale(A(-1),H[0]),scale(A(-1),H[1])))
        D=R.clean({0:Low,1:H});Fflag={2:H}
        rotation=R.clean(blocks(D,R.scale(A(-1),Fflag),Fflag,D))
        assert R.mul(R.adj(rotation),rotation)=={0:pair(eye(4))}
        initial={0:input_zero};prepared=R.mul(rotation,initial)
        Zflag={0:pair(tuple(tuple(ONE if i==j and i<2 else -ONE if i==j else ZERO for j in range(4)) for i in range(4)))}
        assert R.mul(Zflag,Zflag)=={0:pair(eye(4))}
        configurations=[]
        for n in range(1,5):
            for m in range(n+1):
                amplitude=A(1)
                for _ in range(m):amplitude=amplitude*S2/2
                probability=F(1,2**m);assert amplitude*amplitude==A(probability)
                label_effect_sum={};label_rows=[]
                for label in product((0,1),repeat=m):
                    parity=sum(label)%2
                    overlap0=ONE;overlap1=ONE
                    for bit in label:overlap0=overlap0*readout[bit][0];overlap1=overlap1*readout[bit][1]
                    assert overlap0==amplitude and overlap1==A((-1)**parity)*amplitude
                    # Every erased pointer reads in {|+>,|->}. Its conditional
                    # amplitude on copied flag 1 is (-1)^parity times flag 0.
                    if m==n:
                        branch=R.scale(amplitude,R.mul(Zflag,prepared) if parity else prepared)
                        corrected=R.mul(Zflag,branch) if parity else branch
                        undone=R.mul(R.adj(rotation),corrected)
                        assert undone==R.scale(amplitude,initial)
                        effect=R.mul(R.adj(undone),undone)
                        assert effect=={0:qscale(qr(probability),I)}
                        terminal_one={}
                    else:
                        # A remaining copy holds |0...0> versus |1...1>.
                        # Correcting the erased parity leaves the actual gamma
                        # zero copy/undo maps, with both final flags retained.
                        corrected_maps=[R.scale(amplitude,M) for M in base_maps]
                        effect={}
                        for M in corrected_maps:effect=R.add(effect,R.mul(R.adj(M),M))
                        assert effect=={0:qscale(qr(probability),I)}
                        terminal_one=R.add(R.mul(R.adj(corrected_maps[2]),corrected_maps[2]),R.mul(R.adj(corrected_maps[3]),corrected_maps[3]))
                        assert terminal_one=={0:qscale(qmul(qr(2*probability),qmul(ratio,alpha)),H)}
                    label_effect_sum=R.add(label_effect_sum,effect)
                    label_rows.append({'eraser_label':list(label),'flag_phase_feedback_parity':parity,
                                       'label_probability':str(probability),'input_independent':True,
                                       'terminal_flag_one_zero':not terminal_one})
                assert label_effect_sum=={0:I}
                configurations.append({'copied_pointers':n,'X_basis_readouts':m,'unaddressed_copies':n-m,
                                       'labels':label_rows,'label_completeness':True,
                                       'exact_system_flag_reference_recovery':m==n,
                                       'remaining_copy_words':[] if m==n else ['0'*(n-m),'1'*(n-m)],
                                       'other_remaining_copy_words_have_zero_amplitude':True,
                                       'reduced_undo_coherence':qrecord(qr(1) if m==n else ratio),
                                       'Bell_undo_fidelity':qrecord(qr(1) if m==n else qmul(qr(F(1,2)),qa(qr(1),ratio)))})
        # Check the reduced residual channel explicitly if any copy remains.
        for a in range(2):
            for b in range(2):
                X=pair(tuple(tuple(ONE if i==a and j==b else ZERO for j in range(2)) for i in range(2)));actual={}
                for M in base_maps:actual=R.add(actual,R.mul(R.mul(M,{0:X}),R.adj(M)))
                expected=padd(mul(mul(Low,X),Low),mul(mul(H,X),H))
                cross=padd(mul(mul(Low,X),H),mul(mul(H,X),Low))
                assert actual==R.clean({0:padd(expected,qscale(ratio,cross))})
        rows.append({'code':case['code'],'configurations':configurations})
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_retained_quantum_eraser.py'}
    return {
        'schema':'marici.scattering.retained-quantum-eraser.v1',
        'status':'all_accessed_orthogonal_pointer_copies_allow_exact_eraser_feedback_with_random_labels_any_remaining_copy_obstructs',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'protocol':{'orthogonal_copy_state':'|0_flag> N|psi> |0...0> + |1_flag> F|psi> |1...1>',
                     'readout':'measure every accessible pointer in the X basis; retain every +/- label',
                     'readout_basis_matrix':record(readout),
                     'feedback':'apply Z_flag when the number of minus labels is odd',
                     'undo':'then apply full W*; controlled polar factors commute with copy/readout/phase and cancel',
                     'all_copies_accessed_branch':'2^(-n/2)|0_flag> tensor |psi>, for every label string',
                     'eraser_label_probability':'2^(-n), independent of system and arbitrary reference',
                     'which_flag_guess_probability_from_eraser_labels':'1/2 with equal priors',
                     'joint_label_channel':'sum_z 2^(-n)|z><z| tensor input_state',
                     'terminal_flag_restored_zero':True},
        'copy_accounting':{'fixtures':'n=1..4, every m=0..n, both witnessed codes',
                           'all_depth_argument':'each X readout contributes 1/sqrt(2) and a flag-one sign; signs multiply to the parity feedback',
                           'if_m_less_than_n':'remaining pointer words are orthogonal; erased labels are still uniform but residual system coherence is r²',
                           'random_label_is_sufficient_evidence_of_recovery':False,
                           'unaddressed_copy_retains_logical_input_information':True,
                           'terminal_flag_one_effect_if_copy_remains':'2r²(1-r²)Pi_high after summing eraser labels',
                           'coherent_environment_access_required_for_every_which_outcome_copy':True},
        'retained_tests':rows,
        'scope':{'restored_input':'input to inverse-filter dilation, not unknown state before prior successful-history measurements',
                  'input_independent_eraser_record_retained':True,
                  'original_which_outcome_record_retained':False,
                  'eraser_label_can_be_copied_without_disturbing_restored_input':True,
                  'prior_classical_which_outcome_copies_implicitly_deleted':False},
        'control_inputs':['apparatus X-basis readout and phase reference','parity feedforward to neutral flag','inverse polar/flag control','access to every orthogonal which-outcome copy or its coherent removal'],
        'boundary':{'physical_device_noise_or_spin_admitted':False,'native_H_implements_eraser':False,
                    'all_records_erased':False,'formal_outcome_admitted':False},
        'next_gate':'Classify apparatus readout bases and feedforward phases permitting exact reference recovery. Test an imbalanced or misphased eraser readout, checking label input-dependence and actual branch recovery rather than relying on uniform labels alone.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale eraser receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: X-basis eraser labels plus flag parity feedback restore input/reference exactly when every copy is addressed.')
    print('PASS: any remaining orthogonal copy retains disturbance despite uniform eraser labels; all tested records are retained.')


if __name__=='__main__':main()
