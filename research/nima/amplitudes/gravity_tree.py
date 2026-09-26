"""Low-point pure-graviton trees: unordered BCFW and a separate KLT path.

Conventions: external helicities +/-2, all outgoing; strip overall -i and
(kappa/2)^(n-2). Three-point seeds are positive bracket-ratio squares.
For -P=(-lambda_P,tilde_P), spin-two crossing has no spin-one minus:
sewing uses +M_L M_R/P^2: (-i M_L)(i projector/P^2)(-i M_R)
= -i M_L M_R/P^2 in the transverse spin-two state sum.
KLT correspondingly uses -s AA at four points, +ss AA at five.

Physical inputs, not proved here: two-derivative Einstein three-point seeds,
vanishing large-z boundary (indeed 1/z^2) for admitted gravity shifts, and
KLT. The recursion sums ONLY helicity +/-2 internal states. Pure external
YM double-copy graviton trees agree with Einstein gravity; this is NOT a
claim that unprojected YM double copy gives pure Einstein gravity at loops.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations

from qed_fermion_scattering import C, ZERO, dot
import gluon_spinor_helicity as S
import gluon_bcfw as Kinematics


@dataclass(frozen=True)
class Channel:
    left_labels: tuple[int,...]
    right_labels: tuple[int,...]
    momentum: tuple[C,...]
    propagator: C
    shift_coefficient: C
    pole: C
    internal_spinors: S.Spinors
    internal_helicity_left: int
    left: Node
    right: Node
    contribution: C


@dataclass(frozen=True)
class Node:
    spinors: tuple[S.Spinors,...]
    helicities: tuple[int,...]
    value: C
    rule: str
    shift: tuple[int,int] | None = None
    channels: tuple[Channel,...] = ()
    failed_shifts: tuple[tuple[tuple[int,int],str],...] = ()


def validate(zs,hs):
    if len(zs) not in (3,4,5) or len(hs)!=len(zs) or any(h not in (-2,2) for h in hs):
        raise ValueError("Three to five legs with helicities +/-2 required")
    Kinematics.validate(zs,tuple(h//2 for h in hs))


def three_point(zs,hs):
    negative = [i for i,h in enumerate(hs) if h==-2]
    positive = [i for i,h in enumerate(hs) if h==2]
    if not negative or not positive:
        return ZERO
    angles = tuple(S.angle(zs[i],zs[(i+1)%3]) for i in range(3))
    squares = tuple(S.square(zs[i],zs[(i+1)%3]) for i in range(3))
    if all(x==ZERO for x in angles) and all(x==ZERO for x in squares):
        raise Kinematics.ExceptionalKinematics("Degenerate gravitational three-point branch")
    bracket,pair = (S.angle,negative) if len(negative)==2 else (S.square,positive)
    denominator = C.of(1)
    for i in range(3):
        denominator *= bracket(zs[i],zs[(i+1)%3])
    if denominator==ZERO:
        return ZERO
    b = bracket(zs[pair[0]],zs[pair[1]])
    fourth = b*b*b*b
    return fourth*fourth/(denominator*denominator)


def bcfw(spinors,helicities,shift=None):
    zs,hs = tuple(spinors),tuple(helicities)
    validate(zs,hs)
    if shift is not None:
        shift = tuple(shift)
        if len(shift)!=2 or shift[0]==shift[1] or any(i not in range(len(zs)) for i in shift):
            raise ValueError("Two distinct shift labels required")
        if (hs[shift[0]],hs[shift[1]])!=(-2,2):
            raise ValueError("This backend admits only (-2,+2) shifts")

    @lru_cache(None)
    def recurse(zs,hs,forced=None):
        validate(zs,hs)
        n = len(zs)
        if n==3:
            return Node(zs,hs,three_point(zs,hs),"einstein-three-point-seed")
        if len(set(hs))==1:
            return Node(zs,hs,ZERO,"same-helicity-zero")
        choices = (forced,) if forced is not None else tuple((i,j) for i in range(n) for j in range(n) if hs[i]==-2 and hs[j]==2)
        failures = []
        for i,j in choices:
            ps = Kinematics.momenta(zs)
            q = S.vector(S.outer(zs[i].lam,zs[j].tilde))
            remaining = tuple(k for k in range(n) if k not in (i,j))
            channels = []
            try:
                # Gravity is unordered: every subset separating the shifted
                # legs, not just contiguous color-ordered partitions.
                for size in range(1,n-2):
                    for subset in combinations(remaining,size):
                        left_labels = (i,)+subset
                        right_labels = tuple(k for k in remaining if k not in subset)+(j,)
                        p = Kinematics.total(tuple(ps[k] for k in left_labels))
                        denominator = C.of(dot(p,p))
                        coefficient = 2*C.of(dot(p,q))
                        if denominator==ZERO or coefficient==ZERO:
                            raise Kinematics.ExceptionalKinematics("Pole or zero shift coefficient in gravity chart")
                        pole = denominator/coefficient
                        shifted = list(zs)
                        shifted[i] = S.Spinors(zs[i].lam,tuple(a-pole*b for a,b in zip(zs[i].tilde,zs[j].tilde)))
                        shifted[j] = S.Spinors(tuple(a+pole*b for a,b in zip(zs[j].lam,zs[i].lam)),zs[j].tilde)
                        phat = Kinematics.total(Kinematics.momenta(tuple(shifted[k] for k in left_labels)))
                        if dot(phat,phat)!=ZERO:
                            raise ArithmeticError("Gravity cut is not null")
                        try:
                            internal = S.factor(phat)
                        except ValueError as exc:
                            raise Kinematics.ExceptionalKinematics(str(exc)) from exc
                        negative_internal = S.Spinors(tuple(-x for x in internal.lam),internal.tilde)
                        for h in (-2,2):
                            left = recurse(tuple(shifted[k] for k in left_labels)+(negative_internal,),tuple(hs[k] for k in left_labels)+(h,))
                            right = recurse((internal,)+tuple(shifted[k] for k in right_labels),(-h,)+tuple(hs[k] for k in right_labels))
                            value = left.value*right.value/denominator
                            channels.append(Channel(left_labels,right_labels,p,denominator,coefficient,pole,internal,h,left,right,value))
                return Node(zs,hs,sum((c.contribution for c in channels),ZERO),"unordered-bcfw",(i,j),tuple(channels),tuple(failures))
            except Kinematics.ExceptionalKinematics as exc:
                failures.append(((i,j),str(exc)))
        raise Kinematics.ExceptionalKinematics("All gravity shift charts exceptional: "+str(failures))

    return recurse(zs,hs,shift)


@dataclass(frozen=True)
class KLTTerm:
    kernel: C
    left_order: tuple[int,...]
    right_order: tuple[int,...]
    left_amplitude: C
    right_amplitude: C
    contribution: C
    left_history: tuple
    right_history: tuple


def klt(spinors,helicities,left_reference_offset=0,right_reference_offset=0):
    """Independent path: Yang-Mills off-shell Feynman amplitudes, not BCFW."""
    zs,hs = tuple(spinors),tuple(helicities)
    validate(zs,hs)
    if len(zs) not in (4,5):
        raise ValueError("KLT comparison implemented only at four/five points")
    ps = Kinematics.momenta(zs)
    refs_left = S.references_for(zs,left_reference_offset)
    refs_right = S.references_for(zs,right_reference_offset)
    left = tuple(S.polarization(z,r,h//2) for z,r,h in zip(zs,refs_left,hs))
    right = tuple(S.polarization(z,r,h//2) for z,r,h in zip(zs,refs_right,hs))
    return klt_tensor(ps,left,right)


def klt_tensor(ps,left_eps,right_eps):
    """Factorized tensor diagnostic; pure gravitons require aligned helicities.

    The wrapper above supplies those states. Replacing either vector factor
    by its momentum tests the inherited gravitational Ward identity.
    """
    import gluon_ordered_recursion as YM
    YM.validate(ps)
    if len(ps) not in (4,5):
        raise ValueError("KLT tensor supported only at four/five points")
    def s(i,j):
        return 2*C.of(dot(ps[i],ps[j]))
    if len(ps)==4:
        data = ((-s(0,1),(0,1,2,3),(0,1,3,2)),)
    else:
        data = ((s(0,1)*s(2,3),(0,1,2,3,4),(1,0,3,2,4)),
                (s(0,2)*s(1,3),(0,2,1,3,4),(2,0,3,1,4)))
    terms = []
    for kernel,left_order,right_order in data:
        left,left_history = YM.evaluate(ps,left_eps,left_order)
        right,right_history = YM.evaluate(ps,right_eps,right_order)
        terms.append(KLTTerm(kernel,left_order,right_order,left,right,kernel*left*right,left_history,right_history))
    return sum((t.contribution for t in terms),ZERO),tuple(terms)
