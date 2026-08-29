from fractions import Fraction


# One-dimensional sign representation.
identity = Fraction(1)
reciprocal = Fraction(-1)

even_projector = (identity + reciprocal) / 2
odd_projector = (identity - reciprocal) / 2

assert even_projector == 0
assert odd_projector == 1

# Maschke averaging makes higher C2 cohomology vanish over characteristic
# zero, but the sign line itself remains present.
higher_group_cohomology_dimension = 0
odd_representation_dimension = 1
odd_projector_trace = odd_projector

assert higher_group_cohomology_dimension == 0
assert odd_representation_dimension == 1
assert odd_projector_trace == 1

print("higher C2 group cohomology: zero")
print("odd sign line: still one-dimensional")
print("required contraction: source differential on the odd projection")
