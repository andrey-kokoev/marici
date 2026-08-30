"""Exact causal-resonance companion-signal gate."""

import json
from pathlib import Path

import sympy as sp


A, gamma, G = sp.symbols("A gamma G", positive=True, real=True)
disc = A**2 - 4 * G**2 * gamma**2
root = sp.sqrt(disc)
delta_plus = (A + root) / (2 * G)
delta_minus = (A - root) / (2 * G)


def real_response(delta):
    return sp.factor(A * delta / (delta**2 + gamma**2))


def imag_response(delta):
    return sp.factor(A * gamma / (delta**2 + gamma**2))


# The root equation G*delta^2 - A*delta + G*gamma^2 = 0 permits
# denominator reduction without unsafe numerical substitutions.
def reduce_on_root(expr, delta):
    numerator = sp.together(expr).as_numer_denom()[0]
    reduced = sp.rem(numerator, G * delta**2 - A * delta + G * gamma**2, delta)
    return sp.factor(reduced)


d = sp.symbols("d", positive=True, real=True)
root_real_identity = reduce_on_root(real_response(d) - G, d)

# Exact hostile packet.
a0, gamma0, g0 = sp.Integer(5), sp.Integer(1), sp.Integer(1)
rp = sp.sqrt(21)
d0_plus = (5 + rp) / 2
d0_minus = (5 - rp) / 2
r0_plus = sp.simplify(a0 * d0_plus / (d0_plus**2 + gamma0**2))
r0_minus = sp.simplify(a0 * d0_minus / (d0_minus**2 + gamma0**2))
i0_plus = sp.simplify(a0 * gamma0 / (d0_plus**2 + gamma0**2))
i0_minus = sp.simplify(a0 * gamma0 / (d0_minus**2 + gamma0**2))

checks = {
    "target_gain_equation_has_discriminant_A2_minus_4G2gamma2": sp.discriminant(G * d**2 - A * d + G * gamma**2, d) == disc,
    "real_detuning_requires_A_at_least_2Ggamma": sp.solve_univariate_inequality(disc >= 0, A) == (2 * G * gamma <= A),
    "both_formula_roots_satisfy_target_response_equation": root_real_identity == 0,
    "two_detunings_have_product_gamma_squared": sp.simplify(delta_plus * delta_minus) == gamma**2,
    "hostile_pair_has_equal_unit_dispersive_gain": r0_plus == g0 and r0_minus == g0,
    "hostile_pair_has_unequal_absorption": sp.simplify(i0_plus - i0_minus) != 0,
    "hostile_pair_absorption_product_equals_gain_squared": sp.simplify(i0_plus * i0_minus) == g0**2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP424",
    "title": "Causal resonance companion-signal gate",
    "susceptibility": "A/(Delta - i gamma)",
    "target_gain_existence_condition": "A >= 2 G gamma",
    "detuning_roots": {"plus": str(delta_plus), "minus": str(delta_minus)},
    "hostile_pair": {
        "A": str(a0), "gamma": str(gamma0), "G": str(g0),
        "Delta_plus": str(d0_plus), "Delta_minus": str(d0_minus),
        "Re_plus": str(r0_plus), "Re_minus": str(r0_minus),
        "Im_plus": str(i0_plus), "Im_minus": str(i0_minus),
        "absorption_product": str(sp.factor(i0_plus * i0_minus)),
    },
    "classification": "gain-only readout is nonfaithful; resonance requires a calibrated dispersion-absorption frequency scan",
    "smallest_exact_falsifier": "A < 2 G gamma or a measured dispersion-absorption scan inconsistent with the shared pole",
    "remaining_gate": "an admitted resonance substrate with independently fixed pole strength, linewidth, frequency command, and common-frame Higgs readout",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp424_causal_resonance_companion_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
