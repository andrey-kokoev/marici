"""Primitive-step transport of all parses; sum, mean and macro phase are distinct."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_incidence_audit import mm, rank, eye, encode
from check_parse_ambiguity import audit as parse_audit

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/all-parse-transport.v1.json'


def zeros(n,m):return [[F(0)]*m for _ in range(n)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]


def audit():
    prior=parse_audit();dictionary=prior['dictionary']
    source=json.loads((BASE/'three-vertex-candidate.v1.json').read_text(encoding='utf-8'))
    edges=[(a,b) for cycle in source['primitive_cycles'].values() for a,b in zip(cycle,cycle[1:])]
    results=[]
    for pair in [0,1]:
        macros=[d for d in dictionary if d['pair']==pair]
        boundary=sorted({v for d in macros for v in d['edge']})
        states=[('ready',v) for v in boundary]+[('pending',d['word'][1]) for d in macros if len(d['word'])==2]
        assert len(states)==7 and len(set(states))==7
        transitions=[]
        for d in macros:
            word=d['word'];start=states.index(('ready',d['edge'][0]))
            end=states.index(('ready',d['edge'][1])) if len(word)==1 else states.index(('pending',word[1]))
            transitions.append((start,end,word[0],len(word)==1))
        for state in states:
            if state[0]=='pending':
                edge=state[1]
                transitions.append((states.index(state),states.index(('ready',edges[edge][1])),edge,True))
        # Lazy parsing chooses a macro on consuming its first primitive, not in
        # advance. Complete input therefore has no extra next-choice multiplier.
        vertices=[s[1] if s[0]=='ready' else edges[s[1]][0] for s in states]
        groups=[]
        signatures=[]
        for i in range(7):
            signatures.append((vertices[i],tuple(sorted(Counter((e,done) for a,b,e,done in transitions if a==i).items()))))
        for i,sig in enumerate(signatures):
            group=next((g for g in groups if signatures[g[0]]==sig),None)
            if group is None:groups.append([i])
            else:group.append(i)
        assert len(groups)==6
        group_of={s:i for i,g in enumerate(groups) for s in g}
        Q=[[F(s in g) for s in range(7)] for g in groups]
        labels=sorted({(e,done) for _,_,e,done in transitions})
        label_matrices={}
        for label in labels:
            P=zeros(7,7)
            for a,b,e,done in transitions:
                if (e,done)==label:P[b][a]+=1
            reduced=[[sum(P[t][g[0]] for t in target) for g in groups] for target in groups]
            assert mm(Q,P)==mm(reduced,Q)
            label_matrices[label]=reduced
        W=zeros(6,6)
        for matrix in label_matrices.values():W=add(W,matrix)
        G=[[F(bool(x)) for x in row] for row in W]
        assert sorted(x for row in W for x in row if x)==[1,1,1,1,1,1,2]
        # No two distinct primitive labels use the same quotient arc; G really
        # forgets parse multiplicity, not distinct primitive transitions.
        for a in range(6):
            for b in range(6):
                used={e for (e,done),m in label_matrices.items() if m[b][a]}
                assert len(used)<=1
        assert rank(add(add(mm(G,G),G),eye(6)))==6
        assert rank(add(add(mm(W,W),W),eye(6)))==6

        # Source domain: primitive prefixes compatible with this supplied pair
        # dictionary, including incomplete composite words. No general source
        # path is silently asserted to be accepted by the grammar.
        initial=states.index(('ready','A'))
        histories=[((),(),initial)]
        stages=[]
        for depth in range(9):
            words=sorted({h[0] for h in histories});word_index={w:i for i,w in enumerate(words)}
            R=[[F(j==word_index[h[0]]) for j in range(len(words))] for h in histories]
            counts=Counter(h[0] for h in histories)
            D=[[R[i][j]/counts[word] for i in range(len(histories))] for j,word in enumerate(words)]
            assert mm(D,R)==eye(len(words))
            stages.append({'primitive_length':depth,'source_prefixes':len(words),'tagged_parse_prefixes':len(histories),
                           'fiber_sizes':sorted(set(counts.values()))})
            if depth==8:break
            children=[];parents=[]
            for parent,h in enumerate(histories):
                word,trace,state=h
                for event,(a,b,e,done) in enumerate(transitions):
                    if a==state:
                        children.append((word+(e,),trace+(event,),b));parents.append(parent)
            assert len(set(children))==len(children)
            next_words=sorted({h[0] for h in children});next_index={w:i for i,w in enumerate(next_words)}
            Rnext=[[F(j==next_index[h[0]]) for j in range(len(next_words))] for h in children]
            Esource=[[F(j==word_index[word[:-1]]) for j in range(len(words))] for word in next_words]
            Eparse=[[F(j==parent) for j in range(len(histories))] for parent in parents]
            assert mm(Rnext,Esource)==mm(Eparse,R)
            # This is checked on the full retained coefficient carriers, not by
            # assigning a phase to each path from an aggregate eigenvalue.
            histories=children

        # Exact return-word counting: one doubled ambiguity per four-step loop.
        weighted_edges={e:zeros(6,6) for e in range(10)}
        raw_edges={e:zeros(6,6) for e in range(10)}
        for (e,done),matrix in label_matrices.items():weighted_edges[e]=add(weighted_edges[e],matrix)
        for e,matrix in weighted_edges.items():
            raw_edges[e]=[[F(bool(x)) for x in row] for row in matrix]
            assert all(sum(raw_edges[e][b][a] for b in range(6))<=1 for a in range(6))
        # Thus each erased primitive word determines one quotient context: G
        # counts source words, not additional nondeterministic parser choices.
        start=group_of[initial]
        for n in range(1,7):
            weighted=eye(6);raw=eye(6)
            for e in (0,1,8,9)*n:
                weighted=mm(weighted_edges[e],weighted);raw=mm(raw_edges[e],raw)
            assert weighted[start][start]==2**n and raw[start][start]==1
        results.append({'pair':pair,'lazy_states':states,'predictive_classes':groups,
                        'transitions':transitions,'sum_matrix_W':W,'source_word_matrix_G':G,
                        'rank_phi3_W':6,'rank_phi3_G':6,'finite_retained_transport_checks':stages})

    dependencies=list(prior['source_sha256'])+['research/scattering/seed-composition/check_all_parse_transport.py']
    return {
        'schema':'marici.scattering.all-parse-transport.v1',
        'status':'equal_copy_history_transport_closes_fixed_primitive_step_C3_readouts_fail',
        'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'clock':'one primitive arrow per step; partial composites retained; macro choice made on first consumed primitive',
        'domain':'pair-dictionary-compatible primitive prefixes, not every path of the unrestricted glued graph',
        'retained_square':{'identity':'R_(n+1) E_source = E_parse R_n','decoder':'D_n R_n=I, with D_n fiberwise mean',
                           'all_n_reason':'each tagged child has one tagged predecessor and its erased word has that same primitive-prefix predecessor; equal-copy coefficients therefore agree',
                           'checked_primitive_lengths':list(range(9)),
                           'arbitrary_parse_payload_is_not_equal_copy_source_data':True},
        'readout_distinctions':{'sum':'each source-word coefficient is multiplied by its parse-fiber cardinality',
                                'mean':'divide within each retained source-word fiber before endpoint aggregation; returns one coefficient per source word',
                                'endpoint_only_mean':'not substituted for source-word-fiber averaging',
                                'loop_sum_multiplier':'2^n','loop_mean_multiplier':1,
                                'physical_metric_or_probability_normalization_derived':False},
        'pair_results':results,
        'mode_disposition':{'macro_reference_C3_identity_retracted':False,
                            'nonzero_reference_omega_mode_of_either_fixed_primitive_endpoint_readout':False,
                            'exact_test':'rank(M^2+M+I)=6 for both G and W in each pair',
                            'path_phase_from_aggregate_eigenvalue_assumed':False,
                            'scope':'finite prefix-context sum and source-word-mean endpoint readouts at a common primitive-step clock, not every retained-history representation'},
        'boundary':{'native_dictionary_or_parse_policy_derived':False,'physical_clock_identified':False,
                    'independent_outputs_constructed':False,'physical_annihilation_derived':False,
                    'formal_outcomes_admitted':False},
        'next_gate':'Keep the primitive-step generating variable in the boundary return operator; test a clock-aware transport relation rather than identifying macro period three with three primitive steps.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2,default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale all-parse transport receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: equal-copy parse lift commutes with primitive-prefix transport; exact mean decoder.')
    print('PASS: sum weights repeated loops by 2^n; source-word mean does not; both fixed-step Phi3 kernels are zero.')
    print('Boundary: retained transport succeeds, but macro C3 is not a fixed primitive-step or physical clock result.')


if __name__=='__main__':main()
