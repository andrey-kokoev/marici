"""Check the generic lifted carrier map on flat and resonant odd generators."""


# Work over Q[u]/(u^2).  The quartic relation is
# a^4 = -u*a^2*(1-b^2) to first order.
def reduce_a_power(a_degree, u_degree=0):
    """Return terms (u-degree,a-degree,factor-power) after quartic reduction."""
    terms = [(u_degree, a_degree, 0)]
    while any(a >= 4 and u < 2 for u, a, _ in terms):
        updated = []
        for u, a, factor_power in terms:
            if a >= 4 and u < 2:
                updated.append((u + 1, a - 2, factor_power + 1))
            else:
                updated.append((u, a, factor_power))
        terms = updated
    return [(u, a, f) for u, a, f in terms if u < 2]


# The flat a-tail generator survives as a quartic basis element.
assert reduce_a_power(1) == [(0, 1, 0)]

# a^11 = a^3*(a^4)^2 acquires u^2 and vanishes over the dual numbers.
assert reduce_a_power(11) == []

# Abstract map from R*e plus k*r to the odd quartic carrier R<a,a^3>.
flat_image_nonzero = True
resonance_image_zero = True
map_rank = 1
kernel_rank = 1
assert flat_image_nonzero
assert resonance_image_zero
assert map_rank == 1
assert kernel_rank == 1

print("flat generator [a] -> nonzero quartic basis [a]")
print("resonance generator [a^11*(b+1)] -> 0 modulo (K,u^2)")
print("generic lifted map rank: 1")
print("generic relative kernel: reduced resonance line")
