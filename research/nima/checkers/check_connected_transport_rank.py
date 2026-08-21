"""Algebraic precursor of connected future information."""

import json
from pathlib import Path
import sympy as sp


K_sep = sp.Matrix([[1, 2], [3, 6]])
K_conn = sp.eye(2)
spectator = sp.Matrix([[2, 3]])
K_with_spectator = sp.kronecker_product(K_conn, spectator)

assert K_sep.rank() == 1
assert K_conn.rank() == 2
assert K_with_spectator.rank() == K_conn.rank()

# The exterior-square coordinate for a 2x2 map is its determinant.
assert K_sep.det() == 0
assert K_conn.det() == 1

# Sequential transport cannot increase connected rank.
L = sp.Matrix([[1, 1], [1, 1]])
composite = K_conn * L
assert composite.rank() <= min(K_conn.rank(), L.rank())

# Positive readouts: rank one exactly for independence in these full-support
# examples; rank two for correlated Bell-type data.
P_ind = sp.Matrix([[sp.Rational(1, 4), sp.Rational(1, 4)],
                   [sp.Rational(1, 4), sp.Rational(1, 4)]])
P_corr = sp.Matrix([[sp.Rational(9, 20), sp.Rational(1, 20)],
                    [sp.Rational(1, 20), sp.Rational(9, 20)]])
assert P_ind.rank() == 1 and P_corr.rank() == 2

# A nontrivial exact flavor transition kernel (orthostochastic 3/5-4/5
# rotation plus a fixed third flavor) also has connected rank.
P_flavor = sp.Matrix([
    [sp.Rational(9, 25), sp.Rational(16, 25), 0],
    [sp.Rational(16, 25), sp.Rational(9, 25), 0],
    [0, 0, 1],
])
assert P_flavor.rank() == 3

# Forgetting coefficients and retaining only nonzero support can erase the
# distinction: a generic fully supported kernel has all-ones incidence rank 1.
full_support = sp.ones(3)
assert full_support.rank() == 1

result = {
    "status": "PASS",
    "separable_rank": K_sep.rank(),
    "connected_rank": K_conn.rank(),
    "connected_excess_rank_minus_one": K_conn.rank()-1,
    "spectator_extended_rank": K_with_spectator.rank(),
    "composite_rank": composite.rank(),
    "independent_positive_rank": P_ind.rank(),
    "correlated_positive_rank": P_corr.rank(),
    "flavor_kernel_rank": P_flavor.rank(),
    "full_support_incidence_rank": full_support.rank(),
    "conclusion": (
        "Exterior-square/determinantal transport data is a spectator-stable "
        "algebraic precursor of connected information, but coefficients are "
        "essential: bare support incidence can erase it."
    ),
}
out = Path(__file__).parents[1] / "results" / "connected_transport_rank.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
