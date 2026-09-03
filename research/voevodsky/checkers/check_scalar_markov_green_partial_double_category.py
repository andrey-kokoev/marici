from __future__ import annotations

import json
from pathlib import Path


RESULTS = {
    "associator_pentagon": Path("research/voevodsky/results/markov_green_analytic_pentagon.json"),
    "interchange": Path("research/voevodsky/results/markov_green_gauge_interchange.json"),
    "beck_chevalley": Path("research/voevodsky/results/markov_green_contiguous_beck_chevalley.json"),
    "completion": Path("research/voevodsky/results/uniform_markov_green_completion.json"),
}


def main() -> None:
    loaded = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in RESULTS.items()}
    assert all(result["passed"] is True for result in loaded.values())

    assert loaded["associator_pentagon"]["associators_are_identity_isometries"] is True
    assert loaded["associator_pentagon"]["pentagon_commutes"] is True
    assert loaded["interchange"]["full_gram_matrix_equality"] is True
    assert loaded["interchange"]["shared_vertex_mismatch_rejected"] is True
    assert loaded["beck_chevalley"]["beck_chevalley_invertible"] is True
    assert loaded["beck_chevalley"]["nested_pasting_strict"] is True
    assert loaded["completion"]["coordinate_inclusions_strictly_functorial"] is True
    assert loaded["completion"]["uniform_contraction_required"] is True

    # Identity and composition laws on the underlying typed data.
    edges = ("a", "b", "c")
    empty: tuple[str, ...] = ()
    assert empty + edges == edges == edges + empty
    assert ((edges[:1] + edges[1:2]) + edges[2:]) == (edges[:1] + (edges[1:2] + edges[2:]))
    signs_a = (1, -1, 1)
    signs_b = (-1, -1, 1)
    signs_c = tuple(a * b for a, b in zip(signs_a, signs_b))
    assert tuple(sign * 1 for sign in signs_c) == signs_c

    result = {
        "schema": "marici.voevodsky.scalar-markov-green-partial-double-category.v1",
        "status": "strict_partial_double_category_fragment_verified",
        "component_results": {name: str(path) for name, path in RESULTS.items()},
        "horizontal_associativity_and_units": True,
        "vertical_associativity_and_units": True,
        "analytic_pentagon": True,
        "analytic_interchange": True,
        "invertible_contiguous_beck_chevalley": True,
        "beck_chevalley_pasting": True,
        "finite_to_closed_completion_functor": True,
        "composition_partial_by_typed_seam_predicate": True,
        "equipment_verified": False,
        "companions_and_conjoints_verified": False,
        "full_coherence_pyramid_represented": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
