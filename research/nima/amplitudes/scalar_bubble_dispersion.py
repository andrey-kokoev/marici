"""Causal above-threshold bubble dispersion with an explicit principal value.

Input spectral density: Im B(t+i0)=pi sqrt(1-4m^2/t). One subtraction
B(0)=-log(m^2/mu^2) is a renormalization input, NOT determined by the cut.
With t=4m^2/(1-v^2), the dispersive integrand is
2s v^2/(4m^2-s+s v^2). Above threshold its pole is b=sqrt(1-4m^2/s):

  2v^2/(v^2-b^2) = b/(v-b) + (2v+b)/(v+b).

Integrate the smooth term numerically and retain
PV integral b/(v-b)=b log((1-b)/b). The causal boundary contribution is
+/- i pi b. No finite numerical i0 is used for the real-axis result.
Off-axis tests evaluate genuinely complex invariants separately.
All numerical estimates below are non-certified floating-point quantities.
"""
from __future__ import annotations

from dataclasses import dataclass
import cmath
import math

import scalar_one_loop as L


def pole(s,m2,mu2,rim=1):
    L.validate(s,m2,mu2,rim)
    if s<=4*m2:
        raise ValueError("Strictly above-threshold invariant required")
    b = math.sqrt(1-4*m2/s)
    if not 0<b<1:
        raise ValueError("Pole merged with endpoint at available precision")
    return b


@dataclass(frozen=True)
class PrincipalValue:
    invariant: float
    mass_squared: float
    scale_squared: float
    rim: int
    pole: float
    pole_residue: float
    subtraction_constant: float
    logarithmic_boundary_term: float
    smooth_integral: L.Integral
    value: complex


def above(s,m2=1.0,mu2=1.0,rim=1,tolerance=1e-11):
    b = pole(s,m2,mu2,rim)
    q = L.integrate(lambda v:(2*v+b)/(v+b),tolerance=tolerance)
    boundary = b*(math.log1p(-b)-math.log(b))
    subtraction = -math.log(m2/mu2)
    value = complex(subtraction+q.value.real+boundary,rim*math.pi*b)
    return PrincipalValue(s,m2,mu2,rim,b,b,subtraction,boundary,q,value)


@dataclass(frozen=True)
class Excision:
    invariant: float
    mass_squared: float
    scale_squared: float
    pole: float
    half_width: float
    lower_integral: L.Integral
    upper_integral: L.Integral
    missing_smooth_window: L.Integral
    truncated_real_value: float
    corrected_principal_value: float


def symmetric_excision(s,half_width,m2=1.0,mu2=1.0,tolerance=1e-11):
    """Integrate the original spectral integrand outside a symmetric window.

    The singular b/(v-b) contribution cancels inside that symmetric window.
    Adding the missing smooth integral restores the PV without extrapolation.
    The uncorrected integral is retained for a separate convergence test.
    """
    b = pole(s,m2,mu2)
    if not math.isfinite(half_width) or not 0<half_width<min(b,1-b):
        raise ValueError("Excision must fit strictly inside both pole endpoints")
    f = lambda v:2*v*v/((v-b)*(v+b))
    lower = L.integrate(f,0,b-half_width,tolerance=tolerance/3)
    upper = L.integrate(f,b+half_width,1,tolerance=tolerance/3)
    window = L.integrate(lambda v:(2*v+b)/(v+b),b-half_width,b+half_width,tolerance=tolerance/3)
    truncated = -math.log(m2/mu2)+lower.value.real+upper.value.real
    return Excision(s,m2,mu2,b,half_width,lower,upper,window,truncated,truncated+window.value.real)


@dataclass(frozen=True)
class OffAxis:
    invariant: complex
    mass_squared: float
    scale_squared: float
    representation: str
    integral: L.Integral
    value: complex


def validate_off_axis(z,m2,mu2):
    z = complex(z)
    L.validate(z.real,m2,mu2)
    if not math.isfinite(z.imag) or z.imag==0:
        raise ValueError("Finite non-real invariant required; use explicit rim/PV on the cut")
    return z


def off_axis_dispersion(z,m2=1.0,mu2=1.0,tolerance=1e-11):
    z = validate_off_axis(z,m2,mu2)
    q = L.integrate(lambda v:2*z*v*v/(4*m2-z+z*v*v),tolerance=tolerance)
    return OffAxis(z,m2,mu2,"once-subtracted spectral integral",q,-math.log(m2/mu2)+q.value)


def off_axis_parameter(z,m2=1.0,mu2=1.0,tolerance=1e-11):
    z = validate_off_axis(z,m2,mu2)
    q = L.integrate(lambda x:-cmath.log((m2-z*x*(1-x))/mu2),tolerance=tolerance)
    return OffAxis(z,m2,mu2,"complex logarithmic parameter integral",q,q.value)
