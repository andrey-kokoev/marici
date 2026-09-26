"""Heavy-loop matching for massless phi coupled to a distinct massive chi.

L_int=-lambda_phi phi^4/4! - g phi^2 chi^2/4, M_chi^2>0.
The external phi pole mass is tuned to zero. This module assumes the
subtraction; scalar_mass_renormalization_check.py audits it separately.
Only the heavy one-loop g^2 contribution is included; lambda_phi^2 light
loops and other coupling orders are NOT part of this result. There is no
massless internal line or t-channel massless pole in this selected sector.

M=-lambda_phi+g^2/(32 pi^2) sum B(s_i;M_chi^2,mu^2), s+t+u=0.
At zero momentum lambda_EFT=lambda_phi+3g^2/(32pi^2)log(M_chi^2/mu^2).
Derivative matching is independent of this local subtraction constant.
Rational Taylor coefficients are exact; loop values and spectral integrals
are floating point. Analytical remainder bounds are not certified intervals
for the floating-point full amplitude.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
import math

import scalar_one_loop as L


def validate(invariants,heavy_m2,mu2,g,light_quartic=0.0):
    if len(invariants)!=3 or not all(math.isfinite(x) for x in (g,light_quartic)):
        raise ValueError("Three invariants and finite couplings required")
    for x in invariants:
        L.validate(float(x),float(heavy_m2),float(mu2))
    if abs(sum(invariants))>1e-12*max(1.0,*(abs(x) for x in invariants)):
        raise ValueError("Massless external states require s+t+u=0, not 4M_chi^2")


def light_invariants(s,cosine):
    """Exact massless two-to-two invariants for rational inputs."""
    s,cosine = Q(s),Q(cosine)
    if s<0 or not -1<=cosine<=1:
        raise ValueError("Nonnegative energy squared and physical cosine required")
    return s,-s*(1-cosine)/2,-s*(1+cosine)/2


def series_coefficient(n):
    if not isinstance(n,int) or n<1:
        raise ValueError("Positive integer Taylor order required")
    return Q(math.factorial(n)**2,n*math.factorial(2*n+1))


@dataclass(frozen=True)
class Expansion:
    invariants: tuple[Q,...]
    heavy_mass_squared: Q
    order: int
    channel_coefficients: tuple[Q,...]
    invariant_terms: tuple[Q,...]
    dimensionless_sum: Q
    dimensionless_remainder_bound: Q


def expansion(invariants,heavy_m2,order):
    if len(invariants)!=3 or any(not isinstance(x,(int,Q)) for x in (*invariants,heavy_m2)):
        raise ValueError("Exact integer/Fraction matching inputs required")
    invariants,heavy_m2 = tuple(map(Q,invariants)),Q(heavy_m2)
    if heavy_m2<=0 or sum(invariants)!=0:
        raise ValueError("Positive heavy mass and exactly massless on-shell invariants required")
    series_coefficient(order)
    ratios = tuple(x/heavy_m2 for x in invariants)
    if any(abs(x)>=4 for x in ratios):
        raise ValueError("Taylor remainder domain requires |s_i|<4M_chi^2")
    coefficients = tuple(series_coefficient(n) for n in range(1,order+1))
    terms = tuple(c*sum(x**n for x in ratios) for n,c in enumerate(coefficients,1))
    # Integrate the geometric log-series tail using |x(1-x)|<=1/4:
    # |R_N| <= c_(N+1) |s/M^2|^(N+1)/(1-|s|/(4M^2)).
    bound = sum((series_coefficient(order+1)*abs(x)**(order+1)/(1-abs(x)/4) for x in ratios),Q(0))
    return Expansion(invariants,heavy_m2,order,coefficients,terms,sum(terms,Q(0)),bound)


@dataclass(frozen=True)
class HeavyAmplitude:
    invariants: tuple[float,...]
    heavy_mass_squared: float
    scale_squared: float
    portal_coupling: float
    light_quartic: float
    bubbles: tuple[complex,...]
    heavy_loop: complex
    tree_plus_heavy_loop: complex
    matched_quartic: float
    derivative_remainder: complex


def heavy_amplitude(invariants,heavy_m2=1.0,mu2=1.0,g=0.7,light_quartic=0.1):
    invariants = tuple(float(x) for x in invariants)
    validate(invariants,heavy_m2,mu2,g,light_quartic)
    prefactor = g*g/(32*math.pi**2)
    bubbles = tuple(L.bubble_closed(x,heavy_m2,mu2) for x in invariants)
    zero = L.bubble_closed(0.0,heavy_m2,mu2)
    heavy = prefactor*sum(bubbles)
    matched = light_quartic-3*prefactor*zero.real
    remainder = prefactor*sum(b-zero for b in bubbles)
    return HeavyAmplitude(invariants,heavy_m2,mu2,g,light_quartic,bubbles,heavy,-light_quartic+heavy,matched,remainder)


def dimension_eight_operator(heavy_m2,g):
    """c in L_EFT += c (partial_mu phi partial^mu phi)^2.

    Its 24 derivative assignments give M=2c(s^2+t^2+u^2), hence
    c=g^2/(3840 pi^2 M_chi^4), in this portal-vertex normalization.
    """
    validate((0,0,0),heavy_m2,1.0,g)
    return g*g/(3840*math.pi**2*heavy_m2**2)


def forward_spectral_coefficient(heavy_m2,g,tolerance=1e-13):
    """Coefficient of s^2 in the heavy forward amplitude, from its cut.

    a2=(2/pi) integral Im M(t)/t^3 dt. Both right and crossed left cuts
    are included. With v=sqrt(1-4M^2/t), dt/t^3=v(1-v^2)/(8M^4)dv.
    The absorptive part is obtained from on-shell chi-chi phase space and
    the tree process phi phi -> chi chi, M_tree=-g, not from bubble_closed.
    """
    validate((0,0,0),heavy_m2,1.0,g)
    def integrand(v):
        if v==0 or v==1:
            return 0.0
        invariant = 4*heavy_m2/(1-v*v)
        twice_imaginary = L.optical_cut(invariant,heavy_m2,g)
        return twice_imaginary*v*(1-v*v)/(8*math.pi*heavy_m2**2)
    return L.integrate(integrand,tolerance=tolerance)
