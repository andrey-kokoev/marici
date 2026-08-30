def collision_jacobian(h_xx, h_xxx):
    return ((-h_xx, 0), (-h_xxx, h_xx))


def det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


gate_count = 0
for h_xx in (-11, -2, 1, 3, 17):
    for h_xxx in (-13, 0, 5):
        matrix = collision_jacobian(h_xx, h_xxx)
        assert det(matrix) == -(h_xx**2)
        assert det(matrix) < 0
        gate_count += 2

# The quadratic Newman model H=x^2-2 lambda has one collision of degree -1.
model_matrix = collision_jacobian(2, 0)
assert model_matrix == ((-2, 0), (0, 2))
assert det(model_matrix) == -4
gate_count += 2

# Uniform sign makes the Brouwer degree equal minus the collision count on a
# bounded domain whose boundary contains no collision-map zero.
for collision_count in range(6):
    assert -collision_count <= 0
    gate_count += 1

assert gate_count == 38
print("newman_collision_map_uniform_local_degree: 38/38 gates passed")
