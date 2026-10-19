"""All compatible parses, exponential ambiguity, and a shared source-tree witness.

A relation can be constructed without choosing a parse. A unique inverse cannot
recover every intended macro history from the same unmarked source record.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import encode
from check_controller_memory import audit as memory_audit
from check_retained_word_transport import RetainedSuccessorLedger

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/parse-ambiguity.v1.json'


def audit():
    prior=memory_audit()
    source=json.loads((BASE/'three-vertex-candidate.v1.json').read_text(encoding='utf-8'))
    packets=[(owner+':'+a+b,a,b) for owner,cycle in source['primitive_cycles'].items() for a,b in zip(cycle,cycle[1:])]
    edges=[(a,b) for _,a,b in packets]
    composites={tuple(p['edge']):p['path'] for p in source['displayed_composites']}
    dictionary=[]
    for pair_id,pair in enumerate(source['displayed_triangle_pairs']):
        for triangle in pair:
            for a,b in zip(triangle,triangle[1:]):
                path=composites.get((a,b),[a,b])
                word=tuple(edges.index(e) for e in zip(path,path[1:]))
                dictionary.append({'pair':pair_id,'edge':(a,b),'word':word})

    def expand(parse):return tuple(p for macro in parse for p in dictionary[macro]['word'])

    def complete_parses(pair,word):
        word=tuple(word)
        if word and any(edges[a][1]!=edges[b][0] for a,b in zip(word,word[1:])):
            raise ValueError('unsewn primitive word')
        @lru_cache(None)
        def visit(position):
            if position==len(word):return ((),)
            choices=[]
            for i,entry in enumerate(dictionary):
                if entry['pair']!=pair:continue
                block=entry['word']
                if word[position:position+len(block)]==block:
                    choices.extend((i,)+tail for tail in visit(position+len(block)))
            return tuple(choices)
        return visit(0)

    def markers(parse):
        return tuple(mark for macro in parse for mark in ([False]*(len(dictionary[macro]['word'])-1)+[True]))

    cycle=(0,1,8,9)  # AB BC CB BA, returns to A
    census=[]
    for n in range(9):
        word=cycle*n
        for pair in [0,1]:
            parses=complete_parses(pair,word)
            assert len(parses)==2**n and len(set(parses))==len(parses)
            assert all(expand(p)==word for p in parses)
            assert all(all(dictionary[a]['edge'][1]==dictionary[b]['edge'][0] for a,b in zip(p,p[1:])) for p in parses)
            counts=Counter(map(len,parses))
            assert counts==Counter({2*n+k:comb(n,k) for k in range(n+1)})
            assert len({markers(p) for p in parses})==2**n
            census.append({'cycles':n,'pair':pair,'parses':len(parses),
                           'macro_count_distribution':dict(sorted(counts.items()))})
    # A total macro count does not restore the local completion record.
    equal_count=[p for p in complete_parses(0,cycle*2) if len(p)==5]
    assert len(equal_count)==2 and markers(equal_count[0])!=markers(equal_count[1])
    short=(5,2);long=(0,1,2)
    assert expand(short)==expand(long)==cycle
    assert markers(short)==(False,True,False,True)
    assert markers(long)==(True,True,False,True)
    # Two distinct policies can be specified; neither is a recovered unique choice.
    assert min(map(len,complete_parses(0,cycle*8)))==16
    assert max(map(len,complete_parses(0,cycle*8)))==24

    # Actual source provenance can also be identical: one registered tree has
    # both the coarse and fine macro frontiers. No two execution IDs are equated.
    ledger=RetainedSuccessorLedger(packets)
    leaves=[ledger.retain_path_payload((((a,b,label),),),(F(1),)) for label,a,b in packets]
    ab=ledger.compose_payloads(leaves[0],leaves[1])
    ij=ledger.compose_payloads(leaves[8],leaves[9])
    whole=ledger.compose_payloads(ab,ij)
    assert ledger.deconstruct_payload(whole)[0]==(ab,ij)
    assert ledger.deconstruct_payload(ab)[0]==(leaves[0],leaves[1])
    assert ledger.deconstruct_payload(ij)[0]==(leaves[8],leaves[9])
    frontiers=[(ab,ij),(leaves[0],leaves[1],ij)]
    for frontier in frontiers:
        assert tuple(e for payload in frontier for e in payload.paths[0])==whole.paths[0]
        assert all(payload.values==(F(1),) for payload in frontier)
    assert whole.values==(F(1),)
    # Pair 2 has the analogous ambiguity by cutting above or below the ij node.
    assert expand((11,8))==expand((11,9,10))==cycle
    assert tuple(e for payload in (ab,leaves[8],leaves[9]) for e in payload.paths[0])==whole.paths[0]
    # Frontier designation is additional metadata; retain it alongside the one
    # original source tree. It is not fabricated by identifying different trees.
    source_tree=ledger.assembly_history(whole)
    tagged=[{'pair':0,'parse':p,'source_tree':source_tree} for p in [short,long]]
    assert tagged[0]['source_tree']==tagged[1]['source_tree'] and tagged[0]['parse']!=tagged[1]['parse']

    # Copying one source coefficient into every compatible parse is faithful on
    # its equal-copy image, but changes unweighted counting norm by parse count.
    for n in range(1,9):
        count=2**n
        coefficients=[F(3,2)]*count
        decoded=sum(coefficients)/count
        assert decoded==F(3,2)
        assert sum(v*v for v in coefficients)==count*decoded*decoded
        hostile=list(coefficients);hostile[0]+=1
        mean=sum(hostile)/count
        assert any(v!=mean for v in hostile)
    # Invalid, partially parsed, and foreign-pair routes are not accepted.
    try:complete_parses(0,(0,4))
    except ValueError:pass
    else:raise AssertionError('unsewn word accepted')
    assert complete_parses(0,(2,))==()  # CD only is an unfinished CE composite
    assert complete_parses(0,(5,6,7))==()  # other-pair branch AEp EpDp DpC

    dependencies=list(prior['source_sha256'])+[
        'research/scattering/seed-composition/check_parse_ambiguity.py',
        'research/nima/retained-path-family-composition-synthesis.md']
    return {
        'schema':'marici.scattering.parse-ambiguity.v1',
        'status':'canonical_parse_relation_constructed_unique_unmarked_history_inverse_obstructed',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'operation':'enumerate every endpoint-compatible complete macro parse of a retained primitive word; retain pair, source and completion marks',
        'dictionary':dictionary,
        'loop':{'primitive_ids':cycle,'primitive_names':['AB','BC','CB','BA'],
                'pair_0_short_parse':short,'pair_0_long_parse':long,
                'short_markers':markers(short),'long_markers':markers(long),
                'two_cycle_equal_macro_count_witnesses':equal_count},
        'census':census,
        'all_n_result':{'parse_count_per_pair':'2^n','macro_count_polynomial':'(z^2+z^3)^n',
                        'count_at_2n_plus_k':'binomial(n,k)',
                        'proof':'each primitive loop returns to A; independently choose the two-edge macro or its two primitive macros, while the other two-edge portion has a forced parse',
                        'extra_designations_for_all_distinct_parses':'n binary choices for n loops; not entropy, thermodynamic cost or qubits'},
        'same_source_tree':{'tree':source_tree,'coarse_frontier_word_lengths':[2,2],
                            'fine_frontier_word_lengths':[1,1,2],
                            'different_source_executions_identified':False,
                            'macro_frontier_uniquely_selected_by_tree':False},
        'equal_copy_parse_lift':{'decoder':'mean over all compatible tagged parses',
                                 'raw_counting_norm_multiplier':'2^n',
                                 'altered_one_parse_rejected':True,
                                 'physical_normalization_or_probabilities_supplied':False},
        'boundary':{'deterministic_parse_policy_impossible':False,
                    'unique_recovery_of_all_intended_parses_from_unmarked_source_possible':False,
                    'native_parse_policy_or_context_preparation_derived':False,
                    'independent_outputs_constructed':False,'physical_annihilation_derived':False,
                    'formal_outcomes_admitted':False},
        'next_gate':'Test continuation on the full retained parse relation and its source-forgetting map: determine whether all-parse transport preserves the synchronized mode without an unjustified coherent sum or normalization.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:
            raise SystemExit('FAIL: missing or stale parse-ambiguity receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: both pairs have 2^n parses and binomial macro-count distribution through n=8; structural recurrence proves all n.')
    print('PASS: one actual retained source tree admits different macro frontiers; even total macro count need not distinguish them.')
    print('Boundary: all-parse relation constructed; a selected parse policy and physical normalization are not derived.')


if __name__=='__main__':main()
