#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational, sqrt

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/hilbert-schmidt-overlap-budget.json"


def main():
    R = Matrix([[Rational(1, 3), Rational(1, 4)],
                [0, Rational(1, 5)]])
    beta = sum(x * x for x in R)
    assert beta == Rational(769, 3600)
    schur = Matrix.eye(2) - R * R.T
    assert schur[0, 0] > 0 and schur.det() > 0
    guaranteed_lower = 1 - sqrt(beta)
    assert guaranteed_lower > 0

    dim = 5
    diffuse = Rational(1, 2) * Matrix.eye(dim)
    diffuse_beta = sum(x * x for x in diffuse)
    diffuse_gram = Matrix.vstack(
        Matrix.hstack(Matrix.eye(dim), diffuse),
        Matrix.hstack(diffuse, Matrix.eye(dim)),
    )
    assert diffuse_beta == Rational(5, 4) > 1
    assert min(diffuse_gram.eigenvals(), key=lambda z: float(z)) == Rational(1, 2)

    collapse = []
    for n in (2, 4, 8, 16):
        rho = 1 - Rational(1, n)
        gram = Matrix([[1, -rho], [-rho, 1]])
        assert min(gram.eigenvals(), key=lambda z: float(z)) == Rational(1, n)
        collapse.append({"cutoff": n, "budget": str(rho ** 2),
                         "least_eigenvalue": str(Rational(1, n))})

    payload = {
        "schema": "marici.kitaev.hilbert_schmidt_overlap_budget.v1",
        "status": "pass",
        "certifying_fixture": {
            "squared_overlap_budget": str(beta),
            "guaranteed_schur_gap": str(guaranteed_lower),
            "schur_positive": True,
        },
        "sufficient_not_necessary_hostile": {
            "dimension": dim,
            "operator_norm": "1/2",
            "squared_hilbert_schmidt_norm": str(diffuse_beta),
            "block_gram_lower_bound": "1/2",
        },
        "budget_closure_family": collapse,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
