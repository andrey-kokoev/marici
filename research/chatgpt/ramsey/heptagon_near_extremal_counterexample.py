#!/usr/bin/env python3
"""A self-contained 21-vertex obstruction to unrestricted heptagon compression.
Exact arithmetic; no SAT or catalogue needed for this construction.
"""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
from pauli_realization_audit import binary_rank, triangle_free, independent_witness, encode_graph6, factor_paulis
from pauli_low_cost_structure import parity_closed_heptagons
HERE=Path(__file__).resolve().parent

N=21
JUMPS={1,4,6,15,17,20}

def graph():return [sum(1<<j for j in range(N)if (j-i)%N in JUMPS)for i in range(N)]

def polynomial_remainder(a,b):
    if not b:raise ZeroDivisionError('zero polynomial')
    while a and a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
    return a

def polynomial_gcd(a,b):
    while b:a,b=b,polynomial_remainder(a,b)
    return a

def compositions(total,length,minimum=2):
    if length==1:
        if total>=minimum:yield(total,)
        return
    for first in range(minimum,total-minimum*(length-1)+1):
        for rest in compositions(total-first,length-1,minimum):yield(first,)+rest

def gap_violates(gaps):
    return any(g in (1,4,6) for g in gaps) or any(gaps[i]==gaps[(i+1)%len(gaps)] and gaps[i] in (2,3) for i in range(len(gaps)))

def independent_levels(rows,cap):
    levels=[[]for _ in range(cap+1)]
    def visit(available,chosen,k):
        levels[k].append(chosen)
        if k==cap:return
        while available:
            bit=available&-available;available^=bit;v=bit.bit_length()-1
            visit(available&~rows[v],chosen|bit,k+1)
    visit((1<<len(rows))-1,0,0)
    return levels

def verify():
    rows=graph();assert triangle_free(rows)
    assert not any((a+b)%N in JUMPS for a in JUMPS for b in JUMPS)
    # Independent check of the cyclic-gap proof's finite local conditions.
    gaps=list(compositions(21,7));assert len(gaps)==1716 and all(gap_violates(g)for g in gaps)
    assert independent_witness(rows,7)is None
    levels=independent_levels(rows,6);assert list(map(len,levels))==[1,21,147,448,651,441,112]
    cycles=[]
    for residue in range(3):
        cycle=[(residue+6*i)%21 for i in range(7)];mask=sum(1<<i for i in cycle)
        assert all((r&mask).bit_count()==2 for r in rows)
        assert all(rows[cycle[i]]>>cycle[(i+1)%7]&1 for i in range(7))
        cycles.append({'cycle_0based':cycle,'support_mask':mask})
    found,_=parity_closed_heptagons(rows)
    assert set(found)=={c['support_mask']for c in cycles}
    p=sum(1<<j for j in JUMPS);modulus=(1<<21)|1;gcd=polynomial_gcd(p,modulus)
    assert gcd==0b1001 # x^3+1
    assert binary_rank(rows)==21-(gcd.bit_length()-1)==18
    realization=factor_paulis(rows);assert realization['qubits']==9
    sixes=levels[6];extension_witnesses=[]
    for level in levels:
        for candidate in level:
            missed=[s for s in sixes if not(s&candidate)]
            assert missed
            extension_witnesses.append({'neighbor_mask':candidate,'disjoint_independent_six_mask':missed[0],
                                        'missed_six_count':len(missed)})
    assert len(extension_witnesses)==1821
    assert min(r['missed_six_count']for r in extension_witnesses)==26
    return {'schema':'marici.parity-heptagon-near-extremal-counterexample.v1',
            'scope':'Refutes an unrestricted-size implication, NOT the exact 22-vertex conjecture.',
            'vertices':21,'jumps':sorted(JUMPS),'graph6':encode_graph6(rows),
            'degree':6,'independence_number':6,'independent_set_counts':list(map(len,levels)),
            'gap_compositions_checked':len(gaps),'parity_closed_heptagons':cycles,
            'circulant_polynomial_exponents':sorted(JUMPS),'gcd_polynomial_exponents':[0,3],
            'binary_rank':18,'nullity':3,'minimum_qubits':9,'pauli_realization':realization,
            'independent_six_example_0based':[i for i in range(N)if sixes[0]>>i&1],
            'vertex_extension':{'candidates':len(extension_witnesses),'valid':0,'minimum_missed_sixes':26,
                                'witnesses':extension_witnesses}}

if __name__=='__main__':
    result=verify();(HERE/'heptagon-near-extremal-counterexample.json').write_text(json.dumps(result,indent=2)+'\n')
    print({k:v for k,v in result.items()if k not in ['pauli_realization','vertex_extension']})
    print('No vertex extensions among',result['vertex_extension']['candidates'],'independent neighborhoods.')
