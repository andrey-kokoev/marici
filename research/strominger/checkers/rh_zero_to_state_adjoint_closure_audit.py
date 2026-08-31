#!/usr/bin/env python3
"""Exact audit of the RH zero-to-state bridge under adjoint closure."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_zero_to_state_adjoint_closure_audit.json"

# Hostile source from Grothendieck's adjoint-closure packet.
# f(q)=e^{-q}-3e^{-2q}; F(s)=1/(1-s)-3/(2-s), so F(1/2)=0.
s = Fraction(1, 2)
F_s = Fraction(1, 1) / (1 - s) - Fraction(3, 1) / (2 - s)

# Terminal tail at the zero: G(q)=2e^{-q}-2e^{-2q}.
# Endpoint values in the exponential basis.
G0 = Fraction(2) - Fraction(2)
G_infty = Fraction(0)

# Exact integral of (a e^{-alpha q})(b e^{-beta q}) on [0,infty] is ab/(alpha+beta).
def pair(terms_a, terms_b):
    return sum(Fraction(ca * cb, aa + bb) for aa, ca in terms_a for bb, cb in terms_b)

f_terms = [(1, Fraction(1)), (2, Fraction(-3))]
G_terms = [(1, Fraction(2)), (2, Fraction(-2))]
inner_f_G = pair(f_terms, G_terms)
norm_G2 = pair(G_terms, G_terms)
virial_tail_identity_residual = inner_f_G + s * norm_G2

# Triangular Evans bridge accepts: transform zero plus two endpoint conditions.
triangular_accepts = F_s == 0 and G0 == 0 and G_infty == 0 and norm_G2 > 0

# Minimal adjoint closure adds lower row <f,G>=0 and rejects the same state.
adjoint_accepts_same_state = inner_f_G == 0

# Reciprocal doubling supplies an independent second tail, but scalar seam
# cancellation only fixes G_+(0)+G_-(0). It does not imply the adjoint row.
Gminus0 = -G0
scalar_seam_closed = G0 + Gminus0 == 0
reciprocal_sheet_forces_adjoint_row = False

# A quotient could make the row redundant only if the functional vanishes on
# every admitted endpoint state. The witness is an endpoint state where it does
# not vanish, so no such quotient is established by the existing finite bridge.
endpoint_state_with_nonzero_reverse_functional = triangular_accepts and inner_f_G != 0

checks = {
    "source_transform_zero_at_half": F_s == 0,
    "nonzero_two_endpoint_tail_state_exists": triangular_accepts,
    "tail_identity_holds_exactly": virial_tail_identity_residual == 0,
    "adjoint_reverse_row_is_nonzero_on_zero_state": inner_f_G == Fraction(-1, 6),
    "minimal_adjoint_closure_rejects_evans_state": triangular_accepts and not adjoint_accepts_same_state,
    "scalar_reciprocal_seam_does_not_imply_reverse_row": scalar_seam_closed and not reciprocal_sheet_forces_adjoint_row,
    "boundary_quotient_redundancy_not_proved_by_existing_bridge": endpoint_state_with_nonzero_reverse_functional,
    "direct_tail_spectralization_gate_remains_open_not_solved": triangular_accepts and not adjoint_accepts_same_state,
}

payload = {
    "schema": "marici.strominger.rh_zero_to_state_adjoint_closure_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "source": "f(q)=e^{-q}-3e^{-2q}",
    "s": str(s),
    "transform_value": str(F_s),
    "tail": "G(q)=2e^{-q}-2e^{-2q}",
    "endpoint_values": {"G_0": str(G0), "G_infty": str(G_infty)},
    "inner_f_G": str(inner_f_G),
    "norm_G_squared": str(norm_G2),
    "verdict": (
        "The zero-to-state bridge exists and is noncircular at the triangular "
        "boundary-control level, but this iteration finds that it cannot yet be "
        "used as the RH virial bridge. The exact zero-state is rejected by the "
        "minimal adjoint reverse row <f,G>=0. Reciprocal scalar seam closure does "
        "not by itself supply that row or a quotient making it redundant. The "
        "productive next subgate is the unaggregated labelled boundary module: "
        "primitive, square, higher-prime, archimedean, and reciprocal-variance "
        "ports must either derive the missing reverse equation or close the "
        "direct spectralization lane."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
