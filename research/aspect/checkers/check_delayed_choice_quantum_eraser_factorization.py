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

    def encode(self) -> dict[str, str]:
        return {"real": str(self.real), "imag": str(self.imag)}


C = QComplex
ZERO = C()
ONE = C(F(1))
HALF = C(F(1, 2))
Matrix = list[list[QComplex]]


def mm(a: Matrix, b: Matrix) -> Matrix:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO) for j in range(len(b[0]))] for i in range(len(a))]


def add(*matrices: Matrix) -> Matrix:
    return [[sum((m[i][j] for m in matrices), ZERO) for j in range(len(matrices[0][0]))] for i in range(len(matrices[0]))]


def kron(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])] for j in range(len(a[0]) * len(b[0]))] for i in range(len(a) * len(b))]


def tr(a: Matrix) -> QComplex:
    return sum((a[i][i] for i in range(len(a))), ZERO)


def instrument(rho: Matrix, projector: Matrix, on_signal: bool) -> Matrix:
    identity = [[ONE, ZERO], [ZERO, ONE]]
    k = kron(projector, identity) if on_signal else kron(identity, projector)
    return mm(mm(k, rho), k)


def signal_projector(phase: QComplex, record: int) -> Matrix:
    sign = F(record)
    return [
        [HALF, phase.conj().scale(sign * F(1, 2))],
        [phase.scale(sign * F(1, 2)), HALF],
    ]


def marker_eraser_projector(record: int) -> Matrix:
    off = C(F(record, 2))
    return [[HALF, off], [off, HALF]]


def marker_path_projector(record: int) -> Matrix:
    return [[ONE, ZERO], [ZERO, ZERO]] if record == 0 else [[ZERO, ZERO], [ZERO, ONE]]


def dephase_signal(rho: Matrix) -> Matrix:
    return [[rho[i][j] if i // 2 == j // 2 else ZERO for j in range(4)] for i in range(4)]


def probability(rho: Matrix, signal_p: Matrix, marker_p: Matrix, signal_first: bool) -> QComplex:
    if signal_first:
        continuation = instrument(instrument(rho, signal_p, True), marker_p, False)
    else:
        continuation = instrument(instrument(rho, marker_p, False), signal_p, True)
    return tr(continuation)


def main() -> None:
    phases = [C(F(1)), C(imag=F(1)), C(F(-1)), C(imag=F(-1))]
    cosines = [F(1), F(0), F(-1), F(0)]

    # (|00> + |11>)(<00| + <11|) / 2.
    rho = [[ZERO for _ in range(4)] for _ in range(4)]
    rho[0][0] = rho[0][3] = rho[3][0] = rho[3][3] = HALF
    assert tr(rho) == ONE

    eraser_joint: dict[tuple[int, int, int], QComplex] = {}
    order_commutation_checks = 0
    local_flat_checks = 0
    for phase_index, phase in enumerate(phases):
        for signal_record in (-1, 1):
            local_probability = ZERO
            for marker_record in (-1, 1):
                ps = signal_projector(phase, signal_record)
                pm = marker_eraser_projector(marker_record)
                forward = instrument(instrument(rho, ps, True), pm, False)
                reverse = instrument(instrument(rho, pm, False), ps, True)
                assert forward == reverse
                order_commutation_checks += 1
                value = tr(forward)
                eraser_joint[phase_index, signal_record, marker_record] = value
                local_probability = local_probability + value
            assert local_probability == HALF
            local_flat_checks += 1

    conditioned_plus = []
    conditioned_minus = []
    for phase_index, cosine in enumerate(cosines):
        plus = eraser_joint[phase_index, 1, 1].scale(F(2))
        minus = eraser_joint[phase_index, 1, -1].scale(F(2))
        assert plus == C((F(1) + cosine) / 2)
        assert minus == C((F(1) - cosine) / 2)
        assert plus + minus == ONE
        conditioned_plus.append(plus.real)
        conditioned_minus.append(minus.real)

    which_path_flat_checks = 0
    for phase in phases:
        for marker_record in (0, 1):
            marker_probability = ZERO
            signal_plus_joint = ZERO
            for signal_record in (-1, 1):
                value = probability(rho, signal_projector(phase, signal_record), marker_path_projector(marker_record), True)
                marker_probability = marker_probability + value
                if signal_record == 1:
                    signal_plus_joint = value
            assert marker_probability == HALF
            assert signal_plus_joint.scale(F(2)) == HALF
            which_path_flat_checks += 1

    dephased = dephase_signal(rho)
    dephased_flat_checks = 0
    for phase in phases:
        for marker_record in (-1, 1):
            joint = probability(dephased, signal_projector(phase, 1), marker_eraser_projector(marker_record), True)
            assert joint.scale(F(2)) == HALF
            dephased_flat_checks += 1

    result = {
        "schema": "marici.aspect.delayed-choice-quantum-eraser-factorization.v1",
        "status": "pass",
        "phase_samples": ["0", "pi/2", "pi", "3pi/2"],
        "local_flat_probability": "1/2",
        "local_flat_checks": local_flat_checks,
        "eraser_conditioned_fringe": [str(x) for x in conditioned_plus],
        "eraser_conditioned_antifringe": [str(x) for x in conditioned_minus],
        "conditioned_patterns_sum": "1 at every phase sample",
        "which_path_conditioned_flat_checks": which_path_flat_checks,
        "spacelike_instrument_order_commutation_checks": order_commutation_checks,
        "dephased_eraser_flat_checks": dephased_flat_checks,
        "later_join_changes_earlier_local_record": False,
        "classical_join_required_for_conditioned_patterns": True,
        "claim_boundary": "finite ideal two-path four-phase clarification of standard quantum mechanics",
    }
    output = Path(__file__).parents[1] / "results" / "delayed_choice_quantum_eraser_factorization.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
