"""Exact kernel of all currently admitted source equalities acting on t."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp489 = load("wp489_common_source_threshold_constructor.json")
wp490 = load("wp490_dual_gauge_running_gate.json")
wp491 = load("wp491_yukawa_tensor_completeness_gate.json")
wp492 = load("wp492_canonical_messenger_tensor_grammar.json")
wp493 = load("wp493_radial_quartic_rg_closure.json")
wp494 = load("wp494_port_alignment_rg_closure.json")
wp495 = load("wp495_adjoint_gram_rg_closure.json")
wp498 = load("wp498_entrance_stabilizer_quartic_obstruction.json")
wp537 = load("wp537_fixed_v_selector_fiber.json")
wp538 = load("wp538_source_six_port_system_pencil.json")

# Logarithmic coefficient coordinates:
# x=(log a, log w, log g_F^2, log g_P^2).
# Fixed v gives log a+2 log w=constant.  WP490's gauge ray fixes
# log g_P^2-log g_F^2=constant.  Granting a separately frozen g_F adds the
# strongest currently contemplated normalization equality.
fixed_v_row = sp.Matrix([[1, 2, 0, 0]])
gauge_ray_row = sp.Matrix([[0, 0, -1, 1]])
fixed_gf_row = sp.Matrix([[0, 0, 1, 0]])
authorized_jacobian = sp.Matrix.vstack(fixed_v_row, gauge_ray_row, fixed_gf_row)

t_tangent = sp.Matrix([2, -1, 0, 0])
log_ratio_gradient = sp.Matrix([[-sp.Rational(1, 2), 0, sp.Rational(1, 2), 0]])
ratio_tangent = (log_ratio_gradient * t_tangent)[0]

# Without granting the extra g_F normalization, the admitted source equality
# kernel is even larger.
minimal_jacobian = sp.Matrix.vstack(fixed_v_row, gauge_ray_row)

# A readout row detects t but cannot be added to the source constraint
# Jacobian without circularly converting measurement into selection.
readout_augmented = sp.Matrix.vstack(authorized_jacobian, log_ratio_gradient)

dependency_packets = (
    wp489,
    wp490,
    wp491,
    wp492,
    wp493,
    wp494,
    wp495,
    wp498,
    wp537,
    wp538,
)

checks = {
    "dependencies_passed": all(bool(packet["passed"]) for packet in dependency_packets),
    "minimal_source_equalities_have_rank_two": minimal_jacobian.rank() == 2,
    "strongest_existing_equalities_have_rank_three": authorized_jacobian.rank() == 3,
    "strongest_existing_kernel_is_one_dimensional": 4 - authorized_jacobian.rank() == 1,
    "t_tangent_preserves_every_source_equality": authorized_jacobian * t_tangent == sp.zeros(3, 1),
    "t_tangent_changes_the_clock_ratio": ratio_tangent == -1,
    "t_tangent_spans_the_strongest_kernel": (
        len(authorized_jacobian.nullspace()) == 1
        and sp.Matrix.hstack(t_tangent, authorized_jacobian.nullspace()[0]).rank() == 1
    ),
    "readout_row_would_remove_t_only_by_projection_authority": readout_augmented.rank() == 4,
    "gauge_running_has_no_finite_nonzero_fixed_point": "no finite gauge-coupling selector" in wp490["selector"],
    "yukawa_beta_vector_field_is_not_typed": "not yet typed" in wp491["classification"],
    "tensor_shapes_leave_ten_free_scalar_coordinates": "ten real" in wp492["authority_partition"]["free_scalars"],
    "rg_closure_adds_three_radial_coordinates": len(wp493["one_loop_generated_support"]["missing_invariants"]) == 3,
    "port_alignment_adds_an_independent_coordinate": "independent" in wp494["classification"],
    "adjoint_gram_adds_an_independent_coordinate": "independent" in wp495["new_compulsory_invariant"],
    "entrance_stabilizer_has_three_missing_coordinates": wp498["missing_o2_codimension"] == 3,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP543",
    "domain": "All equality authority currently admitted by WP489-WP498 that can act on the fixed-v clock coordinates, plus the strongest separately frozen g_F normalization considered by the instrument programme.",
    "log_coordinate_order": ["log a", "log w", "log g_F^2", "log g_P^2"],
    "authorized_equalities": {
        "fixed_v_row": [str(value) for value in fixed_v_row],
        "dual_gauge_ray_row": [str(value) for value in gauge_ray_row],
        "fixed_g_F_row": [str(value) for value in fixed_gf_row],
        "jacobian": [[str(value) for value in row] for row in authorized_jacobian.tolist()],
        "rank": authorized_jacobian.rank(),
        "kernel_dimension": 4 - authorized_jacobian.rank(),
    },
    "selector_kernel": {
        "t_tangent": [str(value) for value in t_tangent],
        "source_constraint_residual": [str(value) for value in authorized_jacobian * t_tangent],
        "log_clock_ratio_gradient": [str(value) for value in log_ratio_gradient],
        "log_clock_ratio_tangent": str(ratio_tangent),
        "meaning": "The unique surviving source-equality direction is exactly the fixed-v WP537 t fiber, and it changes g_F f_phys/v.",
    },
    "rg_authority_audit": {
        "gauge": "WP490 fixes only a coupling-ratio ray and has no finite nonzero one-loop fixed point.",
        "yukawa": "WP491 proves the beta vector field is not typed; WP492 freezes shapes but leaves ten scalar normalizations.",
        "quartics": "WP493-WP495 and WP498 add compulsory independent running coordinates. Support closure is not a beta-zero equation and cannot fix t.",
        "thresholds": "WP537 exhibits two strict width-closed points along t, so open threshold inequalities do not collapse the fiber.",
        "readout": "WP538 detects the t direction, but adding its readout gradient as a source equation would be circular projection authority.",
    },
    "theorem": "Even after granting fixed v, the WP490 gauge ray, and an independent fixed g_F normalization, the complete currently authorized equality Jacobian has a one-dimensional kernel spanned by the WP537 t tangent. That tangent changes log(g_F f_phys/v) by minus one. Existing RG work adds coordinates and closure requirements but supplies no independent beta-zero equation that removes this kernel.",
    "classification": "Exact negative selector-authority certificate for the current source grammar. The flavor source conditionally selects relational outputs at fixed coefficients, but no admitted equation numerically selects t or g_F f_phys/v.",
    "smallest_exact_falsifier": "The tangent (2,-1,0,0) annihilates fixed-v, gauge-ray and fixed-g_F rows exactly, while its clock-ratio derivative is -1.",
    "remaining_gate": "Complete the independently frozen tensor and quartic grammar, derive the full scheme-declared beta vector field and threshold maps, and exhibit a stable source-derived equation with nonzero contraction against the t tangent. A clock-ratio readout cannot supply that equation.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp543_existing_source_constraint_kernel.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
