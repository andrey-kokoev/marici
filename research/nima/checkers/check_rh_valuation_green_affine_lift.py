import json
from pathlib import Path

import sympy as sp


z, ell = sp.symbols("z ell")
a = sp.Rational(1, 2) + z
b = sp.Rational(1, 2) - z

response = (sp.exp(-a * ell) - sp.exp(-b * ell)) / (1 - sp.exp(-ell))
hyperbolic = -sp.sinh(ell * z) / sp.sinh(ell / 2)

response_residual = sp.simplify(sp.together((response - hyperbolic).rewrite(sp.exp)))
archimedean_limit = sp.simplify(sp.limit(response, ell, 0))

d1p, d1m, d2p, d2m = sp.symbols("d1p d1m d2p d2m")
r1p, r1m, r2p, r2m = sp.symbols("r1p r1m r2p r2m")

M1 = sp.Matrix(
    [
        [d1p, 0, -r1p],
        [0, d1m, -r1m],
        [0, 0, 1],
    ]
)
M2 = sp.Matrix(
    [
        [d2p, 0, -r2p],
        [0, d2m, -r2m],
        [0, 0, 1],
    ]
)

composite = M2 * M1
expected = sp.Matrix(
    [
        [d2p * d1p, 0, -(d2p * r1p + r2p)],
        [0, d2m * d1m, -(d2m * r1m + r2m)],
        [0, 0, 1],
    ]
)
affine_residual = composite - expected
affine_determinant_residual = sp.simplify(M1.det() - d1p * d1m)

# A nonconstant exponential forcing fixture checks the two prime-step orders.
# The packet proves the general identity by splitting the Duhamel integral.
x, lp, lq, c = sp.symbols("x lp lq c")


def reservoir(rate, base, length):
    return sp.exp(-c * base) * (
        sp.exp(-c * length) - sp.exp(-rate * length)
    ) / (rate - c)


def route_residual(rate):
    p_then_q = (
        sp.exp(-rate * lq) * reservoir(rate, x, lp)
        + reservoir(rate, x + lp, lq)
    )
    q_then_p = (
        sp.exp(-rate * lp) * reservoir(rate, x, lq)
        + reservoir(rate, x + lq, lp)
    )
    return sp.simplify(sp.together(p_then_q - q_then_p))


prime_order_residual = [route_residual(a), route_residual(b)]

# The first determinant-visible extension needs a return row.
dp, dm, rp, rm, cp, cm, edge = sp.symbols("dp dm rp rm cp cm edge", nonzero=True)
D = sp.diag(dp, dm)
r = sp.Matrix([rp, rm])
cvec = sp.Matrix([cp, cm])
M = D.row_join(-r).col_join(sp.Matrix([[cp, cm, edge]]))
schur = edge + (cvec.T * D.inv() * r)[0]
schur_determinant_residual = sp.simplify(M.det() - D.det() * schur)

kappa = sp.symbols("kappa")
J = sp.diag(1, 1, 1)
J[:2, :2] = sp.Matrix([[0, 1], [1, 0]])
M_kappa = D.row_join(-r).col_join(
    sp.Matrix([[kappa * rp, kappa * rm, edge]])
)
M_kappa_reflected = sp.diag(dm, dp).row_join(-sp.Matrix([rm, rp])).col_join(
    sp.Matrix([[kappa * rm, kappa * rp, edge]])
)
reciprocal_covariance_residual = M_kappa_reflected - J * M_kappa * J
return_gain_effect = sp.simplify(
    M_kappa.det().subs(kappa, 1) - M_kappa.det().subs(kappa, 0)
)

# A metric-self-adjoint boundary generator fixes the return row relative to
# the chosen channel and boundary metrics, but rescaling the metric changes it.
g, u, h, a0 = sp.symbols("g u h a0", nonzero=True)
G = sp.Matrix([[g, u], [u, g]])
r_metric = sp.Matrix([rp, rm])
c_metric = -G * r_metric / h
K_metric = (a0 * sp.eye(2)).row_join(-r_metric).col_join(
    sp.Matrix([[c_metric[0], c_metric[1], edge]])
)
H_metric = G.row_join(sp.zeros(2, 1)).col_join(sp.Matrix([[0, 0, h]]))
metric_self_adjoint_residual = sp.simplify(K_metric.T * H_metric - H_metric * K_metric)

K_metric_1 = K_metric.subs({g: 1, u: 0, h: 1})
K_metric_2 = K_metric.subs({g: 2, u: 0, h: 1})
metric_scale_determinant_effect = sp.simplify(K_metric_2.det() - K_metric_1.det())

# The moving-endpoint boost selects a Lorentz form, not a positive tail metric.
l11, l12, l22 = sp.symbols("l11 l12 l22", real=True)
sigma_x = sp.Matrix([[0, 1], [1, 0]])
L_general = sp.Matrix([[l11, l12], [l12, l22]])
lorentz_equations = list(sigma_x * L_general + L_general * sigma_x)
lorentz_solution = sp.solve(lorentz_equations, [l12, l22], dict=True)
L_lorentz = sp.diag(l11, -l11)
lorentz_residual = sigma_x * L_lorentz + L_lorentz * sigma_x
lorentz_determinant = sp.factor(L_lorentz.det())

# The Lorentz-to-positive comparison changes the real structure.
W = sp.diag(1, sp.I)
J_lorentz = sp.diag(1, -1)
wick_bilinear_residual = sp.simplify(W.T * W - J_lorentz)
wick_hermitian_residual = sp.simplify(W.conjugate().T * W - sp.eye(2))

zb = sp.symbols("zb")
A_conjugate = -sp.Rational(1, 2) * sp.eye(2) - zb * sigma_x
A_reciprocal = -sp.Rational(1, 2) * sp.eye(2) + zb * sigma_x
real_structure_transport_residual = sp.simplify(
    J_lorentz * A_conjugate * J_lorentz - A_reciprocal
)
real_structure_square_residual = sp.simplify(J_lorentz**2 - sp.eye(2))

# Dagger covariance makes a constant return gain real but does not fix it.
kappa_bar = sp.symbols("kappa_bar")
dagger_return_residual = sp.simplify((kappa - kappa_bar) * J_lorentz * r)
dagger_real_gain_residual = dagger_return_residual.subs(kappa_bar, kappa)

# The additive current reaches a determinant line only through a character.
y1, y2 = sp.symbols("y1 y2")
character_composition_residual = sp.simplify(
    sp.exp(kappa * (y1 + y2))
    - sp.exp(kappa * y1) * sp.exp(kappa * y2)
)
character_tangent = sp.diff(sp.exp(kappa * y1), y1).subs(y1, 0)

# A co-moving odd return row closes the frozen-forcing jet, but a varying
# forcing exposes a quadratic residual.
L, t, f0, slope = sp.symbols("L t f0 slope")


def reservoir_series(rate):
    integrand = sp.exp(-rate * L * (1 - t)) * (f0 + slope * L * t)
    truncated = sp.series(integrand, L, 0, 4).removeO()
    return sp.expand(L * sp.integrate(truncated, (t, 0, 1)))


r_plus_series = reservoir_series(a)
r_minus_series = reservoir_series(b)
odd_jet_series = sp.diff(r_plus_series - r_minus_series, L)
endpoint_current_series = sp.series(
    2 * (f0 + slope * L) * sp.exp(-L / 2) * sp.sinh(z * L),
    L,
    0,
    3,
).removeO()
variable_forcing_residual_series = sp.expand(
    odd_jet_series + endpoint_current_series
)
variable_forcing_quadratic_residual = sp.expand(
    variable_forcing_residual_series
).coeff(L, 2)

# The theta forcing closes nonlinearly but generates an infinite linear jet
# tower on h_k = y^k f.
x_source = sp.symbols("x_source", real=True)
y_source = sp.exp(2 * x_source)
f_source = 2 * sp.exp(-sp.pi * y_source)
forcing_connection_residual = sp.simplify(
    sp.diff(f_source, x_source) + 2 * sp.pi * y_source * f_source
)
forcing_transport_residual = sp.simplify(
    f_source.subs(x_source, x_source + L)
    - f_source
    * sp.exp(-sp.pi * y_source * (sp.exp(2 * L) - 1))
)

k_grade = sp.symbols("k_grade", integer=True, nonnegative=True)
h_grade = y_source**k_grade * f_source
h_next = y_source ** (k_grade + 1) * f_source
forcing_grade_residual = sp.simplify(
    sp.diff(h_grade, x_source) - 2 * k_grade * h_grade + 2 * sp.pi * h_next
)

assert response_residual == 0
assert archimedean_limit == -2 * z
assert affine_residual == sp.zeros(3)
assert affine_determinant_residual == 0
assert prime_order_residual == [0, 0]
assert schur_determinant_residual == 0
assert reciprocal_covariance_residual == sp.zeros(3)
assert return_gain_effect == dm * rp**2 + dp * rm**2
assert metric_self_adjoint_residual == sp.zeros(3)
assert metric_scale_determinant_effect != 0
assert lorentz_solution == [{l12: 0, l22: -l11}]
assert lorentz_residual == sp.zeros(2)
assert lorentz_determinant == -l11**2
assert wick_bilinear_residual == sp.zeros(2)
assert wick_hermitian_residual == sp.zeros(2)
assert real_structure_transport_residual == sp.zeros(2)
assert real_structure_square_residual == sp.zeros(2)
assert dagger_real_gain_residual == sp.zeros(2, 1)
assert dagger_return_residual != sp.zeros(2, 1)
assert character_composition_residual == 0
assert character_tangent == kappa
assert variable_forcing_quadratic_residual == z * slope
assert forcing_connection_residual == 0
assert forcing_transport_residual == 0
assert forcing_grade_residual == 0

result = {
    "schema": "marici.rh-valuation-green-affine-lift.v1",
    "homogeneous_response_residual": str(response_residual),
    "archimedean_limit": str(archimedean_limit),
    "affine_composition_residual": [str(x) for x in affine_residual],
    "affine_determinant_residual": str(affine_determinant_residual),
    "forcing_coordinates_absent_from_determinant": True,
    "sampled_prime_order_residual": [str(x) for x in prime_order_residual],
    "schur_determinant_residual": str(schur_determinant_residual),
    "reciprocal_covariance_residual": [
        str(x) for x in reciprocal_covariance_residual
    ],
    "unit_return_gain_determinant_effect": str(return_gain_effect),
    "metric_self_adjoint_residual": [
        str(x) for x in metric_self_adjoint_residual
    ],
    "metric_scale_determinant_effect": str(metric_scale_determinant_effect),
    "tail_metric_solution": {"l12": "0", "l22": "-l11"},
    "tail_metric_anticommutator_residual": [
        str(x) for x in lorentz_residual
    ],
    "tail_metric_determinant": str(lorentz_determinant),
    "wick_bilinear_residual": [str(x) for x in wick_bilinear_residual],
    "wick_hermitian_residual": [str(x) for x in wick_hermitian_residual],
    "real_structure_transport_residual": [
        str(x) for x in real_structure_transport_residual
    ],
    "real_structure_square_residual": [
        str(x) for x in real_structure_square_residual
    ],
    "dagger_return_residual": [str(x) for x in dagger_return_residual],
    "dagger_real_gain_residual": [str(x) for x in dagger_real_gain_residual],
    "current_character_composition_residual": str(character_composition_residual),
    "current_character_tangent": str(character_tangent),
    "variable_forcing_quadratic_residual": str(
        variable_forcing_quadratic_residual
    ),
    "theta_forcing_connection_residual": str(forcing_connection_residual),
    "theta_forcing_transport_residual": str(forcing_transport_residual),
    "forcing_grade_tower_residual": str(forcing_grade_residual),
    "verdict": "finite_affine_sampling_and_nonlinear_forcing_connection_exact",
    "unresolved": [
        "faithful_retention_of_prime_edge_typing",
        "labelled_aggregation",
        "restricted_product_completion",
        "completion_of_co_moving_forcing_to_schur_incidence",
        "source_varying_extension_of_co_moving_return_row",
        "common_source_metric_for_green_and_boundary_ports",
        "source_comparison_from_lorentz_tails_to_positive_clark_features",
        "dagger_compatible_forcing_to_boundary_return_incidence",
        "source_unit_for_additive_current_to_determinant_character",
        "completion_of_infinite_linear_forcing_jet_tower",
    ],
}

output = Path(__file__).parents[1] / "results" / "rh-valuation-green-affine-lift.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
