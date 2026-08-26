#!/usr/bin/env python3
"""Exact audit of minimal endpoint/forcing incidence directions."""

import hashlib
import json
from itertools import product
from pathlib import Path

from sympy import Matrix, Rational


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/minimal-endpoint-forcing-incidence.json"


def state_operator(p, q):
    # State order is (Y,c1,c2); diagonal blocks are frozen to zero because they
    # do not affect the two-step rank theorem.
    return Matrix([
        [0, p[0], p[1]],
        [q[0], 0, 0],
        [q[1], 0, 0],
    ])


def main():
    J = Matrix.eye(2)
    C0 = Matrix([[0, 1, 0], [0, 0, 1]])
    B0 = Matrix([[0, 0], [1, 0], [0, 1]])

    dynamic_checks = 0
    for p_values, q_values in product(product((-1, 0, 1), repeat=2), repeat=2):
        p = Matrix([p_values[0], p_values[1]]).T
        q = Matrix([q_values[0], q_values[1]])
        A = state_operator(p_values, q_values)
        O2 = C0.col_join(C0 * A)
        R2 = B0.row_join(A * B0)
        assert (O2.rank() == 3) == (q != Matrix.zeros(2, 1))
        assert (R2.rank() == 3) == (p != Matrix.zeros(1, 2))
        dynamic_checks += 1

    # Static one-row theorem, including arbitrary forcing component r.
    static_checks = 0
    for alpha, r1, r2 in product((-1, 0, 1), repeat=3):
        full = C0.col_join(Matrix([[alpha, r1, r2]]))
        assert (full.rank() == 3) == (alpha != 0)
        gram = full.T * full
        assert (gram.rank() == 3) == (alpha != 0)
        static_checks += 1

    # Wrong-way coupling: reachable but unobservable.
    A_wrong = state_operator((1, 0), (0, 0))
    O_wrong = C0.col_join(C0 * A_wrong)
    R_wrong = B0.row_join(A_wrong * B0)
    assert O_wrong.rank() == 2
    assert R_wrong.rank() == 3

    # Duplicated forcing-only rows retain endpoint kernel.
    duplicated = C0.col_join(Matrix([[0, 1, 1], [0, 2, -1], [0, -3, 4]]))
    assert duplicated.rank() == 2
    assert duplicated * Matrix([1, 0, 0]) == Matrix.zeros(5, 1)

    # Finite observability with a collapsing endpoint direction.
    collapse = []
    endpoint = Matrix([1, 0, 0])
    for N in (2, 3, 5, 10, 20):
        eps = Rational(1, N)
        A_N = state_operator((0, 0), (eps, 0))
        O_N = C0.col_join(C0 * A_N)
        assert O_N.rank() == 3
        energy = (endpoint.T * O_N.T * O_N * endpoint)[0]
        assert energy == eps**2
        collapse.append({"N": N, "endpoint_energy": str(energy)})

    payload = {
        "schema": "marici.kitaev.minimal_endpoint_forcing_incidence.v1",
        "status": "pass",
        "strength": "finite-dimensional compiler theorem",
        "dynamic_direction_checks": dynamic_checks,
        "static_row_checks": static_checks,
        "minimal_static_endpoint_rows": 1,
        "wrong_way_hostile": {
            "p_nonzero": True,
            "q_nonzero": False,
            "observability_rank": O_wrong.rank(),
            "reachability_rank": R_wrong.rank(),
        },
        "duplicated_forcing_rows_rank": duplicated.rank(),
        "cutoffwise_observability_collapse": collapse,
        "limiting_endpoint_energy": "0",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "theta incidence derivation", "uniform theta observability",
            "physical controller", "passivity", "zero orientation", "RH"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
