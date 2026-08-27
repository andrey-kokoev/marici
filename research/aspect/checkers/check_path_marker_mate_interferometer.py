from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


@dataclass(frozen=True)
class C:
    real: F = F(0)
    imag: F = F(0)

    def __add__(self, other: "C") -> "C":
        return C(self.real + other.real, self.imag + other.imag)

    def __neg__(self) -> "C":
        return C(-self.real, -self.imag)

    def __sub__(self, other: "C") -> "C":
        return self + (-other)

    def __mul__(self, other: "C") -> "C":
        return C(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def scale(self, value: F) -> "C":
        return C(self.real * value, self.imag * value)

    def conj(self) -> "C":
        return C(self.real, -self.imag)


ZERO = C()
ONE = C(F(1))
HALF = C(F(1, 2))
Matrix = list[list[C]]


def mm(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), ZERO) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def dagger(value: Matrix) -> Matrix:
    return [[value[j][i].conj() for j in range(len(value))] for i in range(len(value[0]))]


def trace(value: Matrix) -> C:
    return sum((value[i][i] for i in range(len(value))), ZERO)


def kron(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            left[i // len(right)][j // len(right[0])] * right[i % len(right)][j % len(right[0])]
            for j in range(len(left[0]) * len(right[0]))
        ]
        for i in range(len(left) * len(right))
    ]


def transform(unitary: Matrix, rho: Matrix) -> Matrix:
    return mm(mm(unitary, rho), dagger(unitary))


def reduced_path(rho: Matrix) -> Matrix:
    return [
        [sum((rho[2 * p + marker][2 * q + marker] for marker in range(2)), ZERO) for q in range(2)]
        for p in range(2)
    ]


def signal_projector(phase: C, record: int) -> Matrix:
    sign = F(record, 2)
    return [
        [HALF, phase.conj().scale(sign)],
        [phase.scale(sign), HALF],
    ]


def marker_projector(record: int) -> Matrix:
    off = C(F(record, 2))
    return [[HALF, off], [off, HALF]]


def probability(rho: Matrix, effect: Matrix) -> F:
    value = trace(mm(effect, rho))
    assert value.imag == 0
    return value.real


def source(gamma: F) -> Matrix:
    rho = [[ZERO for _ in range(4)] for _ in range(4)]
    rho[0][0] = rho[3][3] = HALF
    rho[0][3] = rho[3][0] = C(gamma / 2)
    assert trace(rho) == ONE
    return rho


def main() -> None:
    identity = [[ONE, ZERO], [ZERO, ONE]]
    cnot_path_to_marker = [
        [ONE, ZERO, ZERO, ZERO],
        [ZERO, ONE, ZERO, ZERO],
        [ZERO, ZERO, ZERO, ONE],
        [ZERO, ZERO, ONE, ZERO],
    ]
    assert mm(cnot_path_to_marker, cnot_path_to_marker) == [
        [ONE if i == j else ZERO for j in range(4)] for i in range(4)
    ]

    phases = [C(F(1)), C(imag=F(1)), C(F(-1)), C(imag=F(-1))]
    cosines = [F(1), F(0), F(-1), F(0)]
    cases = {}

    for label, gamma in (("ideal", F(1)), ("partial_environment_overlap", F(3, 5)), ("orthogonal_environment", F(0))):
        rho = source(gamma)
        local = reduced_path(rho)
        uncomputed = transform(cnot_path_to_marker, rho)
        local_after_uncompute = reduced_path(uncomputed)
        untouched_plus = []
        conditioned_plus = []
        conditioned_minus = []
        coherent_plus = []
        late_unitary_record_invariance_checks = 0

        for phase, cosine in zip(phases, cosines):
            plus = signal_projector(phase, 1)
            untouched = probability(local, plus)
            assert untouched == F(1, 2)
            untouched_plus.append(untouched)

            conditional_values = []
            for marker_record in (1, -1):
                joint_effect = kron(plus, marker_projector(marker_record))
                joint = probability(rho, joint_effect)
                marker_probability = F(1, 2)
                conditional_values.append(joint / marker_probability)
            expected_plus = (F(1) + gamma * cosine) / 2
            expected_minus = (F(1) - gamma * cosine) / 2
            assert conditional_values == [expected_plus, expected_minus]
            assert (conditional_values[0] + conditional_values[1]) / 2 == untouched
            conditioned_plus.append(conditional_values[0])
            conditioned_minus.append(conditional_values[1])

            coherent = probability(local_after_uncompute, plus)
            assert coherent == expected_plus
            coherent_plus.append(coherent)

            # Once the signal record is formed, any later unitary continuation
            # preserves its subnormalized trace even if it acts jointly.
            signal_effect = kron(plus, identity)
            continuation = mm(mm(signal_effect, rho), signal_effect)
            after_late_unitary = transform(cnot_path_to_marker, continuation)
            assert trace(after_late_unitary) == trace(continuation)
            late_unitary_record_invariance_checks += 1

        cases[label] = {
            "environment_overlap": str(gamma),
            "untouched_unconditional_signal_plus": [str(value) for value in untouched_plus],
            "late_conditioned_fringe": [str(value) for value in conditioned_plus],
            "late_conditioned_antifringe": [str(value) for value in conditioned_minus],
            "conditioned_totalization_is_untouched_marginal": True,
            "coherent_uncompute_unconditional_signal_plus": [str(value) for value in coherent_plus],
            "coherent_uncompute_visibility": str(gamma),
            "late_joint_unitary_changes_stored_signal_probability": False,
            "late_unitary_record_invariance_checks": late_unitary_record_invariance_checks,
        }

    assert cases["ideal"]["coherent_uncompute_unconditional_signal_plus"] == ["1", "1/2", "0", "1/2"]
    assert cases["orthogonal_environment"]["coherent_uncompute_unconditional_signal_plus"] == ["1/2"] * 4

    result = {
        "schema": "marici.aspect.path-marker-mate-interferometer.v1",
        "status": "pass",
        "phase_samples": ["0", "pi/2", "pi", "3pi/2"],
        "routes": {
            "forward_joint_evolution": "flat local marginal with phase retained in path-marker correlations",
            "backward_record_conditioning": "complementary conditional fibers whose weighted total is the unchanged marginal",
            "coherent_reverse_incidence": "path-controlled marker uncomputation before detection transfers coherence into the local path marginal",
        },
        "cases": cases,
        "decisive_signature": "only coherent pre-detection uncomputation changes unconditional interference",
        "completion_gate": "inaccessible environment overlap gamma bounds both conditional and coherent recovery visibility",
        "claim_boundary": "finite ideal two-qubit instrument with a reduced-state environment-overlap parameter; no loss, multipair, detector-memory, spacelike, or continuum laboratory theorem",
    }
    output = Path(__file__).parents[1] / "results" / "path_marker_mate_interferometer.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
