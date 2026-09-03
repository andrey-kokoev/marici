from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/hausdorff-semigroup-gns-contraction-v1.json")


def principal_nonnegative(matrix: sp.Matrix) -> bool:
    for size in range(1, matrix.rows + 1):
        for subset in itertools.combinations(range(matrix.rows), size):
            if matrix.extract(subset, subset).det() < 0:
                return False
    return True


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    # Exact rational y=e^{-h lambda} fixture; t-weight is absorbed into W.
    y_values = [sp.Rational(1, 3), sp.Rational(3, 4)]
    weights = [sp.Rational(2), sp.Rational(5)]
    V = sp.Matrix([[value**i for value in y_values] for i in range(3)])
    W = sp.diag(*weights)
    Y = sp.diag(*y_values)
    moments = [sum(weight * value**n for value, weight in zip(y_values, weights)) for n in range(7)]
    M_y = sp.Matrix(3, 3, lambda i, j: moments[i + j])
    M_1y = sp.Matrix(3, 3, lambda i, j: moments[i + j] - moments[i + j + 1])
    assert M_y == V * W * V.T
    assert M_1y == V * W * (sp.eye(2) - Y) * V.T
    assert principal_nonnegative(M_y)
    assert principal_nonnegative(M_1y)

    # Difference moments are powers of X=1-Y in the same realization.
    X = sp.eye(2) - Y
    for order in range(6):
        direct = sum(weights[j] * (1 - y_values[j]) ** order for j in range(2))
        represented = (sp.ones(1, 2) * W * X**order * sp.ones(2, 1))[0]
        assert sp.simplify(direct - represented) == 0

    # Rational semigroup fixture Y_(m h)=Y_h^m.
    for m in range(1, 6):
        Y_m = sp.diag(*(value**m for value in y_values))
        assert Y_m == Y**m

    # Signed atom is detected by the moment cone.
    signed_weights = [sp.Rational(1), sp.Rational(-1, 2)]
    signed_moments = [sum(weight * value**n for value, weight in zip(y_values, signed_weights)) for n in range(4)]
    signed_matrix = sp.Matrix(2, 2, lambda i, j: signed_moments[i + j])
    assert signed_matrix.det() < 0

    status = contract["status"]
    assert status["cross_step_common_GNS"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.hausdorff-semigroup-gns-contraction-check.v1",
        "status":"two_cone_semigroup_fixture_verified",
        "moment_hankel_cone":True,
        "one_minus_y_localizing_cone":True,
        "difference_chart_same_contraction":True,
        "semigroup_powers_checked":5,
        "signed_atomic_detection":True,
        "source_two_cone_positivity":False,
        "cross_step_common_GNS":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
