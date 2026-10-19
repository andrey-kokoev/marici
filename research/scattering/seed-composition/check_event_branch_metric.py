"""Rank obstruction for individual branches; conditional combined-map metric witness."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import audit as incidence_audit, mm, transpose, rank, encode
from check_graded_boundary_transport import add
from check_segmented_copy_transport import audit as transport_audit
from check_event_register_parity import audit as register_audit
from check_controller_reflection import zero, minus, permutation_matrix

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/event-branch-metric.v1.json'


def gram(X,H):return mm(mm(transpose(X),H),X)
def det2(G):return G[0][0]*G[1][1]-G[0][1]*G[1][0]


def audit():
    previous=register_audit();transport=transport_audit()
    E=transport['matrices']['synchronized_mode_frame']+[[F(0),F(0)] for _ in range(6)]
    long=transport['segmented_automaton']['length_two_macro_ids']
    cp=[9,10,11,6,7,8,3,4,5,0,1,2]+[12+long.index([9,10,11,6,7,8,3,4,5,0,1,2][e]) for e in long]
    J=permutation_matrix(cp)
    pairs=[i//6 for i in range(12)]+[e//6 for e in long]
    finishes=[i not in long for i in range(12)]+[True]*6
    labels=[tuple(label) for label in previous['event_register']['labels']]
    mats={label:zero(18) for label in labels}
    for a,b,p in transport['segmented_automaton']['transition_labels']:mats[pairs[a],p,finishes[a]][b][a]+=1
    # An explicit conditional witness, not a unique or source-derived metric.
    weights=[F(3) if i in [4,7] else F(1) for i in range(18)]
    H=[[weights[i]*F(i==j) for j in range(18)] for i in range(18)]
    assert mm(H,J)==mm(J,H) and all(w>0 for w in weights)
    G=gram(E,H);assert G==[[10,2],[2,2]] and det2(G)==16
    total=zero(2);rows=[];full_total=zero(18)
    for label in labels:
        T=mats[label];Y=mm(T,E);Q=gram(Y,H)
        assert rank(Y)==rank(Q)
        null=None
        if rank(Y):
            assert rank(Y)==1 and det2(Q)==0
            r=next(row for row in Y if any(row));null=[r[1],-r[0]]
            assert any(null) and mm(Y,[[v] for v in null])==zero(18,1)
            assert sum(null[i]*G[i][j]*null[j] for i in range(2) for j in range(2))>0
        total=add(total,Q);full_total=add(full_total,gram(T,H))
        rows.append({'label':label,'selected_input_branch_rank':rank(Y),'pullback_metric':Q,
                     'kernel_witness_in_mode_parameters':null})
    assert sum(r['selected_input_branch_rank']==1 for r in rows)==12
    assert sum(r['selected_input_branch_rank']==0 for r in rows)==4
    assert total==G
    defect=minus(full_total,H)
    assert mm(mm(transpose(E),defect),E)==zero(2)
    assert defect!=zero(18)
    # An actual kernel direction makes a positive full-controller normalization
    # impossible without keeping additional history/residual outputs.
    lost=[F(i==1)-F(i==14) for i in range(18)]
    assert all(mm(T,[[v] for v in lost])==zero(18,1) for T in mats.values())
    assert sum(lost[i]*H[i][j]*lost[j] for i in range(18) for j in range(18))>0
    P=transport['matrices']['micro_P'];next_frame=mm(P,E)
    next_input=gram(next_frame,H);next_output=zero(2)
    for T in mats.values():next_output=add(next_output,gram(mm(T,next_frame),H))
    assert next_output!=next_input
    step=incidence_audit()['matrices']['reference_mode_step_T']
    assert gram(step,G)!=G

    dependencies=list(previous['source_sha256'])+['research/scattering/seed-composition/check_event_branch_metric.py']
    return {
        'schema':'marici.scattering.event-branch-metric.v1',
        'status':'individual_nonzero_branches_cannot_be_weighted_isometries_combined_one_step_map_has_conditional_positive_metric',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'selected_input':{'frame':'boundary synchronized_mode_frame with six zero internal rows',
                          'dimension':2,'scope':'z=1 boundary-initialized selected plane, not an invariant primitive-step plane'},
        'branch_rank_gate':{'nonzero_rank_one_labels':12,'zero_labels':4,'branches':rows,
                            'proof':'For positive input G and positive output H, nonzero rank-one B gives rank(B^t H B)=1; p*G has rank two for p>0 and is zero for p=0.',
                            'nonzero_branch_scalar_weighted_isometry_possible':False,
                            'scope':'any positive metrics, even separate output metrics per branch; no assertion that general measurements must be isometries'},
        'combined_map_witness':{'common_positive_output_metric_diagonal':weights,'input_pullback_metric':G,
                                'input_metric_determinant':det2(G),'sum_branch_pullbacks_equals_input':True,
                                'norm_conservation_only_on_initial_selected_plane':True,
                                'physical_metric_derived':False,'metric_unique':False,
                                'invariant_under_reference_macro_step':False,
                                'next_aggregate_frame_input_metric':next_input,
                                'next_labelled_output_pullback':next_output,
                                'same_witness_works_after_next_aggregate_step':False},
        'full_controller_gate':{'labelled_endpoint_kernel_witness':lost,
                                'positive_metric_isometry_without_residual_outputs_possible':False,
                                'retain_original_histories_and_two_difference_records':True},
        'boundary':{'all_labelled_instruments_impossible':False,'general_state_dependent_branch_weights_excluded':False,
                    'repeatable_positive_metric_ruled_out_by_one_witness_failure':False,
                    'physical_probabilities_or_metric_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Compute the smallest carrier closed under every labelled primitive transition and containing the selected initial plane; solve or obstruct common positive-metric completeness on that whole carrier, retaining event labels and provenance residuals.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale branch-metric receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: 12 rank-one branches exclude nonzero scalar-weighted isometries on the selected two-plane.')
    print('PASS: a common positive metric normalizes the combined initial labelled map, but not its next-step continuation.')
    print('Boundary: rank-one measurement branches remain possible; no physical metric or repeatable instrument derived.')


if __name__=='__main__':main()
