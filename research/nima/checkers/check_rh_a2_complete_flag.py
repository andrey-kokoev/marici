from fractions import Fraction
import json
from pathlib import Path


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
        for row in a
    ]


def matvec(a, x):
    return [sum(v * w for v, w in zip(row, x)) for row in a]


def dot(x, y):
    return sum(v * w for v, w in zip(x, y))


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


def inverse_3(a):
    aug = [
        [Fraction(x) for x in row]
        + [Fraction(int(i == j)) for j in range(3)]
        for i, row in enumerate(a)
    ]
    for col in range(3):
        pivot = next(i for i in range(col, 3) if aug[i][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for i in range(3):
            if i != col:
                scale = aug[i][col]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[col])]
    return [row[3:] for row in aug]


x = [Fraction(1), Fraction(2), Fraction(3)]
y = [Fraction(1), Fraction(1), Fraction(-1)]
assert dot(y, x) == 0

# Gradient of y(x) in coordinates (x1,x2,x3,y1,y2,y3).
incidence_gradient = y + x
assert rank([incidence_gradient]) == 1
affine_tangent_dimension = 6 - rank([incidence_gradient])
assert affine_tangent_dimension == 5
projective_flag_dimension = affine_tangent_dimension - 2
assert projective_flag_dimension == 3

a = [
    [Fraction(1), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(1)],
    [Fraction(1), Fraction(0), Fraction(2)],
]
a_inv_t = transpose(inverse_3(a))
x_prime = matvec(a, x)
y_prime = matvec(a_inv_t, y)
assert dot(y_prime, x_prime) == dot(y, x)

plucker_coordinates_gr_2_3 = ["Delta12", "Delta13", "Delta23"]
assert len(plucker_coordinates_gr_2_3) == 3
source_decorated_seed_count = 3
required_a2_seed_count = 5
assert source_decorated_seed_count < required_a2_seed_count

result = {
    "homogeneous_coordinate_count": 6,
    "incidence_equation_count": 1,
    "affine_incidence_dimension": affine_tangent_dimension,
    "projective_gauge_directions": 2,
    "complete_flag_dimension": projective_flag_dimension,
    "gl3_incidence_covariance": True,
    "gr_2_3_plucker_coordinate_count": len(plucker_coordinates_gr_2_3),
    "currently_obvious_source_chart_count": source_decorated_seed_count,
    "a2_pentagon_seed_count": required_a2_seed_count,
    "source_cluster_atlas_complete": False,
    "verdict": "the exact A2 object is a complete primal-dual flag; two additional decorated charts are required for a source pentagon",
}

out = Path(__file__).parents[1] / "results" / "rh-a2-complete-flag.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
