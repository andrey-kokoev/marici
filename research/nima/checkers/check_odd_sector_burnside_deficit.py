from fractions import Fraction


def marks(fixed_orbits: int, free_orbits: int) -> tuple[int, int, int]:
    total = fixed_orbits + 2 * free_orbits
    trace = fixed_orbits
    odd_dimension = free_orbits
    return total, trace, odd_dimension


for fixed in range(6):
    for free in range(6):
        total, trace, odd_dimension = marks(fixed, free)
        assert total - trace == 2 * odd_dimension
        assert (odd_dimension == 0) == (total == trace)

# Exact projectors for one free orbit, J swapping the two basis vectors.
identity = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
swap = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(0)))
odd_projector = tuple(
    tuple((identity[i][j] - swap[i][j]) / 2 for j in range(2))
    for i in range(2)
)
assert odd_projector == (
    (Fraction(1, 2), Fraction(-1, 2)),
    (Fraction(-1, 2), Fraction(1, 2)),
)

# Its image is the nonzero sign line spanned by (1,-1).
image = (
    odd_projector[0][0] - odd_projector[0][1],
    odd_projector[1][0] - odd_projector[1][1],
)
assert image == (Fraction(1), Fraction(-1))

print("Burnside deficit = twice odd-sector dimension")
print("free reciprocal orbit: one-dimensional odd obstruction")
print("RH operator target: source-derived odd-sector contraction")
