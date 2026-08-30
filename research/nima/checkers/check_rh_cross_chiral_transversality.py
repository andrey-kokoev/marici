from fractions import Fraction
import json
from pathlib import Path


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    nrows = len(a)
    ncols = len(a[0])
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][c]
        a[r] = [x / scale for x in a[r]]
        for i in range(nrows):
            if i != r and a[i][c]:
                scale = a[i][c]
                a[i] = [x - scale * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def kernel_dimension_two_covectors(epsilon, eta):
    return 3 - rank([epsilon, eta])


epsilon = [Fraction(1), Fraction(1), Fraction(1)]
same_parity_tests = [
    [Fraction(1), Fraction(2), Fraction(3)],
    [Fraction(1), Fraction(-1), Fraction(0)],
    [Fraction(2), Fraction(2), Fraction(2)],
]
same_parity_intersections = [
    kernel_dimension_two_covectors(epsilon, eta)
    for eta in same_parity_tests
]
assert all(dimension >= 1 for dimension in same_parity_intersections)

eta_transverse = [Fraction(1), Fraction(2), Fraction(3)]
eta_crossing = [Fraction(1), Fraction(-1), Fraction(0)]
assert dot(epsilon, eta_transverse) == 6
assert dot(epsilon, eta_crossing) == 0

# For L_epsilon versus L_*eta, a zero pairing contributes one current and one
# covector intersection direction; otherwise neither survives.
opposite_intersection_transverse = 0 if dot(epsilon, eta_transverse) else 2
opposite_intersection_crossing = 0 if dot(epsilon, eta_crossing) else 2
assert opposite_intersection_transverse == 0
assert opposite_intersection_crossing == 2

result = {
    "source_rank": 3,
    "same_parity_intersection_dimensions": same_parity_intersections,
    "same_parity_transverse_possible": False,
    "hodge_flips_one_form_to_degree": 2,
    "cross_chiral_pairing": "g-inverse(epsilon, eta)",
    "nonzero_pairing_intersection_dimension": opposite_intersection_transverse,
    "zero_pairing_intersection_dimension": opposite_intersection_crossing,
    "zero_defect_channels": ["current", "covector"],
    "verdict": "Fourier-Hodge parity exchange is necessary for transversality; orientation still requires nonorthogonality",
}

out = Path(__file__).parents[1] / "results" / "rh-cross-chiral-transversality.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
