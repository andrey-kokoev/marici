"""Exact WP583 local viability radius for the WP580 portal compiler."""

import json
from pathlib import Path

import sympy as sp


z, lambda_s, lambda_h, h = sp.symbols(
    "z lambda_s lambda_H h", positive=True, real=True
)
q = lambda_s * z**2 / lambda_h


def invariant_map(z_value, lambda_s_value):
    return sp.Matrix([z_value, lambda_s_value * z_value**2 / lambda_h])


base = invariant_map(z, lambda_s)
r_minus = sp.Matrix([z - h, lambda_s * z**2 / (z - h) ** 2])
r_plus = sp.Matrix([z + h, lambda_s * z**2 / (z + h) ** 2])
q_minus = sp.Matrix([z, lambda_s - lambda_h * h / z**2])
q_plus = sp.Matrix([z, lambda_s + lambda_h * h / z**2])

responses = {
    "r_minus": sp.simplify(invariant_map(*r_minus) - base),
    "r_plus": sp.simplify(invariant_map(*r_plus) - base),
    "q_minus": sp.simplify(invariant_map(*q_minus) - base),
    "q_plus": sp.simplify(invariant_map(*q_plus) - base),
}

hostile = {z: sp.Rational(1, 4), lambda_s: 1, lambda_h: 1}
hostile_q = sp.simplify(q.subs(hostile))
interior_h = sp.Rational(1, 32)

checks = {
    "r_minus_is_exact": responses["r_minus"] == sp.Matrix([-h, 0]),
    "r_plus_is_exact": responses["r_plus"] == sp.Matrix([h, 0]),
    "q_minus_is_exact": responses["q_minus"] == sp.Matrix([0, -h]),
    "q_plus_is_exact": responses["q_plus"] == sp.Matrix([0, h]),
    "hostile_common_radius_is_one_sixteenth": hostile_q == sp.Rational(1, 16),
    "interior_step_is_inside_common_radius": interior_h < hostile_q,
    "q_boundary_kills_strict_quartic_stability": sp.simplify(
        q_minus[1].subs({**hostile, h: hostile_q})
    ) == 0,
    "r_lower_boundary_hits_blind_point": sp.simplify(
        r_minus[0].subs({**hostile, h: hostile[z]})
    ) == 0,
    "r_upper_boundary_hits_zero_sm_production": sp.simplify(
        r_plus[0].subs({**hostile, h: 1 - hostile[z]})
    ) == 1,
}

if not all(checks.values()):
    raise SystemExit(f"WP583 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}


def encode(expr):
    return sp.sstr(sp.simplify(expr))


result = {
    "work_package": "WP583",
    "status": "PASS",
    "checks": checks,
    "admitted_source_domain": "0<z<1, lambda_s>0, lambda_H>0",
    "domain_typing": {
        "z_positive": "nonzero source sensitivity",
        "z_below_one": "nonzero Standard Model production coupling kappa_t^2=1-z",
        "lambda_s_positive": "strict boundedness on the declared isolated large-s ray",
    },
    "common_symmetric_radius": "0<h<min(z,1-z,q), q=lambda_s*z^2/lambda_H",
    "compiled_responses": {key: [encode(x) for x in value] for key, value in responses.items()},
    "rational_hostile": {
        "base": {"z": "1/4", "lambda_s": "1", "lambda_H": "1"},
        "radius": "1/16",
        "interior_step": "1/32",
        "boundary_falsifier": "h=q=1/16 sends the negative-q endpoint to lambda_s'=0",
    },
    "classification": "exact source-side local viability radius; neither selector nor detector instrument",
    "remaining_gate": "a complete source potential, phenomenological reach domain, and publication-bound mixed-scalar detector transport",
}

out = Path(__file__).resolve().parents[1] / "results" / "wp583_portal_setting_viability_radius.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
