"""Audit boundary valuations in the intrinsic odd Cartier frame."""


# Valuations at (b=+1,b=-1), suppressing powers of a.
eta = (3, 4)  # a*t^3*(b+1) = a*(b-1)^3*(b+1)^4/8
h = (0, 1)  # 3*a^3*(b+1)
g = (1, 1)  # a^3*(1-b^2)
residue_plus_extension = (0, 1)  # g/(b-1) = -a^3*(b+1)
residue_minus_extension = (1, 0)  # g/(b+1) = a^3*(1-b)


def relative(section, frame):
    return tuple(x - y for x, y in zip(section, frame))


assert relative(h, eta) == (-3, -3)
assert relative(residue_plus_extension, eta) == (-3, -3)
assert relative(residue_minus_extension, eta) == (-2, -4)
assert any(order < 0 for order in relative(h, eta))
assert any(order < 0 for order in relative(residue_plus_extension, eta))

print("intrinsic odd frame valuations (+,-): (3,4)")
print("h relative valuations: (-3,-3)")
print("plus-residue relative valuations: (-3,-3)")
print("bare scalar cancellation: true in fraction field")
print("regular intrinsic boundary morphism: not established")
