"""Conditional normalizable one-photon profile on the future light cone.

Convention: dmu=d^3k/(2 k0), with all (2pi)^3 factors absorbed into the operator
normalization. Light-front chart: q=k0+kz>0, u=kx/q, v=ky/q; dmu=(q/2)dq du dv.
The compact top-hat profile and the continuum CCR are declared inputs.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import count

from photon_maxwell_adapter import Q, ZERO, ONE, SQRT3, I, mv, minkowski
from photon_lorentz_transport import LorentzMap, real_positive, determinant
from photon_creation_state import PhotonCreationLedger


def real_coordinates(values):
    result = tuple(Q.coerce(x) for x in values)
    if len(result) != 3 or any(x.conjugate() != x for x in result) or not real_positive(result[0]):
        raise ValueError('Real (q,u,v) with q>0 required')
    return result


def momentum(coordinates):
    q, u, v = real_coordinates(coordinates)
    radius = u * u + v * v
    return (q * (ONE + radius) / 2, q * u, q * v, q * (ONE - radius) / 2)


def coordinates(k):
    k = tuple(Q.coerce(x) for x in k)
    if (len(k) != 4 or any(x.conjugate() != x for x in k)
            or not real_positive(k[0]) or minkowski(k, k) != ZERO):
        raise ValueError('A future nonzero real null momentum is required')
    q = k[0] + k[3]
    if not real_positive(q):
        raise ValueError('North-chart pole: retain the transported frame or use a second chart')
    return (q, k[1] / q, k[2] / q)


@dataclass(frozen=True)
class LightConeBox:
    q: tuple
    u: tuple
    v: tuple

    def __post_init__(self):
        for name in ('q', 'u', 'v'):
            bounds = tuple(getattr(self, name))
            if (len(bounds) != 2 or any(not isinstance(x, (int, F)) for x in bounds)
                    or bounds[0] >= bounds[1]):
                raise ValueError('Nondegenerate exact rational interval required')
            object.__setattr__(self, name, tuple(F(x) for x in bounds))
        if self.q[0] <= 0:
            raise ValueError('Profile support must stay away from q=0')

    def moment(self, a=0, b=0, c=0):
        # Integral q^a u^b v^c with respect to (q/2)dq du dv, not flat d^3k.
        if any(type(n) is not int or n < 0 for n in (a, b, c)):
            raise ValueError('Nonnegative integer powers required')
        def integral(bounds, power):
            return (bounds[1] ** (power + 1) - bounds[0] ** (power + 1)) / (power + 1)
        return integral(self.q, a + 1) * integral(self.u, b) * integral(self.v, c) / 2

    @property
    def volume(self):
        return self.moment()

    def contains(self, point):
        point = real_coordinates(point)
        return all((x == Q(lo) or real_positive(x - Q(lo)))
                   and (x == Q(hi) or real_positive(Q(hi) - x))
                   for x, (lo, hi) in zip(point, (self.q, self.u, self.v)))

    def overlap_volume(self, other):
        if not isinstance(other, LightConeBox):
            raise ValueError('Another light-cone box is required')
        intervals = tuple((max(a[0], b[0]), min(a[1], b[1]))
                          for a, b in zip((self.q, self.u, self.v), (other.q, other.u, other.v)))
        if any(lo >= hi for lo, hi in intervals):
            return F(0)
        return LightConeBox(*intervals).volume

    def boosted_z(self, scale):
        if not isinstance(scale, (int, F)) or scale <= 0:
            raise ValueError('Positive rational longitudinal boost scale required')
        scale = F(scale)
        return LightConeBox(tuple(scale * x for x in self.q), tuple(x / scale for x in self.u),
                            tuple(x / scale for x in self.v))

    def rotated_quarter_z(self):
        return LightConeBox(self.q, (-self.v[1], -self.v[0]), self.u)

    def mean_momentum(self):
        m = self.moment
        V = self.volume
        return ((m(1, 0, 0) + m(1, 2, 0) + m(1, 0, 2)) / (2 * V),
                m(1, 1, 0) / V, m(1, 0, 1) / V,
                (m(1, 0, 0) - m(1, 2, 0) - m(1, 0, 2)) / (2 * V))

    def diagonal_second_moments(self):
        m = self.moment
        V = self.volume
        common = m(2, 0, 0) + m(2, 4, 0) + 2 * m(2, 2, 2) + m(2, 0, 4)
        cross = 2 * m(2, 2, 0) + 2 * m(2, 0, 2)
        return ((common + cross) / (4 * V), m(2, 2, 0) / V, m(2, 0, 2) / V,
                (common - cross) / (4 * V))


def polarization_frame(point, base_energy=ONE):
    q, u, v = real_coordinates(point)
    base_energy = Q.coerce(base_energy)
    if not real_positive(base_energy):
        raise ValueError('Positive base energy required')
    d = ONE + u * u + v * v
    # Smooth north-patch spatial frame, with R e_z along k/|k|.
    R = LorentzMap(((ONE, ZERO, ZERO, ZERO),
                    (ZERO, ONE - 2 * u * u / d, -2 * u * v / d, 2 * u / d),
                    (ZERO, -2 * u * v / d, ONE - 2 * v * v / d, 2 * v / d),
                    (ZERO, -2 * u / d, -2 * v / d, (ONE - u * u - v * v) / d)))
    ratio = q * d / (2 * base_energy)
    B = LorentzMap.boost(3, (ratio + ONE / ratio) / 2, (ratio - ONE / ratio) / 2)
    return R.after(B)


def wigner_phase(transformation, point, helicity, base_energy=ONE):
    if not isinstance(transformation, LorentzMap) or type(helicity) is not int or helicity not in (-1, 1):
        raise ValueError('Validated Lorentz map and helicity +/-1 required')
    base_energy = Q.coerce(base_energy)
    before = polarization_frame(point, base_energy)
    target = mv(transformation.matrix, momentum(point))
    # If this chart fails, the transported frame transformation*before still
    # exists. Do not reinterpret a chart pole as a zero photon amplitude.
    after = polarization_frame(coordinates(target), base_energy)
    little = after.inverse().after(transformation).after(before)
    k0 = (base_energy, ZERO, ZERO, base_energy)
    assert mv(little.matrix, k0) == k0
    epsilon = (ZERO, SQRT3, I * helicity * SQRT3, ZERO)
    acted = mv(little.matrix, epsilon)
    phase = acted[1] / SQRT3
    assert phase * phase.conjugate() == ONE
    alpha = acted[0] / base_energy
    assert acted == tuple(phase * e + alpha * k for e, k in zip(epsilon, k0))
    return phase


@dataclass(frozen=True)
class Jet3:
    value: Q
    derivative: tuple

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Jet3) else Jet3(Q.coerce(x), (ZERO,) * 3)

    def __add__(self, other):
        other = self.coerce(other)
        return Jet3(self.value + other.value, tuple(a + b for a, b in zip(self.derivative, other.derivative)))

    __radd__ = __add__

    def __neg__(self):
        return Jet3(-self.value, tuple(-a for a in self.derivative))

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        return Jet3(self.value * other.value, tuple(a * other.value + self.value * b
                                                    for a, b in zip(self.derivative, other.derivative)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        return Jet3(self.value / other.value, tuple((a * other.value - self.value * b) / (other.value * other.value)
                                                   for a, b in zip(self.derivative, other.derivative)))


def chart_jacobian(transformation, point):
    point = real_coordinates(point)
    q, u, v = tuple(Jet3(x, tuple(ONE if i == j else ZERO for j in range(3))) for i, x in enumerate(point))
    r = u * u + v * v
    k = (q * (1 + r) / 2, q * u, q * v, q * (1 - r) / 2)
    moved = tuple(sum((entry * weight for weight, entry in zip(row, k)), Jet3.coerce(ZERO))
                  for row in transformation.matrix)
    qp = moved[0] + moved[3]
    if not real_positive(qp.value):
        raise ValueError('Image point is outside the north chart')
    output = (qp, moved[1] / qp, moved[2] / qp)
    return tuple(x.value for x in output), tuple(x.derivative for x in output)


@dataclass(frozen=True)
class MomentumPacket:
    label: str
    creation_record: object
    profile: LightConeBox
    coefficients: tuple
    normalization_squared: Q  # denominator V*(|c+|^2+|c-|^2)


class MomentumPacketLedger:
    def __init__(self, creation):
        if not isinstance(creation, PhotonCreationLedger):
            raise ValueError('Retained creation-state ledger required')
        self.creation = creation
        self._serial = count()
        self._packets = {}

    def create(self, creation_record, profile):
        record = self.creation.resolve(creation_record)
        if not isinstance(profile, LightConeBox):
            raise ValueError('Explicit supported light-cone profile required')
        out = MomentumPacket(f'momentum-packet:{next(self._serial)}', record, profile,
                             record.coefficients, Q(profile.volume) * record.norm_squared)
        self._packets[out.label] = out
        return out

    def resolve(self, packet):
        if not isinstance(packet, MomentumPacket) or self._packets.get(packet.label) is not packet:
            raise ValueError('Unknown, foreign or substituted momentum packet')
        self.creation.resolve(packet.creation_record)
        return packet

    def norm_squared(self, packet):
        packet = self.resolve(packet)
        coefficient_norm = sum((c.conjugate() * c for c in packet.coefficients), ZERO)
        return Q(packet.profile.volume) * coefficient_norm / packet.normalization_squared

    def amplitude_numerators(self, packet, point):
        packet = self.resolve(packet)
        return packet.coefficients if packet.profile.contains(point) else (ZERO, ZERO)

    def transported_numerators(self, packet, transformation, source_point):
        # Parametrize the transformed support by the old coordinates. Amplitudes
        # are expressed in the canonical north frame at the target where valid.
        packet = self.resolve(packet)
        values = self.amplitude_numerators(packet, source_point)
        if values == (ZERO, ZERO):
            return values
        E = self.creation.transport.adapter.energy
        return tuple(wigner_phase(transformation, source_point, h, E) * c
                     for h, c in zip((1, -1), values))
