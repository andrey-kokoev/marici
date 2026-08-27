#!/usr/bin/env python3
"""Aggregate the two-prime source Laurent tests at both soft centers."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"
INPUTS = [
    RESULTS / "marked_extension_source_v0_residue.json",
    RESULTS / "marked_extension_source_v2_residue.json",
    RESULTS / "marked_extension_source_v0_residue_prime_default.json",
    RESULTS / "marked_extension_source_v2_residue_prime_default.json",
]
OUTPUT = RESULTS / "two_soft_source_residue_freedom.json"


packets = [json.loads(path.read_text(encoding="utf-8")) for path in INPUTS]
checks = {
    "two_primes": len({packet["prime"] for packet in packets}) == 2,
    "both_soft_centers": {packet["series_center"] for packet in packets} == {0, 2},
    "two_replications_per_center": all(
        sum(packet["series_center"] == center for packet in packets) == 2
        for center in (0, 2)
    ),
    "held_out_identities": all(packet["held_out_polynomial_identity"] for packet in packets),
    "v_derivative_and_series": all(
        packet["derivative_axis"] == packet["series_axis"] == "v"
        for packet in packets
    ),
    "u_zero": all(packet["u_fixed"] == 0 for packet in packets),
    "target_never_pivot": all(not packet["target_is_pivot"] for packet in packets),
    "target_never_fixed": all(not packet["target_fixed"] for packet in packets),
    "rank_replicates_by_center": all(
        len({packet["rank"] for packet in packets if packet["series_center"] == center}) == 1
        for center in (0, 2)
    ),
}

packet = {
    "schema": "marici.benincasa.two_soft_source_residue_freedom.v1",
    "primes": sorted({packet["prime"] for packet in packets}),
    "centers": {
        str(center): {
            "meaning": "X3=0" if center == 0 else "X2=0",
            "rank": next(packet["rank"] for packet in packets if packet["series_center"] == center),
            "target": f"Res_v={center} (B_v)_e6,q0",
            "pivot": False,
            "source_fixed": False,
        }
        for center in (0, 2)
    },
    "checks": checks,
    "verdict": (
        "Neither soft residue of (B_v)_e6,q0 is locally fixed by the full "
        "cleared source Laurent module at u=0."
    ),
    "scope": (
        "This excludes local source selection at either soft germ. It does not "
        "exclude a global rational section that correlates the two free local residues."
    ),
    "next_gate": (
        "Solve the global one-variable polynomial module with common denominator "
        "v(v-2) and test whether the residue-difference functional is fixed."
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

OUTPUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
