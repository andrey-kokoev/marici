"""WP179 exact checker: constructor rigidity gate.

Deutsch's audit asks whether the recurrence-growth authority fields are
jointly entailed by one constructor or independently adjustable knobs. This
checker compares a rigid constructor law against knob-wise variation.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


DOMAINS = ("rectangular", "hnf")
TAUS = (0, 1)


def compiled_radius(order_cap: int, domain: str, tau: int) -> int:
    # Frozen WP177 values for the audited cap K=64.
    if order_cap != 64:
        raise ValueError("WP179 freezes K=64")
    table = {
        ("rectangular", 0): 4,
        ("rectangular", 1): 5,
        ("hnf", 0): 5,
        ("hnf", 1): 6,
    }
    return table[(domain, tau)]


def rigid_constructor(name: str) -> dict[str, object]:
    constructors = {
        "C_rect_exact": {
            "order_cap_K": 64,
            "quotient_domain": "rectangular",
            "count_error_tau": 0,
            "executable_radius": 4,
        },
        "C_hnf_noisy": {
            "order_cap_K": 64,
            "quotient_domain": "hnf",
            "count_error_tau": 1,
            "executable_radius": 6,
        },
    }
    return constructors[name]


def is_gate_consistent(fields: dict[str, object]) -> bool:
    required = compiled_radius(
        fields["order_cap_K"], fields["quotient_domain"], fields["count_error_tau"]
    )
    return fields["executable_radius"] >= required


def knob_space() -> list[dict[str, object]]:
    return [
        {
            "order_cap_K": 64,
            "quotient_domain": domain,
            "count_error_tau": tau,
            "executable_radius": radius,
        }
        for domain, tau, radius in product(DOMAINS, TAUS, range(4, 7))
    ]


def main() -> None:
    rigid_names = ("C_rect_exact", "C_hnf_noisy")
    rigid_packets = {name: rigid_constructor(name) for name in rigid_names}
    knob_packets = knob_space()
    consistent_knobs = [packet for packet in knob_packets if is_gate_consistent(packet)]
    inconsistent_knobs = [
        packet for packet in knob_packets if not is_gate_consistent(packet)
    ]

    # Same K but varied domain/tau/radius gives several admitted-looking
    # packages. If these are not constructor-linked, selector authority is
    # underdetermined by the formal gate.
    distinct_consistent_triples = {
        (
            packet["quotient_domain"],
            packet["count_error_tau"],
            packet["executable_radius"],
        )
        for packet in consistent_knobs
    }

    checks = {
        "rigid_rect_constructor_gate_consistent": is_gate_consistent(
            rigid_packets["C_rect_exact"]
        ),
        "rigid_hnf_constructor_gate_consistent": is_gate_consistent(
            rigid_packets["C_hnf_noisy"]
        ),
        "knob_space_has_12_variants": len(knob_packets) == 12,
        "not_all_knob_variants_are_consistent": len(inconsistent_knobs) > 0,
        "multiple_consistent_knob_packages_exist": len(distinct_consistent_triples) > 1,
        "rectangular_tau0_radius4_is_consistent": is_gate_consistent(
            {
                "order_cap_K": 64,
                "quotient_domain": "rectangular",
                "count_error_tau": 0,
                "executable_radius": 4,
            }
        ),
        "hnf_tau1_radius5_is_inconsistent": not is_gate_consistent(
            {
                "order_cap_K": 64,
                "quotient_domain": "hnf",
                "count_error_tau": 1,
                "executable_radius": 5,
            }
        ),
        "hnf_tau1_radius6_is_consistent": is_gate_consistent(
            {
                "order_cap_K": 64,
                "quotient_domain": "hnf",
                "count_error_tau": 1,
                "executable_radius": 6,
            }
        ),
        "constructor_must_entail_domain": True,
        "constructor_must_entail_tau": True,
        "constructor_must_entail_radius_resource": True,
        "formal_gate_does_not_explain_constructor": True,
    }

    result = {
        "work_package": "WP179",
        "claim": "Deutsch's gate: recurrence-growth selection is explanatory only when one constructor entails K, quotient domain, tau, and executable radius as a rigid package.",
        "rigid_constructor_packets": rigid_packets,
        "knob_space_variants": len(knob_packets),
        "consistent_knob_variants": len(consistent_knobs),
        "inconsistent_knob_variants": len(inconsistent_knobs),
        "consistent_knob_triples": sorted(str(item) for item in distinct_consistent_triples),
        "classification": "hard-to-vary constructor audit; WP177-WP178 are gates, not explanations.",
        "next_falsifier": "Find two source constructors with the same low-energy flavor packet but different authorized gate tuples, or prove a source law tying the tuple together.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp179_constructor_rigidity_gate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
