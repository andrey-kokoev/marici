"""Conditional two-helicity creation-state map from the retained seed plane.

A declared normalized two-mode oscillator fixture is used, not a normalizable
exact-momentum ket in infinite volume. Fock polynomials have finite support but
NO occupation cutoff: creation never gets truncated. The monomial norm n! makes
multiplication and differentiation exact bosonic adjoints without sqrt(n).
"""
from dataclasses import dataclass
from itertools import count
from math import factorial

from photon_maxwell_adapter import Q, ZERO, ONE, I, SQRT3, mv, hermitian_physical
from photon_lorentz_transport import LorentzMap, PhotonTransportLedger, TransportedWave, real_positive

HELICITIES = (1, -1)


@dataclass(frozen=True)
class FockPolynomial:
    # Sum c_(n+,n-) (a+^dagger)^n+ (a-^dagger)^n- |vacuum>.
    terms: tuple

    def __post_init__(self):
        merged = {}
        for occupation, value in self.terms:
            occupation = tuple(occupation)
            if len(occupation) != 2 or any(type(n) is not int or n < 0 for n in occupation):
                raise ValueError('Two nonnegative integer occupations required')
            value = Q.coerce(value)
            merged[occupation] = merged.get(occupation, ZERO) + value
        object.__setattr__(self, 'terms', tuple(sorted((n, c) for n, c in merged.items() if c != ZERO)))

    def __add__(self, other):
        if not isinstance(other, FockPolynomial):
            raise TypeError('Fock polynomial required')
        return FockPolynomial(self.terms + other.terms)

    def scaled(self, scalar):
        scalar = Q.coerce(scalar)
        return FockPolynomial(tuple((n, scalar * c) for n, c in self.terms))

    def __sub__(self, other):
        return self + other.scaled(-ONE)

    @staticmethod
    def _slot(helicity):
        if type(helicity) is not int or helicity not in HELICITIES:
            raise ValueError('Declared helicity +1 or -1 required')
        return HELICITIES.index(helicity)

    def create(self, helicity):
        slot = self._slot(helicity)
        result = []
        for occupation, c in self.terms:
            new = list(occupation)
            new[slot] += 1
            result.append((tuple(new), c))
        return FockPolynomial(tuple(result))

    def annihilate(self, helicity):
        slot = self._slot(helicity)
        result = []
        for occupation, c in self.terms:
            if occupation[slot]:
                new = list(occupation)
                new[slot] -= 1
                result.append((tuple(new), c * occupation[slot]))
        return FockPolynomial(tuple(result))

    def number(self):
        return FockPolynomial(tuple((n, c * sum(n)) for n, c in self.terms))

    def helicity(self):
        return FockPolynomial(tuple((n, c * (n[0] - n[1])) for n, c in self.terms))

    def inner(self, other):
        table = dict(other.terms)
        return sum((c.conjugate() * table.get(n, ZERO) * factorial(n[0]) * factorial(n[1])
                    for n, c in self.terms), ZERO)

    def phase_rotate(self, c, s):
        c, s = Q.coerce(c), Q.coerce(s)
        if c.conjugate() != c or s.conjugate() != s or c * c + s * s != ONE:
            raise ValueError('A real unit-circle rotation pair is required')
        phases = (c - I * s, c + I * s)
        return FockPolynomial(tuple((n, value * phases[0] ** n[0] * phases[1] ** n[1])
                                    for n, value in self.terms))


VACUUM = FockPolynomial((((0, 0), ONE),))
FOCK_ZERO = FockPolynomial(())


def creation_combination(state, coefficients):
    coefficients = tuple(Q.coerce(x) for x in coefficients)
    if len(coefficients) != 2:
        raise ValueError('Exactly two helicity coefficients required')
    return state.create(1).scaled(coefficients[0]) + state.create(-1).scaled(coefficients[1])


@dataclass(frozen=True)
class OnePhotonRecord:
    label: str
    mode_fixture: str
    wave: TransportedWave
    reference_frame: LorentzMap
    coefficients: tuple  # ordered h=+1,-1, before normalization
    numerator: FockPolynomial
    norm_squared: Q
    # The ket means numerator/sqrt(norm_squared), not an unnormalized state.
    # Keeping the positive squared norm avoids pretending sqrt(n) lies in Q.


class PhotonCreationLedger:
    """Own the quantum record; do not infer its Fock assumptions from the seed."""
    def __init__(self, transport, mode_fixture):
        if not isinstance(transport, PhotonTransportLedger):
            raise ValueError('A retained conditional transport ledger is required')
        if not isinstance(mode_fixture, str) or not mode_fixture.strip():
            raise ValueError('An explicitly declared normalized mode fixture is required')
        self.transport = transport
        self.mode_fixture = mode_fixture
        self._serial = count()
        self._states = {}

    def create_one(self, wave, reference_frame=None):
        wave = self.transport.resolve(wave)
        frame = wave.frame if reference_frame is None else reference_frame
        if not isinstance(frame, LorentzMap):
            raise ValueError('A validated polarization frame is required')
        if mv(frame.matrix, self.transport.adapter.momentum) != wave.momentum:
            raise ValueError('Reference frame does not have this wave momentum')
        reference_epsilon = mv(frame.inverse().matrix, wave.polarization)
        seed = self.transport.adapter.decode(reference_epsilon)
        a, b = self.transport.adapter.coordinates(seed)
        # v=alpha*g_plus+beta*g_minus, but g_plus has helicity -1.
        beta = (a + I * b / SQRT3) / 2
        alpha = (a - I * b / SQRT3) / 2
        coefficients = (beta, alpha)
        numerator = creation_combination(VACUUM, coefficients)
        norm_squared = numerator.inner(numerator)
        if not real_positive(norm_squared):
            raise ValueError('A nonzero positive-norm one-photon numerator is required')
        if numerator.number() != numerator:
            raise ValueError('Creation did not land in the one-photon sector')
        if hermitian_physical(reference_epsilon, reference_epsilon) != 6 * norm_squared:
            raise ValueError('Seed-plane/one-photon norm matching failed')
        record = OnePhotonRecord(f'one-photon:{next(self._serial)}', self.mode_fixture,
                                 wave, frame, coefficients, numerator, norm_squared)
        self._states[record.label] = record
        return record

    def resolve(self, record):
        if not isinstance(record, OnePhotonRecord) or self._states.get(record.label) is not record:
            raise ValueError('Unknown, foreign or substituted one-photon record')
        self.transport.resolve(record.wave)
        return record

    def density(self, record):
        record = self.resolve(record)
        return tuple(tuple(a * b.conjugate() / record.norm_squared for b in record.coefficients)
                     for a in record.coefficients)

    def expectation(self, record, operator):
        record = self.resolve(record)
        result = operator(record.numerator)
        if not isinstance(result, FockPolynomial):
            raise ValueError('Operator must return a Fock polynomial')
        return record.numerator.inner(result) / record.norm_squared

    def retained_seed_in_reference_frame(self, record):
        """Uses stored unnormalized amplitudes, NOT the normalized density alone."""
        record = self.resolve(record)
        beta, alpha = record.coefficients
        return self.transport.adapter.seed_from_coordinates(alpha + beta, I * SQRT3 * (alpha - beta))

    def deconstruct(self, record):
        record = self.resolve(record)
        return record.wave, record.reference_frame, record.coefficients, record.norm_squared
