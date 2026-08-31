#!/usr/bin/env python3
"""Validate the candidate source-type factorization and cross-source bridge registry."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/aspect/contracts/source-type-factorization.v1.json"
RESULT = ROOT / "research/aspect/results/source_type_factorization.json"
c = json.loads(CONTRACT.read_text(encoding="utf-8"))

factor_order = c["factor_order"]
source_types = c["source_types"]
source_by_id = {entry["id"]: entry for entry in source_types}
bridges = c["bridges"]
validation_cases = c["validation_cases"]
allowed_factor_status = {"constructed", "partial", "open"}


def signature(entry):
    return tuple(entry["factors"][factor] for factor in factor_order)


def same_source_type(left, right):
    return signature(left) == signature(right)


def changed_factor_hostile(entry, factor, replacement):
    hostile = copy.deepcopy(entry)
    hostile["id"] = f"hostile.{factor}"
    hostile["factors"][factor] = replacement
    return hostile


base = source_types[1]
different_completion = changed_factor_hostile(base, "completion", "hostile weak-star completion")
different_probe = changed_factor_hostile(base, "probe_grammar", "target-adaptive full-Yoneda probes")
different_transport = changed_factor_hostile(base, "transport_composition", "ordinary scalar addition")

checks = {
    "factor_count_nine": len(factor_order) == 9 and len(set(factor_order)) == 9,
    "dependent_order_covers_adjacent_factors": c["dependency_order"] == [
        [factor_order[i], factor_order[i + 1]] for i in range(len(factor_order) - 1)
    ],
    "source_ids_unique": len(source_by_id) == len(source_types),
    "source_object_kinds_typed": all(entry["object_kind"] in c["object_kinds"] for entry in source_types),
    "all_factors_total": all(set(entry["factors"]) == set(factor_order) and all(entry["factors"].values()) for entry in source_types),
    "all_sources_located": all(entry["source_locators"] for entry in source_types),
    "claim_boundary_open": not any(c["claim_boundary"].values()),
    "bridge_ids_unique": len({bridge["id"] for bridge in bridges}) == len(bridges),
    "bridge_inputs_registered": all(all(source in source_by_id for source in bridge["inputs"]) for bridge in bridges),
    "bridge_outputs_registered": all(bridge["output"] in source_by_id for bridge in bridges),
    "bridge_witnesses_nonempty": all(bridge["required_witnesses"] for bridge in bridges),
    "bridge_source_is_explicit": source_by_id["rh.completed-boundary-pencil.v1"]["object_kind"] == "bridge_source",
    "analytic_target_is_explicit": source_by_id["rh.xi-spectral-target.v1"]["object_kind"] == "analytic_target",
    "validation_case_ids_unique": len({case["id"] for case in validation_cases}) == len(validation_cases),
    "validation_case_kinds_typed": all(case["object_kind"] in c["object_kinds"] for case in validation_cases),
    "validation_case_factors_total": all(
        set(case["factor_status"]) == set(factor_order)
        and set(case["factor_status"].values()) <= allowed_factor_status
        for case in validation_cases
    ),
    "validation_case_sources_exist": all((ROOT / case["source_locator"]).is_file() for case in validation_cases),
    "validation_case_scopes_explicit": all(case.get("assessment_scope") for case in validation_cases),
    "validation_case_companions_exist": all(
        not case.get("companion_locator") or (ROOT / case["companion_locator"]).is_file()
        for case in validation_cases
    ),
    "flavor_portal_classified_as_bridge": next(
        case for case in validation_cases if case["id"] == "case.flavor-q-physical16-portal.v1"
    )["object_kind"] == "bridge",
    "magneto_optic_channel_classified_as_bridge_source": next(
        case for case in validation_cases if case["id"] == "case.magneto-optic-loss-channel.v1"
    )["object_kind"] == "bridge_source",
    "magneto_optic_completion_is_scale_bounded": next(
        case for case in validation_cases if case["id"] == "case.magneto-optic-loss-channel.v1"
    )["factor_status"]["completion"] == "partial",
    "amplitude_adapter_is_derived_source": next(
        case for case in validation_cases if case["id"] == "case.three-site-cosmological-correlator-amplitude.v1"
    )["object_kind"] == "derived_source",
    "amplitude_incidence_not_promoted_to_transport": next(
        case for case in validation_cases if case["id"] == "case.three-site-cosmological-correlator-amplitude.v1"
    )["factor_status"]["transport_composition"] == "partial",
    "cosmological_quartic_is_derived_readout": next(
        case for case in validation_cases if case["id"] == "case.cosmological-quartic-real-crossing.v1"
    )["object_kind"] == "derived_readout",
    "cosmological_quartic_authority_is_negative_boundary": (
        next(case for case in validation_cases if case["id"] == "case.cosmological-quartic-real-crossing.v1")
        ["factor_status"]["authority"] == "constructed"
        and "before assigning" in next(
            case for case in validation_cases if case["id"] == "case.cosmological-quartic-real-crossing.v1"
        )["first_open_gate"]
    ),
    "completion_changes_source_type": not same_source_type(base, different_completion),
    "probe_grammar_changes_source_type": not same_source_type(base, different_probe),
    "transport_changes_source_type": not same_source_type(base, different_transport),
    "same_profile_not_source_identity": "do not imply equal source types" in c["profile_projection_rule"],
    "target_adaptive_probe_hostile_present": "target-adaptive probe introduced after target observation" in c["hostile_fixtures"],
    "three_input_zero_sewing_requires_associator": any(
        len(bridge["inputs"]) == 3 and "typed_three_way_associator" in bridge["required_witnesses"]
        for bridge in bridges
    )
}

out = {
    "schema": "marici.aspect.source-type-factorization-check.v1",
    "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
    "passed": all(checks.values()),
    "checks": checks,
    "candidate_source_type_count": len(source_types),
    "bridge_count": len(bridges),
    "validation_case_count": len(validation_cases),
    "factor_count": len(factor_order),
    "source_type_ids": list(source_by_id),
    "open_source_type_ids": [entry["id"] for entry in source_types if "open" in entry["status"]],
    "claim_boundary": "candidate RH registry and exact schema hostiles only; no bridge construction, project-wide census, or RH result"
}
RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
raise SystemExit(0 if out["passed"] else 1)
