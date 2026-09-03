#!/usr/bin/env python3
"""Exact typed-role coefficient and gauge diagnostics."""

import json
from fractions import Fraction as Q
from pathlib import Path

a = Q(2)
gC, gD = Q(3), Q(5)
b = Q(3)
q = Q(7)
adjoint = gD * a / gC
composite = b * a
readout_pullback = q * a
x, y = Q(11, 4), Q(-5, 6)
left_pairing = gD * (a * x) * y
right_pairing = gC * x * (adjoint * y)

sC, sD = Q(2), Q(3)
a_prime = sC * a / sD
gC_prime = sC * sC * gC
gD_prime = sD * sD * gD
adjoint_prime = gD_prime * a_prime / gC_prime
# Coordinates x'=x/sC and y'=y/sD for the same vectors.
x_prime, y_prime = x / sC, y / sD
left_prime = gD_prime * (a_prime * x_prime) * y_prime
right_prime = gC_prime * x_prime * (adjoint_prime * y_prime)
mate_role_residual = adjoint - a
readout_role_residual = readout_pullback - a
roles = (a, adjoint, composite, readout_pullback)
checks = {
    "four_role_coefficients_are_pairwise_distinct": len(set(roles)) == 4,
    "adjoint_is_ten_thirds": adjoint == Q(10, 3),
    "composite_is_six": composite == 6,
    "readout_pullback_is_fourteen": readout_pullback == 14,
    "mate_pairing_identity_holds": left_pairing == right_pairing,
    "basis_changed_mate_pairing_holds": left_prime == right_prime,
    "basis_change_preserves_pairing_value": left_prime == left_pairing,
    "mate_coefficient_transforms_covariantly": adjoint_prime == sD * adjoint / sC,
    "forcing_forward_into_mate_role_has_nonzero_residual": mate_role_residual == Q(4, 3),
    "forcing_forward_into_readout_role_has_nonzero_residual": readout_role_residual == 12,
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.typed-coefficient-proliferation.v1", "status": "passed", "checks": checks, "coefficients": {"forward": str(a), "backward_mate": str(adjoint), "composite": str(composite), "readout_pullback": str(readout_pullback)}, "role_substitution_residuals": {"mate_minus_forward": str(mate_role_residual), "readout_minus_forward": str(readout_role_residual)}, "claim_boundary": "Exact one-dimensional rational fixture; historical Marici attribution remains open."}
output = Path(__file__).parents[1] / "results" / "typed_coefficient_proliferation.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "coefficients": result["coefficients"]}, sort_keys=True))
