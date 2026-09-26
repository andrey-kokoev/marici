"""Exact color-ordered Yang-Mills BCFW recursion using only 3-point seeds.

Adjacent [i,j> shift: tilde_i -> tilde_i-z tilde_j; lambda_j -> lambda_j+z lambda_i.
For Yang-Mills trees, (-,+), (-,-), (+,+) are admitted; (+,-) is rejected.
The vanishing large-z boundary for these shifts is physical input, not proved
by this calculator. No off-shell recursion or n>=4 closed formula is called.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

from qed_fermion_scattering import C, ZERO, dot
import gluon_spinor_helicity as S


class ExceptionalKinematics(ValueError):
    pass


def momenta(zs):
    return tuple(S.vector(S.outer(z.lam,z.tilde)) for z in zs)


def total(ps):
    return tuple(sum((p[mu] for p in ps),ZERO) for mu in range(4))


def validate(zs,hs):
    if len(zs)<3 or len(zs)!=len(hs) or any(h not in (-1,1) for h in hs):
        raise ValueError("At least three legs with valid helicities required")
    ps = momenta(zs)
    if any(p==(ZERO,)*4 for p in ps):
        raise ExceptionalKinematics("Zero external momentum")
    if total(ps)!=(ZERO,)*4:
        raise ValueError("Spinor momenta do not conserve momentum")


def seed(zs,hs):
    negative = [i for i,h in enumerate(hs) if h==-1]
    positive = [i for i,h in enumerate(hs) if h==1]
    if not negative or not positive:
        return ZERO
    angles = tuple(S.angle(zs[i],zs[(i+1)%3]) for i in range(3))
    squares = tuple(S.square(zs[i],zs[(i+1)%3]) for i in range(3))
    if all(x==ZERO for x in angles) and all(x==ZERO for x in squares):
        raise ExceptionalKinematics("Degenerate three-point branch")
    bracket,pair,sign = (S.angle,negative,1) if len(negative)==2 else (S.square,positive,-1)
    denominator = C.of(1)
    for i in range(3):
        denominator *= bracket(zs[i],zs[(i+1)%3])
    if denominator==ZERO:
        return ZERO  # The opposite complex three-point branch.
    numerator = bracket(zs[pair[0]],zs[pair[1]])
    return sign*numerator*numerator*numerator*numerator/denominator


@dataclass(frozen=True)
class Channel:
    split: int
    momentum: tuple[C,...]
    propagator: C
    shift_coefficient: C
    pole: C | None
    internal_spinors: S.Spinors | None
    internal_helicity_left: int | None
    left: Node | None
    right: Node | None
    contribution: C
    status: str


@dataclass(frozen=True)
class Node:
    spinors: tuple[S.Spinors,...]
    helicities: tuple[int,...]
    value: C
    rule: str
    rotation: int | None = None
    shift_vector: tuple[C,...] | None = None
    channels: tuple[Channel,...] = ()
    failed_rotations: tuple[tuple[int,str],...] = ()


def evaluate(spinors,helicities,rotation=None):
    zs,hs = tuple(spinors),tuple(helicities)
    validate(zs,hs)
    if rotation is not None:
        if rotation not in range(len(zs)):
            raise ValueError("Invalid shift rotation")
        if (hs[rotation],hs[(rotation-1)%len(hs)])==(1,-1):
            raise ValueError("Bad (+,-) shift: boundary term not controlled")

    @lru_cache(None)
    def recurse(zs,hs,forced=None):
        validate(zs,hs)
        n = len(zs)
        if n==3:
            return Node(zs,hs,seed(zs,hs),"three-point-seed")
        if len(set(hs))==1:
            return Node(zs,hs,ZERO,"same-helicity-zero")
        choices = [forced] if forced is not None else [i for i in range(n) if (hs[i],hs[(i-1)%n])!=(1,-1)]
        if forced is None:
            choices.sort(key=lambda i: (hs[i],hs[(i-1)%n])!=(-1,1))
        failures = []
        for offset in choices:
            ordered = zs[offset:]+zs[:offset]
            helicities = hs[offset:]+hs[:offset]
            first,last = ordered[0],ordered[-1]
            q = S.vector(S.outer(first.lam,last.tilde))
            ps = momenta(ordered)
            channels = []
            try:
                for split in range(2,n-1):
                    p = total(ps[:split])
                    denominator = C.of(dot(p,p))
                    if denominator==ZERO:
                        raise ExceptionalKinematics("Unshifted factorization pole")
                    coefficient = 2*C.of(dot(p,q))
                    if coefficient==ZERO:
                        # Specialization can send a generic finite pole to
                        # infinity: the generic large-z argument need not be
                        # uniform on this locus. Never silently drop it.
                        raise ExceptionalKinematics("Zero shift coefficient: exceptional large-z chart")
                    pole = denominator/coefficient
                    shifted = list(ordered)
                    shifted[0] = S.Spinors(first.lam,tuple(a-pole*b for a,b in zip(first.tilde,last.tilde)))
                    shifted[-1] = S.Spinors(tuple(a+pole*b for a,b in zip(last.lam,first.lam)),last.tilde)
                    phat = total(momenta(shifted[:split]))
                    if dot(phat,phat)!=ZERO:
                        raise ArithmeticError("Shift failed to put internal momentum on shell")
                    try:
                        internal = S.factor(phat)
                    except ValueError as exc:
                        raise ExceptionalKinematics(str(exc)) from exc
                    # -P uses (-lambda_P,tilde_P), not an unspecified phase.
                    negative_internal = S.Spinors(tuple(-x for x in internal.lam),internal.tilde)
                    for h in (-1,1):
                        left = recurse(tuple(shifted[:split])+(negative_internal,),helicities[:split]+(h,))
                        right = recurse((internal,)+tuple(shifted[split:]),(-h,)+helicities[split:])
                        contribution = left.value*right.value/denominator
                        channels.append(Channel(split,p,denominator,coefficient,pole,internal,h,left,right,contribution,
                                                "sewn-residue"))
                return Node(zs,hs,sum((c.contribution for c in channels),ZERO),"bcfw",offset,q,tuple(channels),tuple(failures))
            except ExceptionalKinematics as exc:
                failures.append((offset,str(exc)))
        raise ExceptionalKinematics("All admitted shift charts exceptional: "+str(failures))

    return recurse(zs,hs,rotation)
