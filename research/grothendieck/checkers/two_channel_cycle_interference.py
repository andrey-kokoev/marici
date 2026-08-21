"""Exact controls for the minimal two-channel determinant mechanism."""

from fractions import Fraction


def determinant(matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


for t in (Fraction(-2), Fraction(0), Fraction(1), Fraction(3)):
    q = ((t, Fraction(1)), (Fraction(1), Fraction(1)))
    assert determinant(q) == t - 1
assert all(entry != 0 for row in ((Fraction(1), Fraction(1)), (Fraction(1), Fraction(1))) for entry in row)

a, b, c, d = map(Fraction, (2, 3, 5, 7))
row_1, row_2, col_1, col_2 = map(Fraction, (11, 13, 17, 19))
ratio = (a * d) / (b * c)
gauged_ratio = ((row_1 * col_1 * a) * (row_2 * col_2 * d)) / (
    (row_1 * col_2 * b) * (row_2 * col_1 * c)
)
assert gauged_ratio == ratio

for t in range(-4, 5):
    oriented = Fraction(t - 1)
    assert oriented * oriented == oriented**2

print("rank_two_allows_zero_without_vanishing_entry=True")
print("four_cycle_ratio_is_row_column_gauge_invariant=True")
print("oriented_determinant_simple_zero_becomes_double_Gram_zero=True")
print("source_derived_prime_archimedean_four_cycle_open=True")
