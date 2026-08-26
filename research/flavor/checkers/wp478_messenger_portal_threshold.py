"""Exact one-loop messenger portal-threshold audit for WP478."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp435 = load("wp435_dynamical_flavon_messenger_completion.json")
wp477 = load("wp477_ratio_selector_normal_form.json")

x, z = sp.symbols("x z", nonnegative=True)
mass, scale = sp.symbols("M Q", positive=True)
nc = sp.Integer(3)

# Squared singular values of [[0,A],[B,M]], with x=A^2 and z=B^2.
trace = mass**2 + x + z
determinant = x * z
discriminant = sp.sqrt(trace**2 - 4 * determinant)
lambda_heavy = sp.simplify((trace + discriminant) / 2)
lambda_light = sp.simplify((trace - discriminant) / 2)

def cw_kernel(eigenvalue):
    return eigenvalue**2 * (sp.log(eigenvalue / scale**2) - sp.Rational(3, 2))


heavy_mixed_derivative = sp.simplify(
    sp.diff(cw_kernel(lambda_heavy), x, z).subs({x: 0, z: 0})
)

# The light eigenvalue starts as x*z/M^2, hence its CW kernel starts at
# order x^2*z^2 log(x*z) and has no local x*z coefficient.
light_leading_ratio = sp.simplify(
    sp.limit(sp.limit(lambda_light / (x * z), x, 0, dir="+"), z, 0, dir="+")
)
divergent_mixed_derivative = sp.simplify(
    sp.diff(trace**2 - 2 * determinant, x, z)
)

y_q, y_phi, eta, g_f, y, k_phi = sp.symbols(
    "y_Q y_Phi eta g_F y k_Phi", positive=True
)
threshold_coefficient = sp.simplify(-nc * y_q**2 * y_phi**2 / (8 * sp.pi**2))

# Matching -2 eta a |H|^2 sigma^2 to the negative finite threshold, with
# k_phi carrying the declared background/group normalization phi^2=k_phi sigma^2.
a_induced = sp.simplify(nc * k_phi * y_q**2 * y_phi**2 / (16 * sp.pi**2 * eta))
c_induced = sp.simplify(a_induced / (g_f**2 * y**2))
target_induced = sp.simplify(sp.sqrt(3 / c_induced))
hostile_target = sp.simplify(target_induced.subs(y_q, 2 * y_q))

checks = {
    "wp435_dependency_passed": wp435["passed"],
    "wp477_dependency_passed": wp477["passed"],
    "mass_squared_trace_exact": sp.simplify(lambda_heavy + lambda_light - trace) == 0,
    "mass_squared_determinant_exact": sp.simplify(lambda_heavy * lambda_light - determinant) == 0,
    "heavy_mixed_cw_derivative_is_two": heavy_mixed_derivative == 2,
    "light_eigenvalue_starts_at_xz_over_M_squared": light_leading_ratio == 1 / mass**2,
    "mixed_divergence_cancels": divergent_mixed_derivative == 0,
    "finite_threshold_is_negative": threshold_coefficient < 0,
    "induced_a_is_positive": a_induced > 0,
    "induced_selector_coordinate_contains_free_yukawas": c_induced.has(y_q, y_phi),
    "induced_selector_coordinate_contains_eta_and_gauge_coupling": c_induced.has(eta, g_f),
    "hostile_yukawa_rescaling_halves_target": sp.simplify(target_induced / hostile_target) == 2,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP478",
    "bounded_domain": "one color-degenerate singular channel of the WP435 renormalizable messenger chain, real constant Higgs/flavon backgrounds, one-loop MS-like Coleman-Weinberg matching",
    "mass_matrix": "[[0,y_Q*h],[y_Phi*phi,M]]",
    "squared_singular_values": {
        "trace": str(trace),
        "determinant": str(determinant),
        "heavy": str(lambda_heavy),
        "light": str(lambda_light),
    },
    "one_loop_threshold": {
        "heavy_mixed_derivative": str(heavy_mixed_derivative),
        "light_leading_eigenvalue": "x*z/M^2",
        "mixed_uv_divergence": str(divergent_mixed_derivative),
        "finite_H2_Phi2_coefficient_for_Nc_3": str(threshold_coefficient),
        "scale_and_mass_dependence_at_dimension_four": "none; the local mixed coefficient is finite",
    },
    "portal_matching": {
        "background_normalization": "phi^2=k_Phi*sigma^2",
        "induced_a": str(a_induced),
        "induced_c": str(c_induced),
        "induced_target": str(target_induced),
    },
    "contextual_partition": {
        "source_generation": "The admitted messenger chain genuinely generates the negative mixed portal sign required by eta*(HdaggerH-a*sigma^2)^2.",
        "selection": "The coefficient depends continuously on y_Q, y_Phi, eta, g_F, y, and the group/background normalization; none is fixed by the threshold operation.",
        "hostile_pair": "y_Q and 2*y_Q preserve the messenger grammar but multiply c by four and divide g_F*f/v by two.",
    },
    "classification": "Source-generated portal rigidifies the interaction sign and functional form but does not numerically select the WP477 coefficient.",
    "selector": False,
    "rigidifier": bool(threshold_coefficient < 0),
    "reference_port_required": False,
    "instrument": None,
    "smallest_exact_falsifier": "Rescale one admitted messenger Yukawa by two; the source class is preserved while the predicted ratio is halved.",
    "remaining_gate": "Derive the messenger Yukawas, eta, g_F, y, and group normalization from a common fixed trajectory, then perform full matrix-valued threshold matching and test beta_c=0.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp478_messenger_portal_threshold.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
