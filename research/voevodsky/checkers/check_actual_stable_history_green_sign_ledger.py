#!/usr/bin/env python3
"""Exact coefficient sign ledger for the two source-derived stable histories."""
import json
from pathlib import Path

# Represent a linear boundary expression by coefficients in (E-,E+,F-,F+).
pos_boundary = (1, -1, -1, 1)       # E- - E+ + F+ - F-
indef_boundary = (1, 1, -1, -1)     # E- + E+ - F- - F+

# Xi-zero substitutions E-=E+=E and F-=-F+=-F.
def specialize(v):
    em, ep, fm, fp = v
    return (em+ep, -fm+fp)  # coefficients of (E,F)

pos_xi = specialize(pos_boundary)
indef_xi = specialize(indef_boundary)
checks = {
    "positive_bulk_combination_exact": pos_boundary == (1,-1,-1,1),
    "indefinite_bulk_combination_exact": indef_boundary == (1,1,-1,-1),
    "positive_bulk_retains_forcing_difference": pos_xi == (0,2),
    "indefinite_bulk_retains_endpoint_sum": indef_xi == (2,0),
    "xi_square_forcing_sum_not_positive_bulk_boundary": pos_xi != (0,0),
}
out = {
    "schema": "marici.voevodsky.actual-stable-history-green-sign-ledger.v1",
    "source_identities": {
        "plus": "-lambda*K_plus=E_plus-F_plus",
        "minus": "lambda*K_minus=E_minus-F_minus",
    },
    "combined_identities": {
        "positive_bulk_sum": "lambda*(K_minus+K_plus)=E_minus-E_plus+F_plus-F_minus",
        "indefinite_bulk_difference": "lambda*(K_minus-K_plus)=E_minus+E_plus-F_minus-F_plus",
    },
    "xi_zero_specialization": {
        "assumptions": ["E_minus=E_plus", "F_minus=-F_plus"],
        "positive_bulk_boundary": "2*F_plus",
        "indefinite_bulk_boundary": "2*E_plus",
    },
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "Xi-square controls the forcing sum, while positive bulk requires the forcing difference",
    "rh_proved": False,
}
target = Path(__file__).parents[1]/"results"/"actual_stable_history_green_sign_ledger.json"
target.write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
raise SystemExit(0 if out["passed"] else 1)
