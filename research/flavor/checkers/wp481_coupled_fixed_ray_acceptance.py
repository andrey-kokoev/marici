"""Exact reduced fixed-ray acceptance theorem for WP481."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp477 = load("wp477_ratio_selector_normal_form.json")
wp478 = load("wp478_messenger_portal_threshold.json")
wp480 = load("wp480_triplicated_messenger_beta_gate.json")

alpha_g, alpha_y = sp.symbols("alpha_g alpha_y", positive=True)
A, C, D, E, F = sp.symbols("A C D E F", positive=True)
delta = sp.symbols("delta", positive=True)

beta_g = 2 * alpha_g**2 * (A + C * alpha_g - D * alpha_y)
beta_y = 2 * alpha_y * (E * alpha_y - F * alpha_g)
yukawa_nullcline = sp.simplify(F * alpha_g / E)
effective_margin = sp.simplify(D * F / E - C)
alpha_g_star = sp.simplify(A / effective_margin)
alpha_y_star = sp.simplify(yukawa_nullcline.subs(alpha_g, alpha_g_star))
beta_g_on_yukawa_nullcline = sp.simplify(beta_g.subs(alpha_y, yukawa_nullcline))

r_q, r_phi, r_eta, k_phi, y_geom = sp.symbols(
    "r_Q r_Phi r_eta k_Phi y_geom", positive=True
)
four_pi_squared = 16 * sp.pi**2

# Fixed-ray normalization: each squared Yukawa and eta is written relative to
# alpha_g using the common (4*pi)^2 convention.
y_q_squared = four_pi_squared * r_q * alpha_g
y_phi_squared = four_pi_squared * r_phi * alpha_g
eta = four_pi_squared * r_eta * alpha_g
g_squared = four_pi_squared * alpha_g
c_ray = sp.simplify(
    3 * k_phi * y_q_squared * y_phi_squared
    / (16 * sp.pi**2 * eta * g_squared * y_geom**2)
)
target_ray = sp.simplify(sp.sqrt(3 / c_ray))

benchmark_c = sp.sympify(
    wp477["conditional_five_TeV_readout"]["required_c_exact"]
)
benchmark_target = sp.sympify(
    wp477["conditional_five_TeV_readout"]["target_exact"]
)
required_ray_ratio = sp.simplify(
    benchmark_target**2 / (16 * sp.pi**2)
)

checks = {
    "wp477_dependency_passed": wp477["passed"],
    "wp478_dependency_passed": wp478["passed"],
    "wp480_dependency_passed": wp480["passed"],
    "nonzero_yukawa_nullcline_exact": sp.simplify(beta_y.subs(alpha_y, yukawa_nullcline)) == 0,
    "gauge_root_exact_on_yukawa_nullcline": sp.simplify(beta_g_on_yukawa_nullcline.subs(alpha_g, alpha_g_star)) == 0,
    "effective_margin_sign_is_DF_minus_CE": sp.simplify(effective_margin - (D * F - C * E) / E) == 0,
    "positive_margin_parameterization_gives_positive_root": sp.simplify(alpha_g_star.subs(D, C * E / F + delta) - A * E / (delta * F)) == 0,
    "fixed_yukawa_root_is_positive_when_margin_positive": alpha_y_star / alpha_g_star == F / E,
    "selector_coordinate_cancels_fixed_point_magnitude": not c_ray.has(alpha_g),
    "selector_coordinate_on_ray_exact": c_ray == 3 * k_phi * r_phi * r_q / (16 * sp.pi**2 * r_eta * y_geom**2),
    "selected_target_on_ray_exact": target_ray == 4 * sp.pi * sp.sqrt(r_eta) * y_geom / (sp.sqrt(k_phi) * sp.sqrt(r_phi) * sp.sqrt(r_q)),
    "benchmark_ray_ratio_reproduces_target": sp.simplify(required_ray_ratio - 3 / (16 * sp.pi**2 * benchmark_c)) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP481",
    "bounded_model": "generic leading reduced gauge-Yukawa subsystem for the triplicated messenger theory; coefficients remain to be derived from the full action",
    "beta_functions": {
        "beta_alpha_g": str(beta_g),
        "beta_alpha_y": str(beta_y),
        "positive_one_loop_gauge_loss": "A=13/2 for WP480 before convention-dependent higher-loop normalization",
    },
    "interacting_fixed_ray": {
        "alpha_y_over_alpha_g": str(F / E),
        "effective_margin": str(effective_margin),
        "alpha_g_star": str(alpha_g_star),
        "alpha_y_star": str(alpha_y_star),
        "existence_condition": "D*F/E-C>0",
        "perturbative_condition": "A/(D*F/E-C) is positive and much smaller than one",
    },
    "selector_on_fixed_ray": {
        "ray_definitions": {
            "y_Q_squared": "16*pi^2*r_Q*alpha_g",
            "y_Phi_squared": "16*pi^2*r_Phi*alpha_g",
            "eta": "16*pi^2*r_eta*alpha_g",
        },
        "c": str(c_ray),
        "g_F_f_over_v": str(target_ray),
        "scale_and_fixed_point_magnitude_cancel": bool(not c_ray.has(alpha_g)),
    },
    "conditional_benchmark_test": {
        "required_c": str(benchmark_c),
        "required_ray_ratio_ygeom2_reta_over_k_rq_rphi": str(required_ray_ratio),
        "required_ray_ratio_numeric": float(sp.N(required_ray_ratio, 16)),
        "authority": "withheld phenomenological test only; it may not determine A,C,D,E,F or the ray ratios",
    },
    "predeclared_acceptance_conditions": [
        "derive A,C,D,E,F from the complete triplicated action in one scheme",
        "prove D*F/E-C>0 and a perturbatively small positive fixed point",
        "derive every Yukawa and quartic ray ratio, including r_Q, r_Phi, r_eta, k_Phi, and y_geom",
        "prove scalar stability and that the equal-port Gram is RG invariant",
        "perform finite messenger-threshold matching and prove c descends to the pole domain",
        "keep all messenger and charged-scalar channels above the vector poles before reusing WP476 widths",
        "compare the resulting c with kaon, Higgs, and pole instruments only after all source coefficients are frozen",
    ],
    "classification": "Exact acceptance theorem for a possible coupled fixed-ray selector; no concrete flavor fixed point or numerical selector is yet admitted.",
    "selector": False,
    "rigidifier": False,
    "reference_port_required": False,
    "instrument": None,
    "smallest_exact_falsifier": "D*F/E-C is nonpositive, in which case the reduced system has no positive interacting gauge-Yukawa root despite the Yukawa port.",
    "remaining_gate": "Compute the actual coefficients and fixed-ray ratios of the triplicated messenger action without using the target value, then run the predeclared acceptance conditions.",
    "source": "https://arxiv.org/abs/1406.2337",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp481_coupled_fixed_ray_acceptance.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
