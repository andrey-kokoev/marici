#!/usr/bin/env python3
"""Exact checks of two reduced R(3,7) contact obstruction motifs.

Requires ramsey_composition_propagation.py in same folder, Python stdlib only.
Enumerates the 478 reduced contact systems; tests only Hall+triangle propagation;
verifies one capacity certificate and one edge-disjoint demand/cut certificate.
"""
from collections import Counter
from itertools import combinations
from ramsey_composition_propagation import (admissible_contact_systems,
                                             exceptional_capacity_contradiction)

A_TRIPLES={(0,1,2),(0,1,3),(0,2,3),(0,4,5)}
A_DOUBLES={(1,4),(1,5),(2,4),(2,5),(3,4),(3,5)}
B_TRIPLES={(0,1,2),(0,1,3),(0,4,5),(2,4,5)}
B_DOUBLES={(0,3),(1,2),(1,5),(2,3),(3,4),(4,5)}


def no_degree_propagation(C):
    masks=[sum(1<<i for i in c) for c in C]
    edges=[e for e in combinations(range(16),2) if not masks[e[0]]&masks[e[1]]]
    index={e:i for i,e in enumerate(edges)}
    clauses=set()
    for k in range(2,6):
        for T in combinations(range(16),k):
            union=0
            for x in T:union|=masks[x]
            if union.bit_count()<k:
                clauses.add(tuple(index[e] for e in combinations(T,2) if e in index))
    triangles=[tuple(index[e] for e in combinations(T,2))
               for T in combinations(range(16),3)
               if all(e in index for e in combinations(T,2))]
    state=[-1]*len(edges)
    while True:
        changed=False
        for clause in clauses:
            if any(state[e]==1 for e in clause):continue
            undecided=[e for e in clause if state[e]==-1]
            if not undecided:return 'Hall'
            if len(undecided)==1:
                state[undecided[0]]=1;changed=True
        for tri in triangles:
            count=sum(state[e]==1 for e in tri)
            if count==3:return 'triangle'
            if count==2:
                for e in tri:
                    if state[e]==-1:
                        state[e]=0;changed=True
        if not changed:return 'survived'


def verify_B_cut(C):
    """Ten edge-disjoint Hall demands vs upper bound e(P)<=9."""
    V={frozenset(c):i for i,c in enumerate(C)}
    def vertex(*labels):return V[frozenset(labels)]
    s=lambda i:vertex(i)
    d=lambda i,j:vertex(i,j)
    t=lambda i,j,k:vertex(i,j,k)
    P={s(0),s(1),s(2),s(3),t(0,1,2),t(0,1,3),d(0,3),d(1,2),d(2,3)}
    M=set(range(16))-P
    demands=[
        [t(0,1,2),t(0,1,3),d(0,3),d(1,2),d(2,3)],
        [s(3),t(0,1,2),t(0,1,3),d(0,3),d(2,3)],
        [s(2),t(0,1,2),t(0,1,3),d(0,3),d(2,3)],
        [s(2),s(3),d(1,2),d(2,3)],
        [s(1),s(3),t(0,1,3),d(0,3)],
        [s(1),s(2),d(1,2)],
        [s(0),t(0,1,2),t(0,1,3),d(0,3),d(2,3)],
        [s(0),s(3),d(0,3)],
        [s(0),s(1),t(0,1,2),d(1,2)],
        [s(1),t(0,1,2),t(0,1,3),d(1,2),d(2,3)]
    ]
    used_edges=set()
    for T in demands:
        assert set(T)<=P
        labels=set().union(*(set(C[x]) for x in T))
        assert len(labels)<len(T), ('not Hall-deficient',T)
        opts={tuple(sorted((a,b))) for a,b in combinations(T,2)
              if not (set(C[a])&set(C[b]))}
        assert opts and not used_edges.intersection(opts), ('overlapping demands',T)
        used_edges.update(opts)
    degree=lambda x:6-len(C[x])
    d_P=sum(map(degree,P));d_M=sum(map(degree,M))
    available_M=sum(not(set(C[a])&set(C[b])) for a,b in combinations(M,2))
    capacity=(d_P-d_M)//2+available_M
    assert d_P==38 and d_M==28 and available_M==4 and capacity==9
    assert len(demands)==10 and len(demands)>capacity
    # The same obstruction is an integer signed-capacity dual certificate:
    # weight each demand by 2; vertex potential +1 on P and -1 on M;
    # allow penalty 2 on each of the four eligible M--M edges.
    for a,b in combinations(range(16),2):
        if set(C[a])&set(C[b]):continue
        multiplicity=sum(a in T and b in T for T in demands)
        potential=(1 if a in P else -1)+(1 if b in P else -1)
        penalty=2 if a in M and b in M else 0
        assert 2*multiplicity<=potential+penalty
    assert 2*len(demands)==20 > d_P-d_M+2*available_M==18
    return {'demands':len(demands),'max_A_edges_in_P':capacity,
            'degree_sum_P':d_P,'degree_sum_M':d_M,
            'max_A_edges_in_M':available_M}


def main():
    stars=immediate=0
    survivors=[]
    for s,C in admissible_contact_systems():
        has_star=any(sum(i in c and set(c)<=set(U) for c in C)>len(U)
           for k in range(1,7) for U in combinations(range(6),k) for i in U)
        stars+=has_star
        has_zero=False
        for k in range(2,6):
            for T in combinations(C,k):
                if len(set().union(*(set(c) for c in T)))<k and all(
                    set(a)&set(b) for a,b in combinations(T,2)):
                    has_zero=True;break
            if has_zero:break
        immediate+=has_zero
        if no_degree_propagation(C)=='survived':survivors.append(C)
    assert (stars,immediate,len(survivors))==(377,380,3)
    types=Counter()
    for C in survivors:
        triangles={tuple(sorted(c)) for c in C if len(c)==3}
        doubles={tuple(sorted(c)) for c in C if len(c)==2}
        if triangles==A_TRIPLES and doubles==A_DOUBLES:
            assert exceptional_capacity_contradiction(C)
            types['A_15_vs_12']+=1
        elif triangles==B_TRIPLES:
            swap=lambda x:{4:5,5:4}.get(x,x)
            if doubles=={tuple(sorted((swap(x),swap(y)))) for x,y in B_DOUBLES}:
                C=[tuple(sorted(swap(x) for x in c)) for c in C]
                doubles={tuple(sorted(c)) for c in C if len(c)==2}
            assert doubles==B_DOUBLES
            assert verify_B_cut(C)['max_A_edges_in_P']==9
            types['B_10_vs_9']+=1
        else:
            raise AssertionError(('unexpected residual',triangles,doubles))
    assert types=={'A_15_vs_12':1,'B_10_vs_9':2}
    print('380 immediate zero-edge Hall contradictions; 377 via overfull stars')
    print('3 survive Hall+triangle propagation (no degree rule)')
    print('Type A: 15 disjoint Hall demands + 3 forced A-edges > 15 degrees (one case)')
    print('Type B: 10 disjoint Hall demands > 9 permitted edges (two label variants)')
    print('All exact checks passed.')

if __name__=='__main__':main()
