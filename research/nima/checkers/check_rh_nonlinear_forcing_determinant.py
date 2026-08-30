import json
from pathlib import Path

import sympy as sp


y0, f0, ell = sp.symbols("y0 f0 ell")
factor = sp.exp(-sp.pi * y0 * (sp.exp(2 * ell) - 1))
flow = sp.Matrix([y0 * sp.exp(2 * ell), f0 * factor])
flow_jacobian = flow.jacobian([y0, f0])
flow_determinant = sp.factor(flow_jacobian.det())
expected_flow_determinant = sp.exp(2 * ell) * factor
flow_determinant_residual = sp.simplify(
    flow_determinant - expected_flow_determinant
)

y, f, m, n, z = sp.symbols("y f m n z")
vector_field = sp.Matrix(
    [
        2 * y,
        -2 * sp.pi * y * f,
        -sp.Rational(1, 2) * m - z * n - f,
        -z * m - sp.Rational(1, 2) * n,
    ]
)
state = [y, f, m, n]
coupled_jacobian = vector_field.jacobian(state)
coupled_trace = sp.simplify(sp.trace(coupled_jacobian))

current = sp.symbols("current")
extended_field = vector_field.col_join(sp.Matrix([2 * sp.sqrt(y) * f * m]))
extended_jacobian = extended_field.jacobian(state + [current])
extended_trace = sp.simplify(sp.trace(extended_jacobian))

forcing_gain = sp.symbols("forcing_gain")
hostile_field = vector_field.subs(
    -sp.Rational(1, 2) * m - z * n - f,
    -sp.Rational(1, 2) * m - z * n - forcing_gain * f,
)
hostile_trace = sp.simplify(sp.trace(hostile_field.jacobian(state)))
forcing_gain_trace_residual = sp.simplify(hostile_trace - coupled_trace)

# Feedback remains invisible to the tangent determinant but enters the
# spectral characteristic determinant through a closed-loop product.
alpha, gain, spectral = sp.symbols("alpha gain spectral")
feedback_generator = sp.Matrix(
    [
        [-sp.Rational(1, 2), -z, alpha],
        [-z, -sp.Rational(1, 2), 0],
        [gain, 0, 0],
    ]
)
feedback_trace = sp.simplify(sp.trace(feedback_generator))
feedback_characteristic = sp.factor(
    (spectral * sp.eye(3) - feedback_generator).det()
)
expected_characteristic = sp.factor(
    spectral
    * ((spectral + sp.Rational(1, 2)) ** 2 - z**2)
    - alpha * gain * (spectral + sp.Rational(1, 2))
)
feedback_characteristic_residual = sp.simplify(
    feedback_characteristic - expected_characteristic
)
feedback_divisor_effect = sp.simplify(
    feedback_characteristic.subs(alpha, 1)
    - feedback_characteristic.subs(alpha, 0)
)

# The Lorentz balance canonically supplies an open input-output colligation.
force = sp.symbols("force", real=True, nonzero=True)
source_input, direct = sp.symbols("source_input direct", nonzero=True)
tail_A = sp.Matrix(
    [
        [-sp.Rational(1, 2), -z],
        [-z, -sp.Rational(1, 2)],
    ]
)
lorentz_J = sp.diag(1, -1)
tail_B = sp.Matrix([-force, 0])
tail_C = -tail_B.T * lorentz_J
tail_v = sp.Matrix([m, n])
tail_q = (tail_v.T * lorentz_J * tail_v)[0]
tail_v_prime = tail_A * tail_v + tail_B * source_input
tail_q_prime = 2 * (tail_v.T * lorentz_J * tail_v_prime)[0]
tail_output = (tail_C * tail_v)[0]
supply_residual = sp.simplify(
    tail_q_prime + tail_q + 2 * source_input * tail_output
)

tail_resolvent = (spectral * sp.eye(2) - tail_A).inv()
transfer_schur = sp.factor(direct - (tail_C * tail_resolvent * tail_B)[0])
expected_transfer = sp.factor(
    direct
    + force**2
    * (spectral + sp.Rational(1, 2))
    / ((spectral + sp.Rational(1, 2)) ** 2 - z**2)
)
transfer_residual = sp.simplify(transfer_schur - expected_transfer)

bordered = (spectral * sp.eye(2) - tail_A).row_join(tail_B).col_join(
    tail_C.row_join(sp.Matrix([[direct]]))
)
bordered_determinant = sp.factor(bordered.det())
expected_bordered_determinant = sp.factor(
    direct * ((spectral + sp.Rational(1, 2)) ** 2 - z**2)
    + force**2 * (spectral + sp.Rational(1, 2))
)
bordered_determinant_residual = sp.simplify(
    bordered_determinant - expected_bordered_determinant
)

port_scale = sp.symbols("port_scale", nonzero=True)
scaled_transfer = sp.factor(
    direct
    - ((tail_C / port_scale) * tail_resolvent * (port_scale * tail_B))[0]
)
port_scale_residual = sp.simplify(scaled_transfer - transfer_schur)
reciprocal_transfer_residual = sp.simplify(
    transfer_schur.subs(z, -z) - transfer_schur
)

# Positive conservative completion has a rank-two defect.  Its minimal
# direct-output norm gives an exact port-count and slack criterion.
r = sp.symbols("r", real=True)
sigma_x = sp.Matrix([[0, 1], [1, 0]])
positive_defect = sp.eye(2) + 2 * r * sigma_x
positive_defect_determinant = sp.factor(positive_defect.det())
positive_defect_rank_generic = positive_defect.rank()
minimal_direct_norm_squared = sp.factor(
    (tail_B.T * positive_defect.inv() * tail_B)[0]
)
expected_minimal_direct_norm_squared = sp.factor(force**2 / (1 - 4 * r**2))
minimal_direct_norm_residual = sp.simplify(
    minimal_direct_norm_squared - expected_minimal_direct_norm_squared
)

# A scalar output row has Gram rank at most one and cannot realize the
# rank-two defect at any interior point.
c1, c2 = sp.symbols("c1 c2", real=True)
scalar_output_row = sp.Matrix([[c1, c2]])
scalar_output_gram = scalar_output_row.T * scalar_output_row
scalar_output_rank_bound = scalar_output_gram.rank()

assert flow_determinant_residual == 0
assert coupled_trace == 1 - 2 * sp.pi * y
assert extended_trace == coupled_trace
assert forcing_gain_trace_residual == 0
assert feedback_trace == -1
assert feedback_characteristic_residual == 0
assert feedback_divisor_effect == -gain * (spectral + sp.Rational(1, 2))
assert supply_residual == 0
assert transfer_residual == 0
assert bordered_determinant_residual == 0
assert port_scale_residual == 0
assert reciprocal_transfer_residual == 0
assert sp.simplify(positive_defect_determinant - (1 - 4 * r**2)) == 0
assert positive_defect_rank_generic == 2
assert minimal_direct_norm_residual == 0
assert scalar_output_rank_bound == 1

result = {
    "schema": "marici.rh-nonlinear-forcing-determinant.v1",
    "flow_determinant_residual": str(flow_determinant_residual),
    "flow_determinant": str(flow_determinant),
    "coupled_trace": str(coupled_trace),
    "extended_current_trace": str(extended_trace),
    "forcing_gain_trace_residual": str(forcing_gain_trace_residual),
    "feedback_trace": str(feedback_trace),
    "feedback_characteristic_residual": str(feedback_characteristic_residual),
    "unit_feedback_divisor_effect": str(feedback_divisor_effect),
    "lorentz_supply_residual": str(supply_residual),
    "transfer_schur_residual": str(transfer_residual),
    "bordered_determinant_residual": str(bordered_determinant_residual),
    "port_scale_residual": str(port_scale_residual),
    "reciprocal_transfer_residual": str(reciprocal_transfer_residual),
    "bordered_characteristic_determinant": str(bordered_determinant),
    "positive_defect_determinant": str(positive_defect_determinant),
    "positive_defect_rank_generic": positive_defect_rank_generic,
    "scalar_output_gram_rank_generic": scalar_output_rank_bound,
    "minimal_direct_norm_squared": str(minimal_direct_norm_squared),
    "positive_conservative_port_classification": {
        "one_output": "rank_obstruction",
        "two_outputs": "possible_only_when_force_squared_equals_1_minus_4r_squared",
        "three_outputs": "possible_with_output_slack_when_force_squared_is_less_than_1_minus_4r_squared",
        "extra_input_or_indefinite_completion": "required_when_force_squared_exceeds_1_minus_4r_squared",
    },
    "verdict": "source_open_loop_is_fixed_but_scalar_conservative_termination_is_rank_obstructed",
    "unresolved": [
        "source_direct_boundary_channel",
        "source_typing_of_positive_defect_outputs",
        "source_typing_of_slack_or_additional_input_reservoir",
        "composition_of_local_source_colligations",
        "completion_domain_of_transfer_colligation",
        "identification_with_characteristic_determinant_line",
        "source_varying_forcing_extension",
    ],
}

output = Path(__file__).parents[1] / "results" / "rh-nonlinear-forcing-determinant.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
