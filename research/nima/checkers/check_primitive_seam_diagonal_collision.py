import json
from fractions import Fraction


p = 2
q = 3
diagonal = [Fraction(1, p), Fraction(1, q)]

diagonal_trace = sum(diagonal, Fraction(0))
diagonal_determinant = diagonal[0] * diagonal[1]

# The rank-one seam image has the same diagonal and off-diagonal squared
# magnitude 1/(pq). Exact determinant calculations need only this square.
off_diagonal_squared = Fraction(1, p * q)
seam_trace = diagonal_trace
seam_determinant = diagonal[0] * diagonal[1] - off_diagonal_squared
residual_determinant = -off_diagonal_squared

assert diagonal_trace == seam_trace == Fraction(5, 6)
assert diagonal_determinant == Fraction(1, 6)
assert seam_determinant == 0
assert residual_determinant == Fraction(-1, 6)

result = {
    "schema": "marici.nima.primitive-seam-diagonal-collision.v1",
    "primes": [p, q],
    "shared_diagonal": [str(value) for value in diagonal],
    "shared_trace": str(diagonal_trace),
    "primitive_density_determinant": str(diagonal_determinant),
    "seam_image_determinant": str(seam_determinant),
    "zero_diagonal_residual_determinant": str(residual_determinant),
    "diagonal_projection_is_faithful": False,
    "shared_scalar_implies_carrier_identity": False,
    "minimum_comparison_port": "off_diagonal_cross_prime_residual",
}
print(json.dumps(result, indent=2, sort_keys=True))

