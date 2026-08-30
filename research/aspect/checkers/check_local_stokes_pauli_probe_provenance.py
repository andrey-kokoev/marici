from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
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

    def encode(self) -> dict[str, str]:
        return {"real": str(self.real), "imag": str(self.imag)}


C = QComplex
ZERO = C()
ONE = C(F(1))
I = [[ONE, ZERO], [ZERO, ONE]]
X = [[ZERO, ONE], [ONE, ZERO]]
Y = [[ZERO, C(imag=F(-1))], [C(imag=F(1)), ZERO]]
Z = [[ONE, ZERO], [ZERO, -ONE]]
PAULI = {"I": I, "X": X, "Y": Y, "Z": Z}
Matrix = list[list[QComplex]]


def mm(a: Matrix, b: Matrix) -> Matrix:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO) for j in range(len(b[0]))] for i in range(len(a))]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(a: Matrix, value: F) -> Matrix:
    return [[entry.scale(value) for entry in row] for row in a]


def kron(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])] for j in range(len(a[0]) * len(b[0]))] for i in range(len(a) * len(b))]


def tr(a: Matrix) -> QComplex:
    return sum((a[i][i] for i in range(len(a))), ZERO)


def expectation(rho: Matrix, observable: Matrix) -> QComplex:
    return tr(mm(rho, observable))


def main() -> None:
    zero2 = [[ZERO, ZERO], [ZERO, ZERO]]
    analyzer_checks = 0
    for name in ("X", "Y", "Z"):
        observable = PAULI[name]
        plus = scale(add(I, observable), F(1, 2))
        minus = scale(add(I, scale(observable, F(-1))), F(1, 2))
        assert mm(plus, plus) == plus
        assert mm(minus, minus) == minus
        assert mm(plus, minus) == zero2
        assert add(plus, minus) == I
        analyzer_checks += 4

    identity4 = kron(I, I)
    yy = kron(Y, Y)
    assert mm(yy, yy) == identity4
    coefficient = F(1, 2)
    rho_plus = scale(add(identity4, scale(yy, coefficient)), F(1, 4))
    rho_minus = scale(add(identity4, scale(yy, -coefficient)), F(1, 4))
    assert tr(rho_plus) == tr(rho_minus) == ONE

    # Since YY has eigenvalues +/-1 twice, both states have eigenvalues
    # (1 +/- coefficient)/4, each with multiplicity two.
    eigenvalues = [F(1 + coefficient, 4), F(1 + coefficient, 4), F(1 - coefficient, 4), F(1 - coefficient, 4)]
    assert all(value >= 0 for value in eigenvalues)

    restricted_equalities = 0
    for left, right in product(("I", "X", "Z"), repeat=2):
        observable = kron(PAULI[left], PAULI[right])
        assert expectation(rho_plus, observable) == expectation(rho_minus, observable)
        restricted_equalities += 1
    assert restricted_equalities == 9

    yy_plus = expectation(rho_plus, yy)
    yy_minus = expectation(rho_minus, yy)
    assert yy_plus == C(coefficient)
    assert yy_minus == C(-coefficient)

    all_coefficients_plus = {}
    all_coefficients_minus = {}
    for left, right in product(("I", "X", "Y", "Z"), repeat=2):
        key = left + right
        observable = kron(PAULI[left], PAULI[right])
        all_coefficients_plus[key] = expectation(rho_plus, observable)
        all_coefficients_minus[key] = expectation(rho_minus, observable)
    differing = [key for key in all_coefficients_plus if all_coefficients_plus[key] != all_coefficients_minus[key]]
    assert differing == ["YY"]

    result = {
        "schema": "marici.aspect.local-stokes-pauli-probe-provenance.v1",
        "status": "pass",
        "local_analyzer_projector_checks": analyzer_checks,
        "physical_local_probe_family": ["I", "X", "Y", "Z"],
        "nontrivial_joint_analyzer_settings": 9,
        "product_probe_count_with_marginals": 16,
        "restricted_ixz_product_equalities": restricted_equalities,
        "missing_y_hostile_states_positive": True,
        "only_full_probe_difference": differing,
        "rho_plus_yy_expectation": yy_plus.encode(),
        "rho_minus_yy_expectation": yy_minus.encode(),
        "y_instrument_requirement": "calibrated quarter-wave retardance plus linear polarization analysis at each port",
        "external_local_oscillator_required_for_local_stokes_y": False,
        "stable_relative_polarization_phase_calibration_required": True,
        "verdict": "All sixteen product probes are physical only when each photon port includes a calibrated local Y analyzer.",
        "claim_boundary": "finite ideal two-qubit polarization tomography with explicit analyzer provenance",
    }
    output = Path(__file__).parents[1] / "results" / "local_stokes_pauli_probe_provenance.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
