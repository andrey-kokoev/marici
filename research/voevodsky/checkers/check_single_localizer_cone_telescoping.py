from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/single-localizer-cone-telescoping-v1.json")


def psd_by_principal_minors(matrix: sp.Matrix) -> bool:
    for size in range(1, matrix.rows + 1):
        for subset in itertools.combinations(range(matrix.rows), size):
            if matrix.extract(subset, subset).det() < 0:
                return False
    return True


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    y_values = [sp.Rational(1, 4), sp.Rational(2, 3)]
    weights = [sp.Rational(3), sp.Rational(5)]

    def moment(n: int) -> sp.Expr:
        return sum(weight * value**n for value, weight in zip(y_values, weights))

    def M(shift: int, size: int = 3) -> sp.Matrix:
        return sp.Matrix(size, size, lambda i, j: moment(i + j + shift))

    V = sp.Matrix([[value**i for value in y_values] for i in range(3)])
    W = sp.diag(*weights)
    Y = sp.diag(*y_values)
    localizer = M(0) - M(1)
    assert localizer == V * W * (sp.eye(2) - Y) * V.T
    assert psd_by_principal_minors(localizer)

    # Exact finite telescoping with its nonzero remainder.
    for cutoff in range(1, 7):
        accumulated = sum((M(r) - M(r + 1) for r in range(cutoff)), sp.zeros(3))
        assert sp.simplify(accumulated + M(cutoff) - M(0)) == sp.zeros(3)
    cutoff_symbol = sp.symbols("R", positive=True, integer=True)
    for i in range(3):
        for j in range(3):
            remainder_entry = sum(
                weight * value ** (i + j + cutoff_symbol)
                for value, weight in zip(y_values, weights)
            )
            assert sp.limit(remainder_entry, cutoff_symbol, sp.oo) == 0
    assert all(value < 1 for value in y_values)

    # Signed atom makes the localizer indefinite.
    signed_weights = [sp.Rational(1), sp.Rational(-1, 2)]
    signed_V = sp.Matrix([[value**i for value in y_values] for i in range(2)])
    signed_W = sp.diag(*signed_weights)
    signed_localizer = signed_V * signed_W * (sp.eye(2) - Y) * signed_V.T
    assert signed_localizer.det() < 0

    status = contract["status"]
    assert status["explicit_arithmetic_localizer_positivity"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.single-localizer-cone-telescoping-check.v1",
        "status":"single_cone_reduction_verified",
        "positive_atomic_localizer_factor":True,
        "telescoping_cutoffs_checked":6,
        "remainder_decay_from_atomic_support":True,
        "signed_atomic_localizer_detected":True,
        "explicit_arithmetic_localizer_positivity":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
