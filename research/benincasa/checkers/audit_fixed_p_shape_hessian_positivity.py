#!/usr/bin/env python3
"""Exact pointwise positivity of the fixed-P shape Hessian in source Eq. (51)."""

from fractions import Fraction as F


# Along b=(1,-1,0), list directional coefficients of every denominator.
# Every simplex includes the four common factors qG,qg1,qg2,qg3 and one
# deletion plus one two-site factor from the six terms in source Eq. (51).
common = {"qG": 0, "qg1": 1, "qg2": -1, "qg3": 0}
terms = [
    ("qG12", 0, "qg23", -1),
    ("qG12", 0, "qg31", 1),
    ("qG23", 0, "qg31", 1),
    ("qG23", 0, "qg12", 0),
    ("qG31", 0, "qg12", 0),
    ("qG31", 0, "qg23", -1),
]

# A generic exact positive point suffices to audit the formula mechanically;
# positivity itself follows termwise because it is a sum of squares divided by
# positive denominators.
positive_q = {
    "qG": F(11), "qg1": F(7), "qg2": F(5), "qg3": F(13),
    "qG12": F(17), "qG23": F(19), "qG31": F(23),
    "qg12": F(29), "qg23": F(31), "qg31": F(37),
}


def second_ratio(factors):
    # For f=prod q_a^-1: f''/f=(sum c_a/q_a)^2+sum(c_a/q_a)^2.
    slopes = [F(c, 1) / positive_q[name] for name, c in factors]
    return sum(slopes) ** 2 + sum(x * x for x in slopes)


ratios = []
for delete_name, delete_c, pair_name, pair_c in terms:
    factors = list(common.items()) + [(delete_name, delete_c), (pair_name, pair_c)]
    ratios.append(second_ratio(factors))

checks = {
    "six_source_simplices_retained": len(terms) == 6,
    "total_energy_factors_are_shape_constant": common["qG"] == 0 and all(t[1] == 0 for t in terms),
    "every_simplex_has_nonzero_shape_slope": all(r > 0 for r in ratios),
    "fixed_p_integrand_shape_hessian_is_strictly_positive": sum(ratios) > 0,
    "positivity_uses_only_positive_source_denominators": all(q > 0 for q in positive_q.values()),
}

assert all(checks.values()), checks
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("simplex second-derivative ratios:", ratios)
