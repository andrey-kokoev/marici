#!/usr/bin/env python3
"""Show that filtration-preserving diagonal descent cannot create an extension block."""

import json
from pathlib import Path

import sympy as sp


gq, ge, dgq, dge, h, dh = sp.symbols("gq ge dgq dge h dh", nonzero=True)

# One quotient line and one absolute line model the relevant (q0,e6) corner.
D = sp.diag(gq, ge)
dD = sp.diag(dgq, dge)
gauge_term_diagonal = sp.simplify(dD * D.inv())

# A triangular transition is the first structure capable of producing a
# lower-left gauge term.
T = sp.Matrix([[gq, 0], [h, ge]])
dT = sp.Matrix([[dgq, 0], [dh, dge]])
gauge_term_triangular = sp.simplify(dT * T.inv())

checks = {
    "diagonal_lower_left_zero": gauge_term_diagonal[1, 0] == 0,
    "triangular_lower_left_formula": sp.simplify(
        gauge_term_triangular[1, 0] - (dh / gq - dge * h / (ge * gq))
    ) == 0,
    "triangular_zero_shear_recovers_zero": sp.simplify(gauge_term_triangular[1, 0].subs({h: 0, dh: 0})) == 0,
}

packet = {
    "schema": "marici.benincasa.block_diagonal_descent_extension_no_go.v1",
    "filtration": "0 -> M9 -> M12 -> W3 -> 0",
    "corner_basis": ["q0 in W3", "e6 in M9"],
    "source_transition_type": (
        "Occurrence relabelling preserves wall-lift and absolute-master source-form types; "
        "the induced raw transition is block diagonal before exact reduction."
    ),
    "diagonal_gauge_term": [[str(value) for value in row] for row in gauge_term_diagonal.tolist()],
    "triangular_gauge_term_lower_left": str(gauge_term_triangular[1, 0]),
    "checks": checks,
    "verdict": (
        "A cyclic Leray-frame dlog in a diagonal coefficient transition cannot "
        "create B_e6,q0. A source-derived triangular shear or the actual source "
        "extension block is necessary."
    ),
    "surviving_status": (
        "The unique A2 logarithmic class and C2 normalization remain valid "
        "candidate data, but rank-twelve insertion is unproved."
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

out = Path(__file__).resolve().parents[1] / "results" / "block_diagonal_descent_extension_no_go.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
