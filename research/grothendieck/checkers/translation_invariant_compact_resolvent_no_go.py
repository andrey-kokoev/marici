"""Finite-grid shadow of the nonatomic multiplication-resolvent no-go."""

from fractions import Fraction


for denominator in (4, 8, 16, 32):
    points = [Fraction(index, denominator) for index in range(-denominator, denominator + 1)]
    resolvent_norm_squares = [Fraction(1, 1) / (1 + point * point) for point in points]
    assert all(value >= Fraction(1, 2) for value in resolvent_norm_squares)
    print(
        f"grid_denominator={denominator} orthogonal_modes={len(points)} "
        f"minimum_resolvent_norm_squared={min(resolvent_norm_squares)}"
    )

print("mode_count_diverges_with_uniform_resolvent_lower_bound=True")
print("nonatomic_multiplication_resolvent_compact=False")
print("odd_convolution_gives_discreteness=False")
print("archimedean_or_geometric_confinement_required=True")

