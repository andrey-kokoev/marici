"""Exact Lorentz/gauge transport of the conditional seed-Maxwell realization.

All spacetime transformations are supplied physical-model data. Registration
retains seed provenance and frame history; it does not derive spacetime or
supply an apparatus/one-photon creation operator.
"""
from dataclasses import dataclass
from itertools import count
from photon_maxwell_adapter import (
    Q, ZERO, ONE, ETA, SeedMaxwellAdapter, AdaptedPlaneWave,
    mv, mm, transpose, validate_wave, vector,
)

IDENTITY = tuple(tuple(ONE if i == j else ZERO for j in range(4)) for i in range(4))


def real_positive(x):
    x = Q.coerce(x)
    if x.j or x.t:
        raise ValueError('An ordered real scalar is required')
    a, b = x.r, x.s
    if b == 0:
        return a > 0
    if a == 0:
        return b > 0
    if a > 0 and b > 0:
        return True
    if a < 0 and b < 0:
        return False
    return a * a > 3 * b * b if a > 0 else 3 * b * b > a * a


def determinant(matrix):
    rows = [list(row) for row in matrix]
    value = ONE
    for col in range(len(rows)):
        pivot = next((i for i in range(col, len(rows)) if rows[i][col] != ZERO), None)
        if pivot is None:
            return ZERO
        if pivot != col:
            rows[pivot], rows[col] = rows[col], rows[pivot]
            value = -value
        element = rows[col][col]
        value *= element
        for i in range(col + 1, len(rows)):
            ratio = rows[i][col] / element
            rows[i] = [a - ratio * b for a, b in zip(rows[i], rows[col])]
    return value


@dataclass(frozen=True)
class LorentzMap:
    matrix: tuple

    def __post_init__(self):
        matrix = tuple(tuple(Q.coerce(x) for x in row) for row in self.matrix)
        if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
            raise ValueError('A four-by-four matrix is required')
        if any(x.conjugate() != x for row in matrix for x in row):
            raise ValueError('A real spacetime transformation is required')
        if mm(transpose(matrix), mm(ETA, matrix)) != ETA:
            raise ValueError('Transformation does not preserve the Minkowski metric')
        if determinant(matrix) != ONE or not real_positive(matrix[0][0]):
            raise ValueError('Proper orthochronous transformations only')
        object.__setattr__(self, 'matrix', matrix)

    def after(self, earlier):
        if not isinstance(earlier, LorentzMap):
            raise ValueError('A validated Lorentz map is required')
        return LorentzMap(mm(self.matrix, earlier.matrix))

    def inverse(self):
        return LorentzMap(mm(ETA, mm(transpose(self.matrix), ETA)))

    @classmethod
    def boost(cls, axis, c, s):
        c, s = Q.coerce(c), Q.coerce(s)
        if axis not in (1, 2, 3) or c * c - s * s != ONE:
            raise ValueError('Spatial axis and exact hyperbolic pair required')
        matrix = [list(row) for row in IDENTITY]
        matrix[0][0] = matrix[axis][axis] = c
        matrix[0][axis] = matrix[axis][0] = s
        return cls(tuple(tuple(row) for row in matrix))

    @classmethod
    def rotation(cls, axis, c, s):
        c, s = Q.coerce(c), Q.coerce(s)
        if axis not in (1, 2, 3) or c * c + s * s != ONE:
            raise ValueError('Spatial axis and exact circular pair required')
        i, j = {1: (2, 3), 2: (3, 1), 3: (1, 2)}[axis]
        matrix = [list(row) for row in IDENTITY]
        matrix[i][i] = matrix[j][j] = c
        matrix[i][j], matrix[j][i] = -s, s
        return cls(tuple(tuple(row) for row in matrix))

    @classmethod
    def null_rotation(cls, a, b):
        """Fix (1,0,0,1); e_x->e_x+a*k0 and e_y->e_y+b*k0."""
        a, b = Q.coerce(a), Q.coerce(b)
        r = (a * a + b * b) / 2
        return cls(((ONE + r, a, b, -r), (a, ONE, ZERO, -a),
                    (b, ZERO, ONE, -b), (r, a, b, ONE - r)))


@dataclass(frozen=True)
class TransportedWave:
    label: str
    origin: AdaptedPlaneWave
    frame: LorentzMap
    momentum: tuple
    polarization: tuple
    parent: str | None
    operation: str
    transformation: LorentzMap | None
    gauge_parameter: Q


class PhotonTransportLedger:
    def __init__(self, adapter):
        if not isinstance(adapter, SeedMaxwellAdapter):
            raise ValueError('The explicit conditional Maxwell adapter is required')
        self.adapter = adapter
        self._serial = count()
        self._waves = {}

    def _register(self, origin, frame, momentum, polarization, parent, operation, transformation=None, gauge=ZERO):
        momentum, polarization = vector(momentum, 4), vector(polarization, 4)
        validate_wave(momentum, polarization)
        if not real_positive(momentum[0]):
            raise ValueError('Future-directed transported momentum required')
        if mv(frame.matrix, origin.momentum) != momentum:
            raise ValueError('Momentum is not bound to this retained frame')
        decoded = self.adapter.decode(mv(frame.inverse().matrix, polarization))
        if decoded != origin.seed_coefficients or origin.packets != self.adapter.packets:
            raise ValueError('Transport did not preserve the origin seed modulo gauge')
        out = TransportedWave(f'lorentz-wave:{next(self._serial)}', origin, frame, momentum,
                              polarization, parent, operation, transformation, Q.coerce(gauge))
        self._waves[out.label] = out
        return out

    def resolve(self, wave):
        if not isinstance(wave, TransportedWave) or self._waves.get(wave.label) is not wave:
            raise ValueError('Unknown, foreign or substituted transport record')
        return wave

    def start(self, seed, gauge=ZERO):
        origin = self.adapter.encode(seed, gauge)
        return self._register(origin, LorentzMap(IDENTITY), origin.momentum, origin.polarization,
                              None, 'origin')

    def transport(self, wave, transformation):
        wave = self.resolve(wave)
        if not isinstance(transformation, LorentzMap):
            raise ValueError('A validated Lorentz map is required')
        return self._register(wave.origin, transformation.after(wave.frame),
                              mv(transformation.matrix, wave.momentum), mv(transformation.matrix, wave.polarization),
                              wave.label, 'lorentz', transformation)

    def regauge(self, wave, parameter):
        wave = self.resolve(wave)
        parameter = Q.coerce(parameter)
        polarization = tuple(e + parameter * k for e, k in zip(wave.polarization, wave.momentum))
        return self._register(wave.origin, wave.frame, wave.momentum, polarization,
                              wave.label, 'gauge', gauge=parameter)

    def decode(self, wave):
        wave = self.resolve(wave)
        return self.adapter.decode(mv(wave.frame.inverse().matrix, wave.polarization))

    def deconstruct(self, wave):
        wave = self.resolve(wave)
        parent = self._waves[wave.parent] if wave.parent is not None else None
        return parent, wave.operation, wave.transformation, wave.gauge_parameter

    def history(self, wave):
        wave = self.resolve(wave)
        records = []
        while wave is not None:
            records.append(wave)
            wave = self._waves[wave.parent] if wave.parent is not None else None
        return tuple(reversed(records))
