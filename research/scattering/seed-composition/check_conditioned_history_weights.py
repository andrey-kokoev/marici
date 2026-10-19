"""Controlled history normalization versus native choice with first rejects retained."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import audit as incidence_audit, mm, transpose, encode
from check_controller_preparation_audit import audit as preparation_audit
from check_segmented_copy_transport import audit as transport_audit
from check_retained_event_arc_lift import audit as arc_audit, weighted_gram
from check_retained_word_transport import RetainedSuccessorLedger

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/conditioned-history-weights.v1.json'


def audit():
    previous=arc_audit();prep=preparation_audit();transport=transport_audit();incidence=incidence_audit()
    contexts=prep['controller']['contexts'];arcs=[tuple(t) for t in transport['segmented_automaton']['transition_labels']]
    targets={s:[b for a,b,p in arcs if a==s] for s in range(18)}
    m=[len(c['available_primitives']) for c in contexts];d=[len(targets[s]) for s in range(18)]
    assert m.count(2)==14 and m.count(1)==4
    E=transport['matrices']['synchronized_mode_frame']+[[F(0),F(0)] for _ in range(6)]
    primitive=incidence['primitive_order'];packets=[(p['owner']+':'+''.join(p['edge']),*p['edge']) for p in primitive]
    ledger=RetainedSuccessorLedger(packets);paths=ledger.root.paths
    neutral=ledger.retain_payload(ledger.root,[F(1)]*10)
    source_tests=[]
    for c in contexts:
        s=c['state'];p=c['expected_primitive']
        incoming=next(i for i,edge in enumerate(paths) if edge[0][1]==c['vertex'])
        parent=ledger.retain_path_payload((paths[incoming],),(F(1),))
        gate=ledger.retain_payload(ledger.root,[F(i==p) for i in range(10)])
        complement=ledger.retain_payload(ledger.root,[F(i!=p) for i in range(10)])
        full=ledger.compose_payloads(parent,neutral)
        accepted=ledger.compose_payloads(parent,gate);rejected=ledger.compose_payloads(parent,complement)
        assert full.paths==accepted.paths==rejected.paths
        assert [a+b for a,b in zip(accepted.values,rejected.values)]==list(full.values)
        assert len(full.paths)==m[s]
        wn=F(1,m[s])
        assert sum(wn*v*v for v in accepted.values)==wn
        assert sum(wn*v*v for v in rejected.values)==1-wn
        assert gate.operation==complement.operation=='supplied'
        source_tests.append({'context':s,'native_available':m[s],'controller_targets':d[s],
                             'accepted_native_weight':wn,'rejected_native_weight':1-wn,
                             'controlled_arc_weight':F(1,d[s]),'accepted_native_arc_weight':F(1,m[s]*d[s]),
                             'metric_ratio_controller_over_native':m[s]})

    # Accepted primitive histories additionally retain supplied macro target
    # choices. These are observer/controller copies, not extra native primitives.
    # First reject stops that control trial; its complete prefix is retained.
    # (start,current,arc_history,primitive_word,native_weight,controlled_weight)
    accepted=[(s,s,(),(),F(1),F(1)) for s in range(18)]
    rejected=[];depths=[];witness=None
    for depth in range(1,7):
        next_accepted=[]
        for start,s,history,word,wn,wc in accepted:
            c=contexts[s];chosen=c['expected_primitive']
            for p in c['available_primitives']:
                if p!=chosen:
                    rejected.append((start,history,s,word+(p,),wn/m[s]))
            for target in targets[s]:
                next_accepted.append((start,target,history+((s,target,chosen),),word+(chosen,),
                                      wn/(m[s]*d[s]),wc/d[s]))
        accepted=next_accepted
        assert len({(r[0],r[2]) for r in accepted})==len(accepted)
        assert len({(r[0],r[1],r[2],r[3]) for r in rejected})==len(rejected)
        survival=[sum(r[4] for r in accepted if r[0]==s) for s in range(18)]
        lost=[sum(r[4] for r in rejected if r[0]==s) for s in range(18)]
        control=[sum(r[5] for r in accepted if r[0]==s) for s in range(18)]
        assert all(a+b==1 for a,b in zip(survival,lost)) and control==[1]*18
        assert all(0<q<=1 for q in survival)
        assert any(q<1 for q in survival)
        for start,s,history,word,wn,wc in accepted:
            assert all(paths[a][0][1]==paths[b][0][0] for a,b in zip(word,word[1:]))
            ratio=1
            for predecessor,target,p in history:ratio*=m[predecessor]
            assert wc/wn==ratio
        pullback=weighted_gram(E,survival);input_gram=weighted_gram(E,[F(1)]*18)
        scalar=pullback[0][0]/input_gram[0][0]
        proportional=all(pullback[i][j]==scalar*input_gram[i][j] for i in range(2) for j in range(2))
        depths.append({'depth':depth,'accepted_histories':len(accepted),'retained_first_reject_histories':len(rejected),
                       'survival_by_initial_context':survival,'accepted_input_mode_pullback':pullback,
                       'scalar_multiple_of_input_mode_metric':proportional,
                       'accepted_plus_first_reject_weight_equals_one':True})
        if depth==2:
            witness={'accepted':accepted[:4],'first_reject':rejected[:4]}
    assert [row['scalar_multiple_of_input_mode_metric'] for row in depths]==[False,False,True,False,False,False]
    assert input_gram==[[9,1],[1,1]]
    assert depths[2]['accepted_input_mode_pullback']==[[F(7,32)*v for v in row] for row in input_gram]
    # Exact backward recurrence for all finite depths, independent of enumeration.
    K=[[F(0)]*18 for _ in range(18)]
    for s in range(18):
        for target in targets[s]:K[s][target]+=F(1,m[s]*d[s])
    q=[F(1)]*18
    for row in depths:
        q=[sum(K[i][j]*q[j] for j in range(18)) for i in range(18)]
        assert q==row['survival_by_initial_context']
    bp=[9,10,11,6,7,8,3,4,5,0,1,2]
    long=transport['segmented_automaton']['length_two_macro_ids'];cp=bp+[12+long.index(bp[e]) for e in long]
    assert all(m[cp[s]]==m[s] and d[cp[s]]==d[s] for s in range(18))
    assert all(row['survival_by_initial_context'][cp[s]]==row['survival_by_initial_context'][s] for row in depths for s in range(18))

    dependencies=list(previous['source_sha256'])+['research/scattering/seed-composition/check_conditioned_history_weights.py']
    return {
        'schema':'marici.scattering.conditioned-history-weights.v1',
        'status':'native_accepted_history_subnorm_differs_from_controller_normalization_rejects_restore_total_weight',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'local_source_tests':source_tests,
        'comparison':{'native_then_conditioned_arc_weight':'1/(m(context)*d(context))',
                       'controller_only_arc_weight':'1/d(context)',
                       'history_metric_ratio':'product of m(context) over accepted steps',
                       'same_metric_after_conditioning':False,
                       'amplitude_gain_if_metric_is_held_fixed':'sqrt(product of m(context))',
                       'all_native_choices_and_first_rejects_retained':True,
                       'macro_target_choice_native_authorized':False},
        'finite_depth_tests':depths,'retained_record_witness':witness,
        'survival_recurrence':{'backward_matrix_K':K,'q0':'all ones','q_next':'K*q',
                               'reflection_invariant':True,'initial_mode_counting_gram':input_gram,
                               'scalar_gain_restores_initial_mode_metric_at_all_tested_depths':False,
                               'depth_three_scalar_exception':'7/32 times the initial mode Gram; not an all-depth rule'},
        'boundary':{'weights_are_physical_probabilities':False,'conditioning_changes_source_coefficients':False,
                    'gain_or_renormalization_source_derived':False,'rejects_silently_erased':False,
                    'all_conditioned_control_schemes_excluded':False,'formal_outcome_admitted':False},
        'next_gate':'Analyze the exact substochastic survival transfer K: certify long-horizon decay and the conditioned limiting profile, testing whether its reweighting is an additional state-dependent control rather than a physical clock or scalar normalization.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale conditioned-history receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: native accepted weights differ by products of available-choice counts from controller-only normalization.')
    print('PASS: six depths retain first-reject histories and total weight; scalar mode normalization fails at some horizons.')
    print('Boundary: rational counting weights, supplied policy and no derived physical normalization or probabilities.')


if __name__=='__main__':main()
