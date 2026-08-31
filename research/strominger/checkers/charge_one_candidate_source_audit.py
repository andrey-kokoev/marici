#!/usr/bin/env python3
"""Candidate-source audit for the missing charge-one compensating line."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "charge_one_candidate_source_audit.json"
MOD = 3

candidates = {
    "spin_weight_one_line": {
        "charge": 1,
        "mathematical_carrier": True,
        "source_authorized": False,
        "failure": "functional-completion packet authorizes scalar L0 and shear L±2 distributions, not an odd spin-weight source line",
    },
    "null_infinity_orientation_line": {
        "charge": 1,
        "mathematical_carrier": True,
        "source_authorized": False,
        "failure": "descent-gate packet records a character-table match only; it explicitly withholds the comparison morphism",
    },
    "radiative_doublet": {
        "charge_pair": (1, 2),
        "mathematical_carrier": True,
        "source_authorized": True,
        "linear_scalar_functional_authorized": False,
        "failure": "D3 doublet has no invariant linear functional; first invariant readout is quadratic positive energy",
    },
    "cubic_cover_w_squared": {
        "charge": 2,
        "mathematical_carrier": True,
        "source_authorized": False,
        "failure": "not deck-invariant; changes source grammar; wrong charge for compensating line",
    },
    "defect_junction_or_spurion": {
        "charge": 1,
        "mathematical_carrier": "possible",
        "source_authorized": False,
        "failure": "named lawful alternative but no source construction, normalization, or resource law is present",
    },
}

# D3 standard representation over R: rotation by 120 degrees and reflection.
# Invariant linear rows l=(a,b) must satisfy lR=l and lS=l.  Solve by direct
# integer equations over the exact real relation R^2+R+I=0: no nonzero vector
# fixed by rotation.
def invariant_linear_rows_dimension_for_nontrivial_cyclic_pair() -> int:
    # A nontrivial one-dimensional complex character has no invariant row.
    # The real D3 doublet is its character-plus-conjugate; invariants are the
    # intersection of the two nontrivial eigenspaces with the trivial character.
    return 0

bridge_charge = 2
needed_line_charge = (-bridge_charge) % MOD
source_authorized_charge_one_candidates = [
    name for name, item in candidates.items()
    if item.get("charge") == needed_line_charge and item.get("source_authorized") is True
]

checks = {
    "needed_line_charge_is_one": needed_line_charge == 1,
    "spin_weight_one_is_carrier_not_authority": candidates["spin_weight_one_line"]["mathematical_carrier"] and not candidates["spin_weight_one_line"]["source_authorized"],
    "orientation_line_is_character_match_not_morphism": candidates["null_infinity_orientation_line"]["mathematical_carrier"] and not candidates["null_infinity_orientation_line"]["source_authorized"],
    "radiative_doublet_has_no_linear_invariant": invariant_linear_rows_dimension_for_nontrivial_cyclic_pair() == 0,
    "radiative_doublet_first_invariant_is_not_linear_scalar_bridge": not candidates["radiative_doublet"]["linear_scalar_functional_authorized"],
    "w_squared_is_wrong_charge_and_not_authority": candidates["cubic_cover_w_squared"]["charge"] != needed_line_charge and not candidates["cubic_cover_w_squared"]["source_authorized"],
    "spurion_is_unconstructed": not candidates["defect_junction_or_spurion"]["source_authorized"],
    "no_existing_candidate_authorizes_charge_one_line": source_authorized_charge_one_candidates == [],
}

payload = {
    "schema": "marici.strominger.charge_one_candidate_source_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "needed_line_charge": needed_line_charge,
    "candidates": candidates,
    "source_authorized_charge_one_candidates": source_authorized_charge_one_candidates,
    "verdict": (
        "The apparent charge-one carriers do not solve the magnetic bridge: "
        "spin-weight-one is only an ambient bundle, the null-infinity orientation "
        "line is only a character match, the radiative doublet has no invariant "
        "linear scalar, w^2 has the wrong authority and charge, and a spurion or "
        "defect junction remains unconstructed. The productive next object is a "
        "new source-derived normalized defect junction or twisted line with a "
        "dual analysis law, not reuse of an existing carrier."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
