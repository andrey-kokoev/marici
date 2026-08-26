from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from pathlib import Path


@dataclass(frozen=True)
class QRoot2:
    rational: F = F(0)
    root2: F = F(0)

    def __add__(self, other: "QRoot2") -> "QRoot2":
        return QRoot2(self.rational + other.rational, self.root2 + other.root2)

    def __neg__(self) -> "QRoot2":
        return QRoot2(-self.rational, -self.root2)

    def __sub__(self, other: "QRoot2") -> "QRoot2":
        return self + (-other)

    def __mul__(self, other: "QRoot2") -> "QRoot2":
        return QRoot2(
            self.rational * other.rational + 2 * self.root2 * other.root2,
            self.rational * other.root2 + self.root2 * other.rational,
        )

    def scale(self, value: F) -> "QRoot2":
        return QRoot2(self.rational * value, self.root2 * value)

    def encode(self) -> dict[str, str]:
        return {"rational": str(self.rational), "sqrt2": str(self.root2)}


Q = QRoot2
ZERO = Q()
ONE = Q(F(1))
HALF = Q(F(1, 2))
QUARTER = Q(F(1, 4))
INV_ROOT2 = Q(root2=F(1, 2))
Matrix = list[list[QRoot2]]


def mm(a: Matrix, b: Matrix) -> Matrix:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO) for j in range(len(b[0]))] for i in range(len(a))]


def add(*matrices: Matrix) -> Matrix:
    return [[sum((m[i][j] for m in matrices), ZERO) for j in range(len(matrices[0][0]))] for i in range(len(matrices[0]))]


def scale(a: Matrix, value: F) -> Matrix:
    return [[entry.scale(value) for entry in row] for row in a]


def kron(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])] for j in range(len(a[0]) * len(b[0]))] for i in range(len(a) * len(b))]


def tr(a: Matrix) -> QRoot2:
    return sum((a[i][i] for i in range(len(a))), ZERO)


def projector(observable: Matrix, record: int) -> Matrix:
    identity = [[ONE, ZERO], [ZERO, ONE]]
    return scale(add(identity, scale(observable, F(record))), F(1, 2))


def instrument(rho: Matrix, local_projector: Matrix, on_alice: bool) -> Matrix:
    identity = [[ONE, ZERO], [ZERO, ONE]]
    k = kron(local_projector, identity) if on_alice else kron(identity, local_projector)
    return mm(mm(k, rho), k)


def joint_instrument(rho: Matrix, pa: Matrix, pb: Matrix) -> Matrix:
    k = kron(pa, pb)
    return mm(mm(k, rho), k)


def partial_trace_alice(rho: Matrix) -> Matrix:
    return [[sum((rho[2 * a + b][2 * a + bp] for a in range(2)), ZERO) for bp in range(2)] for b in range(2)]


def main() -> None:
    identity = [[ONE, ZERO], [ZERO, ONE]]
    x = [[ZERO, ONE], [ONE, ZERO]]
    z = [[ONE, ZERO], [ZERO, -ONE]]
    b0 = scale(add(z, x), F(1, 1))
    b0 = [[entry * INV_ROOT2 for entry in row] for row in b0]
    b1 = [[entry * INV_ROOT2 for entry in row] for row in add(z, scale(x, F(-1)))]
    alice_observables = {0: z, 1: x}
    bob_observables = {0: b0, 1: b1}

    rho = [[ZERO for _ in range(4)] for _ in range(4)]
    rho[1][1] = rho[2][2] = HALF
    rho[1][2] = rho[2][1] = -HALF
    assert tr(rho) == ONE

    probabilities: dict[tuple[int, int, int, int], QRoot2] = {}
    correlators: dict[tuple[int, int], QRoot2] = {}
    static_table_matches = 0
    for x_setting, y_setting in product((0, 1), repeat=2):
        correlation = ZERO
        expected_e = -INV_ROOT2 if (x_setting, y_setting) != (1, 1) else INV_ROOT2
        for a, b in product((-1, 1), repeat=2):
            continuation = joint_instrument(
                rho,
                projector(alice_observables[x_setting], a),
                projector(bob_observables[y_setting], b),
            )
            probability = tr(continuation)
            static_probability = QUARTER * (ONE + Q(F(a * b)) * expected_e)
            assert probability == static_probability
            static_table_matches += 1
            probabilities[x_setting, y_setting, a, b] = probability
            correlation = correlation + probability.scale(F(a * b))
        assert sum((probabilities[x_setting, y_setting, a, b] for a, b in product((-1, 1), repeat=2)), ZERO) == ONE
        assert correlation == expected_e
        correlators[x_setting, y_setting] = correlation

    for x_setting, a in product((0, 1), (-1, 1)):
        marginals = []
        for y_setting in (0, 1):
            marginals.append(sum((probabilities[x_setting, y_setting, a, b] for b in (-1, 1)), ZERO))
        assert marginals == [HALF, HALF]
    for y_setting, b in product((0, 1), (-1, 1)):
        marginals = []
        for x_setting in (0, 1):
            marginals.append(sum((probabilities[x_setting, y_setting, a, b] for a in (-1, 1)), ZERO))
        assert marginals == [HALF, HALF]

    chsh = correlators[0, 0] + correlators[0, 1] + correlators[1, 0] - correlators[1, 1]
    assert chsh == Q(root2=F(-2))
    assert chsh * chsh == Q(F(8))
    local_values = [a0 * b0v + a0 * b1v + a1 * b0v - a1 * b1v for a0, a1, b0v, b1v in product((-1, 1), repeat=4)]
    assert len(local_values) == 16 and set(local_values) == {-2, 2}

    z_plus = projector(z, 1)
    z_minus = projector(z, -1)
    x_plus = projector(x, 1)
    x_minus = projector(x, -1)
    alice_z_plus = instrument(rho, z_plus, True)
    zz_repeat = tr(instrument(alice_z_plus, z_plus, True)).scale(F(2))
    after_x_unread = add(instrument(alice_z_plus, x_plus, True), instrument(alice_z_plus, x_minus, True))
    zxz_repeat = tr(instrument(after_x_unread, z_plus, True)).scale(F(2))
    assert zz_repeat == ONE
    assert zxz_repeat == HALF
    bob_after_nonselective_z = partial_trace_alice(add(alice_z_plus, instrument(rho, z_minus, True)))
    assert bob_after_nonselective_z == scale(identity, F(1, 2))

    result = {
        "schema": "marici.aspect.combined-bell-instrument.v1",
        "status": "pass",
        "instrument_records_forgotten_to_static_table": static_table_matches,
        "normalized_joint_contexts": 4,
        "no_signalling_marginal_checks": 8,
        "deterministic_local_strategy_count": len(local_values),
        "deterministic_local_chsh_values": sorted(set(local_values)),
        "local_absolute_bound": 2,
        "quantum_chsh": chsh.encode(),
        "quantum_chsh_squared": (chsh * chsh).encode(),
        "zz_repeat_probability": zz_repeat.encode(),
        "zxz_repeat_probability": zxz_repeat.encode(),
        "bob_nonselective_state_unchanged": True,
        "claim_boundary": "finite exact composition of Bell joint effects and sequential Lueders continuation",
    }
    output = Path(__file__).parents[1] / "results" / "combined_bell_instrument.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
