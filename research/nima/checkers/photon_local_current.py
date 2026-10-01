"""Local conserved transition-current candidates from the seed plane.

M^{0i}=d_i f, M^{i0}=-d_i f, j^mu=partial_nu M^{nu mu}. Conservation is
identical, not a transverse projection added after computing radiation.
Profiles are new source inputs. Radiation formulas are first-order transition
amplitudes, not the earlier engineered Rabi transfer law.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial

from photon_maxwell_adapter import Q, ZERO, ONE, I, SQRT3, SeedMaxwellAdapter, minkowski, vector


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), ZERO)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


@dataclass(frozen=True)
class FactoredCurrent:
    # Actual current is exp(exponent)*coefficients. None means outside support.
    exponent: F | None
    coefficients: tuple


@dataclass(frozen=True)
class LocalDipoleCurrent:
    packets: tuple
    seed_coefficients: tuple
    dipole: tuple
    widths: tuple  # t,x,y,z positive rational scales
    envelope: str  # gaussian or compact_bump

    @classmethod
    def from_seed(cls, adapter, seed, widths=(1, 1, 1, 1), envelope='compact_bump'):
        if not isinstance(adapter, SeedMaxwellAdapter):
            raise ValueError('Explicit conditional seed-spacetime adapter required')
        seed = vector(seed, 6)
        a, b = adapter.coordinates(seed)
        if all(x == ZERO for x in seed):
            raise ValueError('Nonzero seed polarization required')
        widths = tuple(widths)
        if (len(widths) != 4 or any(not isinstance(w, (int, F)) or w <= 0 for w in widths)
                or envelope not in ('gaussian', 'compact_bump')):
            raise ValueError('Four positive exact scales and a declared envelope required')
        return cls(adapter.packets, seed, (SQRT3 * a, -b, ZERO), tuple(F(w) for w in widths), envelope)

    def sample(self, point):
        point = tuple(point)
        if len(point) != 4 or any(not isinstance(x, (int, F)) for x in point):
            raise ValueError('Four exact rational spacetime coordinates required')
        point = tuple(F(x) for x in point)
        if self.envelope == 'compact_bump':
            if any(abs(x) >= w for x, w in zip(point, self.widths)):
                return FactoredCurrent(None, (ZERO,) * 4)
            ratios = tuple(1 - (x / w) ** 2 for x, w in zip(point, self.widths))
            exponent = -sum((1 / r for r in ratios), F(0))
            gradients = tuple(-2 * x / (w * w * r * r) for x, w, r in zip(point, self.widths, ratios))
        else:
            exponent = -sum(((x / w) ** 2 / 2 for x, w in zip(point, self.widths)), F(0))
            gradients = tuple(-x / (w * w) for x, w in zip(point, self.widths))
        # j^0=-d.grad f, j^i=d_i partial_t f. A shared envelope prefactor is
        # left symbolic so no transcendental rounding enters conservation.
        charge = -dot(self.dipole, tuple(Q(x) for x in gradients[1:]))
        spatial = tuple(d * gradients[0] for d in self.dipole)
        return FactoredCurrent(exponent, (charge,) + spatial)

    def reduced_divergence(self, point):
        point = tuple(F(x) for x in point)
        sample = self.sample(point)
        if sample.exponent is None:
            return ZERO
        if self.envelope == 'compact_bump':
            gradients = tuple(-2 * x / (w * w * (1 - (x / w) ** 2) ** 2) for x, w in zip(point, self.widths))
        else:
            gradients = tuple(-x / (w * w) for x, w in zip(point, self.widths))
        # The envelope is a product of one-coordinate factors. Mixed
        # derivatives commute, giving exact operator-valued continuity.
        return sample.coefficients[0] * gradients[0] + sum(
            (self.dipole[i] * gradients[0] * gradients[i + 1] for i in range(3)), ZERO)

    def reduced_fourier_current(self, k):
        k = vector(k, 4)
        # Fourier convention ftilde(k)=integral exp(i k.x) f(x). The actual
        # current is -i*ftilde(k)*J(k); only the polynomial J is returned.
        return (dot(k[1:], self.dipole),) + tuple(k[0] * d for d in self.dipole)

    def reduced_emission(self, k, epsilon):
        k, epsilon = vector(k, 4), vector(epsilon, 4)
        # Global phase/coupling and ftilde are separate. Conjugated outgoing
        # polarization is used. Existing epsilon modes have squared norm six.
        return -minkowski(tuple(x.conjugate() for x in epsilon), self.reduced_fourier_current(k))

    def angular_intensity(self, direction, helicity):
        direction = vector(direction, 3)
        if (any(x.conjugate() != x for x in direction) or dot(direction, direction) != ONE
                or type(helicity) is not int or helicity not in (-1, 1)):
            raise ValueError('Real unit emission direction and helicity +/-1 required')
        conjugate_d = tuple(x.conjugate() for x in self.dipole)
        transverse = dot(conjugate_d, self.dipole) - dot(direction, self.dipole).conjugate() * dot(direction, self.dipole)
        handed = I * helicity * dot(direction, cross(self.dipole, conjugate_d))
        return (transverse + handed) / 2

    def gaussian_norm_over_pi(self):
        if self.envelope != 'gaussian' or len(set(self.widths[1:])) != 1:
            raise ValueError('This analytic formula requires an isotropic spatial Gaussian')
        # After rescaling the source envelope so ftilde(0)=1:
        # ftilde(on shell)=exp[-a*omega^2/2], a=tau^2+ell^2.
        a = self.widths[0] ** 2 + self.widths[1] ** 2
        D = dot(tuple(x.conjugate() for x in self.dipole), self.dipole)
        return Q(F(2, 3) / (a * a)) * D


def gaussian_odd_radial_moment(power, a):
    # integral_0^infinity r^(2m+1) exp(-a*r^2) dr = m!/(2*a^(m+1)).
    if (type(power) is not int or power < 1 or power % 2 != 1
            or not isinstance(a, (int, F)) or a <= 0):
        raise ValueError('Positive odd power and positive exact Gaussian parameter required')
    m = (power - 1) // 2
    return F(factorial(m), 2) / F(a) ** (m + 1)
