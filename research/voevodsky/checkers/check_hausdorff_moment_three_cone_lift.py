from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/hausdorff-moment-three-cone-lift-v1.json")


def moments(atoms: list[tuple[sp.Rational, sp.Rational]], count: int) -> list[sp.Expr]:
    return [sp.simplify(sum(weight * point**k for point, weight in atoms)) for k in range(count)]


def hankel(sequence: list[sp.Expr], size: int, shift: int = 0) -> sp.Matrix:
    return sp.Matrix(size, size, lambda i, j: sequence[i + j + shift])


def all_principal_minors_nonnegative(matrix: sp.Matrix) -> bool:
    indices = range(matrix.rows)
    for size in range(1, matrix.rows + 1):
        for subset in itertools.combinations(indices, size):
            minor = matrix.extract(subset, subset).det()
            if minor < 0:
                return False
    return True


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    positive_atoms = [
        (sp.Rational(1, 3), sp.Rational(2)),
        (sp.Rational(2, 3), sp.Rational(3)),
    ]
    sequence = moments(positive_atoms, 7)
    M0 = hankel(sequence, 3)
    Mx = hankel(sequence, 3, shift=1)
    M1x = M0 - Mx

    V = sp.Matrix([[point**i for point, _ in positive_atoms] for i in range(3)])
    W = sp.diag(*(weight for _, weight in positive_atoms))
    X = sp.diag(*(point for point, _ in positive_atoms))
    IX = sp.eye(2) - X
    assert M0 == V * W * V.T
    assert Mx == V * W * X * V.T
    assert M1x == V * W * IX * V.T
    assert all_principal_minors_nonnegative(M0)
    assert all_principal_minors_nonnegative(Mx)
    assert all_principal_minors_nonnegative(M1x)

    signed_atoms = [
        (sp.Rational(1, 2), sp.Rational(1)),
        (sp.Rational(3, 4), sp.Rational(-1, 2)),
    ]
    signed_sequence = moments(signed_atoms, 4)
    signed_M0 = hankel(signed_sequence, 2)
    assert signed_M0.det() == sp.Rational(-1, 32)

    status = contract["status"]
    assert status["positive_J_fraction"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.hausdorff-moment-three-cone-lift-check.v1",
        "status":"three_cone_moment_factorization_verified",
        "positive_atomic_hankel_cone":True,
        "positive_atomic_x_localizing_cone":True,
        "positive_atomic_one_minus_x_localizing_cone":True,
        "signed_atomic_negative_hankel_determinant":"-1/32",
        "source_divided_difference_factor":False,
        "positive_J_fraction":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
