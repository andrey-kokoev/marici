#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational, sqrt

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/compact-correlation-fredholm.json"


def rank_one_compression(n):
    u = Matrix([sqrt(3) / (2 ** i) for i in range(1, n + 1)])
    h = Rational(1, 2) * Matrix.eye(n) + Rational(1, 2) * u * u.T
    return u, h


def main():
    compressions = []
    for n in (1, 2, 3, 5, 8):
        u, h = rank_one_compression(n)
        norm_squared = (u.T * u)[0]
        expected_norm = 1 - Rational(1, 4 ** n)
        largest = max(h.eigenvals(), key=lambda z: float(z))
        expected_largest = 1 - Rational(1, 2 * 4 ** n)
        assert norm_squared == expected_norm
        assert largest == expected_largest < 1
        compressions.append({"cutoff": n, "truncated_eigenvector_norm_squared": str(norm_squared),
                             "largest_eigenvalue": str(largest),
                             "coercivity_gap": str(1 - largest)})

    diffuse = []
    for n in (2, 4, 8, 16):
        eigenvalue = 1 - Rational(1, n)
        assert eigenvalue < 1
        diffuse.append({"mode": n, "correlation_eigenvalue": str(eigenvalue),
                        "defect_energy": str(1 - eigenvalue)})

    payload = {
        "schema": "marici.kitaev.compact_correlation_fredholm.v1",
        "status": "pass",
        "rank_one_compact_hostile": {
            "limit_background_ceiling": "1/2",
            "compact_remainder_rank": 1,
            "limit_eigenvalue": "1",
            "finite_compressions": compressions,
        },
        "noncompact_diffuse_escape": {
            "eigenvalue_one_present": False,
            "uniform_coercivity_present": False,
            "modes": diffuse,
        },
        "fredholm_gate": "compact remainder plus background ceiling below one reduces failure to ker(I-H)",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
