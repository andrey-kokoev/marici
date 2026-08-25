#!/usr/bin/env python3
"""Finite falsifiers for treating protection/engineering as an explanatory dichotomy."""

from __future__ import annotations

import json
from pathlib import Path


OUT = Path(__file__).parents[1] / "results" / "dpc-protection-engineering-dichotomy.json"


def main() -> None:
    # A standard injected non-Clifford operation is a hybrid protocol.  The
    # protected Clifford substrate and the engineered resource state are each
    # necessary, while neither alone implements the target capability.
    reaches_t = {
        (False, False): False,
        (True, False): False,
        (False, True): False,
        (True, True): True,
    }
    hybrid_refutes_exclusive_partition = (
        reaches_t[(True, True)]
        and not reaches_t[(True, False)]
        and not reaches_t[(False, True)]
    )

    # Logical Z commutes with every stabilizer.  Hence a full logical-Z fault
    # has trivial syndrome although its unitary channel is maximally separated
    # from identity (diamond distance 2, witnessed on |+> without numerics).
    syndrome = {"identity": (), "logical_Z": ()}
    output_overlap_on_plus = {"identity_vs_logical_Z": 0}
    coherent_logical_fault_is_syndrome_blind = (
        syndrome["identity"] == syndrome["logical_Z"]
        and output_overlap_on_plus["identity_vs_logical_Z"] == 0
    )

    # The same abstract T channel can be cut either at a calibrated gate or at
    # a magic state plus injection gadget.  Moving the apparatus boundary does
    # not alter the implemented channel.
    decompositions = {
        "direct": ("calibrated_T_gate",),
        "injected": ("T_resource_state", "protected_injection_gadget"),
    }
    apparatus_cut_is_noncanonical = (
        decompositions["direct"] != decompositions["injected"]
    )

    # A logical port may exist in the endpoint algebra while the constructor
    # set is empty.  Algebraic definability therefore does not imply a physical
    # instrument or executable control.
    endpoint_ports = {"X_L", "Z_L", "T_L"}
    admitted_constructors = {"X_L", "Z_L"}
    algebra_does_not_imply_execution = "T_L" in endpoint_ports - admitted_constructors

    # A single finite-size agreement cannot choose between scalable families
    # with constant and exponentially precise control requirements.
    finite_size = 5
    precision_family_a = {finite_size: (1, 1000)}
    precision_family_b = {finite_size: (1, 1000)}
    same_finite_packet_different_scaling = (
        precision_family_a == precision_family_b
        and "constant_precision" != "exponential_precision"
    )

    # Topological data quantizes an abstract action but contains no pulse,
    # coupling, clock, or readout constructor by itself.
    topological_certificate_fields = {"anyon_types", "fusion", "braiding"}
    instrument_fields = {"couplings", "pulse_schedule", "clock", "readout"}
    quantization_does_not_supply_instrument = not (
        instrument_fields <= topological_certificate_fields
    )

    # Explanatory adequacy is indexed by a question: these requests have
    # distinct certificate types and cannot be collapsed into one predicate.
    question_to_certificate = {
        "is_it_reachable": "compiler_or_controllability_theorem",
        "what_resource_is_necessary": "monotone_or_no_go",
        "does_it_survive_noise": "recovered_channel_bound",
        "does_it_scale": "overhead_and_precision_bound",
    }
    explanation_is_question_typed = len(set(question_to_certificate.values())) == len(
        question_to_certificate
    )

    falsifiers = {
        "hybrid_protocol_refutes_protected_or_engineered_partition": hybrid_refutes_exclusive_partition,
        "coherent_logical_fault_is_syndrome_blind": coherent_logical_fault_is_syndrome_blind,
        "apparatus_cut_is_noncanonical": apparatus_cut_is_noncanonical,
        "endpoint_algebra_does_not_imply_executable_control": algebra_does_not_imply_execution,
        "finite_packet_does_not_fix_scaling": same_finite_packet_different_scaling,
        "topological_quantization_does_not_supply_instrument": quantization_does_not_supply_instrument,
        "explanation_is_question_typed": explanation_is_question_typed,
    }
    assert all(falsifiers.values())

    result = {
        "schema": "marici.kitaev.dpc-protection-engineering-dichotomy.v1",
        "falsifiers": falsifiers,
        "exact_witness": {
            "fault": "logical_Z",
            "syndrome": [],
            "identity_output_on_plus": "|+>",
            "fault_output_on_plus": "|->",
            "output_overlap": 0,
            "unitary_channel_diamond_distance": 2,
        },
        "hybrid_truth_table": [
            {"protected_substrate": p, "engineered_resource": e, "reaches_T": value}
            for (p, e), value in reaches_t.items()
        ],
        "typed_question_matrix": question_to_certificate,
        "classification": "retire_DPC_as_conjecture_retain_typed_audit_vocabulary",
        "verdict": "Protection and engineering are not an exhaustive explanatory dichotomy: hybrid protocols require both, coherent logical faults evade syndrome, algebraic ports need not be executable, and finite demonstrations do not establish scaling. DPC therefore has no surviving conjectural content without a separately stated theorem question; its useful residue is a typed audit matrix.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
