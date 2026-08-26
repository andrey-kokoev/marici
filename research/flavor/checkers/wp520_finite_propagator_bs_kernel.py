"""Finite-momentum aligned bs kernel for the WP516 pole witness."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp508 = load("wp508_canonical_heavy_gauge_poles.json")
wp513 = load("wp513_aligned_closure_current_no_go.json")
wp516 = load("wp516_hierarchical_mass_basis_vertices.json")
wp519 = load("wp519_wet_matching_domain_audit.json")

z, q_squared = sp.symbols("z q_squared", real=True)
g_f, g_p, g_e, mu, s, a, b = sp.symbols(
    "g_F g_P g_E mu s a b", positive=True
)
symbols = {
    "z": z,
    "g_F": g_f,
    "g_P": g_p,
    "g_E": g_e,
    "mu": mu,
    "s": s,
    "a": a,
    "b": b,
}

v_squared = sp.Integer(246) ** 2
ratio = sp.Integer(400)
b_squared = sp.factor(v_squared / (2 * (ratio**2 + 1)))
a_squared = sp.factor(ratio**2 * b_squared)
substitution = {
    g_f: sp.sqrt(2),
    g_p: sp.Rational(1, 10),
    g_e: sp.Rational(1, 50),
    mu: 1,
    s: 16,
    a: sp.sqrt(a_squared),
    b: sp.sqrt(b_squared),
}

quartics = [
    component
    for component in wp508["heavy_gauge_poles"]["components"]
    if component["size"] == 4
]
sector_a = quartics[0]  # F1,F6,P1,E1
sector_ab = quartics[1]  # F2,F7,P2,E2


def diagonal_current_resolvent(component, local_flavor_position):
    numerator = sp.Matrix(
        [
            [sp.sympify(value, locals=symbols) for value in row]
            for row in component["flavor_current_resolvent"]["numerator_matrix"]
        ]
    )
    denominator = sp.sympify(
        component["flavor_current_resolvent"]["denominator"], locals=symbols
    )
    # WP513 uses M^-2=-[(z I-M^2)^-1] at z=0.  At spacelike
    # transfer z=-q^2 the same sign gives (M^2+q^2)^-1.
    return sp.factor(
        -numerator[local_flavor_position, local_flavor_position] / denominator
    )


k_f6 = diagonal_current_resolvent(sector_a, 1)
k_f7 = diagonal_current_resolvent(sector_ab, 1)
bs_kernel = sp.factor((k_f6 - k_f7) / 4)
bs_kernel_witness = sp.factor(bs_kernel.subs(substitution))
contact_value = sp.factor(bs_kernel_witness.subs(z, 0))
expected_contact = sp.factor(
    b_squared / (4 * a_squared * (a_squared + b_squared))
)
spacelike_kernel = sp.factor(bs_kernel_witness.subs(z, -q_squared))
normalized_form_factor = sp.factor(spacelike_kernel / contact_value)

diagnostic_q_gev = [
    sp.Rational(1, 100),
    sp.Rational(1, 20),
    sp.Rational(1, 10),
    sp.Rational(1, 2),
    sp.Integer(1),
    sp.Integer(5),
]
diagnostic = []
for q_value in diagnostic_q_gev:
    form_factor = sp.N(normalized_form_factor.subs(q_squared, q_value**2), 40)
    diagnostic.append(
        {
            "spacelike_q_GeV": float(q_value),
            "normalized_kernel": float(form_factor),
            "relative_contact_error": float(abs(form_factor - 1)),
        }
    )

# A local coefficient has zero logarithmic momentum slope.  The source kernel
# does not: compute the exact normalized first derivative at q^2=0.
normalized_slope_at_zero = sp.factor(
    sp.diff(normalized_form_factor, q_squared).subs(q_squared, 0)
)
lightest_mass = wp516["mass_basis"]["ordered_masses_GeV"][0]
form_factor_at_lightest_mass = sp.N(
    normalized_form_factor.subs(
        q_squared, sp.Float(lightest_mass, 40) ** 2
    ),
    40,
)

checks = {
    "wp508_dependency_passed": bool(wp508["passed"]),
    "wp513_dependency_passed": bool(wp513["passed"]),
    "wp516_dependency_passed": bool(wp516["passed"]),
    "wp519_dependency_passed": bool(wp519["passed"]),
    "aligned_bs_kernel_uses_f6_minus_f7_over_four": bool(
        sector_a["generators"][:2] == ["F1", "F6"]
        and sector_ab["generators"][:2] == ["F2", "F7"]
    ),
    "zero_momentum_kernel_recovers_wp513_shape": sp.simplify(
        contact_value - expected_contact
    )
    == 0,
    "normalized_form_factor_is_one_at_zero": sp.simplify(
        normalized_form_factor.subs(q_squared, 0) - 1
    )
    == 0,
    "finite_momentum_slope_is_nonzero": normalized_slope_at_zero != 0,
    "contact_error_is_resolved_at_one_tenth_GeV": bool(
        diagnostic[2]["relative_contact_error"] > 1e-2
    ),
    "contact_error_is_order_one_at_one_GeV": bool(
        diagnostic[4]["relative_contact_error"] > 0.5
    ),
    "contact_error_exceeds_one_tenth_at_half_GeV": bool(
        diagnostic[3]["relative_contact_error"] > 0.1
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP520",
    "source_domain": "WP516 aligned propagating pole witness; spacelike current exchange before hadronic convolution",
    "aligned_bs_kernel": {
        "exact_witness_rational_function": str(bs_kernel_witness),
        "zero_momentum_value": str(contact_value),
        "wp513_expected_zero_momentum_value": str(expected_contact),
        "normalized_spacelike_form_factor": str(normalized_form_factor),
        "normalized_q_squared_slope_at_zero_GeV^-2": str(
            normalized_slope_at_zero
        ),
    },
    "diagnostic_spacelike_points": diagnostic,
    "form_factor_at_lightest_pole_mass_scale": float(
        form_factor_at_lightest_mass
    ),
    "classification": "Exact finite-propagator source kernel and a falsifier of momentum-independent contact transport at the WP516 witness. This is not yet a hadronic DeltaM_s instrument because no bound-state momentum functional is declared.",
    "selector": False,
    "rigidifier": bool(normalized_slope_at_zero != 0),
    "instrument": "Source-side momentum-dependent probe only. A lattice or other calibrated bilocal DeltaB=2 matrix element is required to compose it with DeltaM_s.",
    "smallest_exact_falsifier": "The exact normalized q^2 slope at zero is nonzero, whereas a single local WET coefficient has zero momentum slope. The 0.5 GeV diagnostic already differs from contact by more than ten percent.",
    "remaining_gate": "Declare and calibrate the bilocal neutral-B matrix-element functional for the finite propagator, including threshold running and uncertainties; then compare its DeltaM_s prediction with WP511.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp520_finite_propagator_bs_kernel.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
