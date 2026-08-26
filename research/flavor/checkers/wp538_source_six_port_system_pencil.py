"""Exact source-to-six-port system pencil and compression ranks."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp520 = load("wp520_finite_propagator_bs_kernel.json")
wp522 = load("wp522_six_resolvent_bilocal_basis.json")
wp534 = load("wp534_invariant_complex_pole_packet.json")
wp535 = load("wp535_six_port_bilocal_instrument.json")
wp537 = load("wp537_fixed_v_selector_fiber.json")

z, t = sp.symbols("z t", positive=True)
kernel = sp.sympify(
    wp520["aligned_bs_kernel"]["exact_witness_rational_function"],
    locals={"z": z},
)
numerator, denominator = [sp.expand(x) for x in sp.fraction(kernel)]
leading = sp.LC(sp.Poly(denominator, z))
monic_denominator = sp.expand(denominator / leading)
coefficients = sp.Poly(monic_denominator, z).all_coeffs()
degree = sp.degree(monic_denominator, z)

# Controllable companion realization.  With B=e_6,
# (zI-A)^(-1)B=(1,z,...,z^5)^T/D(z).
A = sp.zeros(degree)
for i in range(degree - 1):
    A[i, i + 1] = 1
for j, coefficient in enumerate(reversed(coefficients[1:])):
    A[degree - 1, j] = -coefficient
B = sp.zeros(degree, 1)
B[degree - 1, 0] = 1
C = sp.zeros(1, degree)
C[0, 0] = sp.simplify(numerator / leading)

resolvent_transfer = sp.factor((C * (z * sp.eye(degree) - A).inv() * B)[0])
controllability = sp.Matrix.hstack(*[(A**k) * B for k in range(degree)])
observability = sp.Matrix.vstack(*[C * (A**k) for k in range(degree)])

# Scaling along WP537: all pole mass squares scale as t^-2 while the system
# degree and source/current grammar remain unchanged.
scaled_denominator = sp.factor(monic_denominator.subs(z, t**2 * z) / t ** (2 * degree))
scaled_coefficients = sp.Matrix(sp.Poly(scaled_denominator, z).all_coeffs()[1:])
coefficient_tangent = sp.diff(scaled_coefficients, t)
coefficient_tangent_at_one = coefficient_tangent.subs(t, 1)
ratio = sp.sqrt(3) / t
scaled_scalar_transfer = sp.factor(t**2 * kernel.subs(z, t**2 * z))
t_scalar_tangent_at_zero = sp.factor(
    sp.diff(scaled_scalar_transfer, t).subs({t: 1, z: 0})
)

# The six pole coordinates are the identity output on the companion state.
# One instantaneous scalar command is a line; the source-generated Krylov
# context tower is the controllability matrix.
pointwise_source_map = B
six_port_output = sp.eye(degree)
delta_m_output = C
hostile_state = sp.zeros(degree, 1)
hostile_state[1, 0] = 1

denominator_gcd = sp.gcd(sp.Poly(numerator, z), sp.Poly(denominator, z))
denominator_discriminant = sp.factor(sp.discriminant(denominator, z))

checks = {
    "dependencies_passed": all(
        bool(packet["passed"])
        for packet in (wp520, wp522, wp534, wp535, wp537)
    ),
    "pencil_has_six_states": degree == 6 and A.shape == (6, 6),
    "real_denominator_is_squarefree": denominator_discriminant != 0,
    "constant_numerator_is_coprime_to_denominator": denominator_gcd.degree() == 0,
    "companion_transfer_reconstructs_wp520": sp.simplify(resolvent_transfer - kernel) == 0,
    "single_source_command_is_pointwise_rank_one": pointwise_source_map.rank() == 1,
    "six_port_state_readout_has_rank_six": six_port_output.rank() == 6,
    "six_source_generated_contexts_are_jointly_rank_six": controllability.rank() == 6,
    "frozen_scalar_kernel_is_observable_as_degree_six": observability.rank() == 6,
    "delta_m_compression_is_rank_one": delta_m_output.rank() == 1,
    "delta_m_kernel_has_dimension_five": degree - delta_m_output.rank() == 5,
    "nonzero_six_port_state_collapses_in_delta_m": (
        hostile_state != sp.zeros(degree, 1)
        and delta_m_output * hostile_state == sp.zeros(1, 1)
        and six_port_output * hostile_state != sp.zeros(degree, 1)
    ),
    "fixed_v_source_fiber_moves_the_pencil": coefficient_tangent_at_one != sp.zeros(degree, 1),
    "fixed_v_source_fiber_is_one_dimensional": coefficient_tangent_at_one.rank() == 1,
    "same_fiber_moves_the_target_ratio": sp.diff(ratio, t).subs(t, 1) != 0,
    "formal_scalar_current_does_not_kill_t_at_zero_momentum": (
        t_scalar_tangent_at_zero == 2 * kernel.subs(z, 0)
        and t_scalar_tangent_at_zero != 0
    ),
    "complex_width_completion_preserves_pencil_dimension": len(wp534["signed_bs_pole_residues"]) == degree,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP538",
    "domain": "WP520's exact six-pole b-s kernel, WP534's Ward-complete complex-width continuation, WP535's six-port contract, and the fixed-v WP537 source fiber.",
    "system_pencil": {
        "rule": "P(z)=z I_6-A, x=P(z)^(-1) B u, y_6=I_6 x, DeltaM channel=C x",
        "state_dimension": int(degree),
        "input_dimension": 1,
        "six_port_output_dimension": int(degree),
        "normalized_denominator": str(monic_denominator),
        "source_vector": [str(value) for value in B],
        "scalar_output_vector": [str(value) for value in C],
        "controllability_determinant": str(sp.factor(controllability.det())),
        "observability_determinant": str(sp.factor(observability.det())),
        "denominator_discriminant": str(denominator_discriminant),
    },
    "rank_factorization": {
        "instantaneous_source_to_state_rank": int(pointwise_source_map.rank()),
        "six_context_source_closure_rank": int(controllability.rank()),
        "six_port_state_readout_rank": int(six_port_output.rank()),
        "scalar_DeltaM_output_rank": int(delta_m_output.rank()),
        "scalar_DeltaM_kernel_dimension": int(degree - delta_m_output.rank()),
        "hostile_kernel_state": [str(value) for value in hostile_state],
        "interpretation": "The first rank-one arrow is the instantaneous scalar source command. Six algebraic source-generated Krylov contexts restore joint state faithfulness. DeltaM then introduces a separate five-dimensional output kernel.",
    },
    "fixed_v_source_fiber": {
        "rule": "a=t^2, w=1/t, v^2=2, g_F f_phys/v=sqrt(3)/t",
        "pencil_coefficient_tangent_at_t_1": [str(value) for value in coefficient_tangent_at_one],
        "tangent_rank": int(coefficient_tangent_at_one.rank()),
        "ratio_derivative_at_t_1": str(sp.diff(ratio, t).subs(t, 1)),
        "formal_scalar_kernel_tangent_at_zero": str(t_scalar_tangent_at_zero),
        "t_direction_in_formal_scalar_kernel": bool(t_scalar_tangent_at_zero == 0),
        "physical_DeltaM_survival": "unproved until the calibrated bilocal hadronic functional is supplied",
        "instrument_class_changed": bool(degree != 6),
    },
    "theorem": "The frozen Ward-complete kernel has an exact minimal degree-six source system pencil. One instantaneous source command reaches only a line, while the six source-generated Krylov contexts are jointly rank six. The six-port state readout is faithful, but scalar DeltaM compression has rank one and a five-dimensional kernel. Along WP537's fixed-v source fiber the pencil and target ratio move with one source parameter without changing the six-port instrument class. The formal zero-momentum scalar current does not kill the t direction, although survival through the uncalibrated hadronic DeltaM functional is not established.",
    "classification": "Source dynamics supplies a one-dimensional moving family, the contextual pencil is algebraically jointly faithful, and the proposed six-port readout is separating. None of these facts numerically selects t or realizes the contexts as calibrated physical operations.",
    "smallest_exact_falsifier": "At t=1 the normalized denominator-coefficient tangent is nonzero and rank one, while d(sqrt(3)/t)/dt=-sqrt(3); the source fiber moves both the pole pencil and target ratio inside the same six-state instrument class.",
    "remaining_instrument_gate": "Show that six independent Krylov or equivalent resolvent contexts are executable source-derived lattice preparations with one renormalized 48-real covariance. Algebraic controllability alone is not experimental control.",
    "remaining_selector_gate": "Derive an independent source equation that fixes t before using any clock-ratio or pole readout, then recompute the complex pencil and calibrated likelihood at that selected point.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp538_source_six_port_system_pencil.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
