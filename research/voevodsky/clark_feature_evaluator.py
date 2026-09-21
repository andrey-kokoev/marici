"""Finite numerical evaluator for the declared four Clark tails.

The forcing is injected explicitly: this module never guesses the completed
source Phi. It is therefore suitable for the eventual analytic comparison
once that source is provided.
"""
from __future__ import annotations
import cmath
from dataclasses import dataclass
from typing import Callable, Sequence
import mpmath as mp

Phi=Callable[[float],complex]

def phi_one(u: float, n: int=1) -> float:
    """Completed-theta atom Phi_n from the Grothendieck attachment note."""
    import math
    a=math.pi*n*n; x=math.exp(2*u)
    return math.exp(u/2)*(2*a*a*x*x-3*a*x)*math.exp(-a*x)

def phi_completed(u: float, terms: int=64) -> float:
    """Finite absolutely convergent evaluator for Phi=sum_{n>=1} Phi_n.

    `terms` is an explicit source cutoff; increasing it gives the generic
    completed source on compact u-windows. No unproved interchange is hidden.
    """
    return sum(phi_one(u,n) for n in range(1,terms+1))
@dataclass(frozen=True)
class Shell:
    left: float
    right: float

def phi_one_pair_shell(n: int, m: int, left: float, right: float, separation: float):
    """Exact incomplete-gamma correlation for the recorded atoms Phi_n,Phi_m."""
    A=mp.pi*n*n; C=mp.pi*m*m*mp.exp(2*separation); lam=A+C
    lo=mp.exp(2*left); hi=mp.exp(2*right)
    def delta(s): return mp.gammainc(s,lam*lo,lam*hi)
    return mp.exp(separation/2)/2*(
        4*A*A*C*C/lam**(mp.mpf(9)/2)*delta(mp.mpf(9)/2)
        -6*A*C/lam**(mp.mpf(5)/2)*delta(mp.mpf(7)/2)
        +9*A*C/lam**(mp.mpf(5)/2)*delta(mp.mpf(5)/2))

def event_intervals(start: int, word):
    """Return exact arithmetic windows for a route, preserving event order."""
    x=start
    for p in word:
        y=x*p
        yield (x,y)
        x=y

@dataclass
class ClarkFeatureEvaluator:
    shells: Sequence[Shell]
    forcing: Phi
    quadrature: int=512

    def interval_feature(self, left: float, right: float, z: complex):
        """Return (+,0),(-,0),(+,1),(-,1) traces for one shell interval.

        Composite midpoint quadrature is deliberately exposed as a numerical
        adapter; analytic kernel certification must replace it by the declared
        holomorphic integral comparison.
        """
        n=self.quadrature
        h=(right-left)/n
        out=[]
        # Canonical Clark order is (+,0),(-,0),(+,1),(-,1).
        for j in (0,1):
            for sigma in (1,-1):
                total=0j
                for k in range(n):
                    t=left+(k+.5)*h
                    total += cmath.exp(sigma*1j*z*t)*(t**j)*self.forcing(t)*h
                out.append(total)
        return tuple(out)

    def shell_features(self, intervals, z):
        """Evaluate each interval separately, preserving event attachments."""
        return [self.interval_feature(left,right,z) for left,right in intervals]

    def event_feature(self, intervals, z):
        v=[0j]*4
        for left,right in intervals:
            w=self.interval_feature(left,right,z)
            v=[a+b for a,b in zip(v,w)]
        return tuple(v)

    def divided_difference(self, u, v, w, z, C):
        hu=self.event_feature(u,w); hv=self.event_feature(v,z)
        numerator=sum(hu[i].conjugate()*C[i][j]*hv[j]
                      for i in range(4) for j in range(4))
        return numerator/(-1j*(z-w.conjugate()))
