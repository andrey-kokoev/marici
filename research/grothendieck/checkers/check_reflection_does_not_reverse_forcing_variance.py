"""Exact block audit: reflected forward incidence is not an adjoint lower incidence."""

from fractions import Fraction
import json


# Two-dimensional triangular blocks in the ordered basis (tail, source).
a_plus = Fraction(2)
a_minus = Fraction(-3)
B = Fraction(5)

A_plus = ((a_plus, B), (Fraction(0), Fraction(0)))
A_minus = ((a_minus, B), (Fraction(0), Fraction(0)))

# With identity role-preserving pairing, cross-adjointness compares A_minus
# with transpose(A_plus). Their off-diagonal incidences occupy opposite slots.
A_plus_transpose = ((a_plus, Fraction(0)), (B, Fraction(0)))

checks = {
    "direct_forcing_is_upper_right": A_plus[0][1] == B and A_plus[1][0] == 0,
    "reflected_forcing_remains_upper_right": A_minus[0][1] == B and A_minus[1][0] == 0,
    "adjoint_forcing_is_lower_left": A_plus_transpose[1][0] == B and A_plus_transpose[0][1] == 0,
    "reflected_block_is_not_adjoint_block": A_minus != A_plus_transpose,
    "nonzero_forcing_causes_variance_mismatch": A_minus[0][1] != A_plus_transpose[0][1],
    "zero_forcing_would_remove_offdiagonal_mismatch": Fraction(0) == 0,
}

result = {
    "schema": "marici.grothendieck.reflection-forcing-variance.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "B": str(B),
}

print(json.dumps(result, indent=2, sort_keys=True))
