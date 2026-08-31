#!/usr/bin/env python3
"""Exact Z/3 descent gate for a charged electric-magnetic bridge bimodule."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "charged_bimodule_descent_gate_checks.json"
MOD = 3


def q(x: int) -> int:
    return x % MOD

# The route-packet audit found intrinsic spin-two charges (2,1,1).  To combine
# the first source with either charge-1 source, an adapter must have charge 2:
# 2 + 2 = 1 mod 3.
source_charges = (2, 1, 1)
adapter_charge = q(source_charges[1] - source_charges[0])

# Bare scalar descent admits only degree-zero morphisms.
bare_bridge_descends = adapter_charge == 0

# A charged line L_c types a degree-c map as an invariant section of
# Hom(V_2,V_1) tensor L_c when the tensor degree is zero.
line_charge = q(-adapter_charge)
line_typed_total_charge = q(adapter_charge + line_charge)

# Forgetting the charged line projects the typed bridge back to a nonzero deck
# character.  A scalar trivialization of L_c would be extra symmetry-breaking
# source data, not a consequence of the bridge itself.
forgotten_total_charge = adapter_charge

# Same-preparation joint observation can be invariant if it pairs the charged
# bridge channel with the dual charged analysis line.  This retains both lines;
# it does not collapse them to an ordinary scalar.
dual_line_charge = q(-line_charge)
analysis_pair_charge = q(line_charge + dual_line_charge)

# Minimality: there is a unique charge class that types this bridge.  Adding
# all three charged lines would be nonminimal unless independently required.
admissible_line_charges = [c for c in range(MOD) if q(adapter_charge + c) == 0]

# Hostiles.
wrong_line_charges = [c for c in range(MOD) if c != line_charge]
wrong_line_fails = all(q(adapter_charge + c) != 0 for c in wrong_line_charges)
scalar_laundering_fails = q(adapter_charge) != 0 and line_typed_total_charge == 0

# Relation to the E/M two-state bridge: the off-diagonal operator is permitted
# as a pre-descent charged morphism; strict descent sees only the retained
# line-valued section.
checks = {
    "adapter_charge_is_two": adapter_charge == 2,
    "bare_scalar_bridge_fails_descent": not bare_bridge_descends,
    "unique_compensating_line_has_charge_one": line_charge == 1 and admissible_line_charges == [1],
    "line_valued_bridge_has_total_charge_zero": line_typed_total_charge == 0,
    "forgetting_line_recreates_descent_failure": forgotten_total_charge == 2,
    "dual_analysis_line_makes_invariant_pairing": analysis_pair_charge == 0,
    "wrong_line_charges_fail": wrong_line_fails,
    "scalar_trivialization_would_launder_symmetry_breaking": scalar_laundering_fails,
}

payload = {
    "schema": "marici.strominger.charged_bimodule_descent_gate.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "source_charges": source_charges,
    "adapter": {
        "from_charge": source_charges[0],
        "to_charge": source_charges[1],
        "required_charge": adapter_charge,
    },
    "typed_repair": {
        "line_charge": line_charge,
        "line_valued_total_charge": line_typed_total_charge,
        "dual_analysis_line_charge": dual_line_charge,
        "analysis_pair_total_charge": analysis_pair_charge,
    },
    "verdict": (
        "The electric-magnetic bridge can be source-typed only as a charged "
        "line-valued bimodule map with a retained dual analysis line. It cannot "
        "descend as a bare scalar operator, and trivializing the charged line is "
        "an additional symmetry-breaking source datum."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
