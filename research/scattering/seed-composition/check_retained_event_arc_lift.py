"""Conditional event-arc history lift with inherited positive counting weights."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, rank, eye, apply, encode
from check_retained_word_transport import RetainedSuccessorLedger
from check_segmented_copy_transport import audit as transport_audit
from check_labelled_reachable_carrier import audit as reachable_audit
from check_controller_reflection import zero

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/retained-event-arc-lift.v1.json'


def weighted_gram(matrix,weights):
    n=len(matrix[0]);return [[sum(w*row[i]*row[j] for w,row in zip(weights,matrix)) for j in range(n)] for i in range(n)]
def norm(x,weights):return sum(w*v*v for w,v in zip(weights,x))


def audit():
    previous=reachable_audit();transport=transport_audit()
    arcs=[tuple(t) for t in transport['segmented_automaton']['transition_labels']]
    assert len(arcs)==len(set(arcs))==26
    long=transport['segmented_automaton']['length_two_macro_ids']
    pairs=[i//6 for i in range(12)]+[e//6 for e in long]
    finishes=[i not in long for i in range(12)]+[True]*6
    labels=sorted({(pairs[a],p,finishes[a]) for a,b,p in arcs})
    degrees=[sum(a==s for a,b,p in arcs) for s in range(18)]
    assert set(degrees)=={1,2}
    packets=[(f'controller-arc:{a}:{b}:{p}',a,b) for a,b,p in arcs]
    ledger=RetainedSuccessorLedger(packets)
    # This is a new conditional controller registry using the unchanged ledger
    # implementation, not a relabelling of the native ten-primitive registry.
    L=[[F(a==s) for s in range(18)] for a,b,p in arcs]
    D=[[L[k][s]/degrees[s] for k in range(26)] for s in range(18)]
    weights=[F(1,degrees[a]) for a,b,p in arcs]
    assert mm(D,L)==eye(18) and weighted_gram(L,weights)==eye(18)
    S=zero(18,26)
    labelled=zero(18*len(labels),26)
    for k,(a,b,p) in enumerate(arcs):
        S[b][k]=1;labelled[18*labels.index((pairs[a],p,finishes[a]))+b][k]=1
    P=transport['matrices']['micro_P']
    assert mm(S,L)==P
    V=mm(labelled,L);assert rank(V)==16
    B=previous['labelled_closure']['basis_columns']
    assert rank(mm(L,B))==14 and rank(mm(V,B))==12
    lost=[F(i==1)-F(i==14) for i in range(18)]
    assert any(apply(L,lost)) and not any(apply(V,lost))
    assert norm(apply(L,lost),weights)==sum(v*v for v in lost)>0

    bp=[9,10,11,6,7,8,3,4,5,0,1,2]
    cp=bp+[12+long.index(bp[e]) for e in long]
    # Primitive reflection derived from the actual source graph, as in prior checks.
    pp=[8,9,5,6,7,2,3,4,0,1]
    arc_perm=[arcs.index((cp[a],cp[b],pp[p])) for a,b,p in arcs]
    assert all(degrees[cp[s]]==degrees[s] for s in range(18))
    assert all(weights[arc_perm[k]]==weights[k] for k in range(26))
    edge_map={ledger.root.paths[k][0]:ledger.root.paths[arc_perm[k]][0] for k in range(26)}
    stages=[];stage=ledger.root
    x=[F(i-7) for i in range(18)];initial=apply(L,x);current=initial
    for depth in range(1,5):
        assert len(stage.paths)==len(weights)
        lift,decoder=ledger.transition(ledger.root,stage)
        total_lift=mm(lift,L);total_decoder=mm(D,decoder)
        assert mm(total_decoder,total_lift)==eye(18)
        assert weighted_gram(total_lift,weights)==eye(18)
        assert list(ledger.encode(ledger.root,stage,initial))==apply(total_lift,x)==current
        assert apply(total_decoder,current)==x
        assert norm(current,weights)==sum(v*v for v in x)
        # Complete arc words, including predecessor states, reflect exactly.
        lookup={p:i for i,p in enumerate(stage.paths)}
        reflected=[lookup[tuple(edge_map[e] for e in path)] for path in stage.paths]
        assert all(weights[reflected[i]]==weights[i] for i in range(len(weights)))
        assert all(total_lift[reflected[i]]==[row[cp[j]] for j in range(18)] for i,row in enumerate(total_lift))
        endpoint_lift=mm(stage.summary,total_lift)
        power=eye(18)
        for _ in range(depth):power=mm(P,power)
        assert mm(S,endpoint_lift)==power
        stages.append({'event_depth':depth,'retained_words':len(stage.paths),
                       'weight_min':min(weights),'weight_max':max(weights),
                       'state_lift_rank':rank(total_lift),'reachable_carrier_lift_rank':rank(mm(total_lift,B)),
                       'exact_norm_identity':True,'endpoint_summary_equals_P_power':True})
        if depth==4:break
        child=ledger.successor(stage)
        sizes=[sum(slot==i for slot in child.parent_slots) for i in range(len(stage.paths))]
        assert sizes==[degrees[path[-1][1]] for path in stage.paths]
        child_weights=[weights[i]/sizes[i] for i in child.parent_slots]
        lift1=[list(r) for r in child.step_lift];decode1=[list(r) for r in child.step_decoder]
        assert weighted_gram(lift1,child_weights)==[[weights[i]*F(i==j) for j in range(len(weights))] for i in range(len(weights))]
        # Actual owning API mean/detail readout is weighted-orthogonal under
        # these inherited fiber weights, retaining every child coefficient.
        arbitrary=[F((i%7)-3) for i in range(len(child.paths))]
        means,detail=ledger.split_payload(child,arbitrary)
        inherited=apply(lift1,means)
        assert [a+b for a,b in zip(inherited,detail)]==arbitrary
        assert norm(arbitrary,child_weights)==norm(means,weights)+norm(detail,child_weights)
        assert sum(w*a*b for w,a,b in zip(child_weights,inherited,detail))==0
        assert list(ledger.decode(stage,child,apply(lift1,current)))==current
        current=apply(lift1,current);weights=child_weights;stage=child

    dependencies=list(previous['source_sha256'])+['research/scattering/seed-composition/check_retained_event_arc_lift.py']
    return {
        'schema':'marici.scattering.retained-event-arc-lift.v1',
        'status':'predecessor_preserving_lift_repairs_kernel_with_inherited_fiber_metric_not_physical_preparation',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'conditional_registry':{'states':18,'allowed_arcs':26,'arc_ids':packets,
                                'native_primitive_registry_replaced':False,
                                'source_implementation':'unchanged RetainedSuccessorLedger on explicitly supplied controller arcs',
                                'policy_source_derived':False,'existing_control_rejects_still_required':True},
        'initial_lift':{'L':L,'decoder_D':D,'outdegrees':degrees,
                         'weight_rule':'w_arc=1/outdegree(predecessor)',
                         'D_L_equals_identity':True,'L_t_H_arc_L_equals_identity':True,
                         'aggregate_square':'S L=P','labelled_square':'S_label L=V',
                         'lost_endpoint_direction_retained':lost,'reachable_lift_rank':14},
        'successor_history':{'stages':stages,
                             'weight_rule':'w_child=w_parent/outdegree(last_target)',
                             'path_weight':'product of inverse outdegrees along the entire event path',
                             'decoder':'existing uniform fiber means followed by initial state fiber mean',
                             'mean_detail_split_weighted_orthogonal':True,
                             'reflection_preserves_weights':True,
                             'all_depth_argument':'every nonempty parent fiber copies its coefficient d times with weight w/d; induction gives exact norm and recovery'},
        'boundary':{'metric_is_fixed_on_endpoint_states':False,'counting_weights_are_physical_probabilities':False,
                    'inverse_sqrt_amplitude_gains_implemented':False,'physical_instrument_derived':False,
                    'odd_preparation_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Compare the controller-arc weighted history lift with unrestricted native primitive extension, retaining accepted/rejected control histories; test whether conditioning and inherited norm weights commute or require an additional normalization operation.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale event-arc receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: predecessor-preserving arc lift retains all 14 reachable directions and decodes all 18 controller coordinates.')
    print('PASS: four event depths verify inherited positive fiber-metric isometries, orthogonal detail and endpoint squares.')
    print('Boundary: history-dependent counting metric on a supplied controller registry, not native preparation or physical normalization.')


if __name__=='__main__':main()
