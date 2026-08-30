#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/phase-sensitive-correlation-gram.json"


def max_abs_row_load(h):
    return max(sum(abs(h[i, j]) for j in range(h.cols))
               for i in range(h.rows))


def main():
    R = Rational(1, 4) * Matrix([
        [1, 1, 1, 1], [1, -1, 1, -1],
        [1, 1, -1, -1], [1, -1, -1, 1],
    ])
    correlation = R.T * R
    assert correlation == Rational(1, 4) * Matrix.eye(4)
    assert max_abs_row_load(correlation) == Rational(1, 4)

    absolute_first = R.applyfunc(abs)
    erased_correlation = absolute_first.T * absolute_first
    assert max(erased_correlation.eigenvals(), key=lambda z: float(z)) == 1

    pileup = Rational(1, 2) * Matrix([[1, 1, 1, 1, 1]])
    pileup_correlation = pileup.T * pileup
    assert all(pileup_correlation[j, j] == Rational(1, 4) for j in range(5))
    assert max(pileup_correlation.eigenvals(), key=lambda z: float(z)) == Rational(5, 4)

    gersh_false_negative = Matrix([
        [Rational(3, 5), Rational(1, 5), -Rational(1, 5)],
        [Rational(1, 5), Rational(3, 5), Rational(1, 5)],
        [-Rational(1, 5), Rational(1, 5), Rational(3, 5)],
    ])
    assert min(gersh_false_negative.eigenvals(), key=lambda z: float(z)) > 0
    assert max(gersh_false_negative.eigenvals(), key=lambda z: float(z)) == Rational(4, 5)
    assert max_abs_row_load(gersh_false_negative) == 1

    payload = {
        "schema": "marici.kitaev.phase_sensitive_correlation_gram.v1",
        "status": "pass",
        "hadamard_phase_recovery": {
            "correlation_gram": "(1/4) I_4",
            "signed_operator_norm": "1/2",
            "absolute_first_operator_norm": "1",
        },
        "diagonal_only_failure": {
            "each_column_energy": "1/4",
            "actual_operator_norm_squared": "5/4",
        },
        "gershgorin_sufficient_not_necessary": {
            "absolute_row_load": "1",
            "actual_spectral_radius": "4/5",
        },
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
