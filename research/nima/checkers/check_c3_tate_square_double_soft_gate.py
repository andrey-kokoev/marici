"""Test the double-soft Rees cospan as a physical realization of the Tate square."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARICI = ROOT.parents[1]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    algebra = load(ROOT / "results" / "c3-occurrence-is-depth-two-jet.json")
    rees = load(MARICI / "research" / "benincasa" / "double-soft-rees-certificate.json")
    closure = load(MARICI / "research" / "benincasa" / "double-soft-cospan-closure.json")

    assert algebra["ideal_square_dimension"] == 1
    assert algebra["canonical_quadratic_map"].startswith("every nonzero class")

    assert rees["unimodular_presentation"] == ["1", "2*x", "2*y"]
    assert rees["x_rees_rank"] == 1
    assert rees["y_rees_rank"] == 1
    assert rees["new_carrier_datum"] is False
    assert closure["double_soft_rees"]["mixed_grade_rank"] == 0
    assert closure["exceptional_geometry"]["new_center"] is False
    assert closure["bridge"]["new_support_factor"] is False

    result = {
        "status": "PASS",
        "coefficient_tate_square_target_rank": algebra["ideal_square_dimension"],
        "double_soft_x_shifted_rank": rees["x_rees_rank"],
        "double_soft_y_shifted_rank": rees["y_rees_rank"],
        "double_soft_mixed_grade_rank": closure["double_soft_rees"]["mixed_grade_rank"],
        "new_center": closure["exceptional_geometry"]["new_center"],
        "new_support_factor": closure["bridge"]["new_support_factor"],
        "candidate_status": "FALSIFIED",
        "conclusion": (
            "The nonzero coefficient Tate square is not realized by the mixed grade "
            "of the audited independent double-soft Rees cospan."
        ),
        "scope": (
            "Narrow no-go for the audited double-soft candidate; other independently "
            "derived supported binary correspondences are not excluded."
        ),
    }

    output = ROOT / "results" / "c3-tate-square-double-soft-gate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
