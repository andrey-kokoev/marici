"""Audit the pole-degree symbol of the exact triangle-wall source connection."""

from __future__ import annotations

import contextlib
import importlib
import io
import json

with contextlib.redirect_stdout(io.StringIO()):
    source = importlib.import_module("check_unbounded_twisted_derham_connection_commutator")

P = source.P
POINT = source.POINT


def signed(value):
    value %= P
    return value if value <= P // 2 else value - P


def tangent_k_derivative(axes):
    polynomial = {}
    for axis in axes:
        kd, _ = source.exact_parameter_derivative_data(POINT, axis)
        for exponent, coefficient in kd.items():
            source.add(polynomial, exponent, coefficient)
    return {
        f"a^{exponent[0]}b^{exponent[1]}": signed(coefficient)
        for exponent, coefficient in sorted(polynomial.items())
    }


result = {
    "schema": "marici.triangle-wall-pole-connection-symbol.v1",
    "field": P,
    "point": list(POINT),
    "gamma": source.GAMMA,
    "tangents": {
        "T1=dX1+dX3": tangent_k_derivative((0, 2)),
        "T2=dX2+dX3": tangent_k_derivative((1, 2)),
    },
    "source_relation_pole_raising_coefficients": {
        "de_rham_at_k2": source.GAMMA - 2,
        "principal_at_k2": source.GAMMA - 2 - 1,
        "marked_at_k3": source.GAMMA - 3,
    },
    "both_tangent_K_derivatives_nonzero": True,
    "finite_k_depth_three_source_complex_horizontal": False,
    "connection_structure": "filtered connection with degree-plus-one K-pole symbol",
    "next_gate": "compute the induced exact-valuation symbol from k-depth three to four",
}

assert all(result["tangents"].values())
assert all(result["source_relation_pole_raising_coefficients"].values())
print(json.dumps(result, indent=2))
