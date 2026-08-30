import cmath
import math


def full(alpha, z):
    return 1 / (alpha - z)


def seam(alpha, length, z):
    return (1 - cmath.exp(-(alpha - z) * length)) / (alpha - z)


def shifted_seam(alpha, first, second, z):
    coefficient = math.exp(-first / 2)
    return coefficient * cmath.exp(-alpha * first) * seam(alpha, second, z)


for p, q in ((2, 3), (2, 5), (3, 7)):
    ell = math.log(p)
    m = math.log(q)
    for alpha in (1.0, 2.0):
        for z in (0.1 + 0.7j, -0.2 + 1.1j):
            left = seam(alpha, ell + m, z)
            right = seam(alpha, ell, z) + cmath.exp((z + 0.5) * ell) * shifted_seam(alpha, ell, m, z)
            assert abs(left - right) < 1e-12

            direct = cmath.exp(-(z + 0.5) * (ell + m)) * (full(alpha, z) - left)
            expected = math.exp(-(ell + m) / 2) * cmath.exp(-alpha * (ell + m)) * full(alpha, z)
            assert abs(direct - expected) < 1e-12

print("two_prime_source_translation=commutative")
print("moving_seams=exact_cocycle")
print("source_transition_unit=one")
print("joint_colligation_determinant=still_required")

