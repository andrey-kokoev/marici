"""Conditional fixed-momentum Maxwell adapter for the seed oscillatory plane.

Exact arithmetic in Q(sqrt(3), i), using only the standard library. Minkowski
geometry, a positive null momentum along +z, and a vector-polarization action
are declared adapter data, not outputs derived from seed incidence.
"""
from dataclasses import dataclass
from fractions import Fraction as F


@dataclass(frozen=True)
class Q:
    """r+s*sqrt(3)+j*i+t*i*sqrt(3)."""
    r: F = F(0)
    s: F = F(0)
    j: F = F(0)
    t: F = F(0)

    def __post_init__(self):
        for name in ('r', 's', 'j', 't'):
            value = getattr(self, name)
            if not isinstance(value, (int, F)):
                raise TypeError('Exact rational field coefficients required')
            object.__setattr__(self, name, F(value))

    @property
    def parts(self):
        return (self.r, self.s, self.j, self.t)

    @staticmethod
    def coerce(value):
        if isinstance(value, Q):
            return value
        if isinstance(value, (int, F)):
            return Q(value)
        raise TypeError('Expected an exact Q(sqrt(3),i) scalar')

    def __add__(self, other):
        other = self.coerce(other)
        return Q(*(a + b for a, b in zip(self.parts, other.parts)))

    __radd__ = __add__

    def __neg__(self):
        return Q(*(-a for a in self.parts))

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        out = [F(0)] * 4
        for a, x in enumerate(self.parts):
            for b, y in enumerate(other.parts):
                factor = (3 if a & b & 1 else 1) * (-1 if a & b & 2 else 1)
                out[a ^ b] += factor * x * y
        return Q(*out)

    __rmul__ = __mul__

    def conjugate(self):
        return Q(self.r, self.s, -self.j, -self.t)

    def inverse(self):
        if self == ZERO:
            raise ZeroDivisionError('Zero has no inverse')
        norm = self * self.conjugate()
        assert norm.j == norm.t == 0
        denominator = norm.r * norm.r - 3 * norm.s * norm.s
        return self.conjugate() * Q(norm.r / denominator, -norm.s / denominator)

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) * self.inverse()

    def __pow__(self, n):
        if n < 0:
            return self.inverse() ** (-n)
        value = ONE
        for _ in range(n):
            value = value * self
        return value


ZERO, ONE = Q(), Q(1)
SQRT3, I = Q(s=1), Q(j=1)
SIGNS = (1, -1, -1, -1)
ETA = tuple(tuple(Q(SIGNS[i] if i == j else 0) for j in range(4)) for i in range(4))


def vector(values, size):
    result = tuple(Q.coerce(value) for value in values)
    if len(result) != size:
        raise ValueError('Incorrect vector dimension')
    return result


def mv(matrix, values):
    if len(matrix[0]) != len(values):
        raise ValueError('Matrix-vector dimensions do not match')
    return tuple(sum((a * b for a, b in zip(row, values)), ZERO) for row in matrix)


def transpose(matrix):
    return tuple(zip(*matrix))


def mm(a, b):
    return tuple(tuple(sum((x * y for x, y in zip(row, col)), ZERO) for col in transpose(b)) for row in a)


def rank(matrix):
    rows = [list(row) for row in matrix]
    pivot_row = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][col] != ZERO), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        value = rows[pivot_row][col]
        rows[pivot_row] = [x / value for x in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row:
                value = rows[i][col]
                rows[i] = [x - value * y for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def minkowski(a, b):
    return sum((Q(sign) * x * y for sign, x, y in zip(SIGNS, a, b)), ZERO)


def hermitian_physical(a, b):
    return -minkowski(tuple(x.conjugate() for x in a), b)


def field_strength(k, epsilon):
    # Reduced Fourier coefficient F^{mu nu}=k^mu eps^nu-k^nu eps^mu;
    # the common -i from differentiating exp(-ik.x) is suppressed.
    return tuple(tuple(k[mu] * epsilon[nu] - k[nu] * epsilon[mu] for nu in range(4)) for mu in range(4))


def maxwell_operator(k):
    k2 = minkowski(k, k)
    return tuple(tuple((k2 if mu == nu else ZERO) - k[mu] * SIGNS[nu] * k[nu]
                       for nu in range(4)) for mu in range(4))


def validate_wave(k, epsilon):
    k, epsilon = vector(k, 4), vector(epsilon, 4)
    if k == (ZERO,) * 4 or minkowski(k, k) != ZERO:
        raise ValueError('Nonzero null momentum required')
    if minkowski(k, epsilon) != ZERO:
        raise ValueError('Polarization must be transverse')
    if field_strength(k, epsilon) == ((ZERO,) * 4,) * 4:
        raise ValueError('Pure gauge is the zero physical polarization, not a photon candidate')
    if mv(maxwell_operator(k), epsilon) != (ZERO,) * 4:
        raise ValueError('Free Maxwell equation failed')


def rotation_z(c, s):
    c, s = Q.coerce(c), Q.coerce(s)
    if c.conjugate() != c or s.conjugate() != s or c * c + s * s != ONE:
        raise ValueError('Real cosine and sine on the unit circle required')
    return ((ONE, ZERO, ZERO, ZERO), (ZERO, c, -s, ZERO),
            (ZERO, s, c, ZERO), (ZERO, ZERO, ZERO, ONE))


@dataclass(frozen=True)
class AdaptedPlaneWave:
    packets: tuple
    seed_coefficients: tuple
    momentum: tuple
    polarization: tuple


class SeedMaxwellAdapter:
    """A declared +z null frame; no seed-derived spacetime interpretation."""
    def __init__(self, packets, energy=F(1)):
        self.packets = tuple(packets)
        expected = (('AB', 'A', 'B'), ('BC', 'B', 'C'), ('CA', 'C', 'A'),
                    ('BA', 'B', 'A'), ('AD', 'A', 'D'), ('DB', 'D', 'B'))
        if tuple((p.label, p.source, p.target) for p in self.packets) != expected:
            raise ValueError('Exact ordered seed packet manifest required')
        if not isinstance(energy, (int, F)) or energy <= 0:
            raise ValueError('A supplied positive rational energy is required')
        self.energy = Q(energy)
        self.momentum = (self.energy, ZERO, ZERO, self.energy)

    @staticmethod
    def seed_from_coordinates(a, b):
        a, b = Q.coerce(a), Q.coerce(b)
        return (a, -a, (a + b) / 2, -a, a, -(a + b) / 2)

    def coordinates(self, seed):
        seed = vector(seed, 6)
        a, b = seed[0], 2 * seed[2] - seed[0]
        if self.seed_from_coordinates(a, b) != seed:
            raise ValueError('Seed vector is outside the selected oscillatory plane')
        return a, b

    def encode(self, seed, gauge=ZERO):
        seed = vector(seed, 6)
        a, b = self.coordinates(seed)
        # Pullback of -eta is diag(3,1), the preceding averaged plane metric.
        transverse = (ZERO, SQRT3 * a, -b, ZERO)
        gauge = Q.coerce(gauge)
        epsilon = tuple(x + gauge * k for x, k in zip(transverse, self.momentum))
        validate_wave(self.momentum, epsilon)
        return AdaptedPlaneWave(self.packets, seed, self.momentum, epsilon)

    def decode(self, epsilon):
        # The quotient k.perp/span(k) includes its zero class. It is fine for
        # decode to return zero for pure gauge; encode rejects it as a wave.
        epsilon = vector(epsilon, 4)
        if minkowski(self.momentum, epsilon) != ZERO:
            raise ValueError('Cannot decode a nontransverse representative')
        gauge = epsilon[0] / self.energy
        representative = tuple(x - gauge * k for x, k in zip(epsilon, self.momentum))
        if representative[0] != ZERO or representative[3] != ZERO:
            raise ValueError('Gauge section failed')
        return self.seed_from_coordinates(representative[1] / SQRT3, -representative[2])
