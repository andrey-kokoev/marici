"""Exact first-jet graph-object test for the physical three-wall residue."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    J = sp.Matrix([[0, 1], [1, 0], [1, 1]])
    lam = sp.Matrix([[-1, -1, 1]])
    B = sp.Matrix([[0, -1, -1], [-1, 0, -1], [0, 0, 1]])
    kappa = sp.Matrix([[1, 1, 3]])

    assert J.rank() == 2
    assert lam.rank() == 1
    assert lam * J == sp.zeros(1, 2)
    assert len(lam.nullspace()) == 2
    kernel_basis = sp.Matrix.hstack(*lam.nullspace())
    assert kernel_basis.rank() == 2
    assert J.row_join(kernel_basis).rank() == 2
    assert lam * B == kappa

    # The resolved base-motion map v -> (Bv, kappa v) lands in graph(lambda).
    resolved = B.col_join(kappa)
    graph_equation = lam.row_join(sp.Matrix([[-1]]))
    assert graph_equation * resolved == sp.zeros(1, 3)
    assert resolved.rank() == 3

    # J da = -B v is soluble exactly when kappa v = 0.
    hostile_vectors = [
        sp.Matrix([1, 0, 0]),
        sp.Matrix([0, 1, 0]),
        sp.Matrix([0, 0, 1]),
        sp.Matrix([1, 2, -1]),  # kappa(v)=0
        sp.Matrix([2, -1, 4]),
    ]
    solvability_checks = []
    for vector in hostile_vectors:
        augmented_rank = J.row_join(-B * vector).rank()
        soluble = augmented_rank == J.rank()
        predicted = (kappa * vector)[0] == 0
        assert soluble == predicted
        solvability_checks.append(
            {
                "vector": [int(value) for value in vector],
                "kappa": int((kappa * vector)[0]),
                "homogeneous_correction_exists": soluble,
            }
        )

    # Source relation and its three pair-intersection restrictions.
    q1, q2, q3 = sp.symbols("q1 q2 q3")
    p = -q1 - q2 + q3
    pair_restrictions = {
        "W1_cap_W2": sp.expand(p.subs({q1: 0, q2: 0}) - q3),
        "W1_cap_W3": sp.expand(p.subs({q1: 0, q3: 0}) + q2),
        "W2_cap_W3": sp.expand(p.subs({q2: 0, q3: 0}) + q1),
    }
    assert all(value == 0 for value in pair_restrictions.values())

    result = {
        "status": "PASS",
        "rank_J": int(J.rank()),
        "rank_lambda": int(lam.rank()),
        "lambda_J": [[int(value) for value in row] for row in (lam * J).tolist()],
        "lambda_B": [int(value) for value in (lam * B)],
        "kappa": [int(value) for value in kappa],
        "resolved_graph_rank": int(resolved.rank()),
        "graph_equation_residual": [
            [int(value) for value in row] for row in (graph_equation * resolved).tolist()
        ],
        "solvability_checks": solvability_checks,
        "pair_restriction_residuals": {key: str(value) for key, value in pair_restrictions.items()},
        "first_jet_disposition": "source-derived resolved result closes",
        "higher_coherence_disposition": "open: triple Cech/nearby-cycle D^2 not constructed",
    }

    output = Path(__file__).parents[1] / "results" / "operational-residue-three-wall-graph.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
