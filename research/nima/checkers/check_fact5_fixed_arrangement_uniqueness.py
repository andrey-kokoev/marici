#!/usr/bin/env python3
"""Exact numerator-degree uniqueness on the fixed five-line arrangement."""
import json
from pathlib import Path
from sympy import Matrix, Rational, Poly, expand, symbols

x, y, t = symbols("x y t")
coefficients = symbols("c0:6")
N = coefficients[0] + coefficients[1]*x + coefficients[2]*y + coefficients[3]*x**2 + coefficients[4]*x*y + coefficients[5]*y**2
facets = [x, y, 1-x, Rational(3, 2)-x-y, 1-y]

# Parameterize each line and require the degree-at-most-two numerator to vanish
# identically there. These are exactly the zero-residue divisibility conditions.
substitutions = [
    {x: 0, y: t},
    {x: t, y: 0},
    {x: 1, y: t},
    {x: t, y: Rational(3, 2)-t},
    {x: t, y: 1},
]
equations = []
per_facet_ranks = []
for substitution in substitutions:
    restricted = Poly(expand(N.subs(substitution)), t)
    facet_equations = restricted.all_coeffs()
    equations.extend(facet_equations)
    matrix, _ = Matrix([facet_equations]).jacobian(coefficients), None
    per_facet_ranks.append(matrix.rank())
A = Matrix(equations).jacobian(coefficients)
assert A.rank() == 6
assert A.nullspace() == []

Q = expand(facets[0]*facets[1]*facets[2]*facets[3]*facets[4])
assert Poly(Q, x, y).total_degree() == 5
# Deliberate rival: dx wedge dy has zero facet residues but its projective
# coefficient behaves as z^-3, so infinity regularity excludes it.
result = {
    "schema": "marici.fact5-fixed-arrangement-uniqueness.v1",
    "status": "passed",
    "strength": "exact uniqueness for rational two-forms with at most simple poles on the declared five lines and no infinity-divisor pole",
    "common_denominator_degree": 5,
    "infinity_regular_numerator_degree_bound": 2,
    "zero_residue_constraint_rank": A.rank(),
    "numerator_coefficient_count": len(coefficients),
    "uniqueness_kernel_dimension": len(A.nullspace()),
    "algebraic_argument": "zero residue makes every facet equation divide N; their degree-five product divides N, while infinity regularity gives degree N<=2",
    "deliberate_failure": {
        "difference_form": "dx wedge dy = Q/Q dx wedge dy",
        "facet_residues": "zero",
        "infinity_pole_order": 3,
        "excluded_by": "no infinity-divisor pole",
    },
    "boundary": "the arrangement, simple-pole class, residue convention, and infinity condition are assumptions; uniqueness does not select the arrangement",
}
out = Path("research/nima/results/fact5_fixed_arrangement_uniqueness.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
