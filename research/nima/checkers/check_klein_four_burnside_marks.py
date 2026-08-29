from fractions import Fraction


subgroups = ("e", "J", "K", "I", "G")
orders = {"e": 1, "J": 2, "K": 2, "I": 2, "G": 4}
contains = {
    "e": {"e"},
    "J": {"e", "J"},
    "K": {"e", "K"},
    "I": {"e", "I"},
    "G": {"e", "J", "K", "I", "G"},
}


def mark(fixed_subgroup: str, stabilizer: str) -> int:
    orbit_size = 4 // orders[stabilizer]
    return orbit_size if contains[fixed_subgroup] <= contains[stabilizer] else 0


matrix = tuple(
    tuple(mark(fixed_subgroup, stabilizer) for stabilizer in subgroups)
    for fixed_subgroup in subgroups
)

expected = (
    (4, 2, 2, 2, 1),
    (0, 2, 0, 0, 1),
    (0, 0, 2, 0, 1),
    (0, 0, 0, 2, 1),
    (0, 0, 0, 0, 1),
)
assert matrix == expected


def determinant(a: tuple[tuple[int, ...], ...]) -> Fraction:
    work = [[Fraction(value) for value in row] for row in a]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next(row for row in range(column, len(work)) if work[row][column] != 0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result *= -1
        pivot_value = work[column][column]
        result *= pivot_value
        for entry in range(column, len(work)):
            work[column][entry] /= pivot_value
        for row in range(column + 1, len(work)):
            factor = work[row][column]
            for entry in range(column, len(work)):
                work[row][entry] -= factor * work[column][entry]
    return result


assert determinant(matrix) == 32

# Geometric packet examples: generic quartet, real pair, seam pair, center.
geometric_counts = {
    "generic": (4, 0),
    "real_off_seam": (2, 0),
    "seam_pair": (2, 2),
    "center": (1, 1),
}
for name, (total, i_fixed) in geometric_counts.items():
    rh_admitted = total == i_fixed
    assert rh_admitted == (name in {"seam_pair", "center"})

print("Klein-four Burnside mark determinant: 32")
print("abstract orbit types: five; geometrically realized types: four")
print("RH mark: total equals reciprocal-conjugation fixed count")
