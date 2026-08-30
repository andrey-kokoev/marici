"""Exact WP607 same-family Gaussian no-go and typed bipartite escape."""

import json
from pathlib import Path

import sympy as sp


a, clockwise, counterclockwise = sp.symbols("a b c", real=True)

cyclic_kernel = sp.Matrix(
    [
        [a, clockwise, counterclockwise],
        [counterclockwise, a, clockwise],
        [clockwise, counterclockwise, a],
    ]
)
cycle = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
reflection = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])

cyclic_residual = sp.simplify(cycle.T * cyclic_kernel * cycle - cyclic_kernel)
reciprocity_residual = sp.simplify(cyclic_kernel - cyclic_kernel.T)
reflection_residual = sp.simplify(
    reflection.T * cyclic_kernel * reflection - cyclic_kernel
)

# A completely general reciprocal Gaussian mediator elimination.
h11, h12, h22 = sp.symbols("h11 h12 h22", real=True)
g11, g12, g13, g21, g22, g23 = sp.symbols(
    "g11 g12 g13 g21 g22 g23", real=True
)
heavy_hessian = sp.Matrix([[h11, h12], [h12, h22]])
coupling = sp.Matrix([[g11, g12, g13], [g21, g22, g23]])
schur_kernel = sp.simplify(-coupling.T * heavy_hessian.inv() * coupling)

# The smallest directed cyclic target has unequal two orientations.
directed_target = cyclic_kernel.subs({a: 0, clockwise: 1, counterclockwise: 0})
directed_reflection_residual = sp.simplify(
    reflection.T * directed_target * reflection - directed_target
)

# A reciprocal full kernel may have a directed cross-block between two
# inequivalent channel families; the reverse block is its transpose.
zero_block = sp.zeros(3)
bipartite_kernel = zero_block.row_join(directed_target).col_join(
    directed_target.T.row_join(zero_block)
)
bipartite_cycle = sp.diag(cycle, cycle)

# A non-Gaussian cyclic vertex escapes the quadratic no-go.
x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
oriented_cubic = x1 * x2**2 + x2 * x3**2 + x3 * x1**2
cyclic_cubic = sp.expand(
    oriented_cubic.subs({x1: x2, x2: x3, x3: x1}, simultaneous=True)
    - oriented_cubic
)
reflected_cubic = sp.expand(
    oriented_cubic.subs({x2: x3, x3: x2}, simultaneous=True)
    - oriented_cubic
)
reflection_witness = reflected_cubic.subs({x1: 1, x2: 2, x3: 3})

checks = {
    "general_circulant_kernel_is_c3_invariant": cyclic_residual == sp.zeros(3),
    "reciprocity_forces_clockwise_equal_counterclockwise": reciprocity_residual.subs(
        counterclockwise, clockwise
    )
    == sp.zeros(3),
    "reciprocal_c3_kernel_is_reflection_invariant": reflection_residual.subs(
        counterclockwise, clockwise
    )
    == sp.zeros(3),
    "gaussian_schur_kernel_is_always_symmetric": sp.simplify(
        schur_kernel - schur_kernel.T
    )
    == sp.zeros(3),
    "directed_target_breaks_reciprocity": directed_target != directed_target.T,
    "directed_target_breaks_reflection": directed_reflection_residual
    != sp.zeros(3),
    "typed_bipartite_completion_is_reciprocal": bipartite_kernel
    == bipartite_kernel.T,
    "typed_bipartite_completion_is_c3_invariant": sp.simplify(
        bipartite_cycle.T * bipartite_kernel * bipartite_cycle
        - bipartite_kernel
    )
    == sp.zeros(6),
    "typed_cross_block_retains_orientation": bipartite_kernel[:3, 3:]
    != bipartite_kernel[3:, :3],
    "oriented_cubic_is_c3_invariant": cyclic_cubic == 0,
    "oriented_cubic_breaks_reflection": reflected_cubic != 0
    and reflection_witness == -2,
}

if not all(checks.values()):
    raise SystemExit(f"WP607 check failed: {checks}")

result = {
    "work_package": "WP607",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "admitted_source_family": "one three-channel operator family coupled linearly to any finite reciprocal Gaussian mediator sector with a real symmetric invertible Hessian",
    "effective_kernel": "C=-G^T H^-1 G",
    "exact_obstruction": "the same-family kernel C is symmetric; for a three-channel C3-circulant kernel this forces clockwise and counterclockwise coefficients equal and restores reflection",
    "smallest_exact_falsifier": "the C3-circulant target with clockwise coefficient 1 and counterclockwise coefficient 0 is nonsymmetric and cannot be a reciprocal Gaussian Schur complement",
    "smallest_gaussian_escape": "two inequivalent C3 channel families A and B with full reciprocal block kernel [[0,K],[K^T,0]]; K may be directed",
    "surviving_source_class": "a typed bipartite Gaussian cross-family constructor or a non-Gaussian cyclic vertex",
    "probe_disposition": "untyped masses and total widths cannot certify orientation; the experiment must resolve A-to-B clockwise and counterclockwise cross channels separately",
    "remaining_physical_instrument_gate": "derive inequivalent physical channel families, their directed cross-block and calibrated reversal difference, together with weak-basis-invariant physical16 matching",
    "classification": "negative theorem for same-family reciprocal Gaussian mediation with an exact typed bipartite escape",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp607_reciprocal_gaussian_orientation_no_go.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
