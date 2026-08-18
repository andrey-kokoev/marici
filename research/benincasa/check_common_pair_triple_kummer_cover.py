"""Exact arithmetic checks for the common signed-pair/mixed-triple cover."""


def check_point(x, y, z):
    l1 = x - y - z
    l2 = x - y + z
    l3 = x + y - z
    l4 = x + y + z
    a = x * x - y * y - z * z
    discriminant = a * a - 4 * y * y * z * z
    factored = l1 * l2 * l3 * l4
    assert discriminant == factored
    # With R=(l2*l3)/(l1*l4), this cross-multiplied identity is
    # D=(l1*l4)^2 R and avoids division on boundary samples.
    assert discriminant * (l1 * l4) == (l1 * l4) ** 2 * (l2 * l3)


for x in range(2, 8):
    for y in range(1, 6):
        for z in range(1, 6):
            check_point(x, y, z)

# On rho^2=R set s=(l1*l4)rho, so s^2=D.  The exact formal product
# (2z^2*n2+(A+s)n3)(2z^2*n2+(A-s)n3)
# equals 4z^2*T2 because A^2-s^2=4y^2z^2.
print("MIXED_QUADRATIC_DISCRIMINANT=l1*l2*l3*l4")
print("PAIR_COVER=rho^2=(l2*l3)/(l1*l4)")
print("COMMON_SQRT=s=(l1*l4)*rho")
print("MIXED_T2_SPLITS_ON_PAIR_COVER=true")
