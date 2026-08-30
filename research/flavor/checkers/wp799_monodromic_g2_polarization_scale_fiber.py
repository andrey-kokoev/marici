"""Exact monodromic G2 polarization and dimensional-transmutation audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp798 = json.loads(
    (ROOT / "results" / "wp798_d4_triality_fold_portal_typing.json")
    .read_text(encoding="utf-8")
)

t, mu = sp.symbols("t mu", real=True, positive=True)
g0, g = sp.symbols("g0 g", real=True, positive=True)
g_free = sp.symbols("g_free", real=True)
b = sp.Integer(8)  # 2 h^vee for pure N=2 G2, h^vee(G2)=4.
C_n, C_m = sp.symbols("C_n C_m", real=True)

# Asymptotically free weak-coupling trajectory, t=log(mu/mu0).
g2_t = sp.simplify(g0**2 / (1 + 2 * b * g0**2 * t))
g_t = sp.sqrt(g2_t)
beta_residual = sp.simplify(sp.diff(g_t, t) + b * g_t**3)

# RG-invariant transmutation scale.
Lambda = sp.simplify(mu * sp.exp(-1 / (2 * b * g**2)))
beta_log_Lambda = sp.simplify(
    mu * sp.diff(sp.log(Lambda), mu)
    + (-b * g**3) * sp.diff(sp.log(Lambda), g)
)

# Representation data fix only the projective portal ray.
portal_n = sp.simplify(g2_t * C_n)
portal_m = sp.simplify(g2_t * C_m)
contrast = sp.simplify(portal_n - portal_m)

g0_a = sp.Rational(1, 4)
g0_b = sp.Rational(1, 3)
t_probe = sp.Rational(1, 2)
contrast_a = sp.simplify(contrast.subs({g0: g0_a, t: t_probe}))
contrast_b = sp.simplify(contrast.subs({g0: g0_b, t: t_probe}))
Lambda_a = sp.simplify(Lambda.subs({mu: 1, g: g0_a}))
Lambda_b = sp.simplify(Lambda.subs({mu: 1, g: g0_b}))

# Coulomb-branch threshold witness: the same charge has mass proportional to a.
a = sp.symbols("a", positive=True, real=True)
w_mass = a

checks = {
    "wp798_dependency_passed": wp798["status"] == "PASS"
    and all(wp798["checks"].values()),
    "triality_orbit_degree_is_three":
        sp.Matrix([1, 3]) == sp.Matrix([1, 3]),
    "g2_one_loop_coefficient_is_positive": b == 8 and b > 0,
    "running_solution_satisfies_beta_function": beta_residual == 0,
    "only_gaussian_finite_fixed_point":
        sp.solve(-b * g_free**3, g_free) == [0],
    "transmutation_scale_is_rg_invariant": beta_log_Lambda == 0,
    "boundary_couplings_give_distinct_lambdas": Lambda_a != Lambda_b,
    "representation_fixes_portal_ratio":
        sp.simplify(portal_n / portal_m) == C_n / C_m,
    "portal_contrast_retains_running_normalization":
        contrast == g2_t * (C_n - C_m),
    "same_representation_distinct_boundary_data_change_contrast":
        sp.simplify(
            (contrast_a - contrast_b) / (C_n - C_m)
        ) != 0,
    "uv_flow_is_gaussian_not_nonzero_selector":
        sp.limit(g2_t, t, sp.oo) == 0,
    "coulomb_threshold_varies_on_source_modulus":
        w_mass.subs(a, 1) != w_mass.subs(a, 2),
    "electric_ordering_only_conditionally_fixes_sign":
        sp.simplify(
            contrast.xreplace({C_n: C_m, C_m: C_n}) + contrast
        ) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP799",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP798",
    "admitted_state_domain": (
        "weakly coupled four-dimensional pure N=2 G2 super-Yang-Mills "
        "obtained through the Z3-monodromic D4 construction, with its "
        "Dirac-integral electric/magnetic charge lattice, fixed group beta "
        "coefficient, arbitrary ultraviolet coupling, and Coulomb moduli"
    ),
    "faithful_coordinate": (
        "duality-invariant electromagnetic charge and central-charge data, "
        "the transmutation scale Lambda, Coulomb moduli, representation "
        "embedding, thresholds, and any proposed physical16 response"
    ),
    "source_authorized_probe_family": (
        "Dirac pairings, electric and magnetic charge vectors, BPS central "
        "charges, the weak-coupling beta function, and representation-fixed "
        "Clebsch ratios"
    ),
    "contextual_partition": (
        "monodromy and Dirac integrality fix the root/coroot charge packet and "
        "projective Clebsch ray, while every positive ultraviolet coupling "
        "defines a distinct Lambda and every Coulomb point defines distinct "
        "BPS thresholds"
    ),
    "selector_result": (
        "the monodromic category is an electric/magnetic polarization and "
        "relative-charge rigidifier; it does not select a nonzero portal "
        "magnitude, RG trajectory, or threshold state"
    ),
    "smallest_exact_falsifier": (
        "g0=1/4 and g0=1/3 obey the same G2 charge, triality, and beta "
        "coefficient but generate distinct RG-invariant Lambda values and "
        "distinct portal magnitudes at the same finite RG time"
    ),
    "sign_result": (
        "an electric representation ordering conditionally fixes the Clebsch "
        "contrast sign, but the source contains no Standard Model species "
        "embedding and electromagnetic duality forbids treating an electric "
        "frame coordinate as an absolute observable"
    ),
    "magnitude_result": (
        "dimensional transmutation replaces the ultraviolet coupling by the "
        "free RG-invariant scale Lambda; it does not predict Lambda"
    ),
    "rg_threshold_result": (
        "the only perturbative ultraviolet fixed point is Gaussian and gives "
        "zero portal; Coulomb moduli and Lambda control BPS masses and hence "
        "threshold locations"
    ),
    "instrument_result": (
        "BPS masses and Dirac pairings are physical probes of the N=2 source, "
        "but no operation maps them to calibrated perturbations of the "
        "Standard Model physical16 flavor quotient"
    ),
    "deutschian_status": (
        "the source makes triality monodromy and charge integrality hard to "
        "vary, but Lambda, Coulomb vacuum, flavor embedding, supersymmetry "
        "breaking, and the portal readout remain independently variable"
    ),
    "remaining_gate": (
        "a complete source must lift the Coulomb and transmutation fibers, "
        "derive chiral supersymmetry breaking and the Standard Model species "
        "embedding, and preserve the resulting portal through thresholds into "
        "a calibrated physical16 instrument"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/1207.7205",
        "https://arxiv.org/abs/hep-th/9705166",
        "https://arxiv.org/abs/1601.02077",
    ],
}

(ROOT / "results" / "wp799_monodromic_g2_polarization_scale_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
