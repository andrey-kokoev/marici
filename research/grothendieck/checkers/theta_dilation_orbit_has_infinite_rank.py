import json
from pathlib import Path

import sympy as sp


X = sp.symbols("X")
base = 4 * X**2 - 6 * X


def reduced_dilation(poly):
    return sp.expand(2 * X * sp.diff(poly, X) + (sp.Rational(1, 2) - 2 * X) * poly)


polynomials = [base]
for _ in range(12):
    polynomials.append(reduced_dilation(polynomials[-1]))

witnesses = []
for N in range(13):
    packet = polynomials[: N + 1]
    coefficient_matrix = sp.zeros(N + 1, N + 3)
    for row, poly in enumerate(packet):
        expanded = sp.Poly(poly, X)
        for degree in range(N + 3):
            coefficient_matrix[row, degree] = expanded.coeff_monomial(X**degree)
    leading = [sp.Poly(poly, X).LC() for poly in packet]
    degrees = [int(sp.degree(poly, X)) for poly in packet]
    witnesses.append(
        {
            "N": N,
            "degrees": degrees,
            "leading_coefficients": [str(value) for value in leading],
            "rank": int(coefficient_matrix.rank()),
            "full_rank": bool(coefficient_matrix.rank() == N + 1),
            "next_degree_is_new": degrees[-1] == N + 2,
            "no_constant_coefficient_relation": bool(len(coefficient_matrix.T.nullspace()) == 0),
        }
    )

checks = {
    "degree_grows_once_per_dilation": all(item["next_degree_is_new"] for item in witnesses),
    "every_tested_krylov_packet_has_full_rank": all(item["full_rank"] for item in witnesses),
    "no_tested_constant_coefficient_recurrence": all(item["no_constant_coefficient_relation"] for item in witnesses),
    "leading_coefficient_formula": all(
        sp.Poly(polynomials[k], X).LC() == 4 * (-2) ** k for k in range(13)
    ),
}

result = {
    "schema": "marici.grothendieck.theta_dilation_orbit_has_infinite_rank.v1",
    "reduced_atom": "X^(1/4) exp(-X) times polynomial",
    "reduced_dilation": "P maps to 2 X P' + (1/2 - 2 X) P",
    "checks": checks,
    "witnesses": witnesses,
}

assert all(checks.values())
output = Path("research/grothendieck/results/theta_dilation_orbit_has_infinite_rank.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
