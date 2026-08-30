"""Exact finite checks for the strict Hankel / Evans hostile source."""

from fractions import Fraction
import json


def moment(j):
    return Fraction(2 ** (j + 2) - 1, j + 1)


def determinant(matrix):
    work = [row[:] for row in matrix]
    det = Fraction(1)
    for col in range(len(work)):
        pivot = next((row for row in range(col, len(work)) if work[row][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            det = -det
        value = work[col][col]
        det *= value
        for row in range(col + 1, len(work)):
            ratio = work[row][col] / value
            for j in range(col, len(work)):
                work[row][j] -= ratio * work[col][j]
    return det


ordinary = []
shifted = []
for size in range(1, 9):
    ordinary.append(determinant([[moment(i + j) for j in range(size)] for i in range(size)]))
    shifted.append(determinant([[moment(i + j + 1) for j in range(size)] for i in range(size)]))

# Write r=e^z.  The transform factors as ((r-1)/z)(1+2r).
r = Fraction(-1, 2)
checks = {
    "moment_formula_starts_correctly": [moment(j) for j in range(4)]
    == [Fraction(3), Fraction(7, 2), Fraction(5), Fraction(31, 4)],
    "ordinary_hankel_determinants_positive_through_8": all(x > 0 for x in ordinary),
    "shifted_hankel_determinants_positive_through_8": all(x > 0 for x in shifted),
    "character_factor_vanishes": 1 + 2 * r == 0,
    "uniform_interval_factor_does_not_vanish": r - 1 != 0,
    "off_seam_modulus": abs(r) != 1,
}

result = {
    "schema": "marici.grothendieck.complete-strict-hankel-evans-hostile.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "density": "1_[0,1] + 2*1_[1,2]",
        "moments_0_to_3": [str(moment(j)) for j in range(4)],
        "ordinary_determinants": [str(x) for x in ordinary],
        "shifted_determinants": [str(x) for x in shifted],
        "exp_z": str(r),
        "zero_real_part": "-log(2)",
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
