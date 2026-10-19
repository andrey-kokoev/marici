"""Explicit event register: joint parity is not conditional system parity."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, transpose, rank, eye, apply, encode
from check_graded_boundary_transport import add, scale
from check_segmented_copy_transport import audit as transport_audit
from check_controller_reflection import audit as reflection_audit, zero, minus, permutation_matrix, parity

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/event-register-parity.v1.json'


def gram(a):return mm(transpose(a),a)
def outer(x):return [[a*b for b in x] for a in x]


def audit():
    prior=reflection_audit();transport=transport_audit()
    cp=prior['context_permutation'];pp=prior['primitive_permutation'];J=permutation_matrix(cp)
    ep,em=parity(J)
    long=transport['segmented_automaton']['length_two_macro_ids']
    pairs=[i//6 for i in range(12)]+[e//6 for e in long]
    finishes=[i not in long for i in range(12)]+[True]*6
    transitions=transport['segmented_automaton']['transition_labels']
    labels=sorted({(pairs[a],p,finishes[a]) for a,b,p in transitions})
    mats={label:zero(18) for label in labels}
    for a,b,p in transitions:mats[pairs[a],p,finishes[a]][b][a]+=1
    lp=[labels.index((1-pair,pp[p],done)) for pair,p,done in labels]
    V=[row for label in labels for row in mats[label]]
    # Joint reflection permutes register labels AND system coordinates.
    output_perm=[18*lp[k]+cp[s] for k in range(len(labels)) for s in range(18)]
    VJ=mm(V,J)
    assert VJ==[V[i] for i in output_perm]
    assert all(output_perm[output_perm[i]]==i for i in range(len(output_perm)))
    Vodd=mm(V,em)
    assert [Vodd[i] for i in output_perm]==scale(Vodd,-1)
    P=transport['matrices']['micro_P'];total=zero(18)
    conditional=[];sums=[];differences=[]
    for label in labels:
        T=mats[label];total=add(total,T);Y=mm(T,em)
        Ye=mm(ep,Y);Yo=mm(em,Y)
        assert gram(Ye)==gram(Yo)==scale(gram(Y),F(1,2))
        assert rank(Y)>0 and rank(Ye)==rank(Yo)==rank(Y)
        conditional.append({'label':label,'odd_input_output_rank':rank(Y),
                            'conditional_even_rank':rank(Ye),'conditional_odd_rank':rank(Yo),
                            'even_and_odd_counting_norms_equal':True})
    assert total==P
    for k,label in enumerate(labels):
        if k>lp[k]:continue
        T=mats[label];Tr=mats[labels[lp[k]]]
        assert mm(J,mm(T,J))==Tr
        S=scale(add(T,Tr),F(1,2));D=scale(minus(T,Tr),F(1,2))
        So=mm(S,em);Do=mm(D,em)
        assert mm(ep,So)==zero(18) and mm(em,Do)==zero(18)
        assert gram(So)==gram(Do)
        assert add(S,D)==T and minus(S,D)==Tr
        assert add(gram(T),gram(Tr))==scale(add(gram(S),gram(D)),2)
        sums.extend(So);differences.extend(Do)
    assert rank(sums)>0 and rank(differences)>0
    # Label-bearing endpoint summaries are not full source history. Keep the
    # same two provenance differences already required by the predictive quotient.
    residual=[[F(i==a)-F(i==b) for i in range(18)] for a,b in [(1,14),(10,16)]]
    assert rank(V)==16 and rank(V+residual)==18
    assert mm(V,transpose(residual))==zero(len(V),2)
    assert gram(V)!=eye(18)  # not a normalized instrument in this metric
    assert gram(P)!=gram(V)  # aggregation changes the coefficient norm

    witness=[F(i==0)-F(i==cp[0]) for i in range(18)]
    assert apply(em,witness)==witness
    outputs=[apply(mats[label],witness) for label in labels]
    mixed=zero(18)
    for y in outputs:mixed=add(mixed,outer(y))
    # A coefficient-level analogue of discarding a distinguishable register:
    # it commutes with reflection but has support in both parity sectors.
    assert mm(J,mixed)==mm(mixed,J)
    ee=mm(ep,mm(mixed,ep));oo=mm(em,mm(mixed,em))
    assert rank(ee)>0 and rank(oo)>0
    even_norm=sum(ee[i][i] for i in range(18));odd_norm=sum(oo[i][i] for i in range(18))
    assert even_norm==odd_norm>0
    coherent=apply(P,witness)
    assert apply(em,coherent)==coherent and any(coherent)
    assert outer(coherent)!=mixed

    dependencies=list(prior['source_sha256'])+['research/scattering/seed-composition/check_event_register_parity.py']
    return {
        'schema':'marici.scattering.event-register-parity.v1',
        'status':'joint_odd_output_contains_system_even_and_odd_records_fixed_label_or_incoherent_discard_does_not_prepare_odd',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'event_register':{'labels':labels,'output_dimension':len(V),'map':'Vx = direct sum over labels of T_label*x',
                           'joint_reflection':'label reflection together with system J',
                           'V_J_equals_joint_J_V':True,'joint_odd_input_output':True,
                           'endpoint_summary_rank':16,'rank_with_two_retained_history_differences':18,
                           'counting_metric_isometry':False,'original_source_history_still_required':True},
        'conditional_labels':conditional,
        'orbit_recombination':{'sum_record':'(T_label+T_reflected)/2 applied to odd input is system odd',
                               'difference_record':'(T_label-T_reflected)/2 applied to odd input is system even',
                               'sum_and_difference_reconstruct_both_labels':True,
                               'norm_identity':'||y||^2+||y_ref||^2 = 2(||sum/2||^2+||difference/2||^2)',
                               'even_and_odd_system_channels_have_equal_counting_weight_for_odd_inputs':True,
                               'sum_channel_rank_on_odd_input':rank(sums),'difference_channel_rank_on_odd_input':rank(differences),
                               'odd_system_record_requires_register_even_recombination':True},
        'discard_witness':{'odd_input':witness,'coherent_aggregate':coherent,
                           'label_discard_second_moment':mixed,
                           'even_counting_weight':even_norm,'odd_counting_weight':odd_norm,
                           'coherent_outer_equals_discard_second_moment':False},
        'boundary':{'counting_weights_are_physical_probabilities':False,'V_is_physical_instrument':False,
                    'register_erasure_source_authorized':False,'coherent_recombination_derived':False,
                    'physical_odd_preparation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Test whether one common positive controller metric can make every distinguishable event branch an isometric or scalar-weighted isometric action on the selected sector; retain the register and provenance rather than using coherent aggregate P as an instrument.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale event-register receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: explicit event register preserves joint parity, but each nonzero fixed-label output has both system parities.')
    print('PASS: sum/difference records reconstruct labels; distinguishable-label discard differs from coherent aggregation.')
    print('Boundary: counting coefficients only, not a normalized physical instrument or authorized register erasure.')


if __name__=='__main__':main()
