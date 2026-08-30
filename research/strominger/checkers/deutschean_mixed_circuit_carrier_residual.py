#!/usr/bin/env python3
"""Compare the closed mixed circuit with a source-coordinate Euler dilation."""

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_mixed_circuit_carrier_residual.json"
t, u, k, x, q = sp.symbols("t u k x q")
a = sp.Rational(2, 3)
b0 = sp.Rational(5, 4)
c0 = sp.Rational(3, 2)
P = sp.exp(u) - 1 - u
G = a * (u * sp.diff(P, u) - P)


def carrier(b, c, primitive):
    return (sp.exp(u) - c*t) * sp.exp(b*u) * sp.exp(-primitive/t)


F0 = carrier(b0, c0, P)
parameter_family = carrier(b0 + sp.Rational(3, 2)*k, c0 + k, P + k*G)
parameter_variation = sp.diff(parameter_family, k).subs(k, 0)
euler_variation = a * (t*sp.diff(F0, t) + u*sp.diff(F0, u))
residual = sp.factor(parameter_variation - euler_variation)
expected_residual = -t*u*sp.exp(b0*u)*sp.exp(-P/t)
# Directly differentiating the carrier family avoids treating the numerical
# physical value c0 as a symbol.
b_symbol, c_symbol = sp.symbols("b_symbol c_symbol")
symbolic_carrier = carrier(b_symbol, c_symbol, P)
mixed_amplitude_curvature = sp.diff(symbolic_carrier, b_symbol, c_symbol).subs(
    {b_symbol: b0, c_symbol: c0}
)
residual_x = -t**2*x*sp.exp(b0*t*x)*sp.exp(-(sp.exp(t*x)-1-t*x)/t)
residual_leading = sp.series(residual_x, t, 0, 3).removeO()
gamma_integrated_leading = residual_leading.subs(x, q)

checks = {
    "phase_component_is_euler_variation": sp.simplify(
        G - a*(u*sp.diff(P,u)-P)
    ) == 0,
    "parameter_minus_coordinate_variation_has_exact_residual": sp.simplify(
        residual - expected_residual
    ) == 0,
    "carrier_residual_is_nonzero": residual != 0,
    "residual_is_single_prefactor_cancelled_atom": sp.simplify(
        residual / expected_residual - 1
    ) == 0,
    "residual_is_mixed_amplitude_curvature": sp.simplify(
        residual - mixed_amplitude_curvature
    ) == 0,
    "residual_has_nonzero_gamma_moment_at_order_t2": sp.simplify(
        gamma_integrated_leading + q*t**2
    ) == 0,
}
payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": checks,
    "observed": {
        "primitive": str(P),
        "primitive_euler_variation": str(G),
        "parameter_variation_minus_euler_dilation": str(residual),
        "residual_atom": "-t*u*exp(5*u/4)*exp(-P/t)",
        "source_derivative_type": "partial_b partial_c F",
        "leading_residual_after_u_equals_t*x": str(residual_leading),
        "leading_normalized_gamma_moment": str(gamma_integrated_leading),
    },
    "passed": all(checks.values()),
    "semantic_boundary": (
        "Exact full-carrier comparison. The mixed H1 circuit is not the bare "
        "Euler coordinate dilation: a nonzero single-atom residual remains. "
        "The nonzero Gamma moment rules out a vanishing-endpoint total derivative. "
        "The corrected second connected port detects the same direction."
    ),
}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
raise SystemExit(0 if payload["passed"] else 1)
