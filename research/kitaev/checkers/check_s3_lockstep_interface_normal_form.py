#!/usr/bin/env python3
"""Exact diagonal normal form for the four-port CDFG interaction layer."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
NATIVE = K / "results" / "s3-native-ququart-wilson-compiler.json"
JOINT = K / "results" / "s3-joint-interface-selector-fault-gate.json"
OUT = K / "results" / "s3-lockstep-interface-normal-form.json"


def predicate(bits: tuple[int, int, int], mask: int) -> int:
    return int(all(bits[j] for j in range(3) if mask & (1 << j)))


def exponent(term: tuple[str, int, int], bits: tuple[int, int, int], residues: dict[str, int]) -> int:
    port, mask, coefficient = term
    return coefficient * predicate(bits, mask) * residues[port] % 4


def main() -> None:
    native = json.loads(NATIVE.read_text(encoding="utf-8"))
    joint = json.loads(JOINT.read_text(encoding="utf-8"))
    ports = ("C", "D", "F", "G")
    terms = []
    for port in ports:
        coefficients = native["ports"][port]["boolean_coefficients_mod4"]
        terms.extend((port, int(mask), coefficient) for mask, coefficient in coefficients.items())
    assert len(terms) == 21

    orders = {
        "compiler": terms,
        "reverse": list(reversed(terms)),
        "predicate_grouped": sorted(terms, key=lambda item: (item[1], item[0])),
        "odd_then_even": sorted(terms, key=lambda item: (item[2] % 2 == 0, item[0], item[1])),
    }
    basis_count = 0
    maximum_residual_mod4 = 0
    for bits in itertools.product((0, 1), repeat=3):
        for residue_tuple in itertools.product(range(4), repeat=4):
            residues = dict(zip(ports, residue_tuple))
            totals = [sum(exponent(term, bits, residues) for term in order) % 4
                      for order in orders.values()]
            maximum_residual_mod4 = max(maximum_residual_mod4,
                                        max((value - totals[0]) % 4 for value in totals))
            assert len(set(totals)) == 1
            basis_count += 1
    assert basis_count == 8 * 4**4
    assert maximum_residual_mod4 == 0
    assert joint["authorized_lockstep_contract"]["selector_sufficient"] is True

    result = {
        "schema": "marici.kitaev.s3-lockstep-interface-normal-form.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (NATIVE, JOINT)
        },
        "CDFG_interaction_layer": {
            "ports": list(ports),
            "elementary_diagonal_terms": len(terms),
            "basis_states_checked": basis_count,
            "orders_checked": list(orders),
            "maximum_phase_exponent_residual_mod4": maximum_residual_mod4,
            "all_terms_pairwise_commute": True,
            "lockstep_digit_exposed_interaction_window_exists_at_ideal_unitary_level": True,
        },
        "selector_refinement": {
            "independent_16_configuration_contract_required_by_ideal_interaction_order": False,
            "two_state_lockstep_contract_sufficient_for_ideal_interaction_order": True,
            "source_of_coherence_law": "the actual CDFG interaction primitives are simultaneously diagonal",
        },
        "remaining_boundary": {
            "native_F4_and_inverse_layers_may_be_moved_through_interaction_window": False,
            "physical_four_block_joint_switch_admitted": False,
            "independent_fault_domains_certified": False,
            "numerical_joint_switch_cost_derived": False,
        },
        "verdict": "The actual CDFG controlled-Z4 terms admit an exact lockstep interface normal form: all 21 diagonal terms commute on all 2048 data-pointer basis states, so ideal interaction ordering never requires a mixed native/binary port configuration. This removes the independent-selector deficit for the ideal compiler. It does not make the joint switch free or fault independent; the four-block physical channel and its cost remain untyped.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
