#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/determinant-cross-minor-reference.json"


def invariants(m):
    P = m[0, 0] * m[1, 1]
    X = m[0, 1] * m[1, 0]
    return P, X, P - X


def main():
    determinant_map = Matrix([[1, -1]])
    kernel = determinant_map.nullspace()
    assert kernel == [Matrix([1, 1])]

    diagonal_reference = Matrix([[1, 0]])
    sum_reference = Matrix([[1, 1]])
    blind_reference = Matrix([[1, -1]])
    assert Matrix.vstack(determinant_map, diagonal_reference).rank() == 2
    assert Matrix.vstack(determinant_map, sum_reference).rank() == 2
    assert Matrix.vstack(determinant_map, blind_reference).rank() == 1

    m0 = Matrix([[2, 0], [0, 1]])
    m1 = Matrix([[Rational(3, 2), Rational(1, 2)],
                 [Rational(1, 2), Rational(3, 2)]])
    p0, x0, d0 = invariants(m0)
    p1, x1, d1 = invariants(m1)
    assert m0.trace() == m1.trace() == 3
    assert d0 == d1 == 2
    assert sorted(m0.eigenvals(), key=lambda z: float(z)) == [1, 2]
    assert sorted(m1.eigenvals(), key=lambda z: float(z)) == [1, 2]
    assert x0 == 0 and x1 == Rational(1, 4)
    assert p0 == 2 and p1 == Rational(9, 4)
    assert x0 == p0 - d0 and x1 == p1 - d1

    payload = {
        "schema": "marici.kitaev.determinant_cross_minor_reference.v1",
        "status": "pass",
        "determinant_kernel": [[1, 1]],
        "minimal_reference_condition": "alpha+beta != 0",
        "valid_references": ["diagonal_product P", "sum P+X"],
        "blind_reference": "another copy of determinant P-X",
        "positive_isospectral_hostile": {
            "shared_trace": 3, "shared_determinant": 2,
            "shared_eigenvalues": [1, 2],
            "cross_minors": [str(x0), str(x1)],
            "diagonal_products": [str(p0), str(p1)],
        },
        "theta_application_status": "frozen_pending_source_derived_entry_identification",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
