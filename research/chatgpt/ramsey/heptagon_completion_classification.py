#!/usr/bin/env python3
"""Classify the four certified normal-form completions without a graph catalogue."""
from collections import Counter
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
from heptagon_profile import PAIRS, PROFILE
from pauli_realization_audit import decode_graph6, binary_rank
from pauli_low_cost_structure import kernel_basis, span
HERE=Path(__file__).resolve().parent

def normal_form_orders(rows,cycle):
    """All orders fixing this distinguished C7 to the canonical incidence profile."""
    types=[()]+list(PAIRS)
    for sign in(-1,1):
        for shift in range(7):
            ordered_cycle=[cycle[(sign*i+shift)%7]for i in range(7)]
            groups={t:[]for t in types}
            for v in range(len(rows)):
                if v in cycle:continue
                kind=tuple(i for i,w in enumerate(ordered_cycle)if rows[v]>>w&1)
                if kind not in groups:break
                groups[kind].append(v)
            else:
                if len(groups[()])!=1 or tuple(len(groups[t])for t in PAIRS)!=PROFILE:continue
                for choices in product(*(permutations(groups[t])for t in types)):
                    yield ordered_cycle+[v for choice in choices for v in choice]

def canonical_order(rows,cycle):
    return min(normal_form_orders(rows,cycle),key=lambda order:tuple((rows[order[i]]>>order[j])&1 for i,j in combinations(range(len(rows)),2)))

def cycle_preserving_isomorphism(source,target):
    for order in normal_form_orders(source,list(range(7))):
        if all(((source[order[i]]>>order[j])&1)==((target[i]>>j)&1)for i,j in combinations(range(22),2)):
            mapping=[None]*22
            for new,old in enumerate(order):mapping[old]=new
            return mapping
    return None

def classify(records):
    classes=[]
    for index,record in enumerate(records):
        rows=decode_graph6(record['graph6'])
        weight_enumerator=dict(sorted(Counter(w.bit_count()for w in span(kernel_basis(rows))).items()))
        for group in classes:
            representative=decode_graph6(records[group['representative_record_0based']]['graph6'])
            mapping=cycle_preserving_isomorphism(representative,rows)
            if mapping is not None:
                group['members'].append({'record_0based':index,'representative_to_member_0based':mapping});break
        else:
            classes.append({'representative_record_0based':index,'kernel_weight_enumerator':weight_enumerator,
                            'members':[{'record_0based':index,'representative_to_member_0based':list(range(22))}]})
    # A different kernel weight enumerator rules out even an isomorphism that
    # sends the distinguished C7 to another C7; no graph-library claim needed.
    assert len(classes)==2
    assert classes[0]['kernel_weight_enumerator']!=classes[1]['kernel_weight_enumerator']
    return classes

def switch_certificate(records,classes):
    choices=[]
    for a in classes[0]['members']:
        for b in classes[1]['members']:
            i,j=a['record_0based'],b['record_0based']
            x,y=decode_graph6(records[i]['graph6']),decode_graph6(records[j]['graph6'])
            changed=[(u,v)for u,v in combinations(range(22),2)if (x[u]^y[u])>>v&1]
            choices.append((len(changed),i,j,changed))
    count,i,j,changed=min(choices);assert count==4
    x,y=decode_graph6(records[i]['graph6']),decode_graph6(records[j]['graph6'])
    removed=[p for p in changed if x[p[0]]>>p[1]&1];added=[p for p in changed if y[p[0]]>>p[1]&1]
    assert len(removed)==len(added)==2
    assert sorted(v for p in removed for v in p)==sorted(v for p in added for v in p)
    assert len({v for p in changed for v in p})==4
    codes=[set(span(kernel_basis(rows)))for rows in(x,y)];common=codes[0]&codes[1]
    assert len(common)==32
    shared=[]
    for mask in [(1<<22)-1]+sorted(common,key=lambda w:(w.bit_count(),w)):
        if binary_rank(shared+[mask])>len(shared):shared.append(mask)
    assert len(shared)==5
    extra=[min(code-common,key=lambda w:(w.bit_count(),w))for code in codes]
    assert all(binary_rank(shared+[mask])==6 for mask in extra)
    support=lambda mask:[v for v in range(22)if mask>>v&1]
    return {'source_record_0based':i,'target_record_0based':j,
            'removed_edges_0based':removed,'added_edges_0based':added,
            'shared_relation_supports_0based':[support(w)for w in shared],
            'source_extra_relation_0based':support(extra[0]),'target_extra_relation_0based':support(extra[1]),
            'shared_kernel_dimension':5,'source_nullity':6,'target_nullity':6}

if __name__=='__main__':
    path=HERE/'heptagon-profile-completions.json';data=json.loads(path.read_text())
    assert data['proof_independently_checked']
    classes=classify(data['records'])
    result={'completion_receipt_sha256':sha256(path.read_bytes()).hexdigest(),
            'isomorphism_class_count':2,'classes':classes,'square_switch':switch_certificate(data['records'],classes),
            'scope':'The four certified normal-form completions, with explicit isomorphisms and a distinguishing invariant; no source catalogue used.'}
    (HERE/'heptagon-completion-classification.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Classes:',[len(c['members'])for c in result['classes']])
