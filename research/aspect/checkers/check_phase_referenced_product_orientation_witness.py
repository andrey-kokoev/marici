from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


@dataclass(frozen=True)
class QComplex:
    real: F = F(0)
    imag: F = F(0)

    def __add__(self, other: "QComplex") -> "QComplex":
        return QComplex(self.real + other.real, self.imag + other.imag)

    def __neg__(self) -> "QComplex":
        return QComplex(-self.real, -self.imag)

    def __sub__(self, other: "QComplex") -> "QComplex":
        return self + (-other)

    def __mul__(self, other: "QComplex") -> "QComplex":
        return QComplex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def scale(self, value: F) -> "QComplex":
        return QComplex(self.real * value, self.imag * value)

    def conj(self) -> "QComplex":
        return QComplex(self.real, -self.imag)

    def norm2(self) -> F:
        return self.real * self.real + self.imag * self.imag


C = QComplex
ZERO = C()
ONE = C(F(1))
Matrix = list[list[QComplex]]
Vector = list[QComplex]


def mm(a: Matrix, b: Matrix) -> Matrix:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO) for j in range(len(b[0]))] for i in range(len(a))]


def mv(a: Matrix, v: Vector) -> Vector:
    return [sum((a[i][j] * v[j] for j in range(len(v))), ZERO) for i in range(len(a))]


def dagger(a: Matrix) -> Matrix:
    return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]


def scale_matrix(a: Matrix, value: F) -> Matrix:
    return [[entry.scale(value) for entry in row] for row in a]


def add_vector(a: Vector, b: Vector) -> Vector:
    return [a[i] + b[i] for i in range(len(a))]


def sub_vector(a: Vector, b: Vector) -> Vector:
    return [a[i] - b[i] for i in range(len(a))]


def scale_vector(a: Vector, value: F) -> Vector:
    return [entry.scale(value) for entry in a]


def vector_norm2(v: Vector) -> F:
    return sum((entry.norm2() for entry in v), F(0))


def channel_on_matrix_unit(unit: Matrix, word: Matrix) -> Matrix:
    return mm(mm(word, unit), dagger(word))


def main() -> None:
    x = [[ZERO, ONE], [ONE, ZERO]]
    z = [[ONE, ZERO], [ZERO, -ONE]]
    xz = mm(x, z)
    zx = mm(z, x)
    assert xz == scale_matrix(zx, F(-1))

    channel_equality_checks = 0
    for row in range(2):
        for col in range(2):
            unit = [[ZERO, ZERO], [ZERO, ZERO]]
            unit[row][col] = ONE
            assert channel_on_matrix_unit(unit, xz) == channel_on_matrix_unit(unit, zx)
            channel_equality_checks += 1

    horizontal = [ONE, ZERO]
    reference = mv(x, horizontal)
    signal_xz = mv(xz, horizontal)
    signal_zx = mv(zx, horizontal)
    assert reference == signal_xz
    assert signal_zx == [-entry for entry in reference]

    plus_xz = scale_vector(add_vector(reference, signal_xz), F(1, 2))
    minus_xz = scale_vector(sub_vector(reference, signal_xz), F(1, 2))
    plus_zx = scale_vector(add_vector(reference, signal_zx), F(1, 2))
    minus_zx = scale_vector(sub_vector(reference, signal_zx), F(1, 2))
    port_probabilities = {
        "XZ": {"plus": vector_norm2(plus_xz), "minus": vector_norm2(minus_xz)},
        "ZX": {"plus": vector_norm2(plus_zx), "minus": vector_norm2(minus_zx)},
    }
    assert port_probabilities["XZ"] == {"plus": F(1), "minus": F(0)}
    assert port_probabilities["ZX"] == {"plus": F(0), "minus": F(1)}

    result = {
        "schema": "marici.aspect.phase-referenced-product-orientation-witness.v1",
        "status": "pass",
        "ordered_words_differ_by_global_sign": True,
        "polarization_channel_matrix_unit_checks": channel_equality_checks,
        "polarization_channels_equal": True,
        "unreferenced_intensity_distinguishes_words": False,
        "interferometer_port_probabilities": {
            word: {port: str(value) for port, value in ports.items()}
            for word, ports in port_probabilities.items()
        },
        "phase_reference_required": True,
        "canonical_upgrade_from_polarization_channel_exists": False,
        "verdict": "A source-authorized reference converts erased product orientation into an exact bright/dark port exchange.",
        "claim_boundary": "finite exact ideal coherent orientation witness",
    }
    output = Path(__file__).parents[1] / "results" / "phase_referenced_product_orientation_witness.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
