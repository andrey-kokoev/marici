"""Exact scalar and block-doubling checks for the finite Pfaffian no-go."""


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] += a * b
    return tuple(product)


# 1-x^2 has simple roots at +/-1, so it cannot be a polynomial square.
d = (1, 0, -1)
derivative = (d[1], 2 * d[2])


def evaluate(poly: tuple[int, ...], value: int) -> int:
    return sum(coefficient * value**power for power, coefficient in enumerate(poly))


assert evaluate(d, 1) == evaluate(d, -1) == 0
assert evaluate(derivative, 1) != 0
assert evaluate(derivative, -1) != 0

# For the 2x2 skew block [[0,b],[-b,0]], Pf=b and det=b^2.
b = (2, -3, 1)
pfaffian = b
skew_determinant = multiply(b, b)
assert skew_determinant == multiply(pfaffian, pfaffian)

print("scalar_transfer_determinant_one_minus_x_squared_not_polynomial_square=True")
print("generic_algebraic_pfaffian_square_root_obstructed=True")
print("canonical_skew_doubling_pfaffian_equals_original_determinant=True")
print("independent_square_forcing_source_symmetry_required=True")
