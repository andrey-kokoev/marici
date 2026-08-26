import json
from fractions import Fraction as F


def split_area(t):
    # t is area measured in units of 2*pi.
    grade = t.numerator // t.denominator
    return grade, t - grade


def compose(left, right):
    m, theta = left
    n, phi = right
    carry, residue = split_area(theta + phi)
    return m + n + carry, residue


areas = [F(7, 5), F(9, 8), F(13, 7), F(4, 9)]
lifts = [split_area(t) for t in areas]

left_assoc = compose(compose(lifts[0], lifts[1]), lifts[2])
right_assoc = compose(lifts[0], compose(lifts[1], lifts[2]))
permuted = compose(compose(lifts[2], lifts[0]), lifts[1])
total = split_area(sum(areas[:3], F(0)))

# If both position and frequency spans are refined, the total rectangle has
# cross areas that cannot be reconstructed from the two diagonal rectangles.
dq1, dq2 = F(2, 3), F(5, 4)
dx1, dx2 = F(3, 5), F(7, 6)
full_area = (dq1 + dq2) * (dx1 + dx2)
diagonal_only = dq1 * dx1 + dq2 * dx2
cross_area = dq1 * dx2 + dq2 * dx1

result = {
    "schema": "marici.grothendieck.maslov_carry_cocycle.v1",
    "checks": {
        "carry_composition_is_associative": left_assoc == right_assoc,
        "carry_composition_is_commutative_at_endpoint": left_assoc == permuted,
        "composed_lift_equals_total_area_lift": left_assoc == total,
        "two_axis_refinement_requires_cross_rectangles": full_area == diagonal_only + cross_area and cross_area != 0,
    },
    "three_area_total_lift": [str(total[0]), str(total[1])],
    "cross_area": str(cross_area),
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
