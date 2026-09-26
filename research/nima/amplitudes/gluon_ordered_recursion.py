"""Coupling/i-stripped ordered gluon tree recursion with full current records.

Integer-normalized cubic/quartic tensors and polarizations omitting sqrt(2)
keep all arithmetic rational-complex. The net ordered normalization is
1/2^(n-1): 1/sqrt(2) per cubic vertex, 1/2 per quartic vertex, and
1/sqrt(2) per external polarization; V3+2 V4=n-2.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations

from qed_fermion_scattering import C, ZERO, dot
import gluon_spinor_helicity as S
import yang_mills_four as YM


ZERO_VECTOR = (ZERO,)*4


def vadd(vectors):
    vectors = tuple(vectors)
    return tuple(sum((v[i] for v in vectors), ZERO) for i in range(4))


def partition_contiguous(labels, count):
    for cuts in combinations(range(1,len(labels)),count-1):
        bounds = (0,)+cuts+(len(labels),)
        yield tuple(labels[a:b] for a,b in zip(bounds,bounds[1:]))


def quartic(a,b,c):
    return tuple(2*y*dot(a,c)-x*dot(b,c)-z*dot(a,b) for x,y,z in zip(a,b,c))


@dataclass(frozen=True)
class Term:
    vertex: str
    children: tuple[Current,...]
    numerator: tuple[C,...]


@dataclass(frozen=True)
class Current:
    leaves: tuple[int,...]
    momentum: tuple[C,...]
    denominator: C | None
    terms: tuple[Term,...]
    value: tuple[C,...]


def validate(ps):
    if len(ps) < 3 or any(len(p) != 4 or all(C.of(x)==ZERO for x in p) or C.of(dot(p,p)) != ZERO for p in ps):
        raise ValueError("Nonzero null external four-momenta required")
    if vadd(ps) != ZERO_VECTOR:
        raise ValueError("External momenta do not conserve momentum")


def evaluate(ps, polarizations, order=None):
    validate(ps)
    n = len(ps)
    order = tuple(range(n)) if order is None else tuple(order)
    if sorted(order) != list(range(n)) or len(polarizations) != n or any(len(e)!=4 for e in polarizations):
        raise ValueError("One polarization per leg and a valid cyclic order required")

    def assemble(labels):
        terms = []
        for blocks in partition_contiguous(labels,2):
            a,b = (current(block) for block in blocks)
            numerator = tuple(C.of(x) for x in YM.cubic_current(a.momentum,b.momentum,a.value,b.value))
            terms.append(Term("cubic",(a,b),numerator))
        for blocks in partition_contiguous(labels,3):
            a,b,c = (current(block) for block in blocks)
            terms.append(Term("quartic",(a,b,c),quartic(a.value,b.value,c.value)))
        return tuple(terms)

    @lru_cache(None)
    def current(labels):
        momentum = vadd(ps[i] for i in labels)
        if len(labels)==1:
            return Current(labels,momentum,None,(),tuple(C.of(x) for x in polarizations[labels[0]]))
        denominator = C.of(dot(momentum,momentum))
        if denominator==ZERO:
            raise ValueError("Internal ordered propagator pole")
        terms = assemble(labels)
        numerator = vadd(t.numerator for t in terms)
        return Current(labels,momentum,denominator,terms,tuple(x/denominator for x in numerator))

    # The last external leg closes the ordered current; never divide by its
    # on-shell momentum squared. Its polarization is included before /2^(n-1).
    root_terms = assemble(order[:-1])
    amputated = C.of(dot(vadd(t.numerator for t in root_terms),polarizations[order[-1]]))
    return amputated/(2**(n-1)), root_terms


def helicity(ps, helicities, order=None, references=None):
    if len(helicities)!=len(ps) or any(h not in (-1,1) for h in helicities):
        raise ValueError("One +/-1 helicity per leg required")
    spinors = tuple(S.factor(p) for p in ps)
    references = S.references_for(spinors) if references is None else references
    if len(references)!=len(ps):
        raise ValueError("One reference spinor per leg required")
    eps = tuple(S.polarization(z,r,h) for z,r,h in zip(spinors,references,helicities))
    return evaluate(ps,eps,order)
