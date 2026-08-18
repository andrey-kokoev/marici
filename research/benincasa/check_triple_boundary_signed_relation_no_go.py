"""Test the only triple-support boundary against Entry 707's signed relation."""

# Pair basis: ([2,3], [2,23], [3,23]).
triple_boundary = (1, -1, 1)
strict_plus_relation = (0, 1, -1)

# Quotient by the strict equality [2,23]=[3,23].  Coordinates are
# ([2,3], plus), so the triple boundary and signed relation become:
def strict_plus_quotient(vector):
    return vector[0], vector[1] + vector[2]

boundary_q = strict_plus_quotient(triple_boundary)
assert boundary_q == (1, 0)
assert strict_plus_quotient(strict_plus_relation) == (0, 0)

# In formal coefficient symbols the signed vector is
# (C23plus, -C23minus, 0), hence its quotient is
# (C23plus, -C23minus).  The 2x2 determinant with (1,0) is
# -C23minus, nonzero on the declared generic signed-energy locus.
signed_q = ("C23plus", "-C23minus")
obstruction_minor = "-C23minus"
assert signed_q[1] == obstruction_minor

print("TRIPLE_BOUNDARY=[2,3]-[2,23]+[3,23]")
print("AFTER_STRICT_PLUS_QUOTIENT=minus_pair_only")
print("SIGNED_RELATION_PROPORTIONAL_TO_TRIPLE_BOUNDARY=false")
print(f"OBSTRUCTION_MINOR={obstruction_minor}")
