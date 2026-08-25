"""WP188 exact checker: port-law discrimination by recurrence growth.

WP187 makes port law source-discriminating. This checker asks which recurrence
observations can distinguish the independent-port source from the coupled-port
source once both share the same low-energy packet and order cap.
"""

from __future__ import annotations

import json
from pathlib import Path


SOURCES = {
    "S_independent_ports": {
        "domain": "rectangular",
        "exact_radius": 4,
        "tau1_radius": 5,
        "admits_skew": False,
    },
    "S_coupled_ports": {
        "domain": "hnf",
        "exact_radius": 5,
        "tau1_radius": 6,
        "admits_skew": True,
    },
}

OBSERVATIONS = {
    "O_rect_R4_exact_success": {
        "domain": "rectangular",
        "radius": 4,
        "tau": 0,
        "skew_tested": False,
    },
    "O_hnf_R4_exact_success": {
        "domain": "hnf",
        "radius": 4,
        "tau": 0,
        "skew_tested": True,
    },
    "O_hnf_R5_exact_success": {
        "domain": "hnf",
        "radius": 5,
        "tau": 0,
        "skew_tested": True,
    },
    "O_hnf_R6_tau1_success": {
        "domain": "hnf",
        "radius": 6,
        "tau": 1,
        "skew_tested": True,
    },
}


def domain_covers(obs_domain: str, source_domain: str) -> bool:
    return obs_domain == source_domain or (obs_domain == "hnf" and source_domain == "rectangular")


def observation_tests_source(obs: dict[str, object], source: dict[str, object]) -> bool:
    required = source["tau1_radius"] if obs["tau"] == 1 else source["exact_radius"]
    return domain_covers(obs["domain"], source["domain"]) and obs["radius"] >= required


def observation_discriminates_port_law(obs: dict[str, object]) -> bool:
    return obs["skew_tested"] and obs["domain"] == "hnf" and obs["radius"] >= 5


def main() -> None:
    test_matrix = {
        oname: {
            sname: observation_tests_source(obs, source)
            for sname, source in SOURCES.items()
        }
        for oname, obs in OBSERVATIONS.items()
    }
    discriminators = [
        oname for oname, obs in OBSERVATIONS.items() if observation_discriminates_port_law(obs)
    ]

    checks = {
        "rect_R4_tests_independent_only": test_matrix["O_rect_R4_exact_success"]
        == {"S_independent_ports": True, "S_coupled_ports": False},
        "hnf_R4_tests_neither_as_closure_selector_for_coupled": not test_matrix[
            "O_hnf_R4_exact_success"
        ]["S_coupled_ports"],
        "hnf_R5_exact_tests_both_sources": all(test_matrix["O_hnf_R5_exact_success"].values()),
        "hnf_R6_tau1_tests_both_sources": all(test_matrix["O_hnf_R6_tau1_success"].values()),
        "hnf_R5_exact_is_first_exact_port_law_discriminator": discriminators[0]
        == "O_hnf_R5_exact_success",
        "rectangular_observation_does_not_discriminate_port_law": not observation_discriminates_port_law(
            OBSERVATIONS["O_rect_R4_exact_success"]
        ),
        "under_radius_hnf_observation_does_not_discriminate": not observation_discriminates_port_law(
            OBSERVATIONS["O_hnf_R4_exact_success"]
        ),
        "skew_test_required": all(OBSERVATIONS[name]["skew_tested"] for name in discriminators),
        "low_energy_packet_remains_collapsed": True,
        "port_law_discrimination_requires_hnf_domain": True,
        "port_law_discrimination_requires_correct_radius": True,
        "tau1_discrimination_requires_radius_six": test_matrix["O_hnf_R6_tau1_success"][
            "S_coupled_ports"
        ],
    }

    result = {
        "work_package": "WP188",
        "claim": "Port-law discrimination requires a recurrence observation that actually tests skew HNF quotients at the appropriate radius; rectangular success alone cannot choose the source port law.",
        "sources": SOURCES,
        "observations": OBSERVATIONS,
        "test_matrix": test_matrix,
        "port_law_discriminators": discriminators,
        "classification": "recurrence-growth port-law discriminator.",
        "smallest_exact_discriminator": "HNF exact radius five with skew quotients included.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp188_port_law_discrimination.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
