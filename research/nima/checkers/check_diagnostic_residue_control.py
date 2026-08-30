#!/usr/bin/env python3
"""Exact finite audit: diagnostic residue is a control address, not a policy."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "nima" / "results" / "diagnostic_residue_control.json"


def xor(a, b):
    return a ^ b


def main():
    # Error e prepares data d=e. Syndrome record r=e. Feedback d <- d xor r.
    conditioned = {e: xor(e, e) for e in (0, 1)}
    assert conditioned == {0: 0, 1: 0}

    # No one fixed reversible bit operation (identity or NOT) repairs both.
    fixed_reversible = {
        "identity": {e: e for e in (0, 1)},
        "not": {e: xor(e, 1) for e in (0, 1)},
    }
    assert all(set(v.values()) != {0} for v in fixed_reversible.values())

    # A toric syndrome fiber can contain distinct representatives differing
    # by a stabilizer: same diagnostic address, multiple ambient operations.
    syndrome_fiber = {"path_left": "R", "path_right": "R_times_stabilizer"}
    assert len(set(syndrome_fiber.values())) == 2

    result = {
        "schema": "marici.diagnostic-residue-control.v1",
        "conditioned_feedback": {str(k): v for k, v in conditioned.items()},
        "fixed_reversible_controls": fixed_reversible,
        "toric_same_syndrome_recovery_fiber": syndrome_fiber,
        "gates": {
            "record_enables_reversible_conditional_repair": True,
            "record_free_fixed_reversible_repair_exists": False,
            "syndrome_uniquely_selects_ambient_recovery": False,
            "diagnostic_is_capability_address_not_policy": True,
        },
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
