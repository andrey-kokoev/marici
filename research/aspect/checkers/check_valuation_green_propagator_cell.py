import json

import sympy as sp


ell, eta, z = sp.symbols("ell eta z")


def propagator(length):
    return sp.exp(-length / 2) * sp.Matrix(
        [
            [sp.cosh(length * z), -sp.sinh(length * z)],
            [-sp.sinh(length * z), sp.cosh(length * z)],
        ]
    )


K = propagator(ell)
K_eta = propagator(eta)
K_sum = propagator(ell + eta)
rho = -sp.sinh(ell * z) / sp.sinh(ell / 2)
normalized_off_diagonal = sp.simplify(2 * K[0, 1] / (1 - sp.exp(-ell)))

checks = {
    "normalized_off_diagonal_is_valuation_response": sp.simplify(
        normalized_off_diagonal - rho
    )
    == 0,
    "archimedean_limit_is_boost_generator": sp.limit(
        normalized_off_diagonal, ell, 0
    )
    == -2 * z,
    "reciprocal_reversal_flips_odd_entry": sp.simplify(
        K[0, 1].subs(z, -z) + K[0, 1]
    )
    == 0,
    "diagonal_is_reciprocal_even": sp.simplify(
        K[0, 0].subs(z, -z) - K[0, 0]
    )
    == 0,
    "interval_composition": (K * K_eta - K_sum).applyfunc(sp.simplify)
    == sp.zeros(2),
    "vacuum_normalization_identity": sp.simplify(
        (
            1
            - sp.exp(-ell)
            - 2 * sp.exp(-ell / 2) * sp.sinh(ell / 2)
        ).rewrite(sp.exp)
    )
    == 0,
}

result = {
    "schema": "marici.aspect.valuation-green-propagator-cell.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "propagator": str(K),
    "normalized_off_diagonal": str(normalized_off_diagonal),
    "interpretation": (
        "The normalized valuation response is exactly the odd matrix "
        "coefficient of the moving-tail Green propagator."
    ),
}

print(json.dumps(result, indent=2))
