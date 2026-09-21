"""Exact scalar bounds and typed top-jet probes for marked summability.

Forcing norms enter as arbitrary positive scalars; these tests are not spectral
samples. Existence of small late-window forcing norms uses the H_beta tail
argument in the companion note.
"""
from fractions import Fraction
from math import comb, factorial
from itertools import permutations, product
from pathlib import Path
import json


def choose(n,k):return comb(n,k) if 0<=k<=n else 0


bounds=0
for ratio in (Fraction(1,2),Fraction(1),Fraction(2),Fraction(3)):
    lam=max(Fraction(1),ratio)
    for s in range(1,5):
        t=2*lam*s
        for n in range(13):
            for d in range(n+1):
                total=Fraction(0)
                for k in range(n+1):
                    # Divide out the common product of retained seam norms.
                    coefficient=sum((choose(d,i)*choose(n-d,k-i)*ratio**(d-i)
                                     for i in range(d+1)),Fraction(0))
                    total+=t**k*factorial(k)*coefficient
                top=t**n*factorial(n)
                assert top<=total<=2*top
                bounds+=1


def top_key(word,start=0):
    edges=[]
    for event,mark in word:
        finish=start|(1<<event)
        edges.append((start,finish,mark));start=finish
    return tuple(edges)


probes=0
for n in range(1,6):
    seen=set()
    for order in permutations(range(n)):
        for marks in product((0,1),repeat=n):
            key=top_key(tuple(zip(order,marks)))
            assert key not in seen
            seen.add(key);probes+=1
    assert len(seen)==factorial(n)*2**n

# A conservative contractive-projection bound needs only the 2^n possible
# mark patterns per ordered edge route. The Hilbert special case is stronger.
projection_checks=0
for n in range(1,11):
    coeff=[Fraction((-1)**j*(j%5+1),2**(j%n+1)) for j in range(2**n)]
    assert sum(abs(c) for c in coeff)**2 <= 2**n*sum(c*c for c in coeff)
    # Graph scale s=R pays the cruder factor 2^n since lambda>=1.
    for R in range(1,5):
        assert factorial(n)*R**n*2**n <= factorial(n)*(2*R)**n
        projection_checks+=1


def marked_relation(n):
    suffix=tuple((p,1) for p in range(2,n))
    return {((0,1),(1,0))+suffix:1,
            ((0,0),(1,1))+suffix:1,
            ((1,1),(0,0))+suffix:-1,
            ((1,0),(0,1))+suffix:-1}


witness_checks=0
for n in range(2,33):
    a=marked_relation(n)
    assert len({top_key(w) for w in a})==4
    assert all(sum(mark for _,mark in w)==n-1 for w in a)
    coefficient=Fraction(1,4*factorial(n))
    path_mass=sum(abs(c)*coefficient for c in a.values())
    assert path_mass==Fraction(1,factorial(n))
    eps=Fraction(1,2**n)
    for R in (1,2,4,8):
        raw=factorial(n)*R**n*path_mass
        weighted=raw*eps**(n-1)
        assert raw==R**n
        assert weighted==Fraction(R**n,2**(n*(n-1)))
        next_term=Fraction(R**(n+1),2**(n*(n+1)))
        assert next_term/weighted==Fraction(R,4**n)
        if n>=R:assert next_term<=weighted/2
        witness_checks+=1

result={'schema':'marici.grothendieck.marked-fox-summability-domain.v1','passed':True,
        'exact_full_jet_majorants':bounds,'distinct_typed_top_jet_probes':probes,
        'projection_radius_checks':projection_checks,'late_marked_relation_bounds':witness_checks,
        'scope':'Exact combinatorial and norm-majorant fixtures. The maximal weighted source domain and actual late-forcing witness follow from the proofs and H_beta tail estimate in the companion note.'}
root=Path(__file__).resolve().parents[3]
out=root/'research/grothendieck/results/marked-fox-summability-domain.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
