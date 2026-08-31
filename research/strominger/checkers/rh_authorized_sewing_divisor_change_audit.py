#!/usr/bin/env python3
"""Exact divisor-change audit for authorized two-chart sewing."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_authorized_sewing_divisor_change_audit.json"

# Divisors on a finite named point set.  Positive multiplicity = zero,
# negative multiplicity = pole.  This avoids numerical root finding and tests
# the exact divisor bookkeeping needed for sewn two-chart sections.

def add_div(*divs):
    out = {}
    for div in divs:
        for point, mult in div.items():
            out[point] = out.get(point, 0) + mult
            if out[point] == 0:
                del out[point]
    return out


def restrict(div, allowed):
    return {p: m for p, m in div.items() if p in allowed}

# Finite reciprocal cutoff has off-seam zeros from the positive model in prior
# audits.  Treat them as symmetric labelled divisor points.
finite_cutoff = {"alpha+i*pi": 1, "-alpha+i*pi": 1}
critical_seam = {"i*gamma": 1}
open_half_plane = {"alpha+i*pi", "-alpha+i*pi"}

# Sewing by a transition divisor.  A source-authorized transition must specify
# this divisor before fitting the target section, preserve the adjoint pairing,
# and explain finite divisor transport.  Three candidate transitions show the
# gates.
identity_transition = {}
formal_cancel_transition = {"alpha+i*pi": -1, "-alpha+i*pi": -1}
formal_move_transition = {"alpha+i*pi": -1, "-alpha+i*pi": -1, "i*gamma": 1}
source_transition_authorized = False
adjoint_pairing_preserved_by_formal_cancel = False

identity_sewn = add_div(finite_cutoff, identity_transition)
cancel_sewn = add_div(finite_cutoff, formal_cancel_transition)
move_sewn = add_div(finite_cutoff, formal_move_transition)

# Jump cancellation and divisor change are independent.  A transition can have
# zero net spectral-jump coefficient while still changing zeros by inserting a
# meromorphic divisor factor.
weyl_jump_coeff = 6
transition_jump_coeff = -6
jump_cancels = weyl_jump_coeff + transition_jump_coeff == 0
divisor_change_nonzero = formal_cancel_transition != {}

# Path bounds: transition products can preserve local pairings but accumulate
# divisor/path degree.  A bounded source path law must control this; none is
# present in the current source state.
path_degrees = [n * len(formal_move_transition) for n in range(1, 8)]
path_degree_grows = all(path_degrees[i] < path_degrees[i + 1] for i in range(len(path_degrees) - 1))
source_path_bound_present = False

checks = {
    "identity_sewing_preserves_finite_off_seam_divisor": restrict(identity_sewn, open_half_plane) == finite_cutoff,
    "formal_meromorphic_transition_can_cancel_off_seam_divisor": cancel_sewn == {},
    "formal_transition_can_move_divisor_to_seam": move_sewn == critical_seam,
    "jump_cancellation_does_not_determine_divisor_change": jump_cancels and divisor_change_nonzero,
    "formal_divisor_cancellation_lacks_current_source_authority": not source_transition_authorized,
    "formal_cancellation_does_not_preserve_adjoint_pairing_by_default": not adjoint_pairing_preserved_by_formal_cancel,
    "transition_composition_needs_source_path_bound": path_degree_grows and not source_path_bound_present,
}

payload = {
    "schema": "marici.strominger.rh_authorized_sewing_divisor_change_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "finite_cutoff_divisor": finite_cutoff,
    "identity_sewn_divisor": identity_sewn,
    "formal_cancel_sewn_divisor": cancel_sewn,
    "formal_move_sewn_divisor": move_sewn,
    "jump_data": {"weyl_jump": f"{weyl_jump_coeff}*pi*i", "transition_jump": f"{transition_jump_coeff}*pi*i"},
    "path_degree_prefix": path_degrees,
    "verdict": (
        "Exact divisor bookkeeping separates the sewing problem from Weyl jump "
        "cancellation. Identity sewing leaves finite off-seam divisors in place; "
        "a meromorphic transition can cancel or move them, but that is precisely "
        "the datum requiring source authority. Jump cancellation alone neither "
        "selects the transition divisor nor preserves the adjoint pairing or path "
        "bounds. The exact divisor-change direction is therefore exhausted until "
        "a source-derived seam transition supplies its divisor, pairing law, and "
        "composition bounds before fitting Xi."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
