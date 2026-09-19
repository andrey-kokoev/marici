from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
CONTRACT_PATH = ROOT / "contracts" / "scc-realization-provenance-gate.v1.json"
RESULT_PATH = ROOT / "results" / "scc_realization_provenance_gate.json"
ALLOWED = {"source_constructor", "explicit_assumption", "observer_fitted", "unsupported"}


def validate_arrow(arrow: dict) -> dict:
    errors = []
    required = ["id", "source", "target", "provenance_class", "completion_applicability"]
    errors.extend(f"missing:{key}" for key in required if key not in arrow)
    cls = arrow.get("provenance_class")
    if cls is not None and cls not in ALLOWED:
        errors.append("unknown:provenance_class")
    if cls == "source_constructor":
        for key in ("evidence_locator", "source_formula_or_constructor_id"):
            if not arrow.get(key):
                errors.append(f"missing:{key}")
        locator = arrow.get("evidence_locator")
        if locator and not Path(locator).exists():
            errors.append("unresolved:evidence_locator")
    if arrow.get("completion_applicability") == "applicable":
        for key in ("completion_topology", "bonding_maps", "bonding_variance", "completion_evidence_locator"):
            if not arrow.get(key):
                errors.append(f"missing:{key}")
        locator = arrow.get("completion_evidence_locator")
        if locator and not Path(locator).exists():
            errors.append("unresolved:completion_evidence_locator")
    eligible = not errors and cls == "source_constructor"
    return {"id": arrow.get("id", "missing"), "errors": errors, "promotion_eligible": eligible}


def validate_promotion(promotion: dict, arrows: dict[str, dict]) -> dict:
    checks = []
    for dependency in promotion.get("dependencies", []):
        if dependency not in arrows:
            checks.append({"id": dependency, "errors": ["missing:dependency"], "promotion_eligible": False})
        else:
            checks.append(validate_arrow(arrows[dependency]))
    return {
        "id": promotion["id"],
        "dependency_checks": checks,
        "admitted": bool(checks) and all(check["promotion_eligible"] for check in checks),
    }


def main() -> None:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    assert set(contract["provenance_classes"]) == ALLOWED

    arrows = {
        "sourced_identity": {
            "id": "sourced_identity",
            "source": "A",
            "target": "A",
            "provenance_class": "source_constructor",
            "evidence_locator": "research/aspect/contracts/scc-realization-provenance-gate.v1.json",
            "source_formula_or_constructor_id": "identity_on_A",
            "completion_applicability": "not_applicable",
        },
        "assumed_bridge": {
            "id": "assumed_bridge",
            "source": "A",
            "target": "B",
            "provenance_class": "explicit_assumption",
            "completion_applicability": "not_applicable",
        },
        "fitted_bridge": {
            "id": "fitted_bridge",
            "source": "A",
            "target": "B",
            "provenance_class": "observer_fitted",
            "completion_applicability": "not_applicable",
        },
        "common_operator_from_two_moments": {
            "id": "common_operator_from_two_moments",
            "source": "endpoint_packet",
            "target": "euler_packet",
            "provenance_class": "unsupported",
            "completion_applicability": "applicable",
        },
        "laundered_source_claim": {
            "id": "laundered_source_claim",
            "source": "A",
            "target": "B",
            "provenance_class": "source_constructor",
            "completion_applicability": "not_applicable",
        },
        "missing_class": {
            "id": "missing_class",
            "source": "A",
            "target": "B",
            "completion_applicability": "not_applicable",
        },
    }

    arrow_checks = {key: validate_arrow(value) for key, value in arrows.items()}
    promotions = [
        validate_promotion({"id": "valid_source_promotion", "dependencies": ["sourced_identity"]}, arrows),
        validate_promotion({"id": "assumption_promotion", "dependencies": ["assumed_bridge"]}, arrows),
        validate_promotion({"id": "fitted_promotion", "dependencies": ["fitted_bridge"]}, arrows),
        validate_promotion({"id": "two_moment_operator_promotion", "dependencies": ["common_operator_from_two_moments"]}, arrows),
        validate_promotion({"id": "laundered_promotion", "dependencies": ["laundered_source_claim"]}, arrows),
        validate_promotion({"id": "missing_class_promotion", "dependencies": ["missing_class"]}, arrows),
    ]
    admitted = {item["id"]: item["admitted"] for item in promotions}
    assert admitted == {
        "valid_source_promotion": True,
        "assumption_promotion": False,
        "fitted_promotion": False,
        "two_moment_operator_promotion": False,
        "laundered_promotion": False,
        "missing_class_promotion": False,
    }
    assert "missing:evidence_locator" in arrow_checks["laundered_source_claim"]["errors"]
    assert "missing:provenance_class" in arrow_checks["missing_class"]["errors"]
    assert "missing:completion_topology" in arrow_checks["common_operator_from_two_moments"]["errors"]

    result = {
        "schema": "marici.aspect.scc-realization-provenance-gate-check.v1",
        "status": "pass",
        "arrow_checks": arrow_checks,
        "promotions": promotions,
        "checks": {
            "source_constructor_with_locator_admitted": admitted["valid_source_promotion"],
            "explicit_assumption_not_promoted": not admitted["assumption_promotion"],
            "observer_fit_not_promoted": not admitted["fitted_promotion"],
            "two_moment_hostile_remains_unsupported": not admitted["two_moment_operator_promotion"],
            "laundered_source_claim_refused": not admitted["laundered_promotion"],
            "missing_provenance_refused": not admitted["missing_class_promotion"],
            "applicable_completion_declarations_required": "missing:completion_topology" in arrow_checks["common_operator_from_two_moments"]["errors"],
        },
        "claim_boundary": "Declaration validator only; no ontology or source provenance is inferred.",
    }
    RESULT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
