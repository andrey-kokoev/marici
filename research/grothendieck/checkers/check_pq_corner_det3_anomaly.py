import cmath


def det3(x: complex) -> complex:
    return (1 + x) * cmath.exp(-x + x * x / 2)


def boundary(x: complex) -> complex:
    return cmath.exp(x - x * x / 2)


for a, b in ((0.1, 0.2), (0.1 + 0.2j, -0.05 + 0.1j), (-0.2, 0.3)):
    c = a + b + a * b
    anomaly = a * b * (a + b + a * b / 2)

    det_ratio = det3(c) / (det3(a) * det3(b))
    boundary_ratio = boundary(c) / (boundary(a) * boundary(b))

    assert abs(det_ratio - cmath.exp(anomaly)) < 1e-12
    assert abs(boundary_ratio - cmath.exp(-anomaly)) < 1e-12
    assert abs(det_ratio * boundary_ratio - 1) < 1e-12
    assert abs((1 + c) - (1 + a) * (1 + b)) < 1e-12
    assert abs((1 + a + b) - (1 + a) * (1 + b)) > 1e-6

print("prime_incidences=commuting_overlapping")
print("shared_pq_corner=ab")
print("det3_anomaly=ab_times_a_plus_b_plus_ab_over_2")
print("primitive_square_boundary=cancels_anomaly")

