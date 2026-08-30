"""Exact WP445 flavor-current mass and Wilson kernels."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp443 = json.loads((root / "results" / "wp443_fundamental_flavon_completion.json").read_text(encoding="utf-8"))
I = sp.I
g_f, f = sp.symbols("g_F f", positive=True, real=True)
lambdas = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2)/sp.sqrt(3),
]
generators = [matrix/2 for matrix in lambdas]
A0 = f*lambdas[2]/sp.sqrt(8)
D0 = f*lambdas[0]/sp.sqrt(8)
phi0 = f*sp.Matrix([0, 0, 1/sp.sqrt(2)])

K = sp.Matrix(8, 8, lambda i, j: sp.simplify(
    sp.trace((generators[i]*A0-A0*generators[i]).conjugate().T*(generators[j]*A0-A0*generators[j]))
    + sp.trace((generators[i]*D0-D0*generators[i]).conjugate().T*(generators[j]*D0-D0*generators[j]))
    + (phi0.conjugate().T*(generators[i]*generators[j]+generators[j]*generators[i])*phi0)[0]
)/f**2)
K_inverse = K.inv()
mass_squared = g_f**2*f**2*K
wilson_kernel = sp.simplify(g_f**2*mass_squared.inv())

expected_K = sp.diag(sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(1, 4),
                     sp.Rational(3, 8), sp.Rational(3, 8), sp.Rational(3, 8),
                     sp.Rational(3, 8), sp.Rational(1, 3))
expected_inverse = sp.diag(4, 2, 4, sp.Rational(8, 3), sp.Rational(8, 3),
                           sp.Rational(8, 3), sp.Rational(8, 3), 3)

checks = {
    "wp443_dependency_passed": wp443["passed"],
    "canonical_generator_normalization": all(sp.trace(t*t) == sp.Rational(1, 2) for t in generators),
    "exact_dimensionless_mass_shape": K == expected_K,
    "mass_shape_has_rank_eight": K.rank() == 8,
    "exact_inverse_kernel": K_inverse == expected_inverse,
    "tree_wilson_kernel_is_gauge_coupling_independent": sp.simplify(wilson_kernel-K_inverse/f**2) == sp.zeros(8),
    "hostile_scale_pair_changes_wilson_strength": wilson_kernel.subs(f, 1) != wilson_kernel.subs(f, 2),
    "all_mass_shape_eigenvalues_are_positive": all(value > 0 for value in K.eigenvals()),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP445",
    "current": "J_a^mu=sum over Q_L,u_R,d_R of bar(q) gamma^mu T_a q, with T_a=lambda_a/2",
    "mass_law": "M_F^2=g_F^2 f^2 K",
    "dimensionless_mass_shape": [[str(x) for x in row] for row in K.tolist()],
    "mass_shape_eigenvalues": {str(value): int(multiplicity) for value, multiplicity in K.eigenvals().items()},
    "inverse_current_kernel": [[str(x) for x in row] for row in K_inverse.tolist()],
    "effective_lagrangian": "L_eff=-(1/(2 f^2)) J_a (K^-1)_ab J_b",
    "source_authorized_probe_family": "Eight diagonal-SU(3)_F vector currents fixed by the anomaly-free quark representation.",
    "contextual_partition": "Algebraically faithful on the eight labelled current components because K is positive definite; no claim of faithfulness on physical16 without the quark mass-basis map.",
    "instrument": None,
    "classification": "A source-derived current readout kernel, not a selector and not yet an experimentally calibrated probe.",
    "smallest_exact_falsifier": "A zero eigenvalue of K or residual g_F dependence in g_F^2(M_F^2)^-1.",
    "remaining_gate": "Supply the source-derived map from the WP443 vacuum and messenger sector to a viable physical16 quark mass basis before applying meson or collider constraints.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp445_flavor_current_kernel.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
