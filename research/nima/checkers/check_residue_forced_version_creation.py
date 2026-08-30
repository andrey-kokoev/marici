"""Positive and negative controls for residue-forced version creation."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def truncate(poly: sp.Expr, x: sp.Symbol, maximum_degree: int) -> sp.Expr:
    expanded = sp.Poly(sp.expand(poly), x)
    return sp.expand(
        sum(
            coefficient * x**degree
            for (degree,), coefficient in expanded.terms()
            if degree <= maximum_degree
        )
    )


def main() -> None:
    x, c = sp.symbols("x c")
    nonsplit_depths = []
    for depth in range(1, 9):
        # A section of A_(d+1) -> A_d must lift x to x+c*x^(d+1).
        lifted_generator = x + c * x ** (depth + 1)
        relation_image = truncate(lifted_generator ** (depth + 1), x, depth + 1)
        assert relation_image == x ** (depth + 1)
        assert relation_image != 0
        nonsplit_depths.append(depth)

    # Explicit d=2 collision: equal visible product, unequal extension residue.
    u = 1 + x
    v = 1 + x**2
    u_prime = 1
    v_prime = 1 + x + x**2
    visible = truncate(u * v, x, 2)
    visible_prime = truncate(u_prime * v_prime, x, 2)
    residue = sp.expand(u * v).coeff(x, 3)
    residue_prime = sp.expand(u_prime * v_prime).coeff(x, 3)
    assert visible == visible_prime == 1 + x + x**2
    assert residue == 1
    assert residue_prime == 0

    # Backward compatibility is canonical; forward upgrade is fiber-valued.
    # Over F_3, each depth-d coefficient tuple has exactly three depth-(d+1)
    # lifts, indexed by the new coefficient.
    fiber_cardinalities = {}
    for depth in range(1, 7):
        old_values = list(product(range(3), repeat=depth + 1))
        new_values = list(product(range(3), repeat=depth + 2))
        counts = {old: 0 for old in old_values}
        for new in new_values:
            counts[new[:-1]] += 1
        assert set(counts.values()) == {3}
        fiber_cardinalities[str(depth)] = 3

    # A compatible finite inverse-limit history is uniquely determined by its
    # deepest coefficient tuple; projections do not supply missing coefficients.
    maximum_depth = 5
    deepest_states = list(product(range(3), repeat=maximum_depth + 1))
    histories = {
        tuple(tuple(state[: depth + 1]) for depth in range(maximum_depth + 1))
        for state in deepest_states
    }
    assert len(histories) == len(deepest_states) == 3 ** (maximum_depth + 1)

    # Negative control: the existing horizontal filler is certified mistyped.
    negative_path = RESULTS / "physical_theta_graph_cell_certificate.json"
    negative = json.loads(negative_path.read_text(encoding="utf-8"))
    assert negative["passed"] is True
    stable = negative["stable_typing_signature"]
    assert stable["raw_parity_and_supported_graph_blocks_are_disjoint"] is True
    assert stable["actual_graph_projection_factorization_residual_rank_per_axis"] == [1, 1]
    assert negative["no_fit_rule"].startswith("No higher cell")

    result = {
        "status": "PASS",
        "positive_control": {
            "family": "A_d=k[x]/(x^(d+1))",
            "successor_schema_family_predeclared_by_source": True,
            "nonsplit_depths": nonsplit_depths,
            "shared_visible_product": str(visible),
            "distinct_residues": [int(residue), int(residue_prime)],
            "compatibility_projection_fiber_cardinalities_over_F3": fiber_cardinalities,
            "canonical_forward_upgrade_exists": False,
            "compatible_histories_through_depth_5": len(histories),
            "history_equals_deepest_state_count": True,
            "disposition": "forced adoption and fiber population inside a predeclared tower",
        },
        "negative_control": {
            "system": "physical three-wall horizontal graph filler",
            "raw_graph_intersection_dimension": 0,
            "factorization_residual_rank_per_axis": [1, 1],
            "disposition": "blocked residue; no successor version authorized",
        },
        "criterion": (
            "Residue may force adoption of a source-derived conservative nonsplit successor; "
            "it does not create or authorize the successor schema."
        ),
    }
    output = RESULTS / "residue-forced-version-creation.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
