#!/usr/bin/env python3
"""Verify 95 minimal Hall--triangle obstruction certificates for R(3,7).

Python 3 standard library only. Put ramsey_hall_triangle_minimal_cores.json.gz
in the same directory and run:
    python ramsey_hall_triangle_core_verifier.py

Reconstructs the 478 reduced contact systems, validates all 95 archived
proof cores, checks Boolean unsatisfiability and deletion minimality,
and confirms that these are precisely the 95 cases requiring Hall--triangle
propagation. The analytic reductions to 478 systems are assumptions.

The archive's 26 class labels were independently checked using exact
isomorphism of incidence graphs, but graph isomorphism is not rechecked here.
"""
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations
import gzip
import json
from pathlib import Path

LABELS=tuple(range(6))
EDGES=list(combinations(LABELS,2))
TRIPLES=list(combinations(LABELS,3))


def triple_representatives(s):
    S=set(range(s)); hcount=s-2
    action=[p+q for p in permutations(range(s))
            for q in permutations(range(s,6))]
    seen=set()
    for H in combinations_with_replacement(TRIPLES,hcount):
        if not S <= set().union(*map(set,H)) or H in seen:
            continue
        for perm in action:
            seen.add(tuple(sorted(tuple(sorted(perm[i] for i in tri))
                                  for tri in H)))
        yield H


def admissible_contact_systems():
    by_deg=defaultdict(list)
    for mask in range(1 << len(EDGES)):
        doubles=[EDGES[j] for j in range(len(EDGES)) if mask & (1<<j)]
        deg=tuple(sum(i in e for e in doubles) for i in LABELS)
        by_deg[deg].append(doubles)
    for s in (4,5,6):
        singles=set(range(s));other=set(range(s,6))
        for H in triple_representatives(s):
            target=tuple(5-int(i in singles)-sum(i in tri for tri in H)
                         for i in LABELS)
            options=list(by_deg.get(target,[]))
            if s==4:
                target2=tuple(target[i]-int(i in other) for i in LABELS)
                options += [B+[(4,5)] for B in by_deg.get(target2,[])
                            if (4,5) in B]
            for B in options:
                if len(B)!=18-2*s:
                    continue
                supports=set(B)
                if any((i,j) in supports and (i,k) in supports and
                       (j,k) in supports
                       for i,j,k in combinations(range(s),3)):
                    continue
                C=[(i,) for i in range(s)]+list(H)+list(B)
                assert len(C)==16 and all(sum(i in c for c in C)==5
                                           for i in LABELS)
                excluded=False
                for i in range(s):
                    D=set().union(*(set(b)-{i} for b in B if i in b))
                    if sum(set(c)<=D for c in C)>len(D):
                        excluded=True
                        break
                if not excluded:
                    yield s,C


def eligible_and_clauses(C):
    masks=[sum(1<<i for i in c) for c in C]
    possible=[(x,y) for x,y in combinations(range(16),2)
              if not (masks[x] & masks[y])]
    index={e:j for j,e in enumerate(possible)}
    hall=set()
    for k in range(2,6):
        for T in combinations(range(16),k):
            union=0
            for x in T:union |= masks[x]
            if union.bit_count()<k:
                hall.add(frozenset(index[e] for e in combinations(T,2)
                                   if e in index))
    tri=set()
    for T in combinations(range(16),3):
        if all(e in index for e in combinations(T,2)):
            tri.add(frozenset(index[e] for e in combinations(T,2)))
    return index,hall,tri


def propagation(hall,tri):
    """Unit propagation of Hall-positive and triangle-negative clauses."""
    state={}
    # Order is fixed only for reproducibility; conflict detection is sound.
    H=sorted(hall,key=lambda c:(len(c),tuple(sorted(c))))
    TT=sorted(tri,key=lambda c:tuple(sorted(c)))
    while True:
        old=len(state)
        for clause in H:
            if any(state.get(e)==1 for e in clause):
                continue
            remain=[e for e in clause if e not in state]
            if not remain:
                return 'Hall'
            if len(remain)==1:
                state[remain[0]]=1
        for clause in TT:
            n_true=sum(state.get(e)==1 for e in clause)
            if n_true==3:
                return 'triangle'
            if n_true==2:
                for e in clause:
                    if e not in state:
                        state[e]=0
        if len(state)==old:
            return 'open'


def boolean_satisfiable(hall,tri):
    """Exact DPLL solver for a positive-Hall, negative-triangle CNF."""
    variables=sorted(set().union(*(map(set,hall|tri))))
    ref={v:i for i,v in enumerate(variables)}
    H=[sum(1<<ref[e] for e in clause) for clause in hall]
    T=[sum(1<<ref[e] for e in clause) for clause in tri]
    n=len(variables)
    def dfs(ones,zeros):
        while True:
            prev=(ones,zeros)
            fixed=ones|zeros
            for clause in H:
                if clause&ones:
                    continue
                remain=clause&~fixed
                if not remain:
                    return False
                if remain&(remain-1)==0:
                    ones |= remain
                    fixed |= remain
            for clause in T:
                remain=clause&~fixed
                if not remain:
                    if not (clause&zeros):
                        return False
                elif remain&(remain-1)==0 and not(clause&zeros):
                    zeros |= remain
                    fixed |= remain
            if (ones,zeros)==prev:
                break
        outstanding=[c for c in H if not(c&ones)]
        if not outstanding:
            return True
        counts=Counter()
        for c in outstanding:
            for i in range(n):
                if (c>>i)&1 and not((ones|zeros)>>i)&1:
                    counts[i]+=1
        if not counts:
            return False
        bit=1<<max(counts,key=counts.get)
        return dfs(ones|bit,zeros) or dfs(ones,zeros|bit)
    return dfs(0,0)


def core_clauses(C,rec):
    index,all_h,all_t=eligible_and_clauses(C)
    h=set();t=set()
    for T in rec['hall']:
        assert 2<=len(T)<=5 and len(set(T))==len(T)
        contacts=set().union(*(set(C[x]) for x in T))
        assert len(contacts)<len(T), ('invalid Hall set',T,C)
        clause=frozenset(index[e] for e in combinations(T,2) if e in index)
        assert clause in all_h and clause not in h
        h.add(clause)
    for T in rec['triangle']:
        assert len(T)==3 and len(set(T))==3
        edges=list(combinations(T,2))
        assert all(e in index for e in edges)
        clause=frozenset(index[e] for e in edges)
        assert clause in all_t and clause not in t
        t.add(clause)
    assert h and t
    return h,t


def main():
    archive=Path(__file__).with_name('ramsey_hall_triangle_minimal_cores.json.gz')
    with gzip.open(archive,'rt',encoding='utf8') as f:
        doc=json.load(f)
    assert doc['count']==95 and doc['class_count']==26
    saved={tuple(map(tuple,r['contacts'])):r for r in doc['records']}
    assert len(saved)==95
    counts=Counter(); rounds=Counter(); classes=Counter()
    for s,C in admissible_contact_systems():
        key=tuple(C)
        index,Hall,Tri=eligible_and_clauses(C)
        if frozenset() in Hall:
            assert key not in saved
            counts['immediate Hall']+=1
        else:
            status=propagation(Hall,Tri)
            if status=='open':
                assert key not in saved
                counts['open']+=1
            else:
                assert key in saved
                rec=saved.pop(key)
                assert rec['s']==s
                hs,ts=core_clauses(C,rec)
                assert propagation(hs,ts)!='open'
                assert not boolean_satisfiable(hs,ts)
                # MUS: removing ANY one clause makes the abstract CNF satisfiable.
                for h in hs:
                    assert boolean_satisfiable(hs-{h},ts)
                for t in ts:
                    assert boolean_satisfiable(hs,ts-{t})
                rounds[rec['rounds']]+=1
                classes[rec['motif_class']]+=1
                counts['minimal Hall-triangle core']+=1
    assert not saved
    assert counts=={'immediate Hall':380,'minimal Hall-triangle core':95,'open':3},counts
    assert len(classes)==26
    assert sorted(classes.values(),reverse=True)==[23,17,8,7,4,4]+[2]*12+[1]*8
    assert rounds=={0:45,1:27,2:10,3:9,4:2,6:2}
    print('478 reduced contact systems reconstructed: 380 immediate, 95 MUS, 3 open.')
    print('All 95 certificates are satisfiable after removing any single clause.')
    print('26 stored clause-incidence isomorphism classes; counts:',
          sorted(classes.values(),reverse=True))
    print('Closure depth distribution:',dict(sorted(rounds.items())))
    print('All integer/Boolean checks passed; no external solver required.')

if __name__=='__main__':
    main()
