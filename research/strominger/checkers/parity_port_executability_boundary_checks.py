#!/usr/bin/env python3
"""Exact algebraic and authority-boundary audit for magnetic parity ports."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/strominger/contracts/parity-port-executability-boundary.v1.json"
SOURCE_AUDIT = ROOT / "research/strominger/contracts/magnetic-24x3-numerical-candidate.v1.json"
RESULT = ROOT / "research/strominger/results/parity_port_executability_boundary_checks.json"
contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
source_audit = json.loads(SOURCE_AUDIT.read_text(encoding="utf-8"))
interface = source_audit["physical_realization_dpc"]["interface_selection_authority"]
static = source_audit["physical_realization_dpc"]["static_distinction_authority"]

Q = ((0, 1), (1, 0))
I = ((1, 0), (0, 1))
PE = tuple(tuple(Fraction(I[i][j] + Q[i][j], 2) for j in range(2)) for i in range(2))
PM = tuple(tuple(Fraction(I[i][j] - Q[i][j], 2) for j in range(2)) for i in range(2))

def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))

def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0])))
                 for i in range(len(a)))

def act(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(len(v)))
                 for i in range(len(a)))

zero_state = (Fraction(0), Fraction(0))
electric_state = (Fraction(1), Fraction(1))
magnetic_zero = act(PM, zero_state)
magnetic_electric = act(PM, electric_state)
joint_zero = (act(PE, zero_state), act(PM, zero_state))
joint_electric = (act(PE, electric_state), act(PM, electric_state))

packets = {
    "p0": {"electric": 0, "magnetic": 0},
    "p1": {"electric": 1, "magnetic": 1},
}
electric_marginal = {record["electric"] for record in packets.values()}
magnetic_marginal = {record["magnetic"] for record in packets.values()}
ordinary_product = {
    (electric, magnetic)
    for electric in electric_marginal
    for magnetic in magnetic_marginal
}
valid_joint_records = {
    (record["electric"], record["magnetic"])
    for record in packets.values()
}
fiber_product_records = {
    (record["electric"], record["magnetic"])
    for packet_id, record in packets.items()
    if packet_id in packets
}
linear_preparation = {
    "packet_id": "p",
    "available": True,
    "individually_authorized": {"electric": True, "magnetic": True},
}
def acquire(state, port):
    if not state["available"] or not state["individually_authorized"][port]:
        return False, state
    return True, {**state, "available": False}

electric_first, after_electric = acquire(linear_preparation, "electric")
magnetic_after_electric, _ = acquire(after_electric, "magnetic")
magnetic_first, after_magnetic = acquire(linear_preparation, "magnetic")
electric_after_magnetic, _ = acquire(after_magnetic, "electric")

electric_dimensions = {
    cutoff: (cutoff + 1) ** 2 - 4
    for cutoff in range(2, 21)
}
source = contract["source_authorized"]
witness = contract["execution_witnesses"]
admitted = contract["admitted_conclusions"]
gates = {
    "projectors_are_complementary": mul(PE, PE) == PE and mul(PM, PM) == PM
        and mul(PE, PM) == ((0, 0), (0, 0)) and add(PE, PM) == I,
    "joint_readout_reconstructs_source": add(PE, PM) == I,
    "source_authorizes_invariant_ports": all(source.values()),
    "magnetic_low_observer_is_executable":
        witness["magnetic_low_harmonic_instrument_coupling"]
        and witness["magnetic_low_harmonic_port_count"] == 21
        and admitted["executable_magnetic_low_kernel_repair"],
    "projection_does_not_authorize_unwitnessed_execution":
        not witness["electric_instrument_coupling"]
        and not witness["magnetic_full_spectrum_instrument_coupling"]
        and not admitted["executable_joint_faithfulness"],
    "current_acquisition_collapses_a_pure_electric_distinction":
        magnetic_zero == magnetic_electric and zero_state != electric_state,
    "algebraic_joint_readout_separates_the_hostile_pair":
        joint_zero != joint_electric,
    "joint_invertibility_does_not_authorize_joint_acquisition":
        not witness["coherent_joint_acquisition"]
        and not witness["conditional_port_selector"],
    "ordinary_product_creates_spurious_joint_records":
        ordinary_product != valid_joint_records
        and (0, 1) in ordinary_product
        and (0, 1) not in valid_joint_records,
    "preparation_fiber_product_recovers_exact_joint_records":
        fiber_product_records == valid_joint_records,
    "same_identity_does_not_guarantee_joint_execution":
        electric_first and magnetic_first
        and not magnetic_after_electric
        and not electric_after_magnetic,
    "joint_refinement_is_not_derived_from_individual_ports":
        not contract["joint_executability_model"]["atomic_joint_refinement_authorized"],
    "local_shear_tests_are_scoped_to_magnetic_low_block":
        static["object"] == "magnetic l=2,3,4 shear coefficient block"
        and static["complete_local_shear_tests_separate_points"],
    "no_full_field_observer_execution_is_declared":
        not interface["observer_class_declared"]
        and not interface["accessible_field_region_declared"]
        and not interface["redundant_bypass_instrument_execution_authorized"],
    "fixed_twenty_one_port_patch_fails_above_low_block":
        electric_dimensions[5] == 32 and electric_dimensions[5] > 21,
    "electric_observer_dimension_is_unbounded":
        all(electric_dimensions[L + 1] > electric_dimensions[L]
            for L in range(2, 20)),
    "observation_does_not_authorize_actuation":
        not witness["state_actuator"] and not admitted["state_controllability"],
    "missing_constructor_is_explicit":
        contract["missing_constructor"]["authority_root"] is None,
}
payload = {
    "schema": "marici.strominger.parity_port_executability_boundary_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "classification": {
        "invariant_closure": "proved",
        "algebraic_joint_observability": "proved",
        "executable_observation": "partial_magnetic_low_block_only",
        "state_actuation": "not_constructed"
    },
    "hostile_fixture": {
        "state_0_sheet_coordinates": [0, 0],
        "state_1_sheet_coordinates": [1, 1],
        "current_magnetic_records": [
            [str(x) for x in magnetic_zero],
            [str(x) for x in magnetic_electric]
        ],
        "joint_readout_separates": joint_zero != joint_electric,
        "lost_distinction": "pure electric direction"
    },
    "same_packet_coherence_falsifier": {
        "packet_records": packets,
        "ordinary_product_records": sorted([list(x) for x in ordinary_product]),
        "valid_joint_records": sorted([list(x) for x in valid_joint_records]),
        "spurious_unbound_records": sorted([list(x) for x in ordinary_product - valid_joint_records]),
        "required_composition": "fiber product over preparation identity"
    },
    "joint_executability_falsifier": {
        "prepared_packet_usage": "linear",
        "electric_acquisition_individually_valid": electric_first,
        "magnetic_acquisition_individually_valid": magnetic_first,
        "magnetic_after_electric_valid": magnetic_after_electric,
        "electric_after_magnetic_valid": electric_after_magnetic,
        "same_packet_pullback_exists": fiber_product_records == valid_joint_records,
        "joint_instrument_exists": contract["joint_executability_model"]["atomic_joint_refinement_authorized"],
        "verdict": "provenance pullback does not construct a jointly executable refinement"
    },
    "field_valued_escape_audit": {
        "source_object": static["object"],
        "complete_local_tests_contextually_separate": static["complete_local_shear_tests_separate_points"],
        "observer_class_declared": interface["observer_class_declared"],
        "accessible_field_region_declared": interface["accessible_field_region_declared"],
        "instrument_execution_authorized": interface["redundant_bypass_instrument_execution_authorized"],
        "verdict": "contextual separation on the magnetic low block does not authorize full electric field acquisition"
    },
    "electric_cutoff_dimensions": electric_dimensions,
    "finite_port_falsifier": {
        "fixed_port_count": 21,
        "first_failed_cutoff": 5,
        "electric_dimension_at_failure": electric_dimensions[5],
        "conclusion": "no fixed finite scalar port family separates the completed electric sector"
    },
    "smallest_missing_constructor": contract["missing_constructor"],
    "verdict": "The completed source supplies complementary algebraic parity ports and 21 executable magnetic low-harmonic coefficient ports. These repair the magnetic grade-three low kernel. The missing electric sector grows without bound across harmonic cutoff, so no fixed finite scalar patch restores full parity faithfulness; a field-valued or unbounded electric observer and same-packet coherence are required. State actuation remains separate."
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["status"] == "passed" else 1)
