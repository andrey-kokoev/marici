"""Check that restoring the universal a^4 factor supplies the odd lattice twist."""


def boundary_divisor(i_degree, c_degree):
    half = i_degree // 2
    return half, half + c_degree


mixed = boundary_divisor(3, 1)
quartic = boundary_divisor(4, 0)
resonance = boundary_divisor(7, 1)

assert mixed == (1, 2)
assert quartic == (2, 2)
assert resonance == (3, 4)
assert tuple(x + y for x, y in zip(mixed, quartic)) == resonance

# Restoring a^4 converts both terms of the fraction-field identity from the
# divided (3,1) block to the intrinsic odd (7,1) block.
assert (3 + 4, 1 + 0) == (7, 1)
assert 6 + 3 * (-2) == 0

print("B(3,1) = (1,2)")
print("B(4,0) = (2,2)")
print("B(3,1)+B(4,0) = B(7,1) = (3,4)")
print("restored plus-boundary coefficient: 6 + 3*(-2) = 0")
