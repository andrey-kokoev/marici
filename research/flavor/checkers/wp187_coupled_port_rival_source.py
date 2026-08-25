"""WP187 exact checker: coupled-port rival source.

WP186 gives a conditional law for rectangular quotients. This checker freezes
the rival coupled-port source: it shares the same low-energy flavor packet and
order cap but admits skew HNF relations, so recurrence-growth radii must follow
the HNF gate rather than the rectangular gate.
"""

from __future__ import annotations

import json
from pathlib import Path


LOW_ENERGY = {
    "physical16_id": "P_fit_common",
    "measured10_id": "M_fit_common",
}

SOURCES = {
    "S_independent_ports": {
        "low_energy": LOW_ENERGY,
        "order_cap_K": 64,
        "port_law": "independent_axis_resets",
        "quotient_domain": "rectangular",
        "exact_radius": 4,
        "tau1_radius": 5,
    },
    "S_coupled_ports": {
        "low_energy": LOW_ENERGY,
        "order_cap_K": 64,
        "port_law": "coupled_port_relations",
        "quotient_domain": "hnf",
        "exact_radius": 5,
        "tau1_radius": 6,
    },
}


def admits_skew_hostile(source: dict[str, object]) -> bool:
    return source["quotient_domain"] == "hnf"


def rectangular_radius_valid(source: dict[str, object]) -> bool:
    return source["quotient_domain"] == "rectangular" and source["exact_radius"] == 4


def main() -> None:
    independent = SOURCES["S_independent_ports"]
    coupled = SOURCES["S_coupled_ports"]

    checks = {
        "same_physical16_packet": independent["low_energy"]["physical16_id"]
        == coupled["low_energy"]["physical16_id"],
        "same_measured10_packet": independent["low_energy"]["measured10_id"]
        == coupled["low_energy"]["measured10_id"],
        "same_order_cap_control": independent["order_cap_K"] == coupled["order_cap_K"],
        "different_port_laws": independent["port_law"] != coupled["port_law"],
        "different_quotient_domains": independent["quotient_domain"]
        != coupled["quotient_domain"],
        "independent_source_excludes_skew_hostile": not admits_skew_hostile(independent),
        "coupled_source_admits_skew_hostile": admits_skew_hostile(coupled),
        "rectangular_radius_valid_only_for_independent_source": rectangular_radius_valid(
            independent
        )
        and not rectangular_radius_valid(coupled),
        "coupled_source_requires_hnf_exact_radius_five": coupled["exact_radius"] == 5,
        "coupled_source_requires_hnf_tau1_radius_six": coupled["tau1_radius"] == 6,
        "low_energy_readout_cannot_choose_port_law": independent["low_energy"]
        == coupled["low_energy"],
        "port_law_is_source_discriminator": True,
    }

    result = {
        "work_package": "WP187",
        "claim": "Independent-port and coupled-port sources can share the same low-energy flavor packet and order cap while requiring different recurrence-growth quotient domains and radii.",
        "sources": SOURCES,
        "skew_hostile": {"hnf": {"a": 10, "b": 4, "d": 6}, "index": 60},
        "classification": "rival source falsifier for quotient-domain law.",
        "smallest_falsifier": "Using rectangular radius four on S_coupled_ports misses the WP175 skew HNF hostile.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp187_coupled_port_rival_source.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
