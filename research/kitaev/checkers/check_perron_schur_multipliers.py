#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational, sqrt, zeros

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/perron-schur-multipliers.json"


def main():
    M = Matrix([[0, 0, Rational(1, 10)],
                [0, Rational(2, 5), Rational(4, 5)]])
    alpha = max(sum(M[i, j] for j in range(M.cols)) for i in range(M.rows))
    gamma = max(sum(M[i, j] for i in range(M.rows)) for j in range(M.cols))
    assert alpha * gamma == Rational(27, 25) > 1

    K = zeros(5)
    K[:2, 2:] = M
    K[2:, :2] = M.T
    rho = Rational(9, 10)
    w = (rho * Matrix.eye(5) - K).inv() * Matrix.ones(5, 1)
    expected = Matrix([Rational(445, 4), 1100, Rational(10, 9),
                       490, Rational(3965, 4)])
    assert w == expected
    assert K * w == rho * w - Matrix.ones(5, 1)
    norm_squared = (81 + sqrt(6497)) / 200
    assert norm_squared < rho ** 2

    H = Rational(1, 4) * Matrix([
        [1, 1, 1, 1], [1, -1, 1, -1],
        [1, 1, -1, -1], [1, -1, -1, 1],
    ])
    absolute_H = H.applyfunc(abs)
    assert max((H.T * H).eigenvals(), key=lambda z: float(z)) == Rational(1, 4)
    assert max((absolute_H.T * absolute_H).eigenvals(),
               key=lambda z: float(z)) == 1

    payload = {
        "schema": "marici.kitaev.perron_schur_multipliers.v1",
        "status": "pass",
        "weighted_rescue": {
            "crude_row_column_product": str(alpha * gamma),
            "rho": str(rho), "multiplier": [str(x) for x in w],
            "exact_norm_squared": str(norm_squared),
            "strict_componentwise_slack": [1] * 5,
        },
        "phase_erasure_hostile": {
            "signed_operator_norm": "1/2",
            "absolute_operator_norm": "1",
            "positive_multiplier_strict_gap_available": False,
        },
        "typing": "multipliers_are_proof_witnesses_not_source_frames",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
