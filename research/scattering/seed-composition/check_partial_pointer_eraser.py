"""Exact erasure for nonorthogonal real pointers and retained heterogeneous copies."""
from fractions import Fraction as F
from itertools import product
import argparse
import json

from check_eraser_basis_calibration import audit as basis_audit
from check_inverse_flag_dilation import Radicals
from check_recycling_information_channel import qa,qn,qm as qmul,qr,qrecord
from check_selector_failure_feedback import mul
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,add,scale,eye,record,digest,BASE
from check_diagonal_spin_networks import S2,CI

DEST=BASE/'results/partial-pointer-eraser.v1.json'


def zero():return ((ZERO,ZERO),(ZERO,ZERO))
def pair(X):return (X,zero())
def scalar(X):return (F(X['constant']),F(X['sqrt19']))
def padd(X,Y):return (add(X[0],Y[0]),add(X[1],Y[1]))
def qscale(c,X):return (add(scale(A(c[0]),X[0]),scale(A(19*c[1]),X[1])),add(scale(A(c[0]),X[1]),scale(A(c[1]),X[0])))
def trace(X):return X[0][0]+X[1][1]


def audit():
    previous=basis_audit();I=pair(eye(2));H=pair(((ZERO,ZERO),(ZERO,ONE)));Low=pair(((ONE,ZERO),(ZERO,ZERO)))
    Y=((S2/2,-CI*S2/2),(S2/2,CI*S2/2));X=((S2/2,S2/2),(S2/2,-S2/2))
    assert mm(adj(Y),Y)==mm(adj(X),X)==eye(2)
    pointers=[(F(0),F(1)),(F(3,5),F(4,5)),(F(4,5),F(3,5)),(F(1),F(0))]
    pointer_rows=[]
    for gamma,v in pointers:
        e0=((ONE,),(ZERO,));e1=((A(gamma),),(A(v),));assert mm(adj(e1),e1)==((ONE,),)
        y0=mm(Y,e0);y1=mm(Y,e1);x0=mm(X,e0);x1=mm(X,e1)
        labels=[]
        for y in range(2):
            relative=y1[y][0]/y0[y][0];feedback=relative.flip(8)
            assert relative*feedback==ONE and feedback*y1[y][0]==y0[y][0]
            assert y0[y][0].flip(8)*y0[y][0]==y1[y][0].flip(8)*y1[y][0]==A(F(1,2))
            labels.append({'label':y,'flag_one_phase':relative.record(),'feedback_phase':feedback.record(),'probability':'1/2'})
        biased_X=any(x0[y][0].flip(8)*x0[y][0]!=x1[y][0].flip(8)*x1[y][0] for y in range(2))
        assert biased_X==(gamma*v!=0)
        pointer_rows.append({'gamma':str(gamma),'v':str(v),'Y_eraser_labels':labels,
                             'orthogonal_X_basis_unbiased_for_actual_pointer_pair':not biased_X})
    # Reconstruct every remaining tensor-product pointer amplitude explicitly.
    # Active and inactive environment words are retained, not removed from a
    # truncated model. Addressed labels only contribute a uniform amplitude.
    families=[pointers,[(F(3,5),F(4,5)),(F(4,5),F(3,5)),(F(3,5),F(4,5))]]
    cases=[]
    for case in previous['retained_tests']:
        ratio=scalar(case['ratio']);alpha=qa(qr(1),qn(ratio));R=Radicals((ratio,alpha));configurations=[]
        for family_index,family in enumerate(families):
            n=len(family)
            for access in product((0,1),repeat=n):
                addressed=[i for i,x in enumerate(access) if x];remaining=[family[i] for i,x in enumerate(access) if not x]
                gamma_product=F(1)
                for gamma,v in remaining:gamma_product*=gamma
                m=len(addressed);amplitude=ONE
                for _ in range(m):amplitude*=S2/2
                probability=F(1,2**m);assert amplitude*amplitude==A(probability)
                environment=[]
                for word in product((0,1),repeat=len(remaining)):
                    value=F(1)
                    for bit,(gamma,v) in zip(word,remaining):value*=v if bit else gamma
                    environment.append((word,value))
                assert sum(value*value for word,value in environment)==1
                assert environment[0][1]==gamma_product
                maps=[]
                for word,value in environment:
                    delta=F(int(not any(word)))
                    out0=padd(pair(scale(A(delta),Low[0])),padd(qscale(qmul(qr(delta),ratio),H),qscale(qmul(qr(value),alpha),H)))
                    out1=pair(scale(A(value-delta),H[0]))
                    maps.extend([R.scale(amplitude,R.clean({0:out0})),R.scale(amplitude,R.clean({3:out1}))])
                complete={};terminal={}
                for i,M in enumerate(maps):
                    effect=R.mul(R.adj(M),M);complete=R.add(complete,effect)
                    if i%2:terminal=R.add(terminal,effect)
                assert complete=={0:qscale(qr(probability),I)}
                term=qmul(qr(2*probability*(1-gamma_product)),qmul(ratio,alpha))
                assert terminal==R.clean({0:qscale(term,H)})
                coherence=qa(ratio,qmul(qr(gamma_product),alpha))
                for a in range(2):
                    for b in range(2):
                        input_matrix=pair(tuple(tuple(ONE if i==a and j==b else ZERO for j in range(2)) for i in range(2)));actual={}
                        for M in maps:actual=R.add(actual,R.mul(R.mul(M,{0:input_matrix}),R.adj(M)))
                        expected=padd(mul(mul(Low,input_matrix),Low),mul(mul(H,input_matrix),H))
                        cross=padd(mul(mul(Low,input_matrix),H),mul(mul(H,input_matrix),Low))
                        expected=qscale(qr(probability),padd(expected,qscale(coherence,cross)))
                        assert actual==R.clean({0:expected})
                label_rows=[]
                for label in product((0,1),repeat=m):
                    relative=ONE
                    for bit,index in zip(label,addressed):
                        gamma,v=family[index];relative*=A(gamma)+CI*(v if bit else -v)
                    feedback=relative.flip(8);assert feedback*relative==ONE
                    label_rows.append({'label':list(label),'feedback_flag_one_phase':feedback.record(),
                                       'probability':str(probability),'input_independent':True})
                assert len(label_rows)*probability==1
                configurations.append({'pointer_family':family_index,'addressed_indices':addressed,
                                       'remaining_indices':[i for i,x in enumerate(access) if not x],
                                       'remaining_pointer_words':[{'word':list(word),'flag_one_amplitude':str(value)} for word,value in environment],
                                       'remaining_overlap_product':str(gamma_product),'labels':label_rows,
                                       'exact_input_reference_recovery':gamma_product==1,
                                       'reduced_undo_coherence':qrecord(coherence),
                                       'Bell_undo_fidelity':qrecord(qmul(qr(F(1,2)),qa(qr(1),coherence))),
                                       'joint_map_label_completeness':True,'terminal_flag_one_zero':not terminal})
        cases.append({'code':case['code'],'ratio':qrecord(ratio),'configurations':configurations})
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_partial_pointer_eraser.py'}
    return {
        'schema':'marici.scattering.partial-pointer-eraser.v1',
        'status':'Y_basis_erases_nonorthogonal_real_pointer_pairs_with_exact_phase_feedback_remaining_overlap_product_controls_disturbance',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'actual_pointer_protocol':{'states':'e0=|0>, e1=gamma|0>+v|1>, real gamma>=0, v>=0, gamma²+v²=1',
                                   'readout_basis':record(Y),'relative_amplitudes':'gamma-i*v and gamma+i*v',
                                   'feedback':'conjugate the relative amplitude, multiplied over all addressed labels',
                                   'label_probability':'1/2 per pointer, input independent',
                                   'corrected_branch':'same uniform scalar on both flag amplitudes; W* then restores prefilter input/reference',
                                   'X_readout_is_unbiased_for_all_partial_pointers':False,
                                   'Y_readout_preserves_which_flag_information':False,
                                   'pointer_gamma_and_phase_controls_are_inputs':True},
        'pointer_fixtures':pointer_rows,
        'copy_product_gate':{'families':[[{'gamma':str(g),'v':str(v)} for g,v in family] for family in families],
                             'retained_overlap':'Gamma=product gamma_j over remaining unaddressed copies',
                             'reduced_undo_coherence':'r²+(1-r²)Gamma',
                             'Bell_undo_fidelity':'[1+r²+(1-r²)Gamma]/2',
                             'terminal_flag_one_effect':'2r²(1-r²)(1-Gamma)Pi_high',
                             'exact_recovery_condition':'Gamma=1; any unaddressed identical-state pointer is harmless, any remaining distinguishable pointer disturbs',
                             'all_pointer_words_and_outcomes_accounted_for':True,
                             'count_only_copy_rule_is_sufficient':False},
        'retained_tests':cases,
        'boundary':{'earlier_history_measurements_undone':False,'new_apparatus_readout_and_phase_controls_required':True,
                    'pointer_model_is_measured_physical_noise':False,'native_H_supplies_protocol':False,
                    'records_erased':False,'physical_spin_or_annihilation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Test eraser feedback calibrated with an incorrect pointer pair: compute the actual residual channel and whether retained Y labels can identify gamma. Separate independent calibration-probe resources from unknown-state erasure, and compare with coherent inverse-copy access.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale partial-pointer receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact Y-basis eraser for every tested nonorthogonal pointer, with input-independent retained phase-feedback labels.')
    print('PASS: explicit heterogeneous remaining-copy amplitudes give overlap-product disturbance; identical copies are harmless.')


if __name__=='__main__':main()
