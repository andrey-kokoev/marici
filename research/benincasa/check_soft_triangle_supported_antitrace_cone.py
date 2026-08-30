"""Supported anti-trace cone for the four physical soft-triangle nodes."""

from __future__ import annotations

import json
from math import gcd

import sympy as sp


def main() -> None:
    # Source-oriented hemisphere generators H_+ and iota_*H_+ have the same
    # equator boundary.  The supported endpoint complex is therefore [1 1].
    endpoint_boundary = sp.Matrix([[1, 1]])
    anti_trace = sp.Matrix([1, -1])
    ordinary_trace = sp.Matrix([1, 1])
    assert endpoint_boundary * anti_trace == sp.zeros(1, 1)
    assert endpoint_boundary * ordinary_trace == sp.Matrix([2])
    assert gcd(abs(int(anti_trace[0])), abs(int(anti_trace[1]))) == 1
    assert endpoint_boundary.rank() == 1
    assert len(endpoint_boundary.nullspace()) == 1

    # The physical labels are ordered as in Entries 2369, 2372, and 2374.
    # q_g23 e23 - q_g31 e31 gives the integral endpoint rows below.
    nodes = [
        {"kappa": -1, "xi": -1, "t": 3, "occurrence_relation": (2, -2)},
        {"kappa": -1, "xi": 1, "t": 1, "occurrence_relation": (2, 0)},
        {"kappa": 1, "xi": -1, "t": 1, "occurrence_relation": (2, 0)},
        {"kappa": 1, "xi": 1, "t": 3, "occurrence_relation": (2, -2)},
    ]
    records = []
    for node in nodes:
        relation = sp.Matrix(node["occurrence_relation"])
        # Primitive free quotient covectors, normalized so the retained e31
        # occurrence maps to +1.
        quotient = (
            sp.Matrix([[1, 1]]) if node["t"] == 3 else sp.Matrix([[0, 1]])
        )
        assert quotient * relation == sp.zeros(1, 1)
        assert quotient[0, 1] == 1
        torsion_order = gcd(*(abs(int(value)) for value in relation))
        assert torsion_order == 2
        records.append({
            **{key: node[key] for key in ("kappa", "xi", "t")},
            "occurrence_relation": list(node["occurrence_relation"]),
            "free_occurrence_quotient": [int(value) for value in quotient],
            "integral_occurrence_torsion_order": torsion_order,
            "supported_antitrace_rank_over_Q": 1,
            "positive_sheet_antitrace_coefficient": 1,
        })

    supported_rank = sum(record["supported_antitrace_rank_over_Q"] for record in records)
    physical_image = sp.Matrix([record["positive_sheet_antitrace_coefficient"] for record in records])
    assert supported_rank == 4
    assert physical_image == sp.ones(4, 1)
    assert physical_image.rank() == 1

    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-supported-antitrace-cone.v1",
        "endpoint_complex": {
            "degree_3_generators": ["H_plus", "deck(H_plus)"],
            "degree_2_generator": "equator",
            "boundary_matrix": [[1, 1]],
            "kernel_generator": [1, -1],
            "ordinary_trace_vector": [1, 1],
            "ordinary_trace_boundary": [2],
        },
        "nodes": records,
        "supported_costalk_rank_over_Q": supported_rank,
        "physical_positive_sheet_image": [int(value) for value in physical_image],
        "physical_image_rank_before_global_pushforward": 1,
        "cyclic_assembly": "four free C3 orbits tensored with the deck-sign line",
        "global_character_before_pushforward": [12, 0, 0, -12, 0, 0],
        "status": "primitive_local_antitrace_and_diagonal_supported_physical_ray_derived",
        "scope": (
            "supported local costalks and source positive-sheet anti-trace before "
            "global pushforward; no claim of a nonzero global period, no integral "
            "lattice identification beyond the displayed occurrence presentation, "
            "and no relation between distinct node costalks"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
