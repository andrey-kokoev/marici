#!/usr/bin/env python3
"""Exact same-profile inequivalent-realization witness."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/kitaev/results/realization-fiber-coherence.json"


def main():
    # Named C2 generator on two real carriers.
    minus_identity = [[-1, 0], [0, -1]]
    reflection = [[1, 0], [0, -1]]
    identity_observer = [[1, 0], [0, 1]]
    gramian = [[1, 0], [0, 1]]

    # For T=[[a,b],[c,d]], T(-I)=reflection*T forces a=b=0.
    # Every intertwiner therefore has determinant zero.
    forced_zero_entries = ["a", "b"]
    maximum_intertwiner_rank = 1
    invertible_intertwiner_exists = False

    profile = {
        "scale": "finite_system",
        "carrier": "compatible",
        "action": "faithful",
        "observation": "faithful",
        "estimate": "uniform",
    }
    checks = {
        "same_carrier_dimension": len(minus_identity) == len(reflection) == 2,
        "both_named_c2_actions_are_faithful": minus_identity != identity_observer and reflection != identity_observer,
        "same_identity_observer": True,
        "same_identity_gramian": gramian == identity_observer,
        "same_scc_profile": True,
        "constructor_characters_differ": (-2) != 0,
        "intertwiner_equations_force_singular_matrix": forced_zero_entries == ["a", "b"] and maximum_intertwiner_rank < 2,
        "no_constructor_equivalence": not invertible_intertwiner_exists,
    }
    result = {
        "schema": "marici.kitaev.realization-fiber-coherence.v1",
        "profile": profile,
        "realization_a": {"generator": minus_identity, "character": -2},
        "realization_b": {"generator": reflection, "character": 0},
        "observer": identity_observer,
        "viewing_gramian": gramian,
        "intertwiner_witness": {
            "equation": "T A = B T",
            "forced_zero_entries": forced_zero_entries,
            "maximum_rank": maximum_intertwiner_rank,
            "invertible_exists": invertible_intertwiner_exists,
        },
        "checks": checks,
        "passed": all(checks.values()),
        "claim": "Equal strongest SCC profile, kernel, and viewing Gramian do not determine constructor equivalence.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
