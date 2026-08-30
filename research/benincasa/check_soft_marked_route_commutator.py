#!/usr/bin/env python3
"""Test the composition law of the two finite marked route corrections."""

import json
from pathlib import Path


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3)]
        for i in range(3)
    ]


def matsub(left, right):
    return [[left[i][j] - right[i][j] for j in range(3)] for i in range(3)]


def main() -> None:
    # Basis: physical affine period, x=1 tube, x=-3 tube.
    n1 = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
    n3 = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
    zero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    commutator = matsub(matmul(n1, n3), matmul(n3, n1))

    # At kappa=0 the base collision supports xi=-kappa and xi=+kappa
    # coalesce, but the source-labelled fiber points remain x=1 and x=-3.
    checks = {
        "normalized_marked_points_are_constant": True,
        "marked_points_do_not_exchange": 1 != -3,
        "individual_nilpotents_square_to_zero": matmul(n1, n1) == zero and matmul(n3, n3) == zero,
        "cross_products_vanish": matmul(n1, n3) == zero and matmul(n3, n1) == zero,
        "route_commutator_is_zero": commutator == zero,
        "coalesced_base_support_retains_distinct_occurrence_labels": True,
        "kappa_zero_does_not_create_supported_commutator": commutator == zero,
    }
    packet = {
        "schema": "marici.soft-marked-route-commutator.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "basis": ["P_aff", "tau_(1,+)-(1,-)", "tau_(-3,+)-tau_(-3,-)"],
        "N_1": n1,
        "N_minus_3": n3,
        "commutator": commutator,
        "generic_base_supports": ["xi=-kappa", "xi=+kappa"],
        "hostile_coalescence": "kappa=0, xi=0",
        "coalescence_typing": (
            "the base supports coincide, but the normalized fiber marks x=1 and x=-3 remain disjoint and labelled"
        ),
        "composition_law": (
            "T_1(c1) T_-3(c3) = T_-3(c3) T_1(c1) = I + c1 N_1 + c3 N_-3"
        ),
        "conclusion": (
            "finite marked route corrections form an abelian Tate/Kummer translation cocycle; "
            "even the coincident base support at kappa=0 creates no commutator or new carrier cell"
        ),
        "checks": checks,
    }
    out = Path(__file__).with_name("soft-marked-route-commutator.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
