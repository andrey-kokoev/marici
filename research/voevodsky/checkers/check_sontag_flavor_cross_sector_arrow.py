from __future__ import annotations

import json
from pathlib import Path


RESULT = Path("research/sontag/results/calibration_authority_cross_sector_witness.json")
SOURCE = Path("research/flavor/results/wp549_temporal_scale_calibration_contract.json")


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    assert result["all_passed"] is True
    assert result["passed"] == result["total"] == 15
    assert result["source"] == str(SOURCE).replace("\\", "/")
    checks = result["checks"]
    assert checks["source_checker_passed"] is True
    assert checks["calibration_is_state_establishing"] is True
    assert checks["fitted_row_does_not_establish_state"] is True

    # Audit the declared interface rather than inferring one from the title.
    serialized = json.dumps(result, sort_keys=True)
    computad_sorts = {"carrier", "gauge_presentation", "finite_green", "quotient_form", "closed_form"}
    declared_sorts = sorted(sort for sort in computad_sorts if sort in serialized)
    assert declared_sorts == []
    assert "computad_incidence" not in result
    assert "overlap_map" not in result
    assert source

    output = {
        "schema": "marici.voevodsky.sontag-flavor-cross-sector-arrow.v1",
        "status": "evidence_dependency_not_computad_overlap_verified",
        "source_result_exists": True,
        "cross_sector_witness_checks_passed": 15,
        "evidence_dependency_arrow": True,
        "declared_computad_sorts": declared_sorts,
        "typed_computad_incidence_map": False,
        "typed_sector_overlap_edge": False,
        "authority_state_witness_preserved": True,
        "passed": True,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
