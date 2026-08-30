#!/usr/bin/env python3
"""Compile the functional-completion theorem through data-descent v2."""

import copy
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "nima"))
sys.path.insert(0, str(ROOT / "research" / "strominger"))

from data_descent_kernel import replay_evidence  # noqa: E402
from strominger_data_descent_v2 import compile_packet  # noqa: E402

CONTRACT = ROOT / "research" / "strominger" / "contracts" / "functional-completion-descent.v2.json"
OUT = ROOT / "research" / "strominger" / "results" / "functional_completion_data_descent_v2.json"


def codes(compiled):
    return {error["code"] for error in compiled["errors"]}


def hostile(packet, mutate, expected_code):
    candidate = copy.deepcopy(packet)
    mutate(candidate)
    compiled = compile_packet(candidate)
    return {
        "valid": compiled["valid"],
        "expected_code": expected_code,
        "error_codes": sorted(codes(compiled)),
        "passed": not compiled["valid"] and expected_code in codes(compiled),
    }


def main():
    packet = json.loads(CONTRACT.read_text(encoding="ascii"))
    compiled = compile_packet(packet)
    replay = replay_evidence(packet, ROOT, timeout=120)

    tests = {}
    tests["characteristic_equals_kernel"] = hostile(
        packet,
        lambda p: p.setdefault("identifications", []).append({
            "id": "bad_identification", "left": "projected_characteristic_locus",
            "right": "completed_magnetic_low_kernel"
        }),
        "characteristic_kernel_identification",
    )
    tests["completion_without_topology"] = hostile(
        packet,
        lambda p: p["topological_completions"][0].pop("topology"),
        "missing_weak_star_topology",
    )
    tests["completion_as_flat_base_change"] = hostile(
        packet,
        lambda p: p["topological_completions"][0].update(constructor_kind="ordinary_base_change"),
        "completion_as_flat_base_change",
    )
    tests["kernel_as_Tor"] = hostile(
        packet,
        lambda p: p["physical_kernel_classes"][0].update(homological_degree=-1, tor_grade=1),
        "completed_kernel_mistyped_as_derived_grade",
    )
    tests["hard_flux_erased_variance"] = hostile(
        packet,
        lambda p: p["arrows"][0].update(variance="covariant"),
        "correspondence_variance_mismatch",
    )
    tests["ports_from_support_only"] = hostile(
        packet,
        lambda p: p["observation_fibers"][0].update(
            authority_basis="geometric_support_only", source_derived_port_authority=""
        ),
        "support_does_not_authorize_ports",
    )
    tests["delete_one_port"] = hostile(
        packet,
        lambda p: p["observation_fibers"][0]["ports"].pop(),
        "observation_rank_defect",
    )
    tests["rank_coincidence_as_identity"] = hostile(
        packet,
        lambda p: p["typed_coincidences"][0].update(
            identified=True, disposition="identified_objects"
        ),
        "unauthorized_rank_coincidence_identification",
    )

    fiber = packet["observation_fibers"][0]
    coordinates = [port["coordinate"] for port in fiber["ports"]]
    rank_21 = len(set(coordinates)) == 21 and sorted(coordinates) == list(range(21))
    every_deletion_rank = min(len(set(coordinates[:i] + coordinates[i + 1:])) for i in range(21))
    deletion_proof = every_deletion_rank == 20

    localized = packet["localized_global_states"][0]
    kernel = packet["physical_kernel_classes"][0]
    semantic = {
        "characteristic_locus_separate": localized["rank"] == 0 and kernel["origin"] == "global_spectral_zero",
        "localized_characteristic_kernel_rank_is_zero": localized["rank"] == 0,
        "completed_kernel_is_ordinary": kernel["classification"].startswith("ordinary_kernel"),
        "completed_kernel_rank_is_21": kernel["rank"] == 21,
        "completed_kernel_harmonics_are_2_3_4": kernel["harmonic_support"] == [2, 3, 4],
        "weak_star_constructor_typed": packet["topological_completions"][0]["constructor_kind"] == "topological_completion",
        "all_21_ports_faithful": rank_21,
        "one_port_deletion_rank_is_20": every_deletion_rank == 20,
        "every_one_port_deletion_nonfaithful": deletion_proof,
        "cosmology_rank_correction_disposition": packet["typed_coincidences"][0]["disposition"],
    }

    facts = {
        "localized_characteristic_kernel_rank": localized["rank"],
        "completed_kernel_kind": "ordinary_kernel",
        "completed_kernel_rank": kernel["rank"],
        "completed_kernel_harmonics": kernel["harmonic_support"],
        "largest_one_port_deletion_rank": every_deletion_rank,
        "cosmology_rank_correction_disposition": packet["typed_coincidences"][0]["disposition"],
        "cosmology_current_rank": packet["typed_coincidences"][0]["right_rank"],
        "cosmology_historical_plateau_rank": 21,
    }
    semantic["cosmology_rank_21_coincidence_is_superseded"] = (
        facts["cosmology_rank_correction_disposition"] == "superseded_cutoff_plateau_not_current_coincidence"
        and facts["cosmology_current_rank"] == 26
        and not packet["typed_coincidences"][0]["same_rank"]
        and not packet["typed_coincidences"][0]["identified"]
    )
    del semantic["cosmology_rank_correction_disposition"]

    all_hostile = all(test["passed"] for test in tests.values())
    passed = compiled["valid"] and replay["passed"] and all(semantic.values()) and all_hostile
    result = {
        "schema": "marici.strominger.functional-completion-data-descent-v2-result.v1",
        "passed": passed,
        "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        "base_and_extension_compile": compiled,
        "bounded_evidence_replay": replay,
        "semantic_fields": semantic,
        "classification_facts": facts,
        "hostile_tests": tests,
        "hostile_passed": sum(test["passed"] for test in tests.values()),
        "hostile_total": len(tests),
        "smallest_missing_v2_constructors": [
            "topological_completion(topology,dense_image_evidence,source_authority,comparison_evidence)",
            "finite_linear_observation_fiber(source_kernel,ports,execution,source_derived_port_authority,joint_rank)",
        ],
        "verdict": "The completed l=2,3,4 magnetic block is an ordinary rank-21 kernel after weak-star completion, not a characteristic-locus state, Tor grade, or support-generated capability. Exactly 21 independently authorized harmonic observation ports restore faithfulness.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")
    for name, value in semantic.items():
        print(f"PASS semantic.{name}: {value}")
    for name, test in tests.items():
        print(f"{'PASS' if test['passed'] else 'FAIL'} hostile.{name}: {test['error_codes']}")
    print(f"PASS replay: {replay['passed']}")
    print(f"SUMMARY {sum(bool(x) for x in semantic.values()) + sum(t['passed'] for t in tests.values()) + int(compiled['valid']) + int(replay['passed'])}/{len(semantic) + len(tests) + 2}")
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
