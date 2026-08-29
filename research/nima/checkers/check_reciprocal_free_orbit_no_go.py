points = ("u", "v")


def reciprocal(point: str) -> str:
    return "v" if point == "u" else "u"


grade = {"u": "a", "v": "1-a"}
scalar_null = {"u": True, "v": True}
height = {"u": 1, "v": 1}

# Exact involution and equivariant null locus.
for point in points:
    assert reciprocal(reciprocal(point)) == point
    assert scalar_null[point] == scalar_null[reciprocal(point)]
    assert height[point] == height[reciprocal(point)]

# Complementary grade transport is exact.
assert grade[reciprocal("u")] == "1-a"
assert grade[reciprocal("v")] == "a"

# Yet the reciprocal action has no fixed point.
fixed_points = [point for point in points if reciprocal(point) == point]
assert fixed_points == []

print("reciprocity: exact")
print("common height and scalar nullity: preserved")
print("fixed points: none")
print("verdict: reciprocal equivariance cannot force seam confinement")
