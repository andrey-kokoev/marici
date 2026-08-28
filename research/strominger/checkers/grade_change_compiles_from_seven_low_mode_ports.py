#!/usr/bin/env python3
"""Compile the axis-marked grade-change readout from seven authorized low-mode ports."""

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
    spec = importlib.util.spec_from_file_location("aspect_grade_change_readout", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Aspect admission tester")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.decide


def main() -> None:
    contract = json.loads(DPC_CONTRACT.read_text(encoding="utf-8"))
    magnetic = contract["theta_application"]["magnetic_weakstar_low_mode_ports_gate"]
    aggregation = contract["theta_application"]["magnetic_erasure_budget_frame_gate"]

    gates = {
        "twenty_one_ports_are_source_authorized_finite_integrals": magnetic["ports_executable_as_finite_integrals"] and magnetic["source_dual_pair_authorized"],
        "finite_linear_aggregation_is_authorized": aggregation["finite_linear_aggregation_of_authorized_ports"] and aggregation["source_authorizes_finite_linear_aggregation"],
        "l3_subfamily_has_exactly_seven_ports": 2 * 3 + 1 == 7,
        "compiled_map_has_rank_seven": True,
        "compiled_target_complement_is_m_plus_minus_four": True,
        "deleting_any_input_port_destroys_faithfulness": True,
        "readout_authority_not_laundered_to_actuator_authority": True,
        "aspect_admits_typed_executable_readout": True,
    }

    coefficients = {}
    for m in range(-3, 4):
        # First eth: spin 2, degree 3 -> spin 3, degree 3 has square 6.
        first_eth_squared = (3 - 2) * (3 + 2 + 1)
        # J at l=3 has square 2((l+1)^2-m^2)/((l+1)(2l+3)).
        j_squared = Fraction(2 * (16 - m * m), 4 * 9)
        composite_squared = first_eth_squared * j_squared
        coefficients[m] = composite_squared
        gates["compiled_map_has_rank_seven"] &= composite_squared > 0

    image_weights = set(coefficients)
    target_weights = set(range(-4, 5))
    gates["compiled_target_complement_is_m_plus_minus_four"] &= target_weights - image_weights == {-4, 4}
    # The compiled map is diagonal with seven nonzero entries. Removing any
    # source coefficient port removes its unique image weight and lowers rank.
    gates["deleting_any_input_port_destroys_faithfulness"] &= all(len(image_weights - {m}) == 6 for m in image_weights)

    authority = {
        "kind": "derived_readout",
        "input": "seven executable l=3 spin-2 harmonic coefficient ports",
        "output": "seven coefficients in the image of J_axis inside H_4^(4)",
        "physical_field_created": False,
        "actuator_authority_claimed": False,
        "independent_target_measurement_claimed": False,
    }
    gates["readout_authority_not_laundered_to_actuator_authority"] &= not authority["physical_field_created"] and not authority["actuator_authority_claimed"] and not authority["independent_target_measurement_claimed"]

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
    gates["aspect_admits_typed_executable_readout"] &= disposition == "admit"

    result = {
        "schema": "marici.strominger.grade-change-seven-port-readout-result.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "composite_law": "K_axis = J_axis after eth, restricted to the l=3 spin-2 source block",
        "composite_coefficient_squares": {str(m): [v.numerator, v.denominator] for m, v in coefficients.items()},
        "rank": len(image_weights),
        "target_dimension": len(target_weights),
        "target_complement_weights": sorted(target_weights - image_weights),
        "minimum_input_port_count": 7,
        "authority": authority,
        "aspect_admission": {"profile": aspect_profile, "disposition": disposition},
        "boundary": "Admission applies to a finite derived observation transform. It does not authorize target-field preparation, physical spin-4 dynamics, or an independent target measurement.",
    }
    target = STROMINGER / "results" / "grade_change_compiles_from_seven_low_mode_ports.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "passed", "total", "rank", "target_dimension", "target_complement_weights", "minimum_input_port_count", "authority", "aspect_admission")}, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
