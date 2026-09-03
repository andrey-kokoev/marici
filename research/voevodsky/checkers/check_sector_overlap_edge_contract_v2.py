from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path("research/voevodsky/sector-overlap-edge-contract-v2.json")
CANDIDATE = Path("research/voevodsky/aspect-markov-route-gram-overlap-edge-v1.json")
NEAR_EDGE_RESULT = Path("research/voevodsky/results/aspect_markov_route_gram_overlap.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    required = set(contract["required_fields"])
    assert len(required) == 11
    assert "common_object_identity" in required
    assert "common_object_identity" not in candidate
    assert candidate["comparison_cell"]["source_derived_label_correspondence"] is False
    assert candidate["comparison_cell"]["residual"] == [[0, 0], [0, 0]]
    assert candidate["common_object"]["matrix"] == [[4, 0], [0, 1]]

    v1_fields = {field for field in required if field != "common_object_identity"}
    assert v1_fields.issubset(candidate)
    v1_syntactic_pass = True
    v2_identity_pass = False
    admitted = v1_syntactic_pass and v2_identity_pass
    assert admitted is False

    result = {
        "schema": "marici.voevodsky.sector-overlap-edge-contract-check.v2",
        "status": "identity_provenance_regression_gate_verified",
        "required_fields": len(required),
        "v1_syntactic_fields_pass": v1_syntactic_pass,
        "equal_coordinate_matrices": True,
        "zero_coordinate_residual": True,
        "source_derived_label_correspondence": False,
        "v2_common_object_identity_pass": v2_identity_pass,
        "edge_admitted": admitted,
        "false_edge_promotion_repaired": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
