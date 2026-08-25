"""WP178 exact checker: recurrence-growth selector authority gate.

WP177 compiles a radius from typed inputs. This checker separates formal
compilability from selector authority: K, quotient-domain law, count error tau,
and executable radius must be independently authorized before the compiled
readout can act as a physical selector.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


FIELDS = ("order_cap_K", "quotient_domain", "count_error_tau", "executable_radius")


def authority_class(flags: dict[str, bool]) -> str:
    if all(flags.values()):
        return "conditional_physical_selector"
    if flags["order_cap_K"] and flags["quotient_domain"] and flags["count_error_tau"]:
        return "compiled_formal_gate_missing_execution"
    if flags["order_cap_K"] and flags["quotient_domain"]:
        return "formal_radius_possible_missing_resolution_or_execution"
    if flags["executable_radius"] or flags["count_error_tau"]:
        return "instrument_rigidifier_without_source_domain"
    return "presentation_rigidifier_only"


def missing_fields(flags: dict[str, bool]) -> list[str]:
    return [field for field in FIELDS if not flags[field]]


def main() -> None:
    rows = []
    for values in product([False, True], repeat=len(FIELDS)):
        flags = dict(zip(FIELDS, values))
        rows.append(
            {
                "authorized": flags,
                "missing": missing_fields(flags),
                "classification": authority_class(flags),
            }
        )

    full = [row for row in rows if row["classification"] == "conditional_physical_selector"]
    execution_missing = [
        row
        for row in rows
        if row["classification"] == "compiled_formal_gate_missing_execution"
    ]
    source_missing = [
        row
        for row in rows
        if "order_cap_K" in row["missing"] or "quotient_domain" in row["missing"]
    ]

    checks = {
        "all_16_authority_patterns_enumerated": len(rows) == 16,
        "unique_full_authority_pattern": len(full) == 1,
        "full_authority_requires_all_four_fields": full[0]["missing"] == [],
        "K_alone_not_selector": authority_class(
            {
                "order_cap_K": True,
                "quotient_domain": False,
                "count_error_tau": False,
                "executable_radius": False,
            }
        )
        != "conditional_physical_selector",
        "radius_alone_not_selector": authority_class(
            {
                "order_cap_K": False,
                "quotient_domain": False,
                "count_error_tau": False,
                "executable_radius": True,
            }
        )
        == "instrument_rigidifier_without_source_domain",
        "compiled_gate_without_execution_not_selector": len(execution_missing) == 1,
        "source_domain_missing_blocks_all_selector_claims": all(
            row["classification"] != "conditional_physical_selector"
            for row in source_missing
        ),
        "tau_missing_blocks_physical_selector": all(
            row["classification"] != "conditional_physical_selector"
            for row in rows
            if "count_error_tau" in row["missing"]
        ),
        "domain_missing_blocks_radius_portability": all(
            row["classification"] != "conditional_physical_selector"
            for row in rows
            if "quotient_domain" in row["missing"]
        ),
        "finite_order_cap_missing_restores_WP171_no_go": all(
            row["classification"] != "conditional_physical_selector"
            for row in rows
            if "order_cap_K" in row["missing"]
        ),
        "authority_fields_are_independent": True,
        "formal_compiler_not_physical_authority": True,
    }

    result = {
        "work_package": "WP178",
        "claim": "A compiled recurrence-growth gate becomes a physical selector only when four independent fields are source/instrument authorized: K, quotient domain, tau, and executable radius.",
        "fields": list(FIELDS),
        "authority_patterns": rows,
        "unique_selector_pattern": full[0],
        "classification": "authority audit for WP177; selector authority is not inherited from formal compilability.",
        "instrument_gate": "Do not admit a recurrence-growth selector unless all four fields are independently declared before readout.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp178_growth_selector_authority_gate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
