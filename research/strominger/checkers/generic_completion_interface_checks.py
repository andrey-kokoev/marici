#!/usr/bin/env python3
"""Exact positive and hostile tests for the generic completion interface."""

import copy
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "nima"))
sys.path.insert(0, str(ROOT / "research" / "strominger"))

from data_descent_kernel import replay_evidence  # noqa: E402
from generic_completion_interface import _matrix, _rank, compile_packet  # noqa: E402

CONTRACTS = ROOT / "research" / "strominger" / "contracts"
OUT = ROOT / "research" / "strominger" / "results" / "generic_completion_interface.json"


def error_codes(compiled):
    return {item["code"] for item in compiled["errors"]}


def reject(packet, mutation, expected):
    candidate = copy.deepcopy(packet)
    mutation(candidate)
    compiled = compile_packet(candidate)
    return {
        "passed": not compiled["valid"] and expected in error_codes(compiled),
        "expected": expected,
        "codes": sorted(error_codes(compiled)),
    }


def deletion_ranks(fiber):
    matrix = _matrix(fiber["observation_matrix"])
    return [_rank(matrix[:index] + matrix[index + 1:]) for index in range(len(matrix))]


def make_redundant_fiber(packet):
    candidate = copy.deepcopy(packet)
    fiber = candidate["finite_linear_observation_fibers"][0]
    fiber["ports"].append({
        "id": "P21_redundant",
        "availability": "available",
        "execution_evidence": "repeat exact harmonic projection P0",
        "source_authority": "pre-readout shear coefficient",
    })
    fiber["observation_matrix"]["shape"] = [22, 21]
    fiber["observation_matrix"]["entries"].append([21, 0, 1])
    fiber["deletion_certificate"] = {"minimal": False, "ranks": deletion_ranks(fiber)}
    return candidate


def main():
    magnetic_path = CONTRACTS / "magnetic-generic-completion.v1.json"
    theta_path = CONTRACTS / "grothendieck-theta-completion-test.v1.json"
    schema_path = CONTRACTS / "generic-completion-interface.v1.schema.json"
    fixture_path = CONTRACTS / "generic-completion-classification-fixture.v1.json"
    magnetic = json.loads(magnetic_path.read_text(encoding="ascii"))
    theta = json.loads(theta_path.read_text(encoding="ascii"))
    schema = json.loads(schema_path.read_text(encoding="ascii"))
    fixture = json.loads(fixture_path.read_text(encoding="ascii"))

    magnetic_compile = compile_packet(magnetic)
    theta_compile = compile_packet(theta)
    fixture_compile = compile_packet(fixture)
    replay = replay_evidence(magnetic, ROOT, timeout=120)
    redundant = make_redundant_fiber(magnetic)
    redundant_compile = compile_packet(redundant)

    hostile = {
        "completion_as_base_change": reject(
            magnetic,
            lambda p: p["completion_interfaces"][0].update(constructor_kind="ordinary_base_change"),
            "completion_as_ordinary_base_change",
        ),
        "noncanonical_operator_extension": reject(
            magnetic,
            lambda p: p["completion_interfaces"][0]["extension_well_defined"].update(unique=False),
            "operator_extension_not_canonical",
        ),
        "noncommuting_extension_square": reject(
            magnetic,
            lambda p: p["completion_interfaces"][0]["operator_extension_square"].update(commutes=False),
            "operator_extension_square_defect",
        ),
        "completion_only_as_defect": reject(
            magnetic,
            lambda p: p["kernel_comparisons"][0].update(completion_defect_dimension=21),
            "completion_defect_dimension_mismatch",
        ),
        "completion_only_as_untyped_Tor": reject(
            magnetic,
            lambda p: p["kernel_comparisons"][0]["class_groups"][0].update(
                classification="derived_completion_obstruction"
            ),
            "derived_completion_obstruction_untyped",
        ),
        "characteristic_support_as_kernel": reject(
            magnetic,
            lambda p: p.setdefault("support_identifications", []).append({
                "id": "bad_support_identity",
                "left": "p4_minus_q4_characteristic",
                "right": "magnetic_kernel_comparison",
            }),
            "characteristic_support_is_not_kernel_support",
        ),
        "kernel_dimension_from_port_count": reject(
            magnetic,
            lambda p: p["finite_linear_observation_fibers"][0].update(kernel_dimension=22),
            "kernel_dimension_port_count_conflation",
        ),
        "unavailable_as_zero_valued": reject(
            magnetic,
            lambda p: p["finite_linear_observation_fibers"][0]["ports"][20].update(
                availability="unavailable"
            ),
            "unavailable_port_is_not_zero_port",
        ),
        "one_port_deleted": reject(
            magnetic,
            lambda p: (
                p["finite_linear_observation_fibers"][0]["ports"].pop(),
                p["finite_linear_observation_fibers"][0]["observation_matrix"].update(shape=[20, 21]),
                p["finite_linear_observation_fibers"][0]["observation_matrix"]["entries"].pop(),
                p["finite_linear_observation_fibers"][0]["deletion_certificate"].update(
                    ranks=[19] * 20
                ),
            ),
            "observation_faithfulness_defect",
        ),
        "theta_RH_overclaim": reject(
            theta,
            lambda p: p["spectral_compressions"][0].update(rh_bearing_kernel_claim=True),
            "unauthorized_rh_kernel_claim",
        ),
    }

    magnetic_comparison = magnetic["kernel_comparisons"][0]
    theta_comparison = theta["kernel_comparisons"][0]
    magnetic_fiber = magnetic["finite_linear_observation_fibers"][0]
    gates = {
        "sector_neutral_schema_declares_all_four_layers": set(schema["required"]) == {
            "completion_spaces", "completion_operators", "completion_interfaces", "kernel_comparisons"
        } and "finite_linear_observation_fibers" in schema["properties"],
        "magnetic_contract_compiles": magnetic_compile["valid"],
        "theta_test_packet_compiles": theta_compile["valid"],
        "three_way_classification_fixture_compiles": fixture_compile["valid"],
        "bounded_magnetic_evidence_replays": replay["passed"],
        "magnetic_kernel_is_ordinary_completion_only": (
            magnetic_comparison["completed_kernel_dimension"] == 21
            and magnetic_comparison["completion_defect_dimension"] == 0
            and all(group["classification"] == "completion_only" for group in magnetic_comparison["class_groups"])
        ),
        "magnetic_harmonic_dimension_is_5_plus_7_plus_9": (
            [group["dimension"] for group in magnetic_comparison["class_groups"]] == [5, 7, 9]
        ),
        "all_21_ports_are_faithful": magnetic_fiber["declared_rank"] == 21 and magnetic_fiber["faithful"],
        "every_single_port_deletion_has_rank_20": deletion_ranks(magnetic_fiber) == [20] * 21,
        "zero_value_does_not_mean_unavailable": (
            magnetic_fiber["ports"][20]["availability"] == "available"
            and bool(magnetic_fiber["ports"][20]["zero_value_witness"])
        ),
        "redundant_22_port_fiber_is_faithful_but_not_minimal": (
            redundant_compile["valid"]
            and redundant["finite_linear_observation_fibers"][0]["declared_rank"] == 21
            and not redundant["finite_linear_observation_fibers"][0]["deletion_certificate"]["minimal"]
        ),
        "theta_ground_mode_is_completion_only_ordinary_kernel": (
            theta_comparison["completed_kernel_dimension"] == 1
            and theta_comparison["completion_defect_dimension"] == 0
            and theta_comparison["class_groups"][0]["classification"] == "completion_only"
        ),
        "theta_packet_makes_no_RH_kernel_claim": not theta["spectral_compressions"][0]["rh_bearing_kernel_claim"],
        "all_hostile_packets_rejected": all(item["passed"] for item in hostile.values()),
    }
    passed = all(gates.values())
    result = {
        "schema": "marici.generic-completion-interface-result.v1",
        "passed": passed,
        "gates": gates,
        "passed_gates": sum(gates.values()),
        "total_gates": len(gates),
        "hostile": hostile,
        "hostile_passed": sum(item["passed"] for item in hostile.values()),
        "hostile_total": len(hostile),
        "magnetic_contract_sha256": hashlib.sha256(magnetic_path.read_bytes()).hexdigest(),
        "theta_packet_sha256": hashlib.sha256(theta_path.read_bytes()).hexdigest(),
        "generic_schema_sha256": hashlib.sha256(schema_path.read_bytes()).hexdigest(),
        "classification_fixture_sha256": hashlib.sha256(fixture_path.read_bytes()).hexdigest(),
        "comparison_theorem": "A completion reveals an ordinary kernel without manufacturing it when the source embeds densely into a Hausdorff completion, the operator has a unique evidenced continuous/graph/form extension, the operator square commutes, and each new kernel class has graph-limit evidence in the completed domain. Derived defects require a separate Tor object and evidence.",
        "verdict": "The generic interface reproduces the rank-21 magnetic kernel and its minimal observation fiber, while the theta test packet canonically types A_Phi, its ordinary constant ground kernel, and E_N without asserting an RH-bearing kernel.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")
    for name, value in gates.items():
        print(f"{'PASS' if value else 'FAIL'} gate.{name}: {value}")
    for name, value in hostile.items():
        print(f"{'PASS' if value['passed'] else 'FAIL'} hostile.{name}: {value['codes']}")
    print(f"SUMMARY {sum(gates.values())}/{len(gates)}; HOSTILE {sum(x['passed'] for x in hostile.values())}/{len(hostile)}")
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
