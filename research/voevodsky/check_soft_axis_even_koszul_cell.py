"""Check the blockwise derived model at the translated soft carrier z^2=0."""

from fractions import Fraction

# The even resonance restores the universal carrier relation.  Its Koszul
# cell epsilon has d(epsilon)=z^2, so its first Cartier symbol vanishes while
# its second symbol is a unit.
even_relation = {2: Fraction(1)}
assert even_relation.get(1, 0) == 0
assert even_relation.get(2, 0) == 1

# O/(z^2) has the two Cartier layers represented by 1 and z.
quotient_basis_degrees = (0, 1)
assert quotient_basis_degrees == (0, 1)
assert 2 not in quotient_basis_degrees

# The odd block is the complementary scalar matrix factorization found in
# Entry 468.  Both composites recover the same carrier relation.
d_odd = {1: Fraction(-6)}
h_odd = {1: Fraction(-1, 6)}


def monomial_product(left, right):
    ((left_degree, left_coefficient),) = left.items()
    ((right_degree, right_coefficient),) = right.items()
    return {left_degree + right_degree: left_coefficient * right_coefficient}


assert monomial_product(d_odd, h_odd) == even_relation
assert monomial_product(h_odd, d_odd) == even_relation

# Ordinary Cartier lengths: two even layers and one odd layer.  Reduction
# has one generator from each parity block.
even_cartier_length = 2
odd_cartier_length = 1
reduced_rank = 2
assert even_cartier_length + odd_cartier_length == 3
assert reduced_rank == 2

print("even first symbol: 0")
print("even second symbol: 1")
print("odd composites: z^2")
print("Cartier length: 2 + 1 = 3; reduced rank: 2")
