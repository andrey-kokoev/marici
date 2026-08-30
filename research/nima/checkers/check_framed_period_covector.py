"""Exact audit of gauge-invariant transport paired with a physical covector."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/framed-period-covector.json"
Matrix = tuple[tuple[F, F], tuple[F, F]]
Vector = tuple[F, F]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum((a[i][k] * b[k][j] for k in range(2)), F(0)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def transpose(a: Matrix) -> Matrix:
    return ((a[0][0], a[1][0]), (a[0][1], a[1][1]))


def apply(a: Matrix, v: Vector) -> Vector:
    return tuple(sum((a[i][k] * v[k] for k in range(2)), F(0)) for i in range(2))  # type: ignore[return-value]


def row_apply(ell: Vector, a: Matrix) -> Vector:
    return tuple(sum((ell[k] * a[k][j] for k in range(2)), F(0)) for j in range(2))  # type: ignore[return-value]


def pair(ell: Vector, v: Vector) -> F:
    return ell[0] * v[0] + ell[1] * v[1]


t: Matrix = ((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5)))
v_in: Vector = (1, 2)
ell_out: Vector = (2, -1)
period = pair(ell_out, apply(t, v_in))

q_in: Matrix = ((F(5, 13), F(-12, 13)), (F(12, 13), F(5, 13)))
q_out: Matrix = ((0, -1), (1, 0))
t_prime = multiply(multiply(q_out, t), transpose(q_in))
v_prime = apply(q_in, v_in)
ell_prime = row_apply(ell_out, transpose(q_out))
period_prime = pair(ell_prime, apply(t_prime, v_prime))

untransported_covector_period = pair(ell_out, apply(t_prime, v_prime))
alternate_covector: Vector = (1, 0)
alternate_period = pair(alternate_covector, apply(t, v_in))

gates = {
    "framed_period_is_gauge_invariant": period_prime == period,
    "transport_without_covector_transport_is_not_invariant": (
        untransported_covector_period != period
    ),
    "same_transport_supports_multiple_readouts": alternate_period != period,
    "input_state_transforms_covariantly": v_prime != v_in,
    "output_covector_transforms_contravariantly": ell_prime != ell_out,
    "period_is_scalar_after_pairing": isinstance(period, F),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.framed-period-covector.v1",
    "period": str(period),
    "gauge_transformed_period": str(period_prime),
    "unframed_value": str(untransported_covector_period),
    "alternate_covector_value": str(alternate_period),
    "gates": gates,
    "conclusion": (
        "Transport becomes a gauge-invariant scalar only after pairing with "
        "a contravariantly transported physical covector. The covector is "
        "readout framing, not another property of the transport matrix."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
