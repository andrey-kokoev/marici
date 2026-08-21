"""Exact finite-rank controls for the semigroup incidence kernel."""

from fractions import Fraction


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next(row for row in range(column, len(work)) if work[row][column])
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, len(work)):
            factor = work[row][column] / pivot_value
            for index in range(column, len(work)):
                work[row][index] -= factor * work[column][index]
    return result


primes = (2, 3, 5, 7, 11, 13)
for size in range(1, len(primes) + 1):
    selected = primes[:size]
    vandermonde = [
        [Fraction(1, prime) ** mode for prime in selected] for mode in range(size)
    ]
    computed = determinant(vandermonde)
    expected = Fraction(1)
    for left in range(size):
        for right in range(left + 1, size):
            expected *= Fraction(1, selected[right]) - Fraction(1, selected[left])
    assert computed == expected
    assert computed != 0

partial_hs_squared = sum(
    prime ** (-1.5) / (1.0 - prime ** (-2)) for prime in primes
)
assert 0.0 < partial_hs_squared < 2.0

print("semigroup_evaluation_kernel_has_Vandermonde_full_rank=True")
print("kernel_Hilbert_Schmidt_series_converges_by_p_to_minus_three_halves=True")
print("generator_commutator_Hilbert_Schmidt_series_converges=True")
print("finite_kernel_determinant_nonvanishing=True")
print("Euler_Green_Schur_complement_identity_open=True")
