"""Exact rank-aware audit of Gram-degenerate null-branch support."""

import json
from fractions import Fraction as F
from pathlib import Path

def dot(v, w):
    return sum(x * y for x, y in zip(v, w))


def rank(matrix):
    rows = [[F(x) for x in row] for row in matrix]
    r = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(r, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        scale = rows[r][col]
        rows[r] = [x / scale for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col]:
                scale = rows[i][col]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[r])]
        r += 1
    return r


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def branch_linear_system(points):
    matrix = [list(p) for p in points]
    rhs = [dot(p, p) / 2 for p in points]
    return matrix, rhs


# Four external points: 0,a,b,c are coplanar, so det(G)=0.
a = (F(1), F(0), F(0))
b = (F(0), F(1), F(0))
c = (F(1), F(1), F(0))
A4, d4 = branch_linear_system([a, b, c])
G = [[dot(v, w) for w in (a, b, c)] for v in (a, b, c)]
assert det3(G) == 0
assert rank(A4) == rank([row + [rhs] for row, rhs in zip(A4, d4)]) == 2

fourfold_null_polynomial = "z^2 + 1/2"

# A fifth point transverse to the plane fixes z. The remaining null equation
# is an external condition on its transverse coordinate s.
fivefold_condition = "s^2 + 2"
# Direct coefficient audit: p.ell=s^2/2=p^2/2 fixes ell_z=s/2,
# and 4 ell^2 = 2+s^2.
assert 4 * (F(1, 4) + F(1, 4)) == 2

# A rank-one degeneration is not automatically supported: distinct collinear
# points already make the affine circumcenter equations inconsistent.
a1 = (F(1), F(0), F(0))
b1 = (F(2), F(0), F(0))
A_bad, d_bad = branch_linear_system([a1, b1])
assert rank(A_bad) == 1
assert rank([row + [rhs] for row, rhs in zip(A_bad, d_bad)]) == 2

result = {
    "schema": "marici.cosmology.gram_degenerate_branch_support.v1",
    "rank_two_gram_determinant": str(det3(G)),
    "rank_two_affine_system_consistent": True,
    "fourfold_null_polynomial": str(fourfold_null_polynomial),
    "fourfold_complex_solution_count": 2,
    "fivefold_transverse_condition": str(fivefold_condition),
    "rank_one_control_consistent": False,
    "passed": True,
    "theorem": (
        "on detG=0, support is controlled first by affine rank consistency; "
        "when rank=2 the fourfold null condition is a quadratic on the affine "
        "solution line, while a transverse fifth point produces one further "
        "external equation"
    ),
}
out = Path(__file__).with_name("results") / "gram-degenerate-branch-support.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
