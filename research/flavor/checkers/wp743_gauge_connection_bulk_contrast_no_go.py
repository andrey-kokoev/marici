"""Exact orbifold gauge-connection carrier and bulk-contrast audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

def generator(n, i, j):
    M = sp.zeros(n)
    M[i, j] = 1
    M[j, i] = -1
    return M

p = (1, 1, 1, 1, -1)
adjoint_parities = {(i, j): p[i]*p[j] for i in range(5) for j in range(i+1, 5)}
a_mu_even = [pair for pair, sign in adjoint_parities.items() if sign == 1]
a5_even = [pair for pair, sign in adjoint_parities.items() if sign == -1]

# The four A5 zero modes T_{i5} carry the vector representation of SO(4).
so4 = [generator(4, i, j) for i in range(4) for j in range(i+1, 4)]
so3 = [generator(4, i, j) for i in range(3) for j in range(i+1, 3)]

def symmetric_commutant_dimension(generators):
    variables = sp.symbols("k0:10")
    K = sp.zeros(4)
    cursor = 0
    for i in range(4):
        for j in range(i, 4):
            K[i, j] = K[j, i] = variables[cursor]
            cursor += 1
    equations = []
    for J in generators:
        equations.extend(list(K*J-J*K))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return len(variables)-coefficient_matrix.rank(), K, variables, coefficient_matrix.nullspace()

bulk_dim, bulk_K, bulk_vars, bulk_nullspace = symmetric_commutant_dimension(so4)
boundary_dim, boundary_K, boundary_vars, boundary_nullspace = symmetric_commutant_dimension(so3)

a, b = sp.symbols("a b", real=True)
boundary_form = sp.diag(a, a, a, b)
bulk_form = a*sp.eye(4)
bulk_contrast = sp.simplify(bulk_form[3, 3]-bulk_form[0, 0])
boundary_contrast = sp.simplify(boundary_form[3, 3]-boundary_form[0, 0])

g5, ell = sp.symbols("g5 ell", positive=True)
g4 = g5/sp.sqrt(ell)

# A connection cannot acquire an independent overall intrinsic parity in a
# non-Abelian theory: A -> -A sends dA+[A,A] to -dA+[A,A], neither plus nor
# minus the original curvature for independent nonzero derivative/bracket parts.
dpart, bracket = sp.symbols("D B", nonzero=True)
flipped_curvature = -dpart + bracket
curvature = dpart + bracket

checks = {
    "orbifold_has_six_even_A_mu_generators": len(a_mu_even) == 6,
    "orbifold_has_four_even_A5_generators": len(a5_even) == 4,
    "A_mu_even_sector_is_so4": a_mu_even == [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)],
    "A5_even_sector_is_so5_over_so4": a5_even == [(0,4),(1,4),(2,4),(3,4)],
    "bulk_SO4_symmetric_commutant_is_one_dimensional": bulk_dim == 1,
    "boundary_SO3_symmetric_commutant_is_two_dimensional": boundary_dim == 2,
    "bulk_quadratic_portal_has_zero_ordered_contrast": bulk_contrast == 0,
    "boundary_quadratic_portal_has_free_ordered_contrast": boundary_contrast == b-a,
    "gauge_magnitude_retains_bulk_coupling": sp.simplify(g5*sp.diff(g4,g5)/g4) == 1,
    "gauge_magnitude_retains_compactification_clock": sp.simplify(ell*sp.diff(g4,ell)/g4) == -sp.Rational(1,2),
    "connection_sign_flip_is_not_curvature_covariant": sp.expand(flipped_curvature-curvature) == -2*dpart and sp.expand(flipped_curvature+curvature) == 2*bracket,
    "deliberate_failure_residual_is_nonzero": boundary_contrast.subs({a:1,b:2}) == 1,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP743",
    "status": "PASS",
    "checks": checks,
    "source_domain": "five-dimensional non-Abelian SO(5) gauge connection on S1/Z2 with parity diag(1,1,1,1,-1)",
    "forced_zero_modes": "A5 has exactly the four SO(5)/SO(4) zero modes, decomposing as 3+1 under the declared diagonal SO(3)",
    "repaired_fiber": "one-form covariance fixes the relative A_mu/A5 parity; an independent scalar intrinsic parity is unavailable for the gauge connection",
    "classification": "source-derived carrier selector and coupling parallelizer, but neither an asymmetric portal selector nor a magnitude selector",
    "bulk_no_go": "the symmetric commutant of the SO(4) vector is one-dimensional, so every bulk quadratic portal is proportional to I4 and has zero singlet-triplet contrast",
    "boundary_fiber": "after restriction to diagonal SO(3), the symmetric commutant is two-dimensional diag(a I3,b), restoring the free contrast b-a",
    "magnitude_fiber": "g4=g5/sqrt(ell), with logarithmic sensitivities (1,-1/2)",
    "smallest_exact_falsifier": "the SO(3)-legal boundary form diag(1,1,1,2) has ordered contrast 1 while respecting the residual group",
    "threshold_gate": "bulk gauge symmetry protects equality, but boundary-localized residual-invariant operators can generate or cancel the contrast",
    "instrument": "none; a gauge representation label is not a calibrated physical16 detector response",
    "remaining_source_gate": "derive an asymmetric but coefficient-rigid boundary or holonomy operation, its clock, and its boundary completion from a unique source dynamics",
}
(ROOT / "results" / "wp743_gauge_connection_bulk_contrast_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
