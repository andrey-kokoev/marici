"""Massive real phi^4 one-loop four-point amplitude (numerical benchmark).

L = (d phi)^2/2 - m^2 phi^2/2 - lambda phi^4/4!, S=1+iT.
M_tree=-lambda. In d=4-2 epsilon with unmodified DR measure,
Delta=1/epsilon-gamma_E+log(4 pi). Each bubble has symmetry factor 1/2:
M_loop=lambda^2/(32 pi^2) sum_{s,t,u}(Delta+B).
MSbar delta_lambda=3 lambda^2 Delta/(32 pi^2) cancels the four-point pole.
Use the pole mass m>0: the momentum-independent one-loop tadpole is absorbed
in its mass counterterm, and its LSZ derivative vanishes. Tadpoles are not
independently evaluated here; see scalar_mass_renormalization_check.py for
that separate audit. No massless/IR, higher-loop, or resummed claim.

B(s)=-integral_0^1 log((m^2-s x(1-x)-i0)/mu^2) dx.
'rim=+1' means s+i0; rim=-1 is its Schwarz-reflected lower boundary value,
NOT an implementation of a second Riemann sheet. All transcendental
calculations are floating point. Simpson error estimates are not rigorous
interval bounds or formal certificates.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Panel:
    low: float
    high: float
    value: complex
    estimated_error: float


@dataclass(frozen=True)
class Integral:
    value: complex
    estimated_error: float
    evaluations: int
    panels: tuple[Panel,...]


def integrate(function,low=0.0,high=1.0,tolerance=1e-11,max_depth=28):
    if not (math.isfinite(tolerance) and tolerance>0 and math.isfinite(low) and math.isfinite(high)
            and high>low and isinstance(max_depth,int) and max_depth>=0):
        raise ValueError("Positive quadrature tolerance and interval required")
    evaluations = 0
    panels = []
    def evaluate(x):
        nonlocal evaluations
        evaluations += 1
        y = complex(function(x))
        if not (math.isfinite(y.real) and math.isfinite(y.imag)):
            raise ArithmeticError("Nonfinite quadrature integrand")
        return y
    def recurse(a,b,fa,fm,fb,whole,budget,depth):
        mid = (a+b)/2
        fl,fr = evaluate((a+mid)/2),evaluate((mid+b)/2)
        left = (mid-a)*(fa+4*fl+fm)/6
        right = (b-mid)*(fm+4*fr+fb)/6
        delta = left+right-whole
        error = abs(delta)/15
        if error<=budget:
            value = left+right+delta/15
            panels.append(Panel(a,b,value,error))
            return value,error
        if depth==0:
            raise ArithmeticError("Quadrature depth exhausted; no unverified result returned")
        x,e1 = recurse(a,mid,fa,fl,fm,left,budget/2,depth-1)
        y,e2 = recurse(mid,b,fm,fr,fb,right,budget/2,depth-1)
        return x+y,e1+e2
    a,b = float(low),float(high)
    fa,fm,fb = evaluate(a),evaluate((a+b)/2),evaluate(b)
    value,error = recurse(a,b,fa,fm,fb,(b-a)*(fa+4*fm+fb)/6,tolerance,max_depth)
    return Integral(value,error,evaluations,tuple(panels))


def validate(s,m2,mu2,rim=1):
    if not all(math.isfinite(x) for x in (s,m2,mu2)) or m2<=0 or mu2<=0 or rim not in (-1,1):
        raise ValueError("Finite real invariant, positive mass/scale squared and rim +/-1 required")


def bubble_closed(s,m2=1.0,mu2=1.0,rim=1):
    validate(s,m2,mu2,rim)
    constant = -math.log(m2/mu2)
    if s==0:
        return complex(constant)
    if s<0:
        beta = math.sqrt(1-4*m2/s)
        return complex(constant+2-2*beta*math.atanh(1/beta))
    if s<4*m2:
        r = math.sqrt(4*m2/s-1)
        return complex(constant+2-2*r*math.atan(1/r))
    if s==4*m2:
        return complex(constant+2)
    beta = math.sqrt(1-4*m2/s)
    logarithm = math.log(s/m2)+2*math.log1p(beta)-math.log(4)
    return complex(constant+2-beta*logarithm,rim*math.pi*beta)


@dataclass(frozen=True)
class ParameterIntegral:
    invariant: float
    mass_squared: float
    scale_squared: float
    rim: int
    value: complex
    estimated_error: float
    intervals: tuple[tuple[float,float],...]
    quadratures: tuple[Integral,...]


def bubble_parameter(s,m2=1.0,mu2=1.0,rim=1,tolerance=1e-11):
    """Direct logarithmic parameter integration; no closed bubble call.

    At/above threshold split at both real roots. On each piece use
    x=lo+(hi-lo)*t^4/(t^4+(1-t)^4). Endpoint Jacobians suppress integrable
    logarithms; distances to endpoint roots are evaluated without subtraction.
    """
    validate(s,m2,mu2,rim)
    if s<4*m2:
        def f(x):
            d = m2-s*x*(1-x) if s<0 else m2-s/4+s*(x-0.5)**2
            return -math.log(d/mu2)
        q = integrate(f,tolerance=tolerance)
        return ParameterIntegral(s,m2,mu2,rim,q.value,q.estimated_error,((0.0,1.0),),(q,))
    beta = math.sqrt(1-4*m2/s)
    roots = ((1-beta)/2,(1+beta)/2)
    endpoints = sorted(set((0.0,*roots,1.0)))
    intervals = tuple(zip(endpoints,endpoints[1:]))
    quadratures = []
    for lo,hi in intervals:
        width = hi-lo
        def transformed(t):
            if t==0 or t==1:
                return 0j
            a,b = t**4,(1-t)**4
            f,g = a/(a+b),b/(a+b)
            jacobian = width*4*t**3*(1-t)**3/(a+b)**2
            distances = tuple(width*f if root==lo else -width*g if root==hi else lo-root+width*f
                              for root in roots)
            logarithm = math.log(s/mu2)+sum(math.log(abs(d)) for d in distances)
            phase = rim*math.pi if distances[0]*distances[1]<0 else 0.0
            return jacobian*complex(-logarithm,phase)
        quadratures.append(integrate(transformed,tolerance=tolerance/len(intervals)))
    return ParameterIntegral(s,m2,mu2,rim,sum((q.value for q in quadratures),0j),
                             sum(q.estimated_error for q in quadratures),intervals,tuple(quadratures))


def bubble_dispersion_below(s,m2=1.0,mu2=1.0,tolerance=1e-11):
    """Once-subtracted dispersion reconstruction from Im B(t)=pi beta(t).

    B(s)-B(0)=s integral_{4m2}^infinity beta(t)/(t(t-s)) dt.
    t=4m2/(1-v^2) gives 2s v^2/(4m2-s+s v^2). No principal-value or
    above-threshold dispersion implementation is implied.
    """
    validate(s,m2,mu2)
    if s>=4*m2:
        raise ValueError("Dispersion quadrature restricted below threshold")
    q = integrate(lambda v:2*s*v*v/(4*m2-s+s*v*v),tolerance=tolerance)
    return -math.log(m2/mu2)+q.value,q


def bubble_regulated_spacelike(s,m2=1.0,mu2=1.0,epsilon=0.01,tolerance=1e-11):
    """Finite-epsilon DR representation before subtraction, spacelike only.

    Gamma(epsilon) (4 pi)^epsilon integral (D/mu^2)^(-epsilon) dx.
    Its Laurent expansion is Delta+B+O(epsilon). The O(epsilon) terms
    are retained here, unlike the four-point Laurent bookkeeping.
    """
    validate(s,m2,mu2)
    if s>0 or not math.isfinite(epsilon) or not 0<epsilon<1:
        raise ValueError("Spacelike invariant and 0<epsilon<1 required")
    q = integrate(lambda x:math.exp(-epsilon*math.log((m2-s*x*(1-x))/mu2)),tolerance=tolerance)
    return math.gamma(epsilon)*(4*math.pi)**epsilon*q.value,q


def phase_space_two_body(s,m2=1.0):
    """Unsymmetrized integral dPhi_2 from on-shell radial delta functions.

    dPhi_2/dOmega = |k|/(16 pi^2 sqrt(s)); integrate phi and cos(theta).
    The identical-particle 1/2! is applied by optical_cut(), not here.
    """
    validate(s,m2,1.0)
    if s<=4*m2:
        return 0.0
    energy = math.sqrt(s)/2
    momentum = math.sqrt(energy*energy-m2)
    density = momentum/(16*math.pi**2*math.sqrt(s))
    return (2*math.pi*integrate(lambda cosine:density,-1,1).value).real


def optical_cut(s,m2,coupling):
    if not math.isfinite(coupling):
        raise ValueError("Finite coupling required")
    return coupling*coupling*phase_space_two_body(s,m2)/2


def physical_invariants(s,m2,cosine):
    validate(s,m2,1.0)
    if s<4*m2 or not math.isfinite(cosine) or not -1<=cosine<=1:
        raise ValueError("Physical massive two-to-two kinematics required")
    momentum2 = s/4-m2
    return s,-2*momentum2*(1-cosine),-2*momentum2*(1+cosine)


@dataclass(frozen=True)
class Amplitude:
    invariants: tuple[float,float,float]
    mass_squared: float
    scale_squared: float
    coupling: float
    tree: float
    channel_bubbles: tuple[complex,...]
    loop: complex
    total: complex
    uv_pole_coefficient: float


def amplitude(invariants,m2=1.0,mu2=1.0,coupling=0.7):
    if len(invariants)!=3 or not math.isfinite(coupling):
        raise ValueError("Three Mandelstam invariants and finite coupling required")
    for x in invariants:
        validate(x,m2,mu2)
    if not math.isclose(sum(invariants),4*m2,rel_tol=1e-12,abs_tol=1e-12):
        raise ValueError("On-shell s+t+u=4m^2 required")
    bubbles = tuple(bubble_closed(x,m2,mu2) for x in invariants)
    prefactor = coupling*coupling/(32*math.pi**2)
    loop = prefactor*sum(bubbles)
    return Amplitude(tuple(invariants),m2,mu2,coupling,-coupling,bubbles,loop,-coupling+loop,3*prefactor)


def uv_delta(epsilon):
    if not math.isfinite(epsilon) or epsilon<=0:
        raise ValueError("Positive dimensional regulator required")
    return 1/epsilon-0.5772156649015329+math.log(4*math.pi)
