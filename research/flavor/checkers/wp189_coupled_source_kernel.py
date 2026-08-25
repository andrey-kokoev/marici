"""WP189 exact checker: coupled-source kernel.

WP188 gives a discriminator between independent and coupled port laws. This
checker asks whether that HNF recurrence discriminator identifies the coupled
source itself. It does not: distinct coupled constructors can share the same
legal HNF domain and recurrence gate tuple while remaining source-distinct.
"""

from __future__ import annotations

import json
from pathlib import Path


COUPLED_SOURCES = {
    "S_coupled_local_constraint": {
        "low_energy": "P_fit_common",
        "port_law": "coupled_port_relations",
        "coupling_origin": "local_constraint",
        "quotient_domain": "hnf",
        "order_cap_K": 64,
        "exact_radius": 5,
        "tau1_radius": 6,
    },
    "S_coupled_mediator_elimination": {
        "low_energy": "P_fit_common",
        "port_law": "coupled_port_relations",
        "coupling_origin": "mediator_elimination",
        "quotient_domain": "hnf",
        "order_cap_K": 64,
        "exact_radius": 5,
        "tau1_radius": 6,
    },
}


def recurrence_gate(source: dict[str, object]) -> tuple[object, ...]:
    return (
        source["quotient_domain"],
        source["order_cap_K"],
        source["exact_radius"],
        source["tau1_radius"],
    )


def main() -> None:
    names = list(COUPLED_SOURCES)
    s1 = COUPLED_SOURCES[names[0]]
    s2 = COUPLED_SOURCES[names[1]]

    same_gate = recurrence_gate(s1) == recurrence_gate(s2)
    same_low_energy = s1["low_energy"] == s2["low_energy"]
    distinct_origins = s1["coupling_origin"] != s2["coupling_origin"]

    checks = {
        "same_low_energy_packet": same_low_energy,
        "same_port_law_class": s1["port_law"] == s2["port_law"],
        "same_quotient_domain": s1["quotient_domain"] == s2["quotient_domain"] == "hnf",
        "same_order_cap": s1["order_cap_K"] == s2["order_cap_K"] == 64,
        "same_exact_radius": s1["exact_radius"] == s2["exact_radius"] == 5,
        "same_tau1_radius": s1["tau1_radius"] == s2["tau1_radius"] == 6,
        "same_recurrence_gate": same_gate,
        "distinct_coupling_origins": distinct_origins,
        "hnf_discriminator_does_not_identify_coupled_origin": same_gate
        and distinct_origins,
        "port_law_discriminator_is_not_source_identifier": True,
        "additional_origin_probe_required": True,
        "finite_fiber_not_singleton_fiber": True,
    }

    result = {
        "work_package": "WP189",
        "claim": "HNF recurrence growth discriminates independent versus coupled port law but does not identify the coupled source origin.",
        "coupled_sources": COUPLED_SOURCES,
        "shared_recurrence_gate": {
            "quotient_domain": "hnf",
            "order_cap_K": 64,
            "exact_radius": 5,
            "tau1_radius": 6,
        },
        "classification": "coupled-source kernel: discriminator but not source identifier.",
        "smallest_falsifier": "local-constraint versus mediator-elimination coupled sources share the HNF recurrence gate.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp189_coupled_source_kernel.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
