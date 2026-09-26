"""Exact simple-pole coefficients of ordered Feynman trees.

The 'without_cut' component discards diagrams containing a marked edge. It
is NOT the Laurent finite part (numerator derivatives are not included).
The coefficient component retains exactly one marked propagator. Marks
must be mutually incompatible tree channels, so no diagram has two marks.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations

from qed_fermion_scattering import C, ZERO, dot
import gluon_spinor_helicity as S
import gluon_ordered_recursion as R
import yang_mills_four as YM


@dataclass(frozen=True)
class Term:
    vertex: str
    children: tuple[Current,...]
    without_cut: tuple[C,...]
    coefficient: tuple[C,...]


@dataclass(frozen=True)
class Current:
    leaves: tuple[int,...]
    momentum: tuple[C,...]
    denominator: C | None
    marked_weight: C | None
    without_cut: tuple[C,...]
    coefficient: tuple[C,...]
    terms: tuple[Term,...]


@dataclass(frozen=True)
class Result:
    order: tuple[int,...]
    marks: tuple[tuple[tuple[int,...],C],...]
    value: C
    root_terms: tuple[Term,...]


def coefficient(ps,eps,weighted_marks,order=None):
    """Low-level coefficient at an on-shell pole configuration.

    Zero external momenta are permitted here ONLY as formal boundary data;
    use residue() for physical nonzero external states, or positive_soft()
    for the validated affine soft family. Weight=1 extracts P_cut^2 A;
    weight=1/(d P_cut^2/d tau) extracts the 1/tau propagator coefficient.
    """
    n = len(ps)
    order = tuple(range(n)) if order is None else tuple(order)
    if n<4 or sorted(order)!=list(range(n)) or len(eps)!=n or any(len(p)!=4 for p in (*ps,*eps)):
        raise ValueError("Valid momenta, polarizations and ordering required")
    if R.vadd(ps)!=R.ZERO_VECTOR or any(C.of(dot(p,p))!=ZERO for p in ps):
        raise ValueError("Null conserved boundary momenta required")
    marks = {}
    for labels,weight in weighted_marks:
        marked = frozenset(labels)
        if len(marked)!=len(labels) or not marked<=set(order) or not 2<=len(marked)<=n-2:
            raise ValueError("Proper internal channel required")
        if order[-1] in marked:
            marked = frozenset(order)-marked
        positions = sorted(order.index(i) for i in marked)
        if positions!=list(range(positions[0],positions[-1]+1)):
            raise ValueError("Marked channel is not planar contiguous")
        if marked in marks:
            raise ValueError("Duplicate marked channel")
        if dot(R.vadd(ps[i] for i in marked),R.vadd(ps[i] for i in marked))!=ZERO:
            raise ValueError("Marked propagator is not on its pole")
        marks[marked] = C.of(weight)
    if not marks:
        raise ValueError("At least one marked pole required")
    for a,b in combinations(marks,2):
        if a<=b or b<=a or a.isdisjoint(b):
            raise ValueError("Compatible marks can produce higher-order poles")

    def assemble(labels):
        terms = []
        for arity in (2,3):
            for blocks in R.partition_contiguous(labels,arity):
                children = tuple(current(block) for block in blocks)
                def vertex(values):
                    if arity==2:
                        return tuple(C.of(x) for x in YM.cubic_current(
                            children[0].momentum,children[1].momentum,*values))
                    return R.quartic(*values)
                values = tuple(c.without_cut for c in children)
                ordinary = vertex(values)
                pole = R.vadd(vertex(values[:i]+(child.coefficient,)+values[i+1:])
                              for i,child in enumerate(children))
                terms.append(Term("cubic" if arity==2 else "quartic",children,ordinary,pole))
        return tuple(terms)

    @lru_cache(None)
    def current(labels):
        p = R.vadd(ps[i] for i in labels)
        if len(labels)==1:
            return Current(labels,p,None,None,tuple(C.of(x) for x in eps[labels[0]]),R.ZERO_VECTOR,())
        denominator = C.of(dot(p,p))
        terms = assemble(labels)
        ordinary = R.vadd(t.without_cut for t in terms)
        pole = R.vadd(t.coefficient for t in terms)
        weight = marks.get(frozenset(labels))
        if weight is not None:
            if pole!=R.ZERO_VECTOR:
                raise ArithmeticError("Nested marked pole encountered")
            return Current(labels,p,denominator,weight,R.ZERO_VECTOR,tuple(weight*x for x in ordinary),terms)
        if denominator==ZERO:
            raise ValueError("Unmarked coincident propagator pole")
        return Current(labels,p,denominator,None,tuple(x/denominator for x in ordinary),
                       tuple(x/denominator for x in pole),terms)

    terms = assemble(order[:-1])
    value = C.of(dot(R.vadd(t.coefficient for t in terms),eps[order[-1]]))/(2**(n-1))
    return Result(order,tuple((tuple(sorted(k)),v) for k,v in marks.items()),value,terms)


def residue(ps,eps,channel,order=None):
    R.validate(ps)
    return coefficient(ps,eps,((tuple(channel),C.of(1)),),order)


def vector(z):
    return S.vector(S.outer(z.lam,z.tilde))


def soft_spinors(zs,soft,tau,helicity=1):
    """Conserving chiral soft family, with original point at tau=1.

    Positive helicity scales lambda; negative helicity scales tilde. Swapping
    the spinor spaces here constructs momenta only, not an amplitude parity
    assumption. The negative coefficient is evaluated with its own tensors.
    """
    if helicity not in (-1,1):
        raise ValueError("Valid soft helicity required")
    if helicity==-1:
        swapped = tuple(S.Spinors(z.tilde,z.lam) for z in zs)
        return tuple(S.Spinors(z.tilde,z.lam) for z in soft_spinors(swapped,soft,tau))
    n = len(zs)
    if n<5 or soft not in range(n):
        raise ValueError("At least five legs and a valid soft label required")
    a,b = (soft-1)%n,(soft+1)%n
    denominator = S.angle(zs[a],zs[b])
    if denominator==ZERO:
        raise ValueError("Degenerate adjacent soft basis")
    alpha,beta = S.angle(zs[soft],zs[b])/denominator,S.angle(zs[a],zs[soft])/denominator
    result = list(zs)
    result[soft] = S.Spinors(tuple(tau*x for x in zs[soft].lam),zs[soft].tilde)
    for index,weight in ((a,alpha),(b,beta)):
        result[index] = S.Spinors(zs[index].lam,tuple(x+(1-tau)*weight*y
                            for x,y in zip(zs[index].tilde,zs[soft].tilde)))
    return tuple(result)


@dataclass(frozen=True)
class SoftResult:
    soft_label: int
    helicities: tuple[int,...]
    original_spinors: tuple[S.Spinors,...]
    boundary_spinors: tuple[S.Spinors,...]
    momenta_zero: tuple[tuple[C,...],...]
    momenta_slope: tuple[tuple[C,...],...]
    reference_spinors: tuple[S.Spinors,...]
    leading_polarizations: tuple[tuple[C,...],...]
    propagator_slopes: tuple[C,...]
    soft_factor: C
    coefficient: Result


def positive_soft(zs,hs,soft,reference_offset=0):
    return _leading_soft(zs,hs,soft,reference_offset,1)


def negative_soft(zs,hs,soft,reference_offset=0):
    return _leading_soft(zs,hs,soft,reference_offset,-1)


def _leading_soft(zs,hs,soft,reference_offset,helicity):
    """Coefficient of tau^-2, NOT the value at a zero-momentum external leg.

    The selected chiral soft polarization is epsilon_s(1)/tau; hard polarizations
    are regular at tau=0. Each tree contains at most one of the two adjacent
    soft-channel poles. Thus only boundary numerators and linear propagator
    slopes enter the leading coefficient; no numerical limit is taken.
    """
    zs,hs = tuple(zs),tuple(hs)
    if len(zs)!=len(hs) or any(h not in (-1,1) for h in hs) or soft not in range(len(zs)) or hs[soft]!=helicity:
        name = "Positive" if helicity==1 else "Negative"
        raise ValueError(name+" soft helicity and valid labels required")
    R.validate(tuple(vector(z) for z in zs))
    boundary = soft_spinors(zs,soft,C.of(0),helicity)
    ps0 = tuple(vector(z) for z in boundary)
    ps1 = tuple(tuple(x-y for x,y in zip(vector(z),p)) for z,p in zip(zs,ps0))
    if R.vadd(ps0)!=R.ZERO_VECTOR or R.vadd(ps1)!=R.ZERO_VECTOR:
        raise ArithmeticError("Soft family does not conserve momentum")
    for i,(p,d) in enumerate(zip(ps0,ps1)):
        if dot(p,p)!=ZERO or dot(p,d)!=ZERO or dot(d,d)!=ZERO:
            raise ArithmeticError("Soft family is not identically null")
        if i!=soft and p==R.ZERO_VECTOR:
            raise ValueError("Additional soft external leg")
    polarization_spinors = tuple(zs[i] if i==soft else boundary[i] for i in range(len(zs)))
    refs = S.references_for(polarization_spinors,reference_offset)
    eps = tuple(S.polarization(z,r,h) for z,r,h in zip(polarization_spinors,refs,hs))
    a,b = (soft-1)%len(zs),(soft+1)%len(zs)
    channels = ((a,soft),(soft,b))
    slopes = tuple(2*C.of(dot(R.vadd(ps0[i] for i in labels),R.vadd(ps1[i] for i in labels)))
                   for labels in channels)
    if any(d==ZERO for d in slopes):
        raise ValueError("Higher-order soft propagator zero")
    result = coefficient(ps0,eps,tuple((labels,C.of(1)/d) for labels,d in zip(channels,slopes)))
    bracket = S.angle if helicity==1 else S.square
    # Reverse-determinant square convention: anti-MHV carries (-1)^n,
    # hence the negative soft factor has an additional minus sign.
    factor = helicity*bracket(zs[a],zs[b])/(bracket(zs[a],zs[soft])*bracket(zs[soft],zs[b]))
    return SoftResult(soft,hs,zs,boundary,ps0,ps1,refs,eps,slopes,factor,result)
