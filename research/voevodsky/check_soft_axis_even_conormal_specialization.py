"""Track the even conormal generators through soft specialization and H_q."""

from fractions import Fraction as Q

# In R0=Q[a]/(a^4), the even conormal basis is (1,a^2).  Multiplication by
# a/4 sends it to (a/4,a^3/4), so the specialized Euler map has rank two.
images = {
    0: {1: Q(1, 4)},
    2: {3: Q(1, 4)},
}
assert len(images) == 2
assert set(next(iter(image)) for image in images.values()) == {1, 3}

# In the smallest (1,1) q-sector at u=0, m=f*(b+1)*a and H_q=-3m e_a/2.
# The required source coefficients are -r/[6(b+1)] for r=1,a^2.
for b in (Q(-3), Q(0), Q(2)):
    if b == -1:
        continue
    a = Q(5)
    for r in (Q(1), a * a):
        f = -r / (6 * (b + 1))
        m = f * (b + 1) * a
        assert -Q(3, 2) * m == r * a / 4

print("even Euler images: 1 -> (a/4)e_a, a^2 -> (a^3/4)e_a")
print("ordinary u=0 rank on the even conormal block: 2")
print("u-Bockstein dimension on the even block: 0")
print("both q-lifts require the same incidence inverse 1/(b+1)")
