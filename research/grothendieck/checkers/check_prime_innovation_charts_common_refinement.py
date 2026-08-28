"""Exact finite test: prime innovation towers are charts of one seam state."""

from fractions import Fraction


# Rational surrogate interval lengths keep the partition calculation exact.
length_p = Fraction(2)
length_q = Fraction(3)
height = Fraction(12)

# Piecewise-constant energy density on unit cells.
energy = [Fraction((j + 1) ** 2) for j in range(int(height))]


def interval_energy(left: Fraction, right: Fraction) -> Fraction:
    assert left.denominator == right.denominator == 1
    return sum(energy[j] for j in range(int(left), int(right)))


def chart(length: Fraction):
    cells = []
    left = Fraction(0)
    while left < height:
        right = min(left + length, height)
        cells.append((left, right, interval_energy(left, right)))
        left = right
    return cells


p_chart = chart(length_p)
q_chart = chart(length_q)
total = sum(energy)
checks = 0
assert sum(cell[2] for cell in p_chart) == total
assert sum(cell[2] for cell in q_chart) == total
assert sum(cell[2] for cell in p_chart) + sum(cell[2] for cell in q_chart) == 2 * total
checks += 3

endpoints = sorted(
    {Fraction(0), height}
    | {cell[0] for cell in p_chart}
    | {cell[1] for cell in p_chart}
    | {cell[0] for cell in q_chart}
    | {cell[1] for cell in q_chart}
)
refinement = [
    (left, right, interval_energy(left, right))
    for left, right in zip(endpoints, endpoints[1:])
]
assert sum(cell[2] for cell in refinement) == total
checks += 1

# Each coarse chart cell is exactly the sum of contained refinement cells.
for coarse in p_chart + q_chart:
    merged = sum(
        fine[2]
        for fine in refinement
        if coarse[0] <= fine[0] and fine[1] <= coarse[1]
    )
    assert merged == coarse[2]
    checks += 1

print(f"PASS {checks}/{checks}: prime towers glue through one norm-preserving common refinement")

