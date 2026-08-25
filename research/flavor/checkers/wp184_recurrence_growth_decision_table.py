"""WP184 exact checker: recurrence-growth decision table.

This checker consolidates WP167-WP183 into a compact decision table of
overclaims, missing gates, and smallest exact falsifiers.
"""

from __future__ import annotations

import json
from pathlib import Path


ROWS = [
    {
        "overclaim": "bounded_relation_certifies_infinite_closure",
        "missing_gate": "source exponent cap or nonlocal instrument",
        "smallest_falsifier": "depth L: Z^2 versus (Z/(L+1)Z)^2",
        "governing_wp": "WP167",
        "admissible_claim": "bounded relation rigidifier only",
    },
    {
        "overclaim": "under_depth_adaptive_relation_protocol_suffices",
        "missing_gate": "maximum word depth at least source exponent cap",
        "smallest_falsifier": "E=8: all words through depth 7 agree; +e1^8 separates",
        "governing_wp": "WP169",
        "admissible_claim": "depth-E relation selector under source exponent cap",
    },
    {
        "overclaim": "finite_growth_window_is_order_oracle",
        "missing_gate": "source size bound or unbounded recurrence observation",
        "smallest_falsifier": "R=3: Z^2 versus (Z/7Z)^2 share growth 1,5,13,25",
        "governing_wp": "WP171",
        "admissible_claim": "finite growth-window rigidifier only",
    },
    {
        "overclaim": "rectangular_order_radius_ports_to_all_quotients",
        "missing_gate": "legal quotient-domain law",
        "smallest_falsifier": "K=64: HNF (10,4,6) and (10,5,6) match through radius 4",
        "governing_wp": "WP175",
        "admissible_claim": "domain-relative recurrence radius",
    },
    {
        "overclaim": "noiseless_growth_margin_survives_detector_error",
        "missing_gate": "calibrated count error with d_min(R)>2 tau",
        "smallest_falsifier": "HNF K=64,R=5,tau=1: HNF (10,5,6) has deficit 1",
        "governing_wp": "WP176",
        "admissible_claim": "error-robust recurrence radius",
    },
    {
        "overclaim": "compiled_gate_is_physical_authority",
        "missing_gate": "all four source/instrument fields authorized",
        "smallest_falsifier": "15 incomplete authorization patterns in WP178",
        "governing_wp": "WP178",
        "admissible_claim": "formal gate until fields are authorized",
    },
    {
        "overclaim": "low_energy_packet_explains_gate_tuple",
        "missing_gate": "hard-to-vary constructor law",
        "smallest_falsifier": "C_rect_exact versus C_hnf_noisy share low-energy packet but differ in gate tuple",
        "governing_wp": "WP180",
        "admissible_claim": "constructor-sensitive discriminator",
    },
    {
        "overclaim": "single_noisy_channel_compares_exact_and_noisy_constructors",
        "missing_gate": "typed vector instrument or authorized degradation",
        "smallest_falsifier": "I_hnf_R6_tau1 tests C_hnf_noisy but not C_rect_exact",
        "governing_wp": "WP181",
        "admissible_claim": "vector-channel constructor comparison",
    },
    {
        "overclaim": "exact_channel_automatically_covers_noisy_contract",
        "missing_gate": "authorized exact-to-noisy degradation map",
        "smallest_falsifier": "exact HNF R6 does not test C_hnf_noisy without degradation",
        "governing_wp": "WP182",
        "admissible_claim": "compressed single channel only with degradation authority",
    },
]


def main() -> None:
    governing = {row["governing_wp"] for row in ROWS}
    checks = {
        "nine_decision_rows": len(ROWS) == 9,
        "all_rows_have_overclaim": all(row["overclaim"] for row in ROWS),
        "all_rows_have_missing_gate": all(row["missing_gate"] for row in ROWS),
        "all_rows_have_falsifier": all(row["smallest_falsifier"] for row in ROWS),
        "all_rows_have_admissible_claim": all(row["admissible_claim"] for row in ROWS),
        "wp167_included": "WP167" in governing,
        "wp175_domain_correction_included": "WP175" in governing,
        "wp176_detector_margin_included": "WP176" in governing,
        "wp180_constructor_kernel_included": "WP180" in governing,
        "wp182_degradation_gate_included": "WP182" in governing,
        "overclaims_unique": len({row["overclaim"] for row in ROWS}) == len(ROWS),
        "falsifiers_unique": len({row["smallest_falsifier"] for row in ROWS})
        == len(ROWS),
    }

    result = {
        "work_package": "WP184",
        "claim": "The recurrence-growth branch admits a compact decision table: every selector overclaim has a named missing gate and smallest exact falsifier.",
        "decision_rows": ROWS,
        "classification": "branch closeout and admission table; no new selector.",
        "next_frontier": "Search for a source constructor law that entails K, quotient domain, tau, executable radius, and degradation authority.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp184_recurrence_growth_decision_table.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
