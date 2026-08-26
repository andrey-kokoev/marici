import json
import sympy as sp


a, b, c, d = sp.symbols("a b c d")
g, gp, h, hp = sp.symbols("g gp h hp", nonzero=True)
r = sp.Matrix([[1, 0]])
e2 = sp.Matrix([0, 1])
A = sp.Matrix([[a, b], [c, d]])
Sg = sp.Matrix([[g, 0], [gp, g]])
Sh = sp.Matrix([[h, 0], [hp, h]])
swap = sp.Matrix([[0, 1], [1, 0]])

checks = {
    "propagation_obstruction_is_upper_right_entry": sp.simplify((r * A * e2)[0] - b) == 0,
    "propagation_forces_lower_triangular": sp.solve([b], [b]) == {b: 0},
    "euler_jet_preserves_zero_sieve": r * Sg * e2 == sp.zeros(1, 1),
    "archimedean_jet_preserves_zero_sieve": r * Sh * e2 == sp.zeros(1, 1),
    "cutoff_composition_preserves_zero_sieve": r * Sg * Sh * e2 == sp.zeros(1, 1),
    "future_rows_remain_collinear": sp.Matrix.vstack(r, r * Sg, r * Sg * Sh).rank() == 1,
    "joint_kernel_contains_flux_line": all(
        row == sp.zeros(1, 1) for row in (r * e2, r * Sg * e2, r * Sg * Sh * e2)
    ),
    "internal_swap_falsifies_propagation": (r * swap * e2)[0] == 1,
}

result = {
    "schema": "marici.grothendieck.zero_propagation_joint_faithfulness_no_go.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "theorem": "For r=(1,0), universal ker(r)-invariance forces A_12=0; all generated future rows remain proportional to r, so they cannot be jointly faithful in dimension two.",
    "typed_reciprocal_verdict": "A sewing comparison may preserve zero covariantly between sectors, but then it is not an intra-sector observing arrow. An internal coordinate swap observes the flux line and violates propagation.",
}

print(json.dumps(result, indent=2, sort_keys=True))
