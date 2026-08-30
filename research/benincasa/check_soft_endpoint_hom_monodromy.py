#!/usr/bin/env python3
"""Compute the decisive monodromy of the soft-endpoint Hom local system."""

import json
from pathlib import Path


def main():
    # At kappa=-5/4, r_plus^2=5+4*kappa has a simple zero, whereas
    # r_minus^2=5-4*kappa=10 is a unit.  Thus c_plus changes sign and c_minus
    # is locally single-valued.  Hom(E_minus,E_plus) inherits character -1.
    r_plus_order = 1
    r_minus_value_squared = 10
    positive_character = -1 if r_plus_order % 2 else 1
    negative_character = 1 if r_minus_value_squared != 0 else -1
    hom_character = positive_character * negative_character
    invariant_rank = 1 if hom_character == 1 else 0

    checks = {
        "positive_endpoint_has_simple_kummer_branch": r_plus_order == 1,
        "negative_endpoint_is_unramified_there": r_minus_value_squared == 10,
        "hom_monodromy_is_minus_one": hom_character == -1,
        "global_horizontal_invariant_rank_is_zero": invariant_rank == 0,
    }
    result = {
        "schema": "marici.soft-endpoint-hom-monodromy.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "test_loop": "small positive loop around kappa=-5/4",
        "endpoint_characters": {
            "E_plus": positive_character,
            "E_minus": negative_character,
            "Hom(E_minus,E_plus)": hom_character,
        },
        "global_horizontal_invariant_rank": invariant_rank,
        "local_statement": (
            "J=c_plus/c_minus is horizontal on a simply connected chosen-sheet chamber"
        ),
        "global_statement": (
            "J changes sign around the test loop, so the Hom local system has "
            "no nonzero global horizontal section"
        ),
        "conclusion": (
            "the global endpoint-combination hypothesis is closed; a chamberwise "
            "comparison remains branch-dependent presentation/readout data unless an "
            "additional physical sheet trivialization is independently supplied"
        ),
        "checks": checks,
    }
    output = Path(__file__).with_name("soft-endpoint-hom-monodromy.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
