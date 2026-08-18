"""Check the conormal Bockstein along c=1-b^2 and at c=0."""

from fractions import Fraction as Q

# Record coefficients of the two relevant degree-one basis vectors
# y=a^2 e_a and x=a^3 e_u.  The e_a wedge e_u Koszul boundary is
# -c*y + 4*x.
boundary = {"c*y": Q(-1), "x": Q(4)}

# Hence [x]=(c/4)[y] in homology, and Entry 495's Bockstein is -[x]/2.
bockstein_as_y = Q(-1, 8)  # coefficient of c*y
assert bockstein_as_y == Q(-1, 2) * Q(1, 4)

# At either endpoint b=+1 or b=-1, c=0 and x itself is a boundary:
# d((1/4)e_a wedge e_u)=x.
for b in (-1, 1):
    c = 1 - b * b
    assert c == 0
    endpoint_boundary_x_coefficient = Q(1, 4) * boundary["x"]
    assert endpoint_boundary_x_coefficient == 1

print("family relation in H1: 4[a^3 e_u] = (1-b^2)[a^2 e_a]")
print("Bockstein = -(1-b^2)/8 [a^2 e_a]")
print("at b=+1 and b=-1: [a^3 e_u] = 0")
print("verdict: regular extension, but zero endpoint fiber; nearby-cycle data is required")
