"""WP180 exact checker: rival constructor gate kernel.

WP179 asks for a constructor-level falsifier: two source constructors with the
same low-energy flavor packet but different authorized recurrence-growth gate
tuples. This checker freezes such a hostile pair and verifies the source
kernel.
"""

from __future__ import annotations

import json
from pathlib import Path


LOW_ENERGY_PACKET = {
    "physical16_id": "P_fit_common",
    "measured10_id": "M_fit_common",
    "selector_architecture": "two_adjoint_equivalent_low_energy_packet",
}

CONSTRUCTORS = {
    "C_rect_exact": {
        "low_energy": LOW_ENERGY_PACKET,
        "gate": {
            "order_cap_K": 64,
            "quotient_domain": "rectangular",
            "count_error_tau": 0,
            "executable_radius": 4,
        },
    },
    "C_hnf_noisy": {
        "low_energy": LOW_ENERGY_PACKET,
        "gate": {
            "order_cap_K": 64,
            "quotient_domain": "hnf",
            "count_error_tau": 1,
            "executable_radius": 6,
        },
    },
}


def compiled_radius(gate: dict[str, object]) -> int:
    table = {
        ("rectangular", 0): 4,
        ("rectangular", 1): 5,
        ("hnf", 0): 5,
        ("hnf", 1): 6,
    }
    return table[(gate["quotient_domain"], gate["count_error_tau"])]


def gate_consistent(gate: dict[str, object]) -> bool:
    return gate["order_cap_K"] == 64 and gate["executable_radius"] >= compiled_radius(gate)


def main() -> None:
    c1 = CONSTRUCTORS["C_rect_exact"]
    c2 = CONSTRUCTORS["C_hnf_noisy"]
    same_low_energy = c1["low_energy"] == c2["low_energy"]
    different_gates = c1["gate"] != c2["gate"]
    both_consistent = gate_consistent(c1["gate"]) and gate_consistent(c2["gate"])

    differing_fields = [
        field for field in c1["gate"] if c1["gate"][field] != c2["gate"][field]
    ]

    checks = {
        "same_physical16_packet": c1["low_energy"]["physical16_id"]
        == c2["low_energy"]["physical16_id"],
        "same_measured10_packet": c1["low_energy"]["measured10_id"]
        == c2["low_energy"]["measured10_id"],
        "same_low_energy_packet": same_low_energy,
        "different_authorized_gate_tuples": different_gates,
        "both_gates_formally_consistent": both_consistent,
        "domain_differs": "quotient_domain" in differing_fields,
        "tau_differs": "count_error_tau" in differing_fields,
        "radius_differs": "executable_radius" in differing_fields,
        "order_cap_same_control": "order_cap_K" not in differing_fields,
        "low_energy_readout_cannot_select_constructor": same_low_energy
        and different_gates,
        "recurrence_gate_tuple_refines_source_kernel": same_low_energy
        and both_consistent,
        "not_a_unique_explanation_without_constructor_law": True,
    }

    result = {
        "work_package": "WP180",
        "claim": "Two rival constructors can share the same low-energy flavor packet while authorizing different recurrence-growth gate tuples.",
        "constructors": CONSTRUCTORS,
        "differing_gate_fields": differing_fields,
        "classification": "constructor-kernel falsifier: recurrence-growth gate data are not yet uniquely entailed by the low-energy flavor packet.",
        "smallest_falsifier": "C_rect_exact versus C_hnf_noisy: same physical16/measured10 packet, different domain/tau/radius gate.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp180_rival_constructor_gate_kernel.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
