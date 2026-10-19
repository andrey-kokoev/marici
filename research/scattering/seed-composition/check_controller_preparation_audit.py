"""Exact controller/preparation cost audit; conditional records, not physical rates."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, transpose, rank, eye, apply, encode
from check_segmented_copy_transport import audit as transport_audit
from check_retained_word_transport import RetainedSuccessorLedger

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/controller-preparation-audit.v1.json'


def sub(a,b):
    return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]


def audit():
    previous=transport_audit()
    primitive=json.loads((BASE/'three-vertex-candidate.v1.json').read_text(encoding='utf-8'))
    edges=[(a,b) for cycle in primitive['primitive_cycles'].values() for a,b in zip(cycle,cycle[1:])]
    owners=[owner for owner,cycle in primitive['primitive_cycles'].items() for _ in zip(cycle,cycle[1:])]
    packets=[(owner+':'+a+b,a,b) for owner,(a,b) in zip(owners,edges)]
    ledger=RetainedSuccessorLedger(packets)
    paths=tuple(((a,b,label),) for label,a,b in packets)
    neutral=ledger.retain_path_payload(paths,tuple(F(1) for _ in paths))
    composites={tuple(p['edge']):p['path'] for p in primitive['displayed_composites']}
    words=[]
    for pair in primitive['displayed_triangle_pairs']:
        for triangle in pair:
            for edge in zip(triangle,triangle[1:]):
                word=composites.get(edge,list(edge))
                words.append(tuple(edges.index(e) for e in zip(word,word[1:])))
    long=previous['segmented_automaton']['length_two_macro_ids']
    # Every controller state has exactly one next primitive ID before the
    # separate boundary decision about which next macro-edge to enter.
    expected=[word[0] for word in words]+[words[i][1] for i in long]
    contexts=[]
    for state,selected in enumerate(expected):
        vertex=edges[selected][0]
        outgoing=[i for i,(a,_) in enumerate(edges) if a==vertex]
        incoming=next(i for i,(_,b) in enumerate(edges) if b==vertex) if state<12 else words[long[state-12]][0]
        parent=ledger.retain_path_payload((paths[incoming],),(F(1),))
        full=ledger.compose_payloads(parent,neutral)
        gate=ledger.retain_path_payload(paths,tuple(F(i==selected) for i in range(10)))
        reject_gate=ledger.retain_path_payload(paths,tuple(F(i!=selected) for i in range(10)))
        accepted=ledger.compose_payloads(parent,gate)
        rejected=ledger.compose_payloads(parent,reject_gate)
        assert full.paths==accepted.paths==rejected.paths
        assert len(full.paths)==len(outgoing) and all(v==1 for v in full.values)
        assert [a+b for a,b in zip(accepted.values,rejected.values)]==list(full.values)
        assert sum(v*v for v in accepted.values)==1
        assert sum(v*v for v in rejected.values)==len(outgoing)-1
        assert all(a*b==0 for a,b in zip(accepted.values,rejected.values))
        assert ledger.deconstruct_payload(accepted)[0]==(parent,gate)
        assert ledger.deconstruct_payload(rejected)[0]==(parent,reject_gate)
        # Zero-valued forbidden words are retained, not erased from the carrier.
        assert len(accepted.paths)==len(outgoing)
        contexts.append({'state':state,'vertex':vertex,'expected_primitive':selected,
                         'available_primitives':outgoing,'rejected_primitives':[i for i in outgoing if i!=selected],
                         'accepted_counting_norm_fraction':F(1,len(outgoing)),
                         'gate_record_operation':gate.operation})
    assert sum(len(c['rejected_primitives'])==1 for c in contexts)==14
    assert sum(not c['rejected_primitives'] for c in contexts)==4
    assert all(c['gate_record_operation']=='supplied' for c in contexts)

    # Exact counting-metric projector onto the synchronized mode inputs while
    # retaining d and g. It is audited as an added selector, not inferred dynamics.
    I=eye(10)
    group_a=[F(n) for n in [1,0,-1,0,0,1,0,0,-1,0]]
    group_b=[F(n) for n in [0,1,0,0,-1,0,0,1,0,-1]]
    Prep=[[group_a[i]*group_a[j]/4+group_b[i]*group_b[j]/4+F(i==j and i in [3,6])
           for j in range(10)] for i in range(10)]
    Reject=sub(I,Prep)
    assert rank(Prep)==4 and rank(Reject)==6
    assert transpose(Prep)==Prep and mm(Prep,Prep)==Prep
    assert mm(Prep,Reject)==[[0]*10 for _ in range(10)]
    assert mm(transpose(Prep),Prep)==Prep and mm(transpose(Reject),Reject)==Reject
    Q=previous['matrices']['prefix_copy_Q']
    V=previous['matrices']['synchronized_mode_frame']
    J=previous['matrices']['source_input_mode_frame_J']
    assert mm(Prep,J)==J and rank(mm(Q,Prep))==2
    # The preparation split retains all ten independent coordinates as two
    # orthogonal records; dropping the reject record loses six directions.
    assert rank(Prep+Reject)==10
    witness=I[0]
    prepared=apply(Prep,witness);residual=apply(Reject,witness)
    assert [a+b for a,b in zip(prepared,residual)]==witness
    assert sum(v*v for v in prepared)==F(1,4)
    assert sum(v*v for v in residual)==F(3,4)
    assert prepared!=witness and any(residual)

    # Complete directed graph automorphism audit of the supplied glued carrier.
    # This is not a classification of every possible source operation.
    vertices=sorted({v for e in edges for v in e})
    autos=[]
    for perm in permutations(vertices):
        relabel=dict(zip(vertices,perm))
        moved=[(relabel[a],relabel[b]) for a,b in edges]
        if set(moved)==set(edges):autos.append([edges.index(e) for e in moved])
    assert len(autos)==2 and autos[0]==list(range(10))
    reflection=autos[1]
    R=[[F(i==reflection[j]) for j in range(10)] for i in range(10)]
    assert mm(R,R)==I
    Odd=[[x/2 for x in row] for row in sub(I,R)]
    assert rank(Odd)==5 and mm(Odd,Odd)==Odd
    assert mm(R,J)==[[-x for x in row] for row in J]
    odd_witness=[F(i==0)-F(i==8) for i in range(10)]
    assert apply(Odd,odd_witness)==odd_witness
    assert apply(Prep,odd_witness)!=odd_witness
    assert mm(Prep,R)==mm(R,Prep)  # symmetry-compatible does not mean symmetry-selected
    N=[[F(edges[j][1]==edges[i][0]) for j in range(10)] for i in range(10)]
    commutator=sub(mm(Prep,N),mm(N,Prep))
    assert rank(commutator)>0

    dependencies=list(previous['source_sha256'])+['research/scattering/seed-composition/check_controller_preparation_audit.py']
    return {
        'schema':'marici.scattering.controller-preparation-audit.v1',
        'status':'explicit_retained_selector_and_preparation_split_native_derivation_still_open',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'controller':{'contexts':contexts,'nontrivial_primitive_selectors':14,'endpoint_forced_contexts':4,
                      'selectors_registered_as_supplied_not_derived':True,
                      'accepted_plus_rejected_recovers_full_extension':True,
                      'forbidden_zero_words_retained':True,
                      'scope':'primitive choice given an existing context; next macro-context selection and physical probability are not derived'},
        'preparation':{'rank_with_d_g_residuals':4,'observable_mode_rank':2,'rejected_dimension':6,
                       'alpha':'(a+f-c-i)/4','beta':'(b+h-e-j)/4',
                       'prepared_input':['alpha','beta','-alpha','d','-beta','alpha','g','beta','-alpha','-beta'],
                       'counting_metric_projector':Prep,'rejected_projector':Reject,
                       'input_witness':witness,'prepared_witness':prepared,'residual_witness':residual,
                       'witness_norm_split':[F(1,4),F(3,4)],
                       'split_is_lossless':True,'physical_preparation_or_metric_derived':False,
                       'glued_endpoint_commutator_rank':rank(commutator)},
        'symmetry':{'directed_graph_automorphism_count':2,'primitive_permutations':autos,
                    'odd_projector_rank':5,'desired_mode_is_odd':True,
                    'odd_nonmode_witness':odd_witness,'reflection_parity_alone_selects_mode':False,
                    'preparation_commutes_with_reflection':True},
        'boundary':{'source_derived_controller':False,'source_derived_preparation':False,
                    'branch_fractions_are_physical_probabilities':False,'independent_photons_constructed':False,
                    'physical_annihilation_derived':False,'ratio_372_derived':False,'formal_outcome_admitted':False},
        'next_gate':'Identify a source interaction that supplies the context selectors and correlated preparation while retaining the six rejected directions; do not discard those records or rename counting fractions as emission probabilities.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:
            raise SystemExit('FAIL: missing or stale controller/preparation receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: 14 nontrivial context selectors, 4 forced; allowed and rejected histories retained by source ledger.')
    print('PASS: preparation rank 4 plus rejected rank 6; parity sector rank 5 does not select the rank-2 mode.')
    print('Boundary: explicit conditional selectors and bookkeeping norms, not derived physical controls or rates.')


if __name__=='__main__':main()
