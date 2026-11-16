#!/usr/bin/env python3
"""Independent unit-propagation verification using ALL raw Hall-deficient sets.
No matroid circuit machinery or LP; derives the red-neighborhood and
triangle-free necessary clauses directly from each support multiset.
"""
from itertools import combinations
from collections import Counter
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from ramsey_fractional_witness_certificate import support_classes
from ramsey_circuit_unit_propagation import propagate as circuit_propagate


def raw_constraints(m):
    edgelist=[]
    for a in range(16):
        for b in range(a+1,16):
            if m[a]&m[b]==0:
                edgelist.append((a,b))
    E=set(edgelist)
    H=[]
    for n in range(2,6):
        for U in combinations(range(16),n):
            support_union=0
            for u in U: support_union|=m[u]
            if support_union.bit_count()<n:
                H.append(frozenset(e for e in combinations(U,2) if e in E))
    tr=[]
    for U in combinations(range(16),3):
        t=frozenset(combinations(U,2))
        if t <= E:tr.append(t)
    return H,tr


def unit_propagate(m):
    H,tr=raw_constraints(m)
    reds=set();blues=set()
    trace=[]
    for k in range(100):
        progress=False
        for clause in H:
            if any(e in reds for e in clause):continue
            unknown=clause-blues
            if not unknown:return False, 'hall',trace
            if len(unknown)==1:
                e=next(iter(unknown))
                if e not in reds:
                    reds.add(e);progress=True;trace.append(('R',e,'Hall'))
        for clause in tr:
            if any(e in blues for e in clause):continue
            unknown=clause-reds
            if not unknown:return False,'triangle',trace
            if len(unknown)==1:
                e=next(iter(unknown))
                if e not in blues:
                    blues.add(e);progress=True;trace.append(('B',e,'Triangle'))
        assert not reds&blues
        if not progress:return True,'open',trace
    raise AssertionError('propagation failed to terminate')


def check():
    statuses=Counter();depths=Counter();exceptions=[]
    for r in range(5):
        for index,m in enumerate(support_classes(r)[0]):
            ans,why,trace=unit_propagate(m)
            other= circuit_propagate(m)
            assert ans==other[0],(r,index,ans,why,other)
            if ans:exceptions.append((r,index))
            statuses[(r,why)]+=1
            depths[len(trace)//10]+=1
    print('RAW SUPPORT-CLAUSE PROPAGATION COUNTS:',dict(sorted(statuses.items())))
    print('ONLY SURVIVING SUPPORT PROFILES:',exceptions)
    assert exceptions==[(4,17),(4,188)],exceptions
    assert sum(statuses.values())==695
    print('VERIFIED independent of matroid-circuit reduction and exact LP certificates.')

if __name__=='__main__':check()
