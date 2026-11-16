#!/usr/bin/env python3
"""Reduce Ramsey support Hall witnesses to transversal-matroid circuits.
Verifies all 695 support classes and 115 degree-free rational triangle-cover
certificates after replacing each deficient set by a contained minimal circuit.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction
import gzip, json
from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import ramsey_fractional_witness_certificate as base


def deficient(U,supports):
    mask=0
    for i in U:mask|=supports[i]
    return mask.bit_count()<len(U)


def hall_independent(U,supports):
    return all(not deficient(C,supports) for k in range(1,len(U)+1) for C in combinations(U,k))

def circuits_of(supports,max_size=5):
    circuits=[]
    for size in range(2,max_size+1):
        for U in combinations(range(len(supports)),size):
            if not deficient(U,supports):continue
            if all(hall_independent(U[:j]+U[j+1:],supports) for j in range(size)):
                circuits.append(U)
    return circuits


def find_circuit(U,supports):
    for size in range(2,len(U)+1):
        for C in combinations(U,size):
            if deficient(C,supports) and all(hall_independent(C[:j]+C[j+1:],supports) for j in range(size)):
                return C
    raise AssertionError(f'no circuit in {U}')


def verify_all():
    profile_count=0
    hall_total=0
    circuit_total=0
    size_counts=Counter()
    shrink_counts=Counter()
    largest_reduction=(0,None)
    for r in range(5):
        for idx,supports in enumerate(base.support_classes(r)[0]):
            profile_count+=1
            edges,hall,tris=base.constraints(supports)
            circuits=circuits_of(supports)
            H={U for U,E in hall}
            C=set(circuits)
            assert C.issubset(H)
            for U,inds in hall:
                c=find_circuit(U,supports)
                assert c in C and set(c).issubset(U)
                assert deficient(c,supports)
            # verify all matroid circuits have support-neighborhood of exactly |C|-1
            for c in circuits:
                mask=0
                for v in c: mask |=supports[v]
                assert mask.bit_count()==len(c)-1
                size_counts[len(c)]+=1
            hall_total+=len(hall)
            circuit_total+=len(circuits)
            shrink_counts[(r, len(hall)-len(circuits))]+=1
            if len(hall)-len(circuits)>largest_reduction[0]:largest_reduction=(len(hall)-len(circuits),(r,idx,len(hall),len(circuits)))
    print('profiles:',profile_count)
    print('hall_witness_rows:',hall_total,'circuits:',circuit_total,'factor:',round(hall_total/circuit_total,3))
    print('circuits_by_size:',dict(sorted(size_counts.items())))
    print('largest_row_reduction:',largest_reduction)

    data=json.load(gzip.open(HERE/'ramsey_triangle_cover_supplement.json.gz'))
    assert len(data['records'])==115
    orig_H=red_H=0
    orig_edges=red_edges=0
    shortened=0
    max_U=Counter()
    for record in data['records']:
        support=tuple(record['supports'])
        edges,hall,tri=base.constraints(support)
        E={e:i for i,e in enumerate(edges)}
        hmap=dict(hall)
        transformed=[]
        for typ,U,y in record['inequality_duals']:
            if typ=='H':
                U=tuple(U);C=find_circuit(U,support)
                assert C in hmap
                orig_H+=1
                orig_edges+=len(hmap[U]);red_edges+=len(hmap[C])
                max_U[(len(U),len(C))]+=1
                shortened+=(len(C)<len(U))
                U=C
            transformed.append([typ,list(U),y])
        rec={**record,'inequality_duals':transformed}
        assert base.verify_entry(rec)==Fraction(record['bound'])
    print('dual_H_rows:',orig_H,'rows_shortened:',shortened)
    print('dual_H_edge_occurrences_before_after:',orig_edges,red_edges)
    print('dual_H_size_transform:',dict(sorted(max_U.items())))
    print('all 115 reverified over exact rational arithmetic with circuit-only support clauses')

    # The exceptional ten-versus-nine cut uses 10 pairwise edge-disjoint
    # deficient witnesses; replacing each with a circuit keeps edge disjointness.
    exceptional=base.support_classes(4)[0][17]
    label=lambda m:''.join(str(i) for i in range(6) if m>>i&1)
    labels=tuple(map(label,exceptional));idx={a:i for i,a in enumerate(labels)}
    cut_B={'2','3','4','34','234','5','25','35','245'}
    W=(('2','5','25'),('3','4','34'),('3','5','35'),
       ('2','3','34','234'),('4','5','25','245'),
       ('2','234','25','35','245'),('3','34','234','25','35'),
       ('3','34','234','35','245'),('4','34','234','35','245'),
       ('34','234','5','35','245'))
    used=set();cut_rows=[]
    for row in W:
        U=tuple(sorted(idx[a] for a in row))
        C=find_circuit(U,exceptional)
        edges_C={tuple(sorted(e)) for e in combinations(C,2) if not(exceptional[e[0]] & exceptional[e[1]])}
        assert edges_C and used.isdisjoint(edges_C)
        assert all(labels[i] in cut_B for i in C)
        used.update(edges_C)
        cut_rows.append(([labels[i] for i in C],len(edges_C)))
    print('exceptional_cut_circuitized_10_rows:',cut_rows)
    print('cut_distinct_possible_edges:',len(used))

if __name__=='__main__': verify_all()
