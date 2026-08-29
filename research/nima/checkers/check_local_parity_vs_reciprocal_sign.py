from fractions import Fraction


# Basis order: (++), (+-), (-+), (--), where the first sign is local parity
# and the second is reciprocal character.
identity = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
local_parity = (1, 1, -1, -1)
reciprocal_sign = (1, -1, 1, -1)


def projector(diagonal: tuple[int, ...]) -> tuple[Fraction, ...]:
    return tuple(Fraction(1 - value, 2) for value in diagonal)


p_odd = projector(local_parity)
j_odd = projector(reciprocal_sign)

assert p_odd == (0, 0, 1, 1)
assert j_odd == (0, 1, 0, 1)
assert p_odd != j_odd

# The (+,-) vector is local-even and reciprocal-odd.
probe_index = 1
assert p_odd[probe_index] == 0
assert j_odd[probe_index] == 1

# The diagonal actions commute because they are independent characters.
for index in range(4):
    assert local_parity[index] * reciprocal_sign[index] == reciprocal_sign[index] * local_parity[index]

print("local parity and reciprocal sign: commuting, distinct involutions")
print("hostile state: local-even and reciprocal-odd")
print("required gate: source intertwiner or joint character differential")
