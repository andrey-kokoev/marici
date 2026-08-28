import json

import sympy as sp


tau, sigma, u = sp.symbols("tau sigma u", positive=True)
N, M = sp.symbols("N M", nonnegative=True)

g_tau = sp.exp(-tau * u**2)
g_sigma = sp.exp(-sigma * u**2)

positive_fixed_points = [
    root for root in sp.solve(sp.Eq(tau, 1 / tau), tau) if root.is_positive
]

checks = {
    "semigroup_composition": sp.simplify(
        g_tau * g_sigma - sp.exp(-(tau + sigma) * u**2)
    )
    == 0,
    "rapid_decay_representative": sp.limit(
        sp.exp((7 + 5) * u - sp.Rational(1, 3) * u**2), u, sp.oo
    )
    == 0,
    "unique_positive_reciprocal_fixed_point": positive_fixed_points == [1],
    "selected_multiplier": g_tau.subs(tau, 1) == sp.exp(-u**2),
    "hostile_two_fails_fixedness": sp.Rational(2) != sp.Rational(1, 2),
}

result = {
    "schema": "marici.aspect.reciprocal-log-gaussian-selector.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "positive_fixed_points": [str(x) for x in positive_fixed_points],
    "selected_prime_multiplier": "exp(-(log p)^2)",
    "scope_gate": (
        "Selection is source-derived only if Fourier sewing acts by modulus "
        "reciprocity on the Haar-normalized logarithmic coordinate."
    ),
}

print(json.dumps(result, indent=2))
