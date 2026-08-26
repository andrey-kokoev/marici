import cmath
import json
import math


points = [0.4, 1.1, 2.3]
weights = [1.0, 0.7, 0.2]
x = 1.7
y = 0.31
z = complex(x, y)


def F(w):
    return sum(a * cmath.exp(1j * w * u) for a, u in zip(weights, points))


direct = abs(F(-z)) ** 2 - abs(F(z)) ** 2
double_sum = 0.0
for a, u in zip(weights, points):
    for b, v in zip(weights, points):
        double_sum += 2.0 * a * b * math.sinh(y * (u + v)) * math.cos(x * (u - v))

anti_a = complex(0.3, 1.2)
anti_vector_krein_norm = abs(-anti_a) ** 2 - abs(anti_a) ** 2

result = {
    "schema": "marici.grothendieck.boundary_krein_debranges_identity.v1",
    "checks": {
        "krein_norm_equals_oscillatory_source_double_sum": abs(direct - double_sum) < 1e-11,
        "antisymmetric_boundary_line_is_null": anti_vector_krein_norm == 0.0,
        "source_positivity_does_not_remove_cosine_signs": any(math.cos(x * (u - v)) < 0 for u in points for v in points),
    },
    "krein_norm": direct,
    "double_sum": double_sum,
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
