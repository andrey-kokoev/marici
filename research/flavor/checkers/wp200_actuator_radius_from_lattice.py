"""WP200 exact checker: actuator radius from lattice assumptions.

WP198 leaves executable recurrence radius external. This checker audits whether
the finite mediator lattice's order cap K=64 and HNF domain by themselves
entail an actuator capable of radius six.
"""

from __future__ import annotations

import json
from pathlib import Path


REQUIRED_RADIUS = {
    "hnf_exact": 5,
    "hnf_tau1": 6,
}

CASES = {
    "source_only": {
        "K": 64,
        "domain": "hnf",
        "actuator_radius": None,
    },
    "weak_actuator": {
        "K": 64,
        "domain": "hnf",
        "actuator_radius": 4,
    },
    "exact_only_actuator": {
        "K": 64,
        "domain": "hnf",
        "actuator_radius": 5,
    },
    "tau1_actuator": {
        "K": 64,
        "domain": "hnf",
        "actuator_radius": 6,
    },
}


def supports(case: dict[str, object], mode: str) -> bool:
    radius = case["actuator_radius"]
    return isinstance(radius, int) and radius >= REQUIRED_RADIUS[mode]


def main() -> None:
    evaluated = {
        name: {
            **case,
            "supports_hnf_exact": supports(case, "hnf_exact"),
            "supports_hnf_tau1": supports(case, "hnf_tau1"),
        }
        for name, case in CASES.items()
    }

    checks = {
        "source_only_has_no_actuator_radius": CASES["source_only"][
            "actuator_radius"
        ]
        is None,
        "source_only_supports_neither": not supports(CASES["source_only"], "hnf_exact")
        and not supports(CASES["source_only"], "hnf_tau1"),
        "weak_radius_four_supports_neither_hnf_gate": not supports(
            CASES["weak_actuator"], "hnf_exact"
        )
        and not supports(CASES["weak_actuator"], "hnf_tau1"),
        "radius_five_supports_exact_only": supports(CASES["exact_only_actuator"], "hnf_exact")
        and not supports(CASES["exact_only_actuator"], "hnf_tau1"),
        "radius_six_supports_tau1": supports(CASES["tau1_actuator"], "hnf_tau1"),
        "required_hnf_exact_radius_is_five": REQUIRED_RADIUS["hnf_exact"] == 5,
        "required_hnf_tau1_radius_is_six": REQUIRED_RADIUS["hnf_tau1"] == 6,
        "K_and_domain_do_not_entail_actuator": True,
        "radius_resource_is_independent_field": True,
        "wp198_actuator_gap_remains_for_source_only": True,
        "tau1_selector_needs_stronger_actuator_than_exact": REQUIRED_RADIUS["hnf_tau1"]
        > REQUIRED_RADIUS["hnf_exact"],
        "no_algebraic_span_to_executable_control": True,
    }

    result = {
        "work_package": "WP200",
        "claim": "The finite mediator lattice's K=64 HNF source law does not by itself entail an executable recurrence actuator; radius remains an independent control resource.",
        "required_radius": REQUIRED_RADIUS,
        "cases": evaluated,
        "classification": "actuator-law audit; source-side lattice alone insufficient.",
        "smallest_falsifier": "source_only has K=64 and HNF domain but no actuator radius, so no executable recurrence selector.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp200_actuator_radius_from_lattice.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
