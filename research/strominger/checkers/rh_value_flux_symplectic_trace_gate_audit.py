#!/usr/bin/env python3
"""Audit the value--flux symplectic trace candidate for the RH Evans divisor."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_value_flux_symplectic_trace_gate_audit.json"


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]

# Raw two-route value--flux traces.  The scalar theta/Evans readout in the
# doubled-tail model is the aggregate value X=u_value+v_value, while the native
# symplectic candidate on the boundary plane is det(u,v).

# Cross zero need not be boundary rank loss.
u_cross_zero = (Fraction(1), Fraction(0))
v_cross_zero = (Fraction(-1), Fraction(1))
X_cross_zero = u_cross_zero[0] + v_cross_zero[0]
D_cross_zero = det(u_cross_zero, v_cross_zero)
rank_loss_at_cross_zero = D_cross_zero == 0

# Boundary rank loss need not be scalar cross zero.
u_rank_loss = (Fraction(1), Fraction(2))
v_rank_loss = (Fraction(3), Fraction(6))
X_rank_loss = u_rank_loss[0] + v_rank_loss[0]
D_rank_loss = det(u_rank_loss, v_rank_loss)

# No fixed scalar unit can make det equal the aggregate value on the raw trace
# plane.  The first sample would require unit 0; a nonzero unit is required to
# preserve a divisor.
sample_a_u = (Fraction(1), Fraction(0))
sample_a_v = (Fraction(0), Fraction(1))
sample_a_X = sample_a_u[0] + sample_a_v[0]
sample_a_D = det(sample_a_u, sample_a_v)
required_unit_a = sample_a_X / sample_a_D
sample_b_u = u_cross_zero
sample_b_v = v_cross_zero
sample_b_X = X_cross_zero
sample_b_D = D_cross_zero
required_unit_b = sample_b_X / sample_b_D
fixed_nonzero_unit_impossible = required_unit_a != required_unit_b and required_unit_b == 0

# Imported quarter-turn repair: choosing a fixed reference flux axis e=(0,1)
# gives det((X,phi),e)=X.  This proves only that an external axis can force the
# answer; it is not derived from the two route traces.
external_axis = (Fraction(0), Fraction(1))
trace_with_aggregate_value = (sample_a_X, Fraction(5))
imported_axis_recovers_X = det(trace_with_aggregate_value, external_axis) == sample_a_X

# Evans bordered determinant remains exact in the nonselfadjoint source--observer
# typing: det [[0,delta A^-1 f],[-1,1]] = delta A^-1 f up to sign.  This is a
# Schur border, not the passive Gram/Weyl determinant or raw trace determinant.
X = Fraction(7, 5)
evans_border = ((Fraction(0), X), (Fraction(-1), Fraction(1)))
evans_border_det = evans_border[0][0] * evans_border[1][1] - evans_border[0][1] * evans_border[1][0]

checks = {
    "scalar_cross_zero_can_have_nonzero_trace_determinant": X_cross_zero == 0 and D_cross_zero != 0,
    "trace_rank_loss_can_have_nonzero_scalar_readout": D_rank_loss == 0 and X_rank_loss != 0,
    "raw_trace_determinant_has_no_fixed_nonzero_unit_to_evans_readout": fixed_nonzero_unit_impossible,
    "external_axis_can_recover_readout_but_is_not_route_derived": imported_axis_recovers_X,
    "evans_border_preserves_divisor_as_schur_not_raw_trace": evans_border_det == X,
}

payload = {
    "schema": "marici.strominger.rh_value_flux_symplectic_trace_gate_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "cross_zero_sample": {"u": [str(x) for x in u_cross_zero], "v": [str(x) for x in v_cross_zero], "scalar_readout": str(X_cross_zero), "trace_determinant": str(D_cross_zero)},
    "rank_loss_sample": {"u": [str(x) for x in u_rank_loss], "v": [str(x) for x in v_rank_loss], "scalar_readout": str(X_rank_loss), "trace_determinant": str(D_rank_loss)},
    "unit_test": {"required_unit_sample_a": str(required_unit_a), "required_unit_sample_b": str(required_unit_b)},
    "evans_border_test": {"readout": str(X), "border_determinant": str(evans_border_det)},
    "verdict": (
        "The native value--flux idea remains the sharpest RH direction, but the "
        "raw doubled-tail trace determinant is exhausted: scalar cross zeros and "
        "boundary rank loss are independent unless an extra source law supplies "
        "a quarter-turn/reference axis or constrained Lagrangian relation. The "
        "nonselfadjoint Evans border still preserves the divisor exactly as a "
        "Schur determinant. The next productive target is therefore not passive "
        "trace rank, but a source-derived Green symplectic structure proving that "
        "the theta boundary data lie in the special rank-one/Lagrangian subclass "
        "where the Evans border becomes the native determinant."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
