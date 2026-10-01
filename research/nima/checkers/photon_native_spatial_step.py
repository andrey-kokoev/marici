"""Clock-attached continuation of native two-packet histories.

No Maxwell/Fock, emission model, Born probabilities or translational step is
inserted. A continuation tick uses the positive adjoint rotor lift theta=pi/3;
clock values are stored as exact coefficients of pi. This explicitly attaches
the existing unit-rate angular clock rather than identifying endpoint order
with elapsed time.
"""
from dataclasses import dataclass
from fractions import Fraction as F

from check_natural_tower_return import PACKETS, LABELS, mm, transpose
from check_triangle_half_phase import TwoPacket

REGISTRY = tuple(TwoPacket(*p) for p in PACKETS)
VERTICES = {'A': (1, 1, 1), 'B': (1, -1, -1), 'C': (-1, 1, -1), 'D': (-1, -1, 1)}
SEED = (F(1), F(-1), F(1, 2), F(-1), F(1), F(-1, 2))
U = SEED
W = (F(0), F(0), F(1, 2), F(0), F(0), F(-1, 2))
PLANE_STEP = ((F(-1, 2), F(1, 2)), (F(-3, 2), F(-1, 2)))
COMPATIBLE_FRAME = ((F(1), F(1, 3)), (F(-1), F(1, 3)), (F(0), F(2, 3)))


def mv(matrix, vector):
    return tuple(sum((x * y for x, y in zip(row, vector)), F(0)) for row in matrix)


def coordinates(coefficients):
    if len(coefficients) != 6:
        raise ValueError('Six retained occurrence coefficients required')
    a, b = coefficients[0], 2 * coefficients[2] - coefficients[0]
    if tuple(a * u + b * w for u, w in zip(U, W)) != tuple(coefficients):
        raise ValueError('Coefficient summary is outside the selected seed plane')
    return a, b


def continuation_matrix(registry=REGISTRY):
    return tuple(tuple(F(a.target == b.source) for a in registry) for b in registry)


def target_reader(registry=REGISTRY):
    return tuple(tuple(F(p.target == vertex) for p in registry) for vertex in LABELS)


def contrast_reader(registry=REGISTRY):
    # Signed amplitude contrast, NOT a position or normalized probability mean.
    # Uses the already declared tetrahedral scale, with no factor of 1/2.
    positions = tuple(tuple(VERTICES[v][axis] for v in LABELS) for axis in range(3))
    return mm(positions, target_reader(registry))


@dataclass(frozen=True)
class RetainedPath:
    packets: tuple
    coefficient: F

    def __post_init__(self):
        if not self.packets or any(p not in REGISTRY for p in self.packets):
            raise ValueError('Registered seed packets required')
        if any(a.target != b.source for a, b in zip(self.packets, self.packets[1:])):
            raise ValueError('Incomposable retained path')

    @property
    def continuation_displacement(self):
        # The initial primitive is part of preparation. Subsequent appends are
        # the timed continuation steps, starting at that primitive's target.
        start = VERTICES[self.packets[0].target]
        end = VERTICES[self.packets[-1].target]
        return tuple(b - a for a, b in zip(start, end))


@dataclass(frozen=True)
class ClockedHistory:
    updates: int
    paths: tuple

    def __post_init__(self):
        if type(self.updates) is not int or self.updates < 0 or not self.paths:
            raise ValueError('Nonnegative update count and nonempty retained history required')
        if any(len(p.packets) != self.updates + 1 for p in self.paths):
            raise ValueError('Clock/history depth mismatch')
        words = [p.packets for p in self.paths]
        if len(set(words)) != len(words):
            raise ValueError('Duplicate formal path record')

    @classmethod
    def initial(cls, coefficients=SEED):
        coefficients = tuple(F(c) for c in coefficients)
        coordinates(coefficients)
        return cls(0, tuple(RetainedPath((p,), c) for p, c in zip(REGISTRY, coefficients)))

    @property
    def clock_over_pi(self):
        return F(self.updates, 3)

    def summary(self):
        return tuple(sum((path.coefficient for path in self.paths if path.packets[-1] == p), F(0)) for p in REGISTRY)

    def advance(self):
        # Prefix extension retains branching and every old occurrence. No
        # aggregation/cancellation is used to generate subsequent path records.
        children = tuple(RetainedPath(path.packets + (p,), path.coefficient)
                         for path in self.paths for p in REGISTRY if path.packets[-1].target == p.source)
        result = ClockedHistory(self.updates + 1, children)
        if result.summary() != mv(continuation_matrix(), self.summary()):
            raise AssertionError('Retained continuation/summary square failed')
        return result

    def target_amplitudes(self):
        return mv(target_reader(), self.summary())

    def spatial_contrast(self):
        return mv(contrast_reader(), self.summary())

    def retained_counting_norm(self):
        return sum((p.coefficient * p.coefficient for p in self.paths), F(0))
