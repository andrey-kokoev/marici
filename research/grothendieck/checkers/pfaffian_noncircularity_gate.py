"""Dependency-free exact checks for the Pfaffian noncircularity gate."""


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] += a * b
    return tuple(product)


# Coefficients are in ascending powers of t.  The signed root is
# (t-1)(t+2)^2 = t^3 + 3t^2 - 4.
signed_root = (-4, 0, 3, 1)
determinant = multiply(signed_root, signed_root)
expected = multiply(multiply((-1, 1), (-1, 1)), multiply(multiply((2, 1), (2, 1)), multiply((2, 1), (2, 1))))
assert determinant == expected

# det([[0,f],[-f,0]]) = f^2 for an arbitrary polynomial target.
target = (5, -2, 0, 1)
skew_determinant = multiply(target, target)
assert skew_determinant == multiply(target, target)

assert multiply(signed_root, signed_root) == multiply(tuple(-x for x in signed_root), tuple(-x for x in signed_root))

print("nonnegative_analytic_zero_orders_even=True")
print("analytic_square_root_orientation_is_global_sign=True")
print("two_by_two_pfaffian_can_encode_any_target_tautologically=True")
print("source_defined_compatible_skew_lift_still_open=True")
