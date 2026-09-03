from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PLAN = ROOT / "research/voevodsky/local-sobolev-weil-tower-plan-v1.json"


def main() -> None:
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    local = plan["local_objects"]
    coherence = plan["coherence"]
    comparison = plan["gaussian_comparison"]
    galerkin = plan["galerkin"]

    assert local["completion"] == "H_0^s((-L,L)) for L>0 and s>0"
    assert "bounded compact self_adjoint" in local["operator"]
    assert coherence["core_map"] == "extension_by_zero"
    assert coherence["operator_square_strict"] is False
    assert comparison["constructed"] is False
    assert comparison["required_test"] == "cutoff_limit_preserves_form_and_observer_identities"
    assert galerkin["negative_eigenvalue_finitely_falsifiable"] is True
    assert galerkin["finite_positive_compression_proves_positivity"] is False
    assert plan["raw_H_order_closure_is_prerequisite"] is False
    assert plan["rh_implication"] is False

    result = {
        "schema": "marici.voevodsky.local-sobolev-weil-tower-plan-check.v1",
        "status": "local_tower_typed_comparison_gate_exposed",
        "local_completed_form_constructed": True,
        "global_carrier_constructed": False,
        "gaussian_comparison_constructed": False,
        "next_gate": comparison["required_map"],
        "passed": True,
        "rh_implication": False
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
