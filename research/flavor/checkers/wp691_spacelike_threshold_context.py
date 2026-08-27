"""Exact rank test for a physical spacelike threshold context."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
a, b = sp.symbols("a b", real=True)
z1, z2, x = sp.symbols("z1 z2 x", nonnegative=True)

# Equal-mass, once-subtracted Euclidean two-propagator threshold kernel.
# Phi(z) = integral_0^1 log(1 + z*x*(1-x)) dx.
u = x * (1 - x)
moments = [sp.integrate(u**n, (x, 0, 1)) for n in range(1, 5)]
expected_moments = [sp.factorial(n) ** 2 / sp.factorial(2 * n + 1) for n in range(1, 5)]
series = sum(
    (-1) ** (n + 1) * z1**n * moments[n - 1] / n
    for n in range(1, 5)
)

phi1, phi2 = sp.symbols("Phi_1 Phi_2", real=True)
response = sp.Matrix([a + b * phi1, a + b * phi2])
jacobian = response.jacobian([a, b])

# Positivity is certified pointwise: for z >= 0 and 0 < x < 1,
# dPhi/dz = u/(1+z*u) is positive.  Use a rational witness as well.
derivative_integrand = sp.cancel(u / (1 + z1 * u))
ordered_log_argument_gap = sp.expand((1 + 3 * u) - (1 + u))

checks = {
    "beta_moments_exact": all(sp.simplify(got - want) == 0 for got, want in zip(moments, expected_moments)),
    "low_momentum_slope_is_one_sixth": moments[0] == sp.Rational(1, 6),
    "low_momentum_curvature_coefficient_is_minus_one_sixtieth": sp.expand(series).coeff(z1, 2) == -sp.Rational(1, 60),
    "two_context_determinant_is_kernel_difference": jacobian.det() == phi2 - phi1,
    "local_limit_has_rank_one": jacobian.det().subs(phi2, phi1) == 0,
    "derivative_integrand_positive_at_interior_witness": derivative_integrand.subs({x: sp.Rational(1, 2), z1: 2}) > 0,
    "ordered_log_arguments_have_positive_interior_gap": ordered_log_argument_gap.subs(x, sp.Rational(1, 2)) == sp.Rational(1, 2),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP691",
    "status": "PASS",
    "checks": checks,
    "admitted_mathematical_domain": "equal-mass once-subtracted Euclidean two-propagator kernel Phi(z), z=Q^2/M^2 nonnegative",
    "contextual_partition": "a local momentum-independent response has one class; a nonzero threshold coefficient separates every pair of distinct spacelike momenta because Phi is strictly increasing",
    "rank_result": "det J=b-independent kernel difference Phi(z2)-Phi(z1); it is nonzero for z2 unequal to z1",
    "classification": "physical-context rank repair for the minimal threshold kernel, not yet a flavor selector or an experimentally typed portal instrument",
    "smallest_exact_falsifier": "b=0 or Q1=Q2 collapses the response to rank one; replacing the nonlocal kernel by its local constant also collapses it",
    "remaining_gate": "derive the complete messenger four-point form factor with its Mandelstam dependence, project it onto an observable final state, and calibrate two spacelike or timelike bins",
}
(ROOT / "results" / "wp691_spacelike_threshold_context.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
