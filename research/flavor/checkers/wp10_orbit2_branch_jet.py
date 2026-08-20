"""Exact kernel-to-cokernel quadratic jet at the orbit-2 rank-drop locus."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
packet = json.loads(
    (RESULTS / "wp10_phase_aware_invariant_jacobians.json").read_text())
record = next(
    r for r in packet["records"]
    if r["orientation"] == "original" and r["orbit"] == 2)

m = sp.symbols("m0:9", positive=True)
l = sp.symbols("l0:9", real=True)
phi = sp.symbols("phi", real=True)
c, s = sp.symbols("c s", real=True)
coords = [
    sp.sympify(expr, locals={
        **{f"m{i}": m[i] for i in range(9)}, "c": c, "s": s})
    for expr in record["coordinates"]
]
coords = [
    expr.subs({c: sp.cos(phi), s: sp.sin(phi)})
        .subs({m[i]: sp.exp(l[i]) for i in range(9)})
    for expr in coords
]
x = list(l)+[phi]
origin = {value: 0 for value in x}
jac = sp.Matrix([[sp.diff(expr, value).subs(origin)
                  for value in x] for expr in coords])
kernel = sp.Matrix.hstack(*jac.nullspace())
cokernel = sp.Matrix.hstack(*jac.T.nullspace())

assert jac.rank() == 9
assert kernel.cols == 1 and cokernel.cols == 1
# Follow the intrinsic null direction and project to the intrinsic cokernel.
# The first nonzero derivative classifies the one-variable transverse jet.
t = sp.symbols("t", real=True)
curve = {x[i]: t*kernel[i, 0] for i in range(10)}
left = cokernel[:, 0]
scalar = sp.simplify(sum(
    left[i]*coords[i].subs(curve) for i in range(10)))
jet = {
    order: sp.factor(
        sp.diff(scalar, t, order).subs(t, 0)/sp.factorial(order))
    for order in range(2, 7)
}
leading_order = next(order for order, value in jet.items() if value != 0)

# Exact Lyapunov--Schmidt reduction.  Remove one domain coordinate along
# which the null vector is nonzero, retain the other coordinate axes as a
# regular complement, and select nine independent output rows.  Solve those
# nine range equations recursively as formal series in the null coordinate.
drop_col = next(i for i in range(10) if kernel[i, 0] != 0)
keep_cols = [i for i in range(10) if i != drop_col]
complement = sp.zeros(10, 9)
for j, i in enumerate(keep_cols):
    complement[i, j] = 1
regular_jac = jac*complement
pivot_rows = list(regular_jac.T.rref()[1])
assert len(pivot_rows) == 9
minor = regular_jac.extract(pivot_rows, range(9))
assert minor.det() != 0

center_values = [expr.subs(origin) for expr in coords]
y_series = sp.zeros(9, 1)
range_coefficients = {}
for order in range(2, 7):
    parameter_curve = sp.Matrix(x)
    displacement = kernel[:, 0]*t+complement*y_series
    substitutions = {
        x[i]: displacement[i] for i in range(10)
    }
    known = sp.Matrix([
        sp.expand(coords[row].subs(substitutions)-center_values[row])
            .series(t, 0, order+1).removeO().coeff(t, order)
        for row in pivot_rows
    ])
    correction = sp.simplify(-minor.inv()*known)
    range_coefficients[str(order)] = [str(value) for value in correction]
    y_series += correction*t**order

reduced_substitutions = {
    x[i]: (kernel[:, 0]*t+complement*y_series)[i]
    for i in range(10)
}
reduced_scalar = sp.expand(sum(
    left[i]*(coords[i].subs(reduced_substitutions)-center_values[i])
    for i in range(10))).series(t, 0, 7).removeO()
reduced_jet = {
    order: sp.factor(reduced_scalar.coeff(t, order))
    for order in range(2, 7)
}
reduced_leading_order = next(
    (order for order, value in reduced_jet.items() if value != 0), None)

# The vanishing reduced germ has an exact explanation.  On phi=0 the
# balanced central invariants admit a positive one-parameter fiber.
r = sp.symbols("r", positive=True)
fiber_magnitudes = {
    m[0]: 1, m[1]: 1, m[2]: 1,
    m[3]: r,
    m[4]: sp.sqrt(2-r**2),
    m[5]: 1/r,
    m[6]: sp.sqrt(2-r**-2),
    m[7]: 1/r,
    m[8]: sp.sqrt(2-r**-2),
    c: 1, s: 0,
}
fiber_invariants = [
    sp.simplify(
        sp.sympify(expr, locals={
            **{f"m{i}": m[i] for i in range(9)}, "c": c, "s": s})
        .subs(fiber_magnitudes))
    for expr in record["coordinates"]
]
central_invariants = [
    sp.simplify(
        sp.sympify(expr, locals={
            **{f"m{i}": m[i] for i in range(9)}, "c": c, "s": s})
        .subs({**{value: 1 for value in m}, c: 1, s: 0}))
    for expr in record["coordinates"]
]
assert all(sp.simplify(a-b) == 0
           for a, b in zip(fiber_invariants, central_invariants))

out = {
    "schema": "marici.flavor.orbit2_branch_jet.v1",
    "status": "exact_collapsed_positive_fiber",
    "jacobian_rank": jac.rank(),
    "kernel_dimension": kernel.cols,
    "cokernel_dimension": cokernel.cols,
    "kernel_basis": [[str(v) for v in kernel.col(j)]
                     for j in range(kernel.cols)],
    "cokernel_basis": [[str(v) for v in cokernel.col(j)]
                       for j in range(cokernel.cols)],
    "cokernel_projected_null_jet": {
        str(order): str(value) for order, value in jet.items()},
    "leading_null_order": leading_order,
    "straight_null_interpretation":
        "quartic straight-null jet is superseded by the exact Lyapunov-Schmidt and collapsed-fiber calculation",
    "lyapunov_schmidt": {
        "dropped_domain_coordinate": drop_col,
        "regular_output_rows": pivot_rows,
        "range_series_coefficients": range_coefficients,
        "reduced_cokernel_jet": {
            str(order): str(value)
            for order, value in reduced_jet.items()},
        "leading_reduced_order": reduced_leading_order,
    },
    "exact_collapsed_fiber": {
        "parameter_domain": "1/sqrt(2) < r < sqrt(2)",
        "magnitudes_m3_to_m8": [
            "r", "sqrt(2-r^2)", "1/r", "sqrt(2-r^(-2))",
            "1/r", "sqrt(2-r^(-2))"],
        "phase": "0",
        "all_ten_invariants_constant": True,
        "interpretation":
            "positive one-dimensional fiber collapsed by the invariant map; not a finite branched cover",
    },
}
(RESULTS / "wp10_orbit2_branch_jet.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))
