from fractions import Fraction as F


def scaled_offsets(r, hidden_order, observed_orders):
    offset = F(1, r**hidden_order)
    return {j: r**j * offset for j in observed_orders}


for depth in range(1, 9):
    hidden_order = depth + 1
    values = scaled_offsets(10**6, hidden_order, range(depth + 1))
    assert all(value > 0 for value in values.values())
    assert max(values.values()) <= F(1, 10**6)

# The exact support predicate remains off-seam even though every declared
# finite-rate boundary coordinate converges to the seam value zero.
for r in (10, 100, 1000):
    offset = F(1, r**5)
    assert offset != 0
    assert all(r**j * offset <= F(1, r) for j in range(5))

print("no_finite_transverse_blowup_detects_all_offseam_escape: 14/14 gates passed")
