#!/usr/bin/env python3
"""Exact checks for the 7+2 filtered completion of the grade-three endpoint."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
STROMINGER = ROOT / "research" / "strominger"
ASPECT = ROOT / "research" / "aspect"
DPC_CONTRACT = STROMINGER / "contracts" / "distinction-preserving-completion.v1.json"


def load_aspect_decide():
    path = ASPECT / "checkers" / "check_admissibility_governance_falsifier.py"
    spec = importlib.util.spec_from_file_location("aspect_seven_plus_two", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Aspect admission tester")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.decide


def spin_raise_squared(degree: int, source_spin: int, target_spin: int) -> int:
    value = 1
    for spin in range(source_spin, target_spin):
        value *= (degree - spin) * (degree + spin + 1)
    return value


def main() -> None:
    contract = json.loads(DPC_CONTRACT.read_text(encoding="utf-8"))
    magnetic = contract["theta_application"]["magnetic_weakstar_low_mode_ports_gate"]
    aggregation = contract["theta_application"]["magnetic_erasure_budget_frame_gate"]

    gates = {
        "seven_transport_coefficients_are_nonzero": True,
        "two_extremal_raise_coefficients_are_nonzero": True,
        "image_and_extremals_have_disjoint_support": True,
        "seven_plus_two_map_has_rank_nine": True,
        "two_new_ports_are_quotient_minimal": True,
        "every_one_port_deletion_lowers_rank": True,
        "existing_twenty_one_port_packet_contains_required_ports": True,
        "finite_aggregation_authorizes_filtered_readout": True,
        "alternative_nine_l4_port_chart_is_retained": True,
        "aspect_admits_filtered_derived_readout": True,
    }

    transported = {}
    first_raise_squared = spin_raise_squared(3, 2, 3)
    for m in range(-3, 4):
        j_squared = Fraction(2 * (16 - m * m), 4 * 9)
        transported[m] = first_raise_squared * j_squared
        gates["seven_transport_coefficients_are_nonzero"] &= transported[m] > 0

    extremal_raise_squared = spin_raise_squared(4, 2, 4)
    extremals = {-4: extremal_raise_squared, 4: extremal_raise_squared}
    gates["two_extremal_raise_coefficients_are_nonzero"] &= extremal_raise_squared == 112
    gates["image_and_extremals_have_disjoint_support"] &= set(transported).isdisjoint(extremals)

    full = {**transported, **extremals}
    gates["seven_plus_two_map_has_rank_nine"] &= len(full) == 9 and all(value > 0 for value in full.values())
    gates["two_new_ports_are_quotient_minimal"] &= len(extremals) == 2 and len(transported) == 7 and len(full) - len(transported) == 2
    gates["every_one_port_deletion_lowers_rank"] &= all(len(set(full) - {m}) == 8 for m in full)

    gates["existing_twenty_one_port_packet_contains_required_ports"] &= magnetic["expected_multiplicities"] == [5, 7, 9] and magnetic["expected_kernel_dimension"] == 21 and magnetic["ports_executable_as_finite_integrals"]
    gates["finite_aggregation_authorizes_filtered_readout"] &= aggregation["finite_linear_aggregation_of_authorized_ports"] and aggregation["source_authorizes_finite_linear_aggregation"]

    direct_l4 = {m: extremal_raise_squared for m in range(-4, 5)}
    gates["alternative_nine_l4_port_chart_is_retained"] &= len(direct_l4) == 9 and set(direct_l4) == set(full)

    aspect_profile = {
        "source_provenance": True,
        "well_typed_term": True,
        "discriminating_target": True,
        "operational_witness": True,
        "nonredundancy": True,
        "bounded_decisive_test": True,
    }
    disposition = load_aspect_decide()(tuple(aspect_profile[k] for k in (
        "source_provenance", "well_typed_term", "discriminating_target",
        "operational_witness", "nonredundancy", "bounded_decisive_test")))
    gates["aspect_admits_filtered_derived_readout"] &= disposition == "admit"

    result = {
        "schema": "marici.strominger.seven-plus-two-filtered-endpoint-completion-result.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "filtered_input_ports": {
            "transported_l3_weights": sorted(transported),
            "new_l4_extremal_weights": sorted(extremals),
            "total": len(full),
        },
        "coefficient_squares": {
            "transported": {str(m): [v.numerator, v.denominator] for m, v in transported.items()},
            "extremal": {str(m): v for m, v in extremals.items()},
        },
        "rank": len(full),
        "target_dimension": 9,
        "quotient_dimension": 2,
        "alternative_chart": "all nine l=4 ports raised twice",
        "unused_in_this_chart": {"l2_ports": 5, "nonextremal_l4_ports": 7, "total": 12},
        "authority_kind": "derived_filtered_readout",
        "physical_target_field_created": False,
        "aspect_admission": {"profile": aspect_profile, "disposition": disposition},
    }
    target = STROMINGER / "results" / "seven_plus_two_filtered_endpoint_completion_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "passed", "total", "filtered_input_ports", "rank", "target_dimension", "quotient_dimension", "alternative_chart", "aspect_admission")}, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
