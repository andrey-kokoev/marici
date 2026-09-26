"""One-loop scalar tadpoles, mass subtraction and the constant LSZ correction.

Use inverse propagator p^2-m_R^2-Sigma_R and 1PI insertion -i Sigma.
For either -lambda phi^4/4! or -g phi^2 chi^2/4 with two external phi,
the contraction factor is 1/2. Write c=lambda or g and internal mass M.

T(epsilon)=M^2 Gamma(epsilon)/(1-epsilon)*(4pi mu^2/M^2)^epsilon
         =M^2[Delta+1-log(M^2/mu^2)]+O(epsilon).
The analytically continued Euclidean tadpole is J_E=-T/(16pi^2).
(-ic/2) J_E=+ic T/(32pi^2)=-i Sigma_loop, hence Sigma_loop=-cT/(32pi^2).
A mass counterterm contributes -i delta_m^2, so Sigma_R=Sigma_loop+delta_m^2.

Near d=4 this is analytic dimensional continuation, NOT an ordinary
convergent positive Euclidean integral. Explicit proper-time subtractions
make that continuation visible. At d=1 (epsilon=3/2), the unsubtracted
Euclidean integral does converge and is positive; its sign is also tested.
Only this one-loop constant self-energy is treated; no resummation or
higher-loop mass/running/residue prediction is implied.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

import scalar_one_loop as L


def validate(m2,mu2,epsilon):
    L.validate(0.0,m2,mu2)
    if not math.isfinite(epsilon) or not 0<epsilon<2 or epsilon==1:
        raise ValueError("Require 0<epsilon<2 away from the d=2 pole epsilon=1")


def tadpole_gamma(m2,mu2,epsilon):
    validate(m2,mu2,epsilon)
    return m2*math.gamma(epsilon)/(1-epsilon)*(4*math.pi*mu2/m2)**epsilon


def tadpole_finite(m2,mu2):
    L.validate(0.0,m2,mu2)
    return m2*(1-math.log(m2/mu2))


@dataclass(frozen=True)
class ProperTime:
    mass_squared: float
    scale_squared: float
    epsilon: float
    split: float
    analytic_subtractions: tuple[float,...]
    ultraviolet_remainder: L.Integral
    infrared_tail: L.Integral
    continued_gamma: float
    tadpole: float
    propagated_error_estimate: float


def tadpole_proper_time(m2,mu2,epsilon,split=1.0,tolerance=5e-13):
    """Continue Gamma(epsilon-1) by subtracting six small-u Taylor terms.

    Gamma(e-1)=integral_0^a u^(e-2)[exp(-u)-sum_(n=0)^5(-u)^n/n!]du
      +sum_(n=0)^5 (-1)^n a^(e+n-1)/(n!(e+n-1))
      +integral_a^infinity u^(e-2)exp(-u)du.
    UV poles are explicit. The remainder is evaluated by its stable series,
    not subtraction of nearly equal exponentials. The tested split domain is
    deliberately bounded. Quadrature estimates are not certified intervals.
    """
    validate(m2,mu2,epsilon)
    if not math.isfinite(split) or not 0.5<=split<=2:
        raise ValueError("Proper-time split restricted to [1/2,2]")
    analytic = tuple((-1)**n*split**(epsilon+n-1)/(math.factorial(n)*(epsilon+n-1)) for n in range(6))
    def ultraviolet(v):
        u = split*v
        # [exp(-u)-Taylor_5]/u^6. On 0<=u<=2, 32 terms are ample
        # in double precision; this is not an interval-arithmetic assertion.
        term = 1/math.factorial(6)
        tail = term
        for k in range(1,32):
            term *= -u/(k+6)
            tail += term
        return split*u**(epsilon+4)*tail
    def infrared(v):
        if v==1:
            return 0.0
        u = split/(1-v)
        return math.exp(epsilon*math.log(u)-u)/split
    uv = L.integrate(ultraviolet,tolerance=tolerance)
    ir = L.integrate(infrared,tolerance=tolerance)
    continued = sum(analytic)+uv.value.real+ir.value.real
    normalization = -m2*(4*math.pi*mu2/m2)**epsilon
    return ProperTime(m2,mu2,epsilon,split,analytic,uv,ir,continued,
                      normalization*continued,abs(normalization)*(uv.estimated_error+ir.estimated_error))


@dataclass(frozen=True)
class MassRenormalization:
    coupling: float
    internal_mass_squared: float
    scale_squared: float
    sigma_delta_coefficient: float
    sigma_finite: float
    msbar_counterterm_delta_coefficient: float
    on_shell_counterterm_finite: float
    momentum_derivative: float = 0.0
    lsz_residue_through_one_loop: float = 1.0

    def bare_laurent(self,epsilon):
        """Through epsilon^0 only, not the finite-epsilon Gamma expression."""
        return self.sigma_delta_coefficient*L.uv_delta(epsilon)+self.sigma_finite

    def counterterm(self,epsilon,scheme):
        value = self.msbar_counterterm_delta_coefficient*L.uv_delta(epsilon)
        if scheme=="MSbar":
            return value
        if scheme=="on-shell":
            return value+self.on_shell_counterterm_finite
        raise ValueError("Use MSbar or on-shell mass scheme")

    def self_energy(self,p2,scheme):
        if not math.isfinite(p2):
            raise ValueError("Finite external momentum squared required")
        if scheme=="MSbar":
            return self.sigma_finite
        if scheme=="on-shell":
            return 0.0
        raise ValueError("Use MSbar or on-shell mass scheme")

    def pole_mass_squared(self,external_parameter,scheme):
        if not math.isfinite(external_parameter):
            raise ValueError("Finite mass parameter required")
        return external_parameter+self.self_energy(external_parameter,scheme)

    def tuned_msbar_parameter(self,target_pole_mass_squared):
        if not math.isfinite(target_pole_mass_squared) or target_pole_mass_squared<0:
            raise ValueError("Nonnegative target pole mass squared required")
        return target_pole_mass_squared-self.sigma_finite

    def inverse_propagator(self,p2,external_parameter,scheme):
        if not math.isfinite(external_parameter):
            raise ValueError("Finite mass parameter required")
        return p2-external_parameter-self.self_energy(p2,scheme)


def mass_renormalization(coupling,internal_m2,mu2):
    L.validate(0.0,internal_m2,mu2)
    if not math.isfinite(coupling):
        raise ValueError("Finite scalar coupling required")
    prefactor = coupling/(32*math.pi**2)
    finite = -prefactor*tadpole_finite(internal_m2,mu2)
    return MassRenormalization(coupling,internal_m2,mu2,-prefactor*internal_m2,
                              finite,prefactor*internal_m2,-finite)


def running_mass_change(coupling,internal_m2,old_mu2,new_mu2):
    """One-loop change c M^2/(32pi^2) log(mu_new^2/mu_old^2).

    Hold c and the loop mass at reference-order values; feeding their own
    running back in would introduce higher-order terms not computed here.
    """
    mass_renormalization(coupling,internal_m2,old_mu2)
    L.validate(0.0,internal_m2,new_mu2)
    return coupling*internal_m2/(32*math.pi**2)*math.log(new_mu2/old_mu2)
