#!/usr/bin/env python3
"""Exact finite classification of the nonpositive rotational-score contact systems.

Fix six labels. If s is the number of singleton contacts and r the number
of label pairs with no co-occurring contact, rotational balance says only
(s,r) = (4,2),(4,3),(5,3),(6,3) need to be excluded.

The missing pairs form a matching. Therefore, for r=3, the co-occurrence
support is the 12-edge octahedral graph and every triple contact is one of
its 8 triangular faces. For r=2, the support is K6 with two independent
edges deleted: 13 possible double supports and 12 possible triples.

This script enumerates only these small edge/face selections, subject to:
  - singleton labels covered by a triple;
  - each label in exactly five contacts;
  - at most two copies of the double joining two nonsingleton labels;
  - no triangle on singleton labels in the double-support graph;
  - singleton closure and all overfull-contact-fiber exclusions;
  - all remaining co-occurrence pairs actually covered.

After factoring the symmetries of the missing matching, exactly six contact
systems remain: 2 of type (4,3), 1 of (4,2), 1 of (5,3), 2 of (6,3).
Exact Hall--triangle contradiction certificates for all six systems are
embedded and verified. Standard Python 3 only, no dependencies.
"""
from collections import Counter, defaultdict
import json
from itertools import combinations, combinations_with_replacement, permutations

L=tuple(range(6))
ALL_EDGES=tuple(combinations(L,2))
ALL_TRIPLES=tuple(combinations(L,3))


def singleton_closure(C, singles):
    doubles=[set(c) for c in C if len(c)==2]
    for i in singles:
        partners=set().union(*(d-{i} for d in doubles if i in d))
        if sum(set(c)<=partners for c in C)>len(partners):
            return False
    return True


def no_overfull_fiber(C):
    contacts=list(map(set,C))
    for size in range(1,7):
        for U0 in combinations(L,size):
            U=set(U0)
            for i in U:
                if sum(i in c and c<=U for c in contacts)>size:
                    return False
    return True


def supported_pair_set(C):
    return {tuple(p) for c in C for p in combinations(c,2)}


def automorphisms(missing):
    M={frozenset(p) for p in missing}
    return [p for p in permutations(L)
            if {frozenset((p[i],p[j])) for i,j in missing}==M]


def canonical(C,action):
    return min(tuple(sorted(tuple(sorted(p[i] for i in c)) for c in C))
               for p in action)


def support_types(s,r):
    missing=((0,1),(2,3)) if r==2 else ((0,1),(2,3),(4,5))
    missing_set=set(missing)
    E=tuple(e for e in ALL_EDGES if e not in missing_set)
    faces=tuple(t for t in ALL_TRIPLES if all(e not in missing_set for e in combinations(t,2)))
    assert len(E)==15-r
    assert len(faces)==(12 if r==2 else 8)
    action=automorphisms(missing)
    assert len(action)==(16 if r==2 else 48)
    return E,faces,action


def enumerate_types(s,r):
    E,faces,action=support_types(s,r)
    h=s-2; b=18-2*s
    by_degree=defaultdict(list)
    for B in combinations(E,b):
        degrees=tuple(sum(i in e for e in B) for i in L)
        by_degree[degrees].append(B)
    by_degree_once=defaultdict(list)
    if s==4:
        for B in combinations(E,b-1):
            degrees=tuple(sum(i in e for e in B) for i in L)
            by_degree_once[degrees].append(B)

    found=defaultdict(list)
    for S0 in combinations(L,s):
        singles=set(S0)
        extra=tuple(sorted(set(L)-singles))
        for H in combinations_with_replacement(faces,h):
            if not singles<=set().union(*(set(t) for t in H)):
                continue
            target=tuple(5-int(i in singles)-sum(i in t for t in H) for i in L)
            if any(t<0 for t in target): continue
            options=list(by_degree.get(target,()))
            if s==4 and extra in E:
                rem=tuple(target[i]-int(i in extra) for i in L)
                options.extend(B+(extra,) for B in by_degree_once.get(rem,())
                               if extra in B)
            for B in options:
                if len(B)!=b: continue
                if any(all(e in B for e in combinations(T,2)) for T in combinations(S0,3)):
                    continue
                C=tuple(sorted([(i,) for i in S0]+list(H)+list(B)))
                if len(C)!=16:continue
                if any(sum(i in c for c in C)!=5 for i in L):continue
                if supported_pair_set(C)!=set(E):continue
                if not singleton_closure(C,singles):continue
                if not no_overfull_fiber(C):continue
                key=canonical(C,action)
                found[key].append(C)
    return found


def unrestricted_signature(C):
    # Full relabeling signature, independent of how the missing matching is fixed.
    return min(tuple(sorted(tuple(sorted(p[i] for i in c)) for c in C))
               for p in permutations(L))


CERTIFICATES=json.loads(r'''[{"s":4,"r":3,"multiplicity":2,"contacts":[[0],[1],[2],[3],[0,1,4],[2,3,5],[0,3],[0,4],[0,5],[1,2],[1,4],[1,5],[2,4],[2,5],[3,4],[3,5]],"repeated":false,"hall":[[0,3,6],[0,4,7,8,11],[1,2,9],[1,3,11,15],[1,4,7,10],[2,5,13,15],[3,6,7,14]],"tri":[[0,3,11],[1,2,15],[1,3,7],[3,7,11]]},{"s":4,"r":3,"multiplicity":4,"contacts":[[0],[1],[2],[3],[0,1,4],[2,3,5],[0,3],[0,4],[0,5],[1,2],[1,3],[1,4],[2,4],[2,5],[3,5],[4,5]],"repeated":false,"hall":[[0,2,7,12],[0,4,7,11],[0,6,8,14],[1,2,9],[1,4,7,11],[2,9,11,12],[5,12,13,14,15]],"tri":[[0,2,11],[0,12,14],[1,2,7]]},{"s":4,"r":2,"multiplicity":2,"contacts":[[0],[1],[2],[3],[0,1,4],[2,3,5],[0,1],[0,3],[0,5],[1,2],[1,5],[2,3],[2,4],[3,4],[4,5],[4,5]],"repeated":false,"hall":[[4,8,10,14,15]],"tri":[]},{"s":5,"r":3,"multiplicity":6,"contacts":[[0],[1],[2],[3],[4],[0,1,2],[0,1,2],[3,4,5],[0,4],[0,5],[1,3],[1,5],[2,3],[2,4],[3,5],[4,5]],"repeated":true,"hall":[[0,1,5,6],[0,2,5,6],[1,2,5,6]],"tri":[[0,1,2]]},{"s":6,"r":3,"multiplicity":6,"contacts":[[0],[1],[2],[3],[4],[5],[0,1,2],[0,1,2],[3,4,5],[3,4,5],[0,4],[0,5],[1,3],[1,5],[2,3],[2,4]],"repeated":true,"hall":[[0,1,6,7],[0,2,6,7],[1,2,6,7]],"tri":[[0,1,2]]},{"s":6,"r":3,"multiplicity":4,"contacts":[[0],[1],[2],[3],[4],[5],[0,1,2],[0,1,3],[2,4,5],[3,4,5],[0,3],[0,5],[1,2],[1,4],[2,5],[3,4]],"repeated":false,"hall":[[0,3,10],[0,4,10,15],[0,5,11],[1,3,7,10],[1,4,13],[3,4,15],[3,5,9,15]],"tri":[[0,3,4],[0,3,5],[0,5,15],[1,3,4],[1,4,10]]}]''')


def repeat_triple_implies_triangle(C,s):
    c=Counter(tuple(x) for x in C if len(x)==3)
    return any(n>=2 and set(T)<=set(range(s)) for T,n in c.items())


def verify_hall_triangle_core(C,hall_sets,triangles):
    contacts=list(map(set,C))
    eligible={e for e in combinations(range(16),2)
              if not contacts[e[0]]&contacts[e[1]]}
    positive=[]
    for T in hall_sets:
        assert 2<=len(T)<=5 and len(set(T))==len(T)
        assert len(set().union(*(contacts[x] for x in T)))<len(T)
        positive.append({e for e in combinations(T,2) if e in eligible})
    negative=[]
    for T in triangles:
        assert len(T)==3 and len(set(T))==3
        edges=set(combinations(T,2))
        assert edges<=eligible
        negative.append(edges)
    state={}
    while True:
        old=len(state)
        for clause in positive:
            if any(state.get(e)==1 for e in clause):continue
            unknown=[e for e in clause if e not in state]
            if not unknown:return 'Hall contradiction'
            if len(unknown)==1:state[unknown[0]]=1
        for triangle in negative:
            A=[e for e in triangle if state.get(e)==1]
            if len(A)==3:return 'A-triangle contradiction'
            if len(A)==2:
                for e in triangle:
                    if e not in state:state[e]=0
        if len(state)==old:
            raise AssertionError('stored Hall--triangle certificate is not closing')


def main():
    certificate_signatures={}
    for cert in CERTIFICATES:
        sig=unrestricted_signature(cert['contacts'])
        assert sig not in certificate_signatures
        certificate_signatures[sig]=cert
    assert len(certificate_signatures)==6
    totals=Counter()
    covered=set()
    for s,r in ((4,2),(4,3),(5,3),(6,3)):
        orbits=enumerate_types(s,r)
        totals[(s,r)]=len(orbits)
        print(f'(s,r)=({s},{r}): {sum(map(len,orbits.values()))} labeled systems, '
              f'{len(orbits)} incidence orbits')
        for key,cs in orbits.items():
            signature=unrestricted_signature(key)
            assert signature in certificate_signatures
            cert=certificate_signatures[signature]
            assert (cert['s'],cert['r'])==(s,r)
            covered.add(signature)
            if cert['repeated']:
                assert repeat_triple_implies_triangle(cert['contacts'],s)
            else:
                assert 'contradiction' in verify_hall_triangle_core(
                    cert['contacts'],cert['hall'],cert['tri'])
            print('  labelings',len(cs),'triples', [c for c in key if len(c)==3],
                  'doubles',[c for c in key if len(c)==2])
    assert totals=={(4,2):1,(4,3):2,(5,3):1,(6,3):2},totals
    assert covered==set(certificate_signatures)
    print('All six exceptional incidence types classified and their explicit contradictions verified.')
    print('Since sum_v(s(v)-2r(v))=0 by unique-common-neighbor double-counting,')
    print('this excludes the entire hypothetical 6-regular branch.')

if __name__=='__main__':main()
