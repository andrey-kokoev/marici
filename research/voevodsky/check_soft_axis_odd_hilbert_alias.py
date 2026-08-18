"""Show the Hilbert-polynomial alias behind the odd defect normal form."""


def higher_a3_tail(cutoff):
    # a^3 b^j, j >= 1, total degree <= cutoff.
    return max(0, cutoff - 3)


def resonance_endpoint(cutoff):
    # a^11 b has total degree twelve.
    return int(cutoff >= 12)


def naive_shift_three_tail(cutoff):
    # A hypothetical single Q[b] generator in degree three.
    return max(0, cutoff - 2)


# The two models have the same stable Hilbert polynomial but different
# low-degree support and different generator content.
for cutoff in range(12, 40):
    assert higher_a3_tail(cutoff) + resonance_endpoint(cutoff) == naive_shift_three_tail(cutoff)

assert higher_a3_tail(3) + resonance_endpoint(3) == 0
assert naive_shift_three_tail(3) == 1
assert higher_a3_tail(11) + resonance_endpoint(11) == 8
assert naive_shift_three_tail(11) == 9

print("actual stable normal form: a^3*b*Q[b] plus endpoint <a^11*b>")
print("stable cumulative dimension: D-2")
print("naive degree-three free tail has same stable polynomial")
print("module identification from stable Hilbert polynomial: impossible")
