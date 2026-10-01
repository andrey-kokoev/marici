"""Quantum number audit for the declared local transition-current coupling.

Finite-support Fock polynomials have no occupation cutoff. The modal witness
exposes selection rules, not a full continuum scattering solver. Gaussian
bounds concern first-order channel weights only, not all-orders fidelity.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial

from photon_maxwell_adapter import Q, ZERO, ONE, I
from photon_creation_state import FockPolynomial, creation_combination
from photon_local_current import LocalDipoleCurrent


def annihilation_combination(state, coefficients):
    coefficients = tuple(Q.coerce(c) for c in coefficients)
    if len(coefficients) != 2:
        raise ValueError('Two modal coefficients required')
    return state.annihilate(1).scaled(coefficients[0].conjugate()) + state.annihilate(-1).scaled(coefficients[1].conjugate())


@dataclass(frozen=True)
class SourceFieldState:
    ground: FockPolynomial
    excited: FockPolynomial

    def __add__(self, other):
        return SourceFieldState(self.ground + other.ground, self.excited + other.excited)

    def __sub__(self, other):
        return SourceFieldState(self.ground - other.ground, self.excited - other.excited)

    def scaled(self, scalar):
        return SourceFieldState(self.ground.scaled(scalar), self.excited.scaled(scalar))

    def inner(self, other):
        return self.ground.inner(other.ground) + self.excited.inner(other.excited)

    def excitation(self):
        return SourceFieldState(self.ground.number(), self.excited.number() + self.excited)

    def parity(self):
        def transform(p, source_excited):
            return FockPolynomial(tuple((n, c * (-1) ** (sum(n) + source_excited)) for n, c in p.terms))
        return SourceFieldState(transform(self.ground, 0), transform(self.excited, 1))

    def photon_sector(self, number):
        def select(p):
            return FockPolynomial(tuple((n, c) for n, c in p.terms if sum(n) == number))
        return SourceFieldState(select(self.ground), select(self.excited))


@dataclass(frozen=True)
class LocalModalCoupling:
    emission: tuple       # sigma_- A_g^dagger+h.c.
    countercreation: tuple  # sigma_+ A_r^dagger+h.c.

    def __post_init__(self):
        for name in ('emission', 'countercreation'):
            values = tuple(Q.coerce(x) for x in getattr(self, name))
            if len(values) != 2:
                raise ValueError('Two retained polarization mode coefficients required')
            object.__setattr__(self, name, values)

    def rotating(self, state):
        return SourceFieldState(creation_combination(state.excited, self.emission),
                                annihilation_combination(state.ground, self.emission))

    def counter(self, state):
        return SourceFieldState(annihilation_combination(state.excited, self.countercreation),
                                creation_combination(state.ground, self.countercreation))

    def full(self, state):
        return self.rotating(state) + self.counter(state)


def free_action(state, gap, frequencies):
    frequencies = tuple(F(x) for x in frequencies)
    gap = F(gap)
    if len(frequencies) != 2 or gap <= 0 or any(x <= 0 for x in frequencies):
        raise ValueError('Positive source gap and two positive mode frequencies required')
    def field_action(p):
        return FockPolynomial(tuple((n, c * (frequencies[0] * n[0] + frequencies[1] * n[1])) for n, c in p.terms))
    return SourceFieldState(field_action(state.ground), field_action(state.excited) + state.excited.scaled(gap))


@dataclass(frozen=True)
class GapCurrentSample:
    common_envelope_exponent: F | None
    time_phase_argument: F  # extra factor exp(i*argument)
    coefficients: tuple


def modulated_current_sample(current, gap, point, raising=False):
    if not isinstance(current, LocalDipoleCurrent) or not isinstance(gap, (int, F)) or gap <= 0:
        raise ValueError('Declared local current and positive exact gap required')
    # Differentiate M(t,x), INCLUDING sigma_-(t)~exp(-i Omega t).
    # Modulating j afterward would omit this indispensable derivative term.
    base = current.sample(point)
    if base.exponent is None:
        return GapCurrentSample(None, F(0), (ZERO,) * 4)
    lower = (base.coefficients[0],) + tuple(x - I * gap * d for x, d in zip(base.coefficients[1:], current.dipole))
    if raising:
        return GapCurrentSample(base.exponent, F(gap) * F(point[0]), tuple(x.conjugate() for x in lower))
    return GapCurrentSample(base.exponent, -F(gap) * F(point[0]), lower)


@dataclass(frozen=True)
class GaussianGapSpectrum:
    gap: F
    temporal_width: F
    spatial_width: F

    def __post_init__(self):
        for name in ('gap', 'temporal_width', 'spatial_width'):
            value = getattr(self, name)
            if not isinstance(value, (int, F)) or value <= 0:
                raise ValueError('Positive exact gap and Gaussian widths required')
            object.__setattr__(self, name, F(value))

    def log_intensity(self, energy, raising=False):
        if not isinstance(energy, (int, F)) or energy <= 0:
            raise ValueError('Positive exact photon energy required')
        detuning = F(energy) + self.gap if raising else F(energy) - self.gap
        return -self.temporal_width ** 2 * detuning ** 2 - self.spatial_width ** 2 * F(energy) ** 2

    def log_counter_ratio(self, energy):
        return self.log_intensity(energy, True) - self.log_intensity(energy, False)

    def integrated_ratio_bound(self, half_bandwidth, taylor_terms=32):
        """Bound I_raise/I_lower, I=int_0^inf omega^3 exp(log_intensity)domega.

        Common angular factors cancel after summing helicities and directions.
        This is NOT an all-orders multiphoton error bound.
        """
        if (not isinstance(half_bandwidth, (int, F)) or not 0 < half_bandwidth < self.gap
                or type(taylor_terms) is not int or taylor_terms < 1):
            raise ValueError('Band inside positive frequencies and positive Taylor order required')
        delta = F(half_bandwidth)
        O, tau, ell = self.gap, self.temporal_width, self.spatial_width
        a = tau * tau + ell * ell
        suppression = tau * tau * O * O - tau * tau * delta * delta - ell * ell * (O + delta) ** 2
        if suppression <= 0:
            raise ValueError('This simple integrated bound is not suppressive for these parameters')
        prefactor = 1 / (4 * a * a * delta * (O - delta) ** 3)
        # exp(suppression)>=this positive partial Taylor sum, so its reciprocal
        # is a rigorous rational upper bound, not floating-point quadrature.
        partial_exp = sum((suppression ** n / factorial(n) for n in range(taylor_terms + 1)), F(0))
        return {'suppression_exponent': suppression, 'prefactor': prefactor,
                'positive_exp_lower_bound': partial_exp, 'ratio_upper_bound': prefactor / partial_exp,
                'taylor_order': taylor_terms}
