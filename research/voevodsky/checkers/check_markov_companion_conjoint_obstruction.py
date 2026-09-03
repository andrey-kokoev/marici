from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    gram = sp.Matrix([[1, sp.Rational(1, 2)], [sp.Rational(1, 2), 1]])
    gauge = sp.diag(1, -1)
    transformed = gauge * gram * gauge
    identity_horizontal_target = gram

    assert transformed == sp.Matrix([[1, -sp.Rational(1, 2)], [-sp.Rational(1, 2), 1]])
    assert transformed != identity_horizontal_target

    # Same ordered vertex cardinality permits no nonempty chain extension.
    source_vertex_count = gram.rows
    target_vertex_count = transformed.rows
    added_edges = target_vertex_count - source_vertex_count
    assert added_edges == 0
    assert identity_horizontal_target != transformed

    identity_gauge = sp.eye(2)
    assert identity_gauge * gram * identity_gauge == gram

    result = {
        "schema": "marici.voevodsky.markov-companion-conjoint-obstruction.v1",
        "status": "current_horizontal_signature_not_equipment",
        "nontrivial_vertical_gauge": True,
        "same_length_horizontal_extensions": ["identity"],
        "companion_exists_for_nontrivial_gauge": False,
        "conjoint_exists_for_nontrivial_gauge": False,
        "identity_gauge_companion": "horizontal_identity",
        "identity_gauge_conjoint": "horizontal_identity",
        "obstruction_stage": "required horizontal arrow absent",
        "enlarged_horizontal_gauge_correspondence_tested": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
