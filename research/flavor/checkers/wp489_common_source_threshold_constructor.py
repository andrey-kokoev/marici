"""Exact common-source radial and threshold constructor for WP489."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp467 = load("wp467_common_dilaton_clock_portal.json")
wp487 = load("wp487_total_width_closure_cone.json")
wp488 = load("wp488_flavor_clock_normalization_correction.json")

# Canonical radial coordinates: physical flavor norm F, electroweak v,
# connector norm R=sqrt(Tr S^T S), and singlet sigma.
F, V, R, sigma = sp.symbols("F V R sigma", real=True)
radial_variables = (F, V, R, sigma)

# Exact nonempty source witness. Large positive quartics are used only to prove
# that the source cone intersects the independently preregistered width cone.
y = sp.Integer(1)
a = sp.Integer(1)
b = sp.Integer(32)
w = sp.Integer(1)
lambda_x = rho = eta = lambda_s = kappa = sp.Integer(100)

radial_potential = sp.expand(
    rho * (F**2 - 6 * y**2 * sigma**2) ** 2
    + eta * (V**2 / 2 - a * sigma**2) ** 2
    + lambda_s / 3 * (R**2 - 3 * b * sigma**2) ** 2
    + kappa * (sigma**2 - w**2) ** 2
)
vacuum = {
    F: sp.sqrt(6) * y * w,
    V: sp.sqrt(2 * a) * w,
    R: sp.sqrt(3 * b) * w,
    sigma: w,
}
radial_gradient = sp.Matrix([sp.diff(radial_potential, field) for field in radial_variables]).subs(vacuum)
radial_hessian = sp.hessian(radial_potential, radial_variables).subs(vacuum)
shifted_hessian = radial_hessian - sp.eye(4)
leading_minors = [sp.factor(shifted_hessian[:n, :n].det()) for n in range(1, 5)]

# Source-selected relational scales and masses.
mu2 = y**2 * w**2
f_phys2 = 6 * mu2
v2 = 2 * a * w**2
s2 = b * w**2
z_a = z_b = sp.Integer(1)
messenger_a2 = z_a**2 * w**2
messenger_b2 = z_b**2 * w**2

# Gauge witness inherited as a point in coefficient space, now pulled back to
# the same singlet clock rather than declaring independent masses.
g_f2 = sp.Integer(1)
g_p2 = sp.Rational(1, 68)
triplet_a = g_f2 * mu2
triplet_d = g_p2 * (4 * mu2 + 2 * s2)
triplet_b2 = 4 * g_f2 * g_p2 * mu2**2
triplet_disc = sp.factor((triplet_a - triplet_d) ** 2 + 4 * triplet_b2)
m_minus2 = sp.simplify((triplet_a + triplet_d - sp.sqrt(triplet_disc)) / 2)
m_plus2 = sp.simplify((triplet_a + triplet_d + sp.sqrt(triplet_disc)) / 2)
m_quintet2 = 3 * g_f2 * mu2
vector_masses2 = [m_minus2, m_quintet2, m_plus2]

# Nonradial physical scalar lower bounds at this witness. The old flavon block
# scales uniformly when its positive coefficients are both multiplied by 100;
# the connector symmetric modes scale as 8 lambda_S s^2.
flavon_nonradial_min2 = 16 * rho * w**2
connector_nonradial_min2 = 8 * lambda_s * s2
tau2 = min(messenger_a2, messenger_b2, flavon_nonradial_min2, connector_nonradial_min2)

vector_margins = [sp.simplify(4 * left - right) for left in vector_masses2 for right in vector_masses2]
threshold_margins = [sp.simplify(4 * tau2 - mass2) for mass2 in vector_masses2]
clock_ratio = sp.simplify(sp.sqrt(g_f2 * f_phys2 / v2))

checks = {
    "wp467_dependency_passed": bool(
        wp467["scale_kernel_repaired"] and not wp467["numerical_selector_admitted"]
    ),
    "wp487_dependency_passed": wp487["passed"],
    "wp488_dependency_passed": wp488["passed"],
    "radial_vacuum_is_stationary": radial_gradient == sp.zeros(4, 1),
    "radial_hessian_exceeds_unit_threshold": all(value > 0 for value in leading_minors),
    "omitted_representation_square_is_positive_semidefinite": lambda_x > 0,
    "physical_norm_is_six_mu_squared": f_phys2 == 6 * mu2,
    "connector_ratio_is_source_fixed": sp.simplify(s2 / mu2 - b / y**2) == 0,
    "messenger_masses_share_singlet_clock": messenger_a2 == w**2 and messenger_b2 == w**2,
    "minimum_nonquark_threshold_is_one": tau2 == 1,
    "all_vector_pair_closure_margins_are_positive": all(value > 0 for value in vector_margins),
    "all_nonquark_threshold_margins_are_positive": all(value > 0 for value in threshold_margins),
    "physical_clock_ratio_uses_corrected_norm": clock_ratio == sp.sqrt(3),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP489",
    "source_action_extension": {
        "connector_square": "lambda_S ||S^T S-b sigma^2 I_3||_F^2",
        "singlet_lift": "kappa (sigma^2-w^2)^2",
        "messenger_masses": ["z_A sigma Abar A", "z_B sigma Bbar B"],
        "renormalizability": "all terms have canonical dimension at most four",
    },
    "selected_relations": {
        "mu_squared": "y^2 w^2",
        "f_phys_squared": "6 y^2 w^2",
        "v_squared": "2 a w^2",
        "s_squared": "b w^2",
        "M_A_squared": "z_A^2 w^2",
        "M_B_squared": "z_B^2 w^2",
        "g_F_f_phys_over_v": "g_F y sqrt(3/a)",
    },
    "exact_nonempty_witness": {
        "coefficients": "y=a=z_A=z_B=g_F^2=w^2=1, b=32, g_P^2=1/68, lambda_X=rho=eta=lambda_S=kappa=100",
        "radial_lower_bound_hessian": [[str(value) for value in row] for row in radial_hessian.tolist()],
        "hessian_scope": "norm, Higgs, connector-frame, and singlet-lift squares; the omitted representation square adds a positive-semidefinite Hessian at the zero-residual vacuum",
        "shifted_leading_minors": [str(value) for value in leading_minors],
        "minimum_nonquark_mass_squared": str(tau2),
        "vector_mass_squares": [str(value) for value in vector_masses2],
        "physical_clock_ratio": str(clock_ratio),
    },
    "classification": "One renormalizable source can select all relational scale ratios and occupy the tree-level total-width cone; the numerical coefficient witness is existence evidence, not a derived numerical selector.",
    "selector": "conditional relational selector for fixed source coefficients",
    "rigidifier": "preserves the isotropic connector Gram",
    "instrument": None,
    "smallest_exact_falsifier": "The same symmetries admit positive changes of a, b, y, z_A, z_B, g_F, or g_P that move the clock ratio, residues, or thresholds; therefore the witness cannot be promoted to a numerical prediction without coefficient dynamics.",
    "remaining_gate": "Derive the dimensionless coefficients on a complete coupled RG trajectory and attach the WP486 pole/current instrument; only then are the selected ratio and total widths predictions rather than conditional source outputs.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp489_common_source_threshold_constructor.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
