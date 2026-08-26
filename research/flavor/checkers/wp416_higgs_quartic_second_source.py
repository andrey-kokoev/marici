"""Exact two-source Higgs response audit for WP416."""

import json
from pathlib import Path

import sympy as sp


phi, h = sp.symbols("phi h", real=True)
mu2, lam, v0 = sp.symbols("mu2 lambda v0", positive=True, real=True)
dc, dl = sp.symbols("delta_c delta_lambda", real=True)
d_h, d_j = sp.symbols("Delta_H Delta_J", real=True)
w_h, w_j = sp.symbols("w_H w_J", positive=True)

potential = (-mu2 + dc) * phi**2 / 2 + (lam + dl) * phi**4 / 4
expanded = sp.expand(potential.subs(phi, v0 + h))
vacuum_shell = {lam * v0**2: mu2}

tadpole = sp.factor(sp.diff(expanded, h).subs(h, 0).subs(vacuum_shell))
curvature = sp.factor(sp.diff(expanded, h, 2).subs(h, 0).subs(vacuum_shell))
response = sp.Matrix([curvature, tadpole]).jacobian([dc, dl])
wedge = sp.factor(response.det())
weighted_gram_det = sp.factor((response.T * sp.diag(w_h, w_j) * response).det())

inverse_reconstruction = sp.simplify(response.inv() * sp.Matrix([d_h, d_j]))

# At the equilibrium belonging to either deformed potential, its own first
# derivative vanishes.  The two readouts therefore remain relational to v0.
equilibrium_squared = sp.factor((mu2 - dc) / (lam + dl))
equilibrium = sp.sqrt(equilibrium_squared)
equilibrium_tadpole = sp.simplify(sp.diff(potential, phi).subs(phi, equilibrium))
expected_inverse = sp.Matrix(
    [-d_h / 2 + 3 * d_j / (2 * v0), (d_h * v0 - d_j) / (2 * v0**3)]
)

checks = {
    "quadratic_and_quartic_operators_are_center_even": sp.expand(potential.subs(phi, -phi) - potential) == 0,
    "relative_curvature_has_expected_two_source_form": curvature == dc + 3 * dl * v0**2 + 2 * mu2,
    "relative_tadpole_has_expected_two_source_form": tadpole == v0 * (dc + dl * v0**2),
    "response_wedge_is_nonzero_in_broken_phase": wedge == -2 * v0**3,
    "positive_weighted_gram_is_nonzero": weighted_gram_det == 4 * v0**6 * w_h * w_j,
    "source_errors_are_exactly_reconstructible": all(
        sp.simplify(x) == 0 for x in inverse_reconstruction - expected_inverse
    ),
    "recentering_removes_tadpole": equilibrium_tadpole == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP416",
    "title": "Higgs quartic second-source gate",
    "source_operators": ["delta_c times H-dagger-H", "delta_lambda times (H-dagger-H)^2"],
    "fixed_reference_readouts": {
        "curvature": str(curvature),
        "relative_tadpole": str(tadpole),
    },
    "response_jacobian": [[str(x) for x in row] for row in response.tolist()],
    "response_wedge": str(wedge),
    "weighted_gram_determinant": str(weighted_gram_det),
    "inverse_source_reconstruction": {
        "delta_c": str(inverse_reconstruction[0]),
        "delta_lambda": str(inverse_reconstruction[1]),
    },
    "classification": "source-derived and weak-basis-independent rank-two relational response; executable quartic control and instrument remain absent",
    "smallest_exact_falsifier": "v0 = 0, where the broken-phase reference and response wedge collapse",
    "remaining_gate": "independently vary the physical Higgs quartic while retaining and reading the same broken-vacuum reference",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp416_higgs_quartic_second_source.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
