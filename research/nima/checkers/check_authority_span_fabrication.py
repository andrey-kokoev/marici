"""Finite witness that linear span fabricates cross-authority fillers."""

# Coordinates are over F_2. The differential is the 2x2 identity.
e1 = (1, 0)
e2 = (0, 1)
obstruction = (1, 1)


def differential(cell):
    return cell


domain_a = {e1}
domain_b = {e2}
mixed = tuple((e1[i] + e2[i]) % 2 for i in range(2))

a_fills = any(differential(x) == obstruction for x in domain_a)
b_fills = any(differential(x) == obstruction for x in domain_b)
span_fills = differential(mixed) == obstruction

assert not a_fills
assert not b_fills
assert mixed == obstruction
assert span_fills

witness = {
    "code": "cross_authority_span_fabrication",
    "obstruction": ["z1", "z2"],
    "partial_fillers": {"domain_A": ["z1"], "domain_B": ["z2"]},
    "span_would_fill": True,
    "crossing_constructor_present": False,
}

print("domain A fills:", a_fills)
print("domain B fills:", b_fills)
print("linear span fills:", span_fills)
print("rejection witness:", witness)
print("PASS: alternative authority branches cannot be replaced by their span")
