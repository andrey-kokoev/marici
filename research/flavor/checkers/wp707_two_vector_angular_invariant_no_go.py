"""Exact invariant-grammar no-go for angular rigidity at lambda_c=0."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
theta = sp.symbols("theta", real=True)
gamma, mun, mum, ln, lm, lx, lc = sp.symbols(
    "gamma mu_n mu_m lambda_n lambda_m lambda_x lambda_c", real=True
)
a, b, c = sp.symbols("a b c", real=True)

# Degree counts in the original triplet fields: a,b,c each have degree two.
one = sp.Integer(1)
gram_monomials_degree_le_four = [one, a, b, c, a**2, a*b, a*c, b**2, b*c, c**2]

def flip_even(expr):
    return sp.expand(expr.subs(c, -c)-expr) == 0

flip_even_basis = [expr for expr in gram_monomials_degree_le_four if flip_even(expr)]
expected_basis = [one, a, b, a**2, a*b, b**2, c**2]

V = gamma + mun*a + mum*b + ln*a**2 + lm*b**2 + lx*a*b + lc*c**2
angular_V = sp.expand(V.subs({a: 1, b: 1, c: sp.sin(theta)}))
angular_force = sp.diff(angular_V, theta).subs(theta, 0)
angular_stiffness = sp.diff(angular_V, theta, 2).subs(theta, 0)

checks = {
    "complete_flip_even_basis_through_degree_four": flip_even_basis == expected_basis,
    "general_potential_uses_complete_basis": len(sp.Poly(V, a, b, c).terms()) == 7,
    "orthogonal_frame_is_stationary": angular_force == 0,
    "only_correlation_controls_angular_stiffness": angular_stiffness == 2*lc,
    "protected_slice_has_flat_physical_angle": angular_stiffness.subs(lc, 0) == 0,
    "nonzero_correlation_lifts_angle": angular_stiffness.subs(lc, 1) == 2,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP707",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "two real triplets with diagonal SO(3), independent flips, polynomial locality, and field degree at most four",
    "faithful_coordinate": "the Gram triple (a,b,c), with relative orientation carried by c at fixed norms",
    "largest_source_authorized_probe_family": "all renormalizable diagonal-SO(3), flip-even scalar invariants",
    "contextual_partition": "when lambda_c=0 every relative angle at fixed norms is indistinguishable to the complete admitted scalar potential",
    "classification": "complete invariant-grammar obstruction: the same operator is necessary for angular rigidification and supplies the WP705 transverse mode; no selector exists on this field grammar",
    "smallest_exact_falsifier": "the angular stiffness is exactly 2 lambda_c and vanishes on the proposed protected slice",
    "remaining_gate": "enlarge the source grammar or derive a full-domain attractive ray with nonzero lambda_c; any reference port defines a new stabilizer-groupoid experiment",
}
(ROOT / "results" / "wp707_two_vector_angular_invariant_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
