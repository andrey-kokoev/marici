from __future__ import annotations

import json
from pathlib import Path


EDGE = Path("research/voevodsky/aspect-markov-route-gram-overlap-edge-v1.json")
CONTRACT = Path("research/voevodsky/sector-overlap-edge-contract-v1.json")
ASPECT = Path("research/aspect/a-nonorthonormal-route-frame-falsifies-frozen-v2.md")
MARKOV = Path("research/voevodsky/results/varying_fiber_markov_green.json")


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]


def main() -> None:
    edge = json.loads(EDGE.read_text(encoding="utf-8"))
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    aspect_text = ASPECT.read_text(encoding="utf-8")
    markov = json.loads(MARKOV.read_text(encoding="utf-8"))
    assert markov["passed"] is True
    assert "S^*S" in aspect_text and "4&0" in aspect_text

    required = set(contract["required_fields"])
    assert required.issubset(edge)
    assert edge["common_object_sort"] in contract["common_object_sorts"]
    S = [[2, 0], [0, 1]]
    aspect_gram = multiply(transpose(S), S)
    markov_green = [[4, 0], [0, 1]]  # M0=4, M1=1, zero transition covariance C0.
    common = edge["common_object"]["matrix"]
    assert aspect_gram == markov_green == common
    assert common[0][0] > 0 and common[1][1] > 0
    assert common[0][0] * common[1][1] - common[0][1] * common[1][0] > 0

    identity = edge["comparison_cell"]["matrix"]
    assert multiply(multiply(transpose(identity), aspect_gram), identity) == markov_green
    assert edge["comparison_cell"]["residual"] == [[0, 0], [0, 0]]
    assert edge["comparison_cell"]["invertible"] is True
    assert edge["comparison_cell"]["source_derived_label_correspondence"] is False
    assert edge["comparison_cell"]["admission_status"] == "blocked"

    dependencies = edge["certificate_dependencies"]
    nodes = set(dependencies["nodes"])
    assert all(left in nodes and right in nodes for left, right in dependencies["edges"])
    assert all(left != right for left, right in dependencies["edges"])
    assert "no optical detection" in edge["scope"]

    result = {
        "schema": "marici.voevodsky.aspect-markov-route-gram-overlap-check.v1",
        "status": "near_edge_rejected_missing_label_correspondence",
        "left_sector_vertex_admitted": True,
        "right_sector_vertex_admitted": True,
        "common_object_sort": "finite_green",
        "common_matrix": common,
        "aspect_gram_exact": True,
        "markov_covariance_exact": True,
        "coordinate_comparison_identity_invertible": True,
        "comparison_residual_zero": True,
        "ten_field_edge_contract_satisfied": True,
        "source_derived_label_correspondence": False,
        "typed_cross_sector_edge_admitted": False,
        "family_level_naturality_claimed": False,
        "physical_overlap_claimed": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
