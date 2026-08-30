import cmath
from fractions import Fraction


def potential(w, tau):
    return Fraction(w**3, 3) - tau * w


def readout(w, tau):
    return w**2 - tau


def roots(tau):
    root = cmath.sqrt(tau)
    return (-root, root)


assert potential(2, 3) - potential(1, 3) == Fraction(-2, 3)
assert readout(0, 0) == 0
assert readout(1, 0) - 2 * readout(0, 0) + readout(-1, 0) == 2
assert 4 * 4 > 0 and 4 * -4 < 0

# The signed side of the discriminant determines whether the two critical
# points lie on the real seam coordinate or form an off-seam conjugate pair.
assert roots(4) == (-2 + 0j, 2 + 0j)
assert roots(-4) == (-2j, 2j)

print("newman_cubic_fold_transition: 6/6 exact gates passed")
