"""Minimal predictive quotient for the supplied segmented controller.

Observations retain pair, current vertex, primitive ID and completion marker.
Predictive minimization is not a lossless history quotient or physical memory law.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, rank, eye, encode
from check_segmented_copy_transport import audit as transport_audit
from check_controller_preparation_audit import audit as preparation_audit

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/controller-memory.v1.json'


def zeros(n,m):return [[F(0)]*m for _ in range(n)]


def audit():
    transport=transport_audit();preparation=preparation_audit()
    contexts=preparation['controller']['contexts']
    long=transport['segmented_automaton']['length_two_macro_ids']
    transitions=transport['segmented_automaton']['transition_labels']
    pairs=[i//6 for i in range(12)]+[edge//6 for edge in long]
    finishes=[i not in long for i in range(12)]+[True]*6
    vertices=[c['vertex'] for c in contexts]
    colors=[(pairs[i],vertices[i]) for i in range(18)]
    labels=sorted({(pairs[a],edge,finishes[a]) for a,b,edge in transitions})
    matrices={label:zeros(18,18) for label in labels}
    for a,b,edge in transitions:
        assert pairs[a]==pairs[b]
        matrices[(pairs[a],edge,finishes[a])][b][a]+=1
    assert [[sum(m[i][j] for m in matrices.values()) for j in range(18)] for i in range(18)]==transport['matrices']['micro_P']

    # First-event signatures already distinguish every class except two pairs.
    # This is a finite lower-bound witness, not merely a refinement heuristic.
    signature=[]
    for state in range(18):
        events=tuple((label,int(sum(matrices[label][row][state] for row in range(18)))) for label in labels)
        signature.append((colors[state],events))
    groups=[]
    for state,sig in enumerate(signature):
        existing=next((g for g in groups if signature[g[0]]==sig),None)
        if existing is None:groups.append([state])
        else:existing.append(state)
    assert len(groups)==16
    assert [g for g in groups if len(g)>1]==[[1,14],[10,16]]
    group_of={s:i for i,g in enumerate(groups) for s in g}
    Q=[[F(s in g) for s in range(18)] for g in groups]
    assert rank(Q)==16
    reduced={}
    for label,P in matrices.items():
        bar=zeros(16,16)
        for col,g in enumerate(groups):
            representative=g[0]
            for row,targets in enumerate(groups):bar[row][col]=sum(P[t][representative] for t in targets)
        assert mm(Q,P)==mm(bar,Q)
        reduced[label]=bar
    # The labelwise intertwining square proves preservation of every future
    # event-word count by induction, including segmentation completion events.
    # No further merge can preserve first-event counts plus initial colors.
    assert len({signature[g[0]] for g in groups})==16
    per_attachment=Counter(colors[g[0]] for g in groups)
    assert max(per_attachment.values())==2

    # The actuator's current right-profile bit is not the predictive memory bit.
    profile=[c['available_primitives'].index(c['expected_primitive']) for c in contexts]
    hostile_pairs=[(0,5),(8,9)]
    for a,b in hostile_pairs:
        assert colors[a]==colors[b] and profile[a]==profile[b]
        assert contexts[a]['expected_primitive']==contexts[b]['expected_primitive']
        assert finishes[a]!=finishes[b] and group_of[a]!=group_of[b]
    # With pair and vertex kept, a separate binary predictive state is sufficient
    # as an encoding of this supplied machine. The transition law is still supplied.
    local_code={}
    for color in per_attachment:
        matches=[i for i,g in enumerate(groups) if colors[g[0]]==color]
        for bit,group in enumerate(matches):local_code[group]=(color[0],color[1],bit)
    assert len(set(local_code.values()))==16

    # Quotient sums current coefficients in equivalent states. Keep differences
    # for lossless recovery; do NOT substitute it for the original path ledger.
    residuals=[[F(i==a)-F(i==b) for i in range(18)] for a,b in [(1,14),(10,16)]]
    assert rank(Q+residuals)==18
    assert mm(Q,[[row[i] for row in residuals] for i in range(18)])==zeros(16,2)
    decoder=zeros(18,18)
    for col,g in enumerate(groups):
        for s in g:decoder[s][col]=F(1,len(g))
    for r,(a,b) in enumerate([(1,14),(10,16)]):
        decoder[a][16+r]=F(1,2);decoder[b][16+r]=-F(1,2)
    assert mm(decoder,Q+residuals)==eye(18)
    # The aggregate micro-matrix already forgets these predecessor differences;
    # retained full paths, not its endpoint summary, must carry provenance.
    assert mm(transport['matrices']['micro_P'],[[row[i] for row in residuals] for i in range(18)])==zeros(18,2)

    dependencies=list(preparation['source_sha256'])+[
        'research/scattering/seed-composition/check_controller_memory.py',
        'research/scattering/seed-composition/contracts/seed-composition-work-net.v1.json']
    return {
        'schema':'marici.scattering.controller-memory.v1',
        'status':'exact_predictive_quotient_with_explicit_provenance_residuals',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'observation_contract':{'initial':['pair','current_vertex'],
                                'event':['pair','owner_labelled_primitive_id','macro_completed'],
                                'scope':'future labelled event counts, not recovery of the previous macro/history'},
        'quotient':{'original_states':18,'minimal_predictive_classes':16,'classes':groups,
                    'merged_pairs':[[1,14],[10,16]],'first_event_signatures_distinguish_classes':True,
                    'labelwise_intertwining_verified':True,'state_sum_Q':Q,
                    'local_codes':[{'class':g,'pair':c[0],'vertex':c[1],'bit':c[2]} for g,c in sorted(local_code.items())],
                    'labelled_reduced_transitions':[{'label':list(label),'arcs':[[j,i,int(m[i][j])] for j in range(16) for i in range(16) if m[i][j]]} for label,m in reduced.items()]},
        'actuator_memory_obstruction':{'pairs':hostile_pairs,'same_pair_vertex_and_current_profile':True,
                                      'different_completion_events':True,
                                      'profile_bit_alone_sufficient':False,
                                      'one_extra_local_predictive_bit_suffices_given_pair_vertex':True},
        'retention':{'quotient_kernel_dimension':2,'required_difference_records':residuals,
                     'augmented_rank':18,'exact_decoder':decoder,
                     'aggregate_micro_matrix_already_kills_these_differences':True,
                     'full_history_carrier_not_replaced':True},
        'boundary':{'physical_memory_or_clock_derived':False,'native_context_update_derived':False,
                    'controller_preparation_derived':False,'independent_outputs_constructed':False,
                    'physical_annihilation_derived':False,'formal_outcomes_admitted':False},
        'next_gate':'Test whether the native retained source can update the local parse bit and pair attachment, while preserving the two predictor-quotient residuals and the six preparation-reject directions.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:
            raise SystemExit('FAIL: missing or stale controller-memory receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: 18 contexts -> 16 minimal event-predictive classes; every labelled transition square commutes.')
    print('PASS: current profile bit loses completion information; pair+vertex+local parse bit suffices conditionally.')
    print('PASS: two difference records give exact 18-coordinate recovery; no physical memory/preparation promotion.')


if __name__=='__main__':main()
