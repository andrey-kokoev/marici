#!/usr/bin/env python3
"""Bounded falsifier for the extension-admission conjecture."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


NIMA = Path(__file__).resolve().parents[1]
RESULT = NIMA / "results" / "extension-admission-census.json"

# Routes are assigned from provenance and conservativity, not from outcome.
# U: universal/conservative; P: independently source-provenanced;
# F: fitted/post-hoc content amplification; ?: authority unresolved.
CASES = [
    ("normalization_connector", "P", True, "physical_success", "entries 400,436"),
    ("filtered_jordan_recollement", "P", True, "physical_success", "entries 410-436"),
    ("cut_localization_quotient", "U", False, "formal_success", "entries 533; event 2641"),
    ("thom_twisted_cut_line", "P", True, "physical_success", "entries 446,533"),
    ("formal_koszul_completion", "U", False, "formal_success", "entry 160"),
    ("formal_koszul_cell_as_physical_Q", "F", True, "rejected", "entries 160,524"),
    ("newton_weighted_blowup", "P", False, "geometric_success", "entries 451-460"),
    ("exceptional_form_promoted_to_physical_current", "F", True, "rejected", "entries 747,788,801"),
    ("all_soft_flat_differential_character", "P", True, "coefficient_success_readout_silent", "nima packet"),
    ("fitted_conic_Q_connection", "F", True, "rejected", "entries 526-528"),
    ("QD_torsion_module_interpretation", "F", True, "rejected_untyped", "entries 512-516"),
    ("flavor_chart_phase_as_physical_law", "F", True, "rejected", "entries 1042,1047"),
    ("source_normalized_leray_covector", "?", True, "open", "cosmology frontier"),
    ("theta_positive_order_two_stieltjes_measure", "?", True, "open", "RH frontier"),
    ("primitive_verdier_quotient_diagnostic", "U", False, "formal_success", "entries 406-409"),
    ("erase_A2_contact_sector_physically", "F", True, "rejected", "entries 406-410"),
    ("generic_Q_quartic_as_intrinsic_support", "F", True, "rejected_apparent", "Q lifecycle closure"),
    ("six_point_fs_kato_physical_pullback", "P", True, "physical_success", "entries 435-436"),
]


def main() -> None:
    rows = [
        {
            "case": case,
            "route": route,
            "novel_governed_readout": novel,
            "outcome": outcome,
            "evidence": evidence,
        }
        for case, route, novel, outcome, evidence in CASES
    ]
    route_counts = Counter(row["route"] for row in rows)
    outcome_counts = Counter(row["outcome"] for row in rows)
    fitted_physical_successes = [
        row for row in rows
        if row["route"] == "F" and row["outcome"] == "physical_success"
    ]
    successful_content_without_provenance = [
        row for row in rows
        if row["novel_governed_readout"]
        and row["outcome"] == "physical_success"
        and row["route"] not in {"P"}
    ]
    checks = {
        "routes_predeclared": set(route_counts) == {"U", "P", "F", "?"},
        "universal_route_contains_no_novel_readout": all(
            not row["novel_governed_readout"] for row in rows if row["route"] == "U"
        ),
        "no_fitted_physical_success_in_census": not fitted_physical_successes,
        "all_physical_successes_are_source_provenanced":
            not successful_content_without_provenance,
        "negative_controls_present": route_counts["F"] > 0,
        "unresolved_frontiers_preserved": route_counts["?"] > 0,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    payload = {
        "schema": "marici.extension-admission-census.v1",
        "status": "pass",
        "scope": "bounded retrospective census; evidence, not a universal theorem",
        "routes": {
            "U": "universal or conservative; no new governed readout",
            "P": "independently source-provenanced content",
            "F": "fitted or post-hoc content amplification",
            "?": "authority unresolved",
        },
        "route_counts": dict(route_counts),
        "outcome_counts": dict(outcome_counts),
        "cases": rows,
        "checks": checks,
    }
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
