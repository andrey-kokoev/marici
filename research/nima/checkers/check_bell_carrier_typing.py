from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path


@dataclass(frozen=True)
class QRoot2:
    rational: Fraction = Fraction(0)
    root2: Fraction = Fraction(0)

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

    def encode(self) -> dict[str, str]:
        return {"rational": str(self.rational), "sqrt2": str(self.root2)}


ZERO = QRoot2()
ONE = QRoot2(Fraction(1))
QUARTER = QRoot2(Fraction(1, 4))
HALF = QRoot2(Fraction(1, 2))
INV_ROOT2 = QRoot2(root2=Fraction(1, 2))


def main() -> None:
    local_values = []
    for a0, a1, b0, b1 in product((-1, 1), repeat=4):
        value = a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1
        local_values.append(value)
    assert len(local_values) == 16
    assert set(local_values) == {-2, 2}
    assert max(abs(value) for value in local_values) == 2

    correlators = {
        (0, 0): -INV_ROOT2,
        (0, 1): -INV_ROOT2,
        (1, 0): -INV_ROOT2,
        (1, 1): INV_ROOT2,
    }
    quantum_chsh = correlators[0, 0] + correlators[0, 1] + correlators[1, 0] - correlators[1, 1]
    assert quantum_chsh == QRoot2(root2=Fraction(-2))
    assert quantum_chsh * quantum_chsh == QRoot2(Fraction(8))

    probabilities: dict[tuple[int, int, int, int], QRoot2] = {}
    for x, y in product((0, 1), repeat=2):
        for a, b in product((-1, 1), repeat=2):
            probability = QUARTER * (ONE + QRoot2(Fraction(a * b)) * correlators[x, y])
            probabilities[x, y, a, b] = probability
            # Both algebraic values 1/4 +/- sqrt(2)/8 are strictly positive.
            assert probability.rational == Fraction(1, 4)
            assert abs(probability.root2) == Fraction(1, 8)

        normalization = sum(
            (probabilities[x, y, a, b] for a, b in product((-1, 1), repeat=2)),
            ZERO,
        )
        assert normalization == ONE

    for x, a, y in product((0, 1), (-1, 1), (0, 1)):
        alice_marginal = sum((probabilities[x, y, a, b] for b in (-1, 1)), ZERO)
        assert alice_marginal == HALF
    for y, b, x in product((0, 1), (-1, 1), (0, 1)):
        bob_marginal = sum((probabilities[x, y, a, b] for a in (-1, 1)), ZERO)
        assert bob_marginal == HALF

    # Hostile: renaming each deterministic local strategy a "closure" does not change its bound.
    renamed_closure_values = list(local_values)
    assert max(abs(value) for value in renamed_closure_values) == 2
    assert (quantum_chsh * quantum_chsh).rational > 4

    result = {
        "schema": "marici.nima.bell-carrier-typing.v1",
        "status": "pass",
        "deterministic_local_strategy_count": len(local_values),
        "deterministic_local_chsh_values": sorted(set(local_values)),
        "local_absolute_bound": 2,
        "quantum_chsh": quantum_chsh.encode(),
        "quantum_chsh_squared": (quantum_chsh * quantum_chsh).encode(),
        "joint_probability_values": sorted(
            {json.dumps(value.encode(), sort_keys=True) for value in probabilities.values()}
        ),
        "normalized_context_pairs": 4,
        "alice_no_signalling_checks": 8,
        "bob_no_signalling_checks": 8,
        "hostile_renamed_closure_rejected": True,
        "claim_boundary": "finite two-setting two-record Bell typing obstruction",
    }
    output = Path(__file__).parents[1] / "results" / "bell-carrier-typing.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
