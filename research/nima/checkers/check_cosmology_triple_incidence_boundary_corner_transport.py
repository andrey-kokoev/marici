"""Exact local transport type at the triple-incidence divisor.

The source walls admit coordinates u=q1 and v=q2 with q3=u+v+p.  This
checker distinguishes the resulting relative boundary-corner collision from
the ordinary interior A1 folds used in earlier positive activation results.
"""

from __future__ import annotations

import json
from pathlib import Path

NIMA = Path(__file__).resolve().parents[1]
OUT = NIMA / "results" / "cosmology_triple_incidence_boundary_corner_transport.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def main() -> None:
    source = load("cosmology_source_principal_wall_cell.json")
    coefficient = load("cosmology_triple_incidence_physical_coefficient.json")
    authority = load("cosmology_analytic_continuation_authority_gate.json")

    # Fiber gradients in (a,b), ordered as q1,q2,q3.
    gradients = [(0, 1), (1, 0), (1, 1)]
    circuit = [-1, -1, 1]
    normal_sum = [
        sum(circuit[i] * gradients[i][j] for i in range(3))
        for j in range(2)
    ]
    assert normal_sum == [0, 0]
    assert source["wall_relation_coefficients"] == circuit

    # In local coordinates u=q1, v=q2 the source identity gives q3=u+v+p.
    # The three pairwise vertices are (0,0), (0,-p), and (-p,0), and coalesce
    # only at p=0.
    pairwise_vertices = {
        "q1_q2": ["0", "0"],
        "q1_q3": ["0", "-p"],
        "q2_q3": ["-p", "0"],
    }
    assert source["remaining_wall_on_pair_intersections"]["q1_q2"] == "x + y + 3*z"

    # The circuit has mixed signs under either projective rescaling, unlike the
    # common-sign multiplier frame of an ordinary interior physical fold.
    common_sign_multiplier_frame = len(set(circuit)) == 1
    assert common_sign_multiplier_frame is False

    # The Cayley--Menger cover is nonsingular at a generic incidence point:
    # x=1,y=3 avoids x=2y, x=-y, and 2x=y.  Hence the degeneration belongs to
    # the marked-wall arrangement, not to a simultaneous K=0 fiber pinch.
    x, y = 1, 3
    restricted_k_numerator = 64 * (x - 2 * y) ** 2 * (x + y) ** 2 * (2 * x - y) ** 2
    assert restricted_k_numerator != 0
    assert coefficient["algebraic_coefficient_generically_nonzero"] is True
    assert coefficient["restricted_cover_generically_split_over_function_field"] is True

    assert authority["source_authorized_local_boundary_germ_present"] is True
    assert authority["local_regulator_sign_on_positive_cone"] == -1

    packet = {
        "schema": "marici.cosmology-triple-incidence-boundary-corner-transport.v1",
        "local_coordinates": {"u": "q1", "v": "q2", "q3": "u+v+p"},
        "pairwise_vertices": pairwise_vertices,
        "vertices_coalesce_at": "p=0",
        "fiber_normal_circuit": circuit,
        "common_sign_interior_fold_multiplier_frame": False,
        "generic_cayley_menger_boundary_at_collision": False,
        "generic_algebraic_coefficient_nonzero": True,
        "source_boundary_side": "p-i*(epsilon1+epsilon2+3*epsilon3)",
        "transport_type": "relative marked-wall boundary-corner collision",
        "ordinary_interior_A1_intersection_one_precedent_applicable": False,
        "required_resolution": "blow up the coalescing three-vertex boundary corner while retaining ordered wall and deck labels",
        "picard_lefschetz_variation_computed": False,
        "physical_period_activated": False,
        "conclusion": (
            "the local p-i0 germ reaches a source-derived three-wall boundary-corner "
            "degeneration, but the ordinary interior-fold criterion cannot assign "
            "intersection magnitude one; a relative corner blow-up transport is required"
        ),
        "next_gate": (
            "construct the oriented real blow-up of (u,v,p)=(0,0,0), lift the "
            "p-i0 source germ, and compute the variation of the sewn relative chain"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
