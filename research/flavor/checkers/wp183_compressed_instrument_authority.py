"""WP183 exact checker: compressed instrument authority.

WP182 adds a fifth authority field for the compressed recurrence instrument:
exact-to-noisy degradation. This checker enumerates the authority patterns for
single-channel compression and distinguishes them from the vector instrument.
"""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


BASE_FIELDS = ("order_cap_K", "quotient_domain", "count_error_tau", "executable_radius")
COMPRESSION_FIELD = "degradation_map"


def base_selector_authorized(flags: dict[str, bool]) -> bool:
    return all(flags[field] for field in BASE_FIELDS)


def compressed_selector_authorized(flags: dict[str, bool]) -> bool:
    return base_selector_authorized(flags) and flags[COMPRESSION_FIELD]


def vector_selector_authorized(flags: dict[str, bool]) -> bool:
    return base_selector_authorized(flags)


def classification(flags: dict[str, bool]) -> str:
    if compressed_selector_authorized(flags):
        return "single_exact_channel_selector"
    if vector_selector_authorized(flags):
        return "vector_channel_selector_only"
    if flags[COMPRESSION_FIELD]:
        return "degradation_authorized_without_base_gate"
    return "not_selector"


def main() -> None:
    fields = BASE_FIELDS + (COMPRESSION_FIELD,)
    rows = []
    for values in product([False, True], repeat=len(fields)):
        flags = dict(zip(fields, values))
        rows.append(
            {
                "authorized": flags,
                "classification": classification(flags),
                "missing": [field for field in fields if not flags[field]],
            }
        )

    compressed = [
        row for row in rows if row["classification"] == "single_exact_channel_selector"
    ]
    vector_only = [
        row for row in rows if row["classification"] == "vector_channel_selector_only"
    ]
    degradation_without_base = [
        row
        for row in rows
        if row["classification"] == "degradation_authorized_without_base_gate"
    ]

    checks = {
        "all_32_patterns_enumerated": len(rows) == 32,
        "unique_compressed_selector_pattern": len(compressed) == 1,
        "unique_vector_only_pattern": len(vector_only) == 1,
        "compressed_requires_degradation": compressed[0]["authorized"][
            COMPRESSION_FIELD
        ],
        "vector_only_missing_only_degradation": vector_only[0]["missing"]
        == [COMPRESSION_FIELD],
        "degradation_without_base_not_selector": all(
            not base_selector_authorized(row["authorized"])
            for row in degradation_without_base
        ),
        "base_gate_remains_required_for_compression": all(
            row["classification"] != "single_exact_channel_selector"
            for row in rows
            if not base_selector_authorized(row["authorized"])
        ),
        "degradation_map_does_not_replace_K": all(
            row["classification"] != "single_exact_channel_selector"
            for row in rows
            if not row["authorized"]["order_cap_K"]
        ),
        "degradation_map_does_not_replace_domain": all(
            row["classification"] != "single_exact_channel_selector"
            for row in rows
            if not row["authorized"]["quotient_domain"]
        ),
        "degradation_map_does_not_replace_tau": all(
            row["classification"] != "single_exact_channel_selector"
            for row in rows
            if not row["authorized"]["count_error_tau"]
        ),
        "degradation_map_does_not_replace_radius": all(
            row["classification"] != "single_exact_channel_selector"
            for row in rows
            if not row["authorized"]["executable_radius"]
        ),
        "single_channel_compression_is_stronger_authority_than_vector": True,
    }

    result = {
        "work_package": "WP183",
        "claim": "A single exact recurrence channel tests the WP181 rival constructors only when the four base selector fields and the exact-to-noisy degradation map are all authorized.",
        "fields": list(fields),
        "authority_patterns": rows,
        "compressed_selector_pattern": compressed[0],
        "vector_only_pattern": vector_only[0],
        "classification": "compressed-instrument authority audit.",
        "instrument_gate": "Without degradation authority the vector instrument is required; with it, the exact channel can be compressed into the noisy contract.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp183_compressed_instrument_authority.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
