#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational, sqrt

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/core-tail-schur-gap.json"


def main():
    safe = Matrix([[2, -1], [-1, 3]])
    safe_eigs = sorted(safe.eigenvals(), key=lambda z: float(z))
    sharp_lower = (5 - sqrt(5)) / 2
    assert safe.det() == 5
    assert safe_eigs[0] == sharp_lower
    assert sharp_lower > 0

    threshold = Matrix([[1, -1], [-1, 1]])
    hidden = Matrix([1, 1])
    assert threshold * hidden == Matrix.zeros(2, 1)
    assert threshold[:1, :1] == Matrix([[1]])
    assert threshold[1:, 1:] == Matrix([[1]])

    collapse = []
    for n in (2, 3, 5, 10):
        rho = 1 - Rational(1, n)
        gram = Matrix([[1, -rho], [-rho, 1]])
        least = Rational(1, n)
        assert gram.det() > 0
        assert min(gram.eigenvals(), key=lambda z: float(z)) == least
        collapse.append({"cutoff": n, "normalized_cross_norm": str(rho),
                         "least_eigenvalue": str(least)})

    payload = {
        "schema": "marici.kitaev.core_tail_schur_gap.v1",
        "status": "pass",
        "finite_safe_fixture": {
            "A_lower": 2, "C_lower": 3, "cross_norm": 1,
            "sharp_lower_bound": str(sharp_lower), "determinant": 5,
        },
        "threshold_falsifier": {
            "diagonal_blocks_positive": True,
            "normalized_cross_norm": 1,
            "hidden_state": [1, 1],
        },
        "completion_collapse_family": collapse,
        "uniform_theorem": "sup_N ||A_N^-1/2 B_N C_N^-1/2|| <= 1-delta",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
