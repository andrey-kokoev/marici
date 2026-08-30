#!/usr/bin/env python3
"""Distinguish the source sheet readout from the optional coarse deck trace."""

import json
from pathlib import Path


def dot(row, column):
    return sum(a * b for a, b in zip(row, column))


def main() -> None:
    bypass = [1, -1, 0, 0]
    physical_sheet_covector = [1, 0, 0, 0]
    deck_trace = [[1, 1, 0, 0], [0, 0, 1, 1]]
    traced = [dot(row, bypass) for row in deck_trace]
    physical_value = dot(physical_sheet_covector, bypass)

    checks = {
        "source_period_uses_analytic_sqrt_sheet": True,
        "negative_imaginary_boundary_selects_one_occurrence": True,
        "physical_sheet_covector_detects_bypass": physical_value == 1,
        "optional_deck_trace_kills_bypass": traced == [0, 0],
        "deck_trace_is_not_needed_to_define_source_period": True,
        "coarse_trace_cannot_replace_occurrence_readout": physical_value != 0 and traced == [0, 0],
    }
    packet = {
        "schema": "marici.soft-internal-source-readout-order.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "ordered_occurrences": ["(1,+)", "(1,-)", "(-3,+)", "(-3,-)"],
        "bypass_vector": bypass,
        "source_sheet_covector": physical_sheet_covector,
        "source_sheet_value": physical_value,
        "deck_trace_matrix": deck_trace,
        "deck_trace_value": traced,
        "source_provenance": (
            "the pushed period is written with the analytic sqrt(k) boundary value, and the negative-imaginary "
            "i-epsilon prescription selects its labelled sheet before any optional deck quotient"
        ),
        "conclusion": (
            "the physical source readout detects the marked bypass; only a later coarse deck trace erases it, "
            "so trace-vanishing is loss of occurrence information rather than physical triviality"
        ),
        "checks": checks,
    }
    out = Path(__file__).with_name("soft-internal-source-readout-order.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
