#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational, symbols

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/analytic-fredholm-discreteness.json"


def main():
    s = symbols("s")
    K = Matrix.diag(s, Rational(1, 2))
    A = Matrix.eye(2) - K
    assert A.det() == (1 - s) / 2
    assert A.subs(s, 0).det() != 0
    assert A.subs(s, 1).nullspace() == [Matrix([1, 0])]
    inverse = A.inv()
    assert inverse == Matrix.diag(-1 / (s - 1), 2)

    scalar_readout = (Matrix([0, 1]).T * A * Matrix([0, 1]))[0]
    assert scalar_readout == Rational(1, 2)

    everywhere_K = Matrix.diag(1, s / 2)
    everywhere_A = Matrix.eye(2) - everywhere_K
    assert everywhere_A.det() == 0
    assert everywhere_A.nullspace()

    payload = {
        "schema": "marici.kitaev.analytic_fredholm_discreteness.v1",
        "status": "pass",
        "discrete_exception_fixture": {
            "invertible_base_point": "s=0",
            "exceptional_parameter": "s=1",
            "kernel": [1, 0], "inverse_pole_order": 1,
        },
        "scalar_operator_mismatch": {
            "scalar_matrix_element": "1/2",
            "operator_kernel_at_s_1": True,
        },
        "identically_singular_alternative": {
            "determinant": "0", "invertible_base_point_exists": False,
        },
        "typing": "compact analytic inversion does not itself supply a Fredholm determinant",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
