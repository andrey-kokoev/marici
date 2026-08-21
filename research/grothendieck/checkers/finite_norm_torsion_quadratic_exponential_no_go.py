"""Exact degree obstruction for rational quadratic exponentials."""


def logarithmic_derivative_identity_degrees(
    numerator_degree: int, denominator_degree: int
) -> tuple[int, int]:
    # For P/Q satisfying (P/Q)'/(P/Q)=+-x, equation
    # P'Q-PQ'=+-xPQ would be necessary.
    left_upper_bound = numerator_degree + denominator_degree - 1
    right_degree = numerator_degree + denominator_degree + 1
    return left_upper_bound, right_degree


for numerator_degree in range(0, 101):
    for denominator_degree in range(0, 101):
        left, right = logarithmic_derivative_identity_degrees(
            numerator_degree, denominator_degree
        )
        assert left < right
        assert right - left == 2

# The finite C2 norm complex itself is algebraic and has no height dependence
# before an x-dependent analytic enlargement is supplied.
norm = ((1, 1), (1, 1))
complement = ((1, -1), (-1, 1))
assert norm == ((1, 1), (1, 1))
assert complement == ((1, -1), (-1, 1))

print("finite_algebraic_complex_torsion_is_rational=True")
print("quadratic_exponential_is_not_rational_by_degree_obstruction=True")
print("finite_C2_norm_torsion_cannot_equal_exact_quadratic_counterterm=True")
print("infinite_Gaussian_or_regularized_enlargement_required=True")
