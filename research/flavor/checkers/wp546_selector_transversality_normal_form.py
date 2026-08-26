"""Exact transversality normal form for the surviving flavor selector fiber."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp537 = load("wp537_fixed_v_selector_fiber.json")
wp543 = load("wp543_existing_source_constraint_kernel.json")
wp544 = load("wp544_typed_source_instrument_pencil.json")
wp545 = load("wp545_rg_completion_debt.json")

J = sp.Matrix([[sp.sympify(x) for x in row] for row in wp543["authorized_equalities"]["jacobian"]])
k = sp.Matrix([sp.sympify(x) for x in wp543["selector_kernel"]["t_tangent"]])
la, lw, lg, lp = sp.symbols("ell_a ell_w ell_g ell_p")
ell = sp.Matrix([[la, lw, lg, lp]])
augmented = J.col_join(ell)
transverse_contraction = sp.factor((ell * k)[0])
augmented_determinant = sp.factor(augmented.det())

fixed_v_covector = sp.Matrix([[1, 2, 0, 0]])
clock_readout_covector = sp.Matrix(
    [[sp.sympify(x) for x in wp543["selector_kernel"]["log_clock_ratio_gradient"]]]
)
example_source_covector = sp.Matrix([[1, 0, 0, 0]])

left, right = wp537["hostile_pair"]
left_masses = [sp.sympify(x) for x in left["vector_mass_squares"]]
right_masses = [sp.sympify(x) for x in right["vector_mass_squares"]]
mass_square_ratios = [sp.simplify(x / y) for x, y in zip(left_masses, right_masses)]

checks = {
    "dependencies_passed": all(bool(packet["passed"]) for packet in (wp537, wp543, wp544, wp545)),
    "current_kernel_is_exactly_one_dimensional": J.rank() == 3 and len(J.nullspace()) == 1,
    "declared_tangent_spans_kernel": J * k == sp.zeros(3, 1),
    "augmented_determinant_equals_transverse_contraction": sp.simplify(
        augmented_determinant - transverse_contraction
    )
    == 0,
    "rank_four_exactly_when_new_row_is_transverse": transverse_contraction == 2 * la - lw,
    "fixed_v_equation_is_tangent_blind": (fixed_v_covector * k)[0] == 0,
    "example_source_equation_would_be_transverse": (example_source_covector * k)[0] == 2,
    "clock_readout_is_algebraically_transverse": (clock_readout_covector * k)[0] == -1,
    "clock_readout_is_not_source_authority": "circular projection authority"
    in wp543["rg_authority_audit"]["readout"],
    "completion_debt_precedes_rg_authority": wp545["conservative_unresolved_coordinate_count"] == 18,
    "instrument_controls_remain_external": wp544["external_control_registry"]["dimension"] == 29,
    "hostile_pair_changes_every_vector_mass_square": all(ratio == 4 for ratio in mass_square_ratios),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP546",
    "domain": "The WP543 log-coordinate source quotient, augmented by one proposed source-derived equality after the WP545 RG-completion gate.",
    "coordinate_order": list(wp543["log_coordinate_order"]),
    "existing_jacobian": [[str(x) for x in row] for row in J.tolist()],
    "surviving_tangent": [str(x) for x in k],
    "candidate_gradient": ["ell_a", "ell_w", "ell_g", "ell_p"],
    "transverse_contraction": str(transverse_contraction),
    "augmented_determinant": str(augmented_determinant),
    "exact_acceptance_condition": "2*ell_a-ell_w != 0",
    "typing_split": {
        "source_candidate": "A complete scheme-declared beta-zero, invariant-manifold, or threshold equation derived independently from the flavor action.",
        "readout_candidate": "The clock-ratio gradient is transverse but cannot be promoted to a source equation.",
        "instrument_candidate": "WP544 external controls can measure the selected realization but are not coordinates of the source vector field.",
    },
    "post_selection_recomputation": {
        "hostile_pair_vector_mass_square_ratios": [str(x) for x in mass_square_ratios],
        "rule": "After a source equation selects t, recompute the vacuum, complex poles, residues, every open partial width, total widths, and the WP535 response in that selected packet. Existing benchmark widths or residues cannot be transported.",
        "independent_freeze_gate": "Widths and residues acquire evidence authority only from the recomputed complete channel packet and its separately typed instrument calibration.",
    },
    "theorem": "For the strongest admitted source Jacobian, one additional differentiable source equality removes the surviving t fiber exactly when 2 ell_a-ell_w is nonzero. This algebraic criterion is necessary and sufficient locally, but it grants no authority to the measured clock-ratio row or external instrument controls.",
    "classification": "Exact selector transversality acceptance theorem. It identifies the missing orientation but does not supply the source equation or select a numerical value.",
    "smallest_exact_falsifier": "Any candidate with ell_w=2 ell_a is tangent to the fixed-v fiber and leaves rank three; the fixed-v row itself is the primitive example.",
    "remaining_gate": "Complete the WP545 source action and derive an independently normalized stable beta or threshold equation satisfying 2 ell_a-ell_w != 0, then recompute and independently freeze poles, residues, widths, and instrument response at its selected solution.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp546_selector_transversality_normal_form.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
