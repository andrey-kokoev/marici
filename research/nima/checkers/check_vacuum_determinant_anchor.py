from fractions import Fraction


vacuum = Fraction(1)


def incidence(scale: Fraction, state: Fraction) -> Fraction:
    return scale * state


positive_image = incidence(Fraction(1), vacuum)
negative_image = incidence(Fraction(-1), vacuum)
zero_image = incidence(Fraction(0), vacuum)

assert positive_image == 1
assert negative_image == -1
assert zero_image == 0

# Both signs have identical rank, magnitude, and Real equivariance.
assert abs(positive_image) == abs(negative_image)
assert positive_image != negative_image

# Finite nonvanishing can collapse in completion.
cutoff_images = [incidence(Fraction(1, n), vacuum) for n in range(1, 33)]
assert all(value != 0 for value in cutoff_images)
assert cutoff_images[-1] == Fraction(1, 32)

print("a and -a: structurally equal, oppositely oriented")
print("vacuum in incidence kernel: no determinant anchor")
print("cutoffwise nonzero anchor: may collapse at completion")
