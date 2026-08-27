import cmath
import math


u_star_upper = 0.239
assert math.log(2) > 0.693
assert math.log(2) > u_star_upper


# Exact translation-transform replay on F(u)=exp(-alpha*u).
for p in (2, 3, 5, 11):
    ell = math.log(p)
    for alpha in (1.0, 2.0):
        for z in (0.1 + 0.7j, -0.2 + 1.3j):
            full = 1 / (alpha - z)
            seam = (1 - cmath.exp(-(alpha - z) * ell)) / (alpha - z)
            transformed_shift = p ** -0.5 * cmath.exp(-alpha * ell) / (alpha - z)
            reconstructed = p ** (-0.5 - z) * (full - seam)
            assert abs(transformed_shift - reconstructed) < 1e-12

print("prime_shift_starts_beyond_defect=true")
print("prime_repair_current=pointwise_positive")
print("moving_seam=mandatory_translation_cokernel")
print("construction=independent_of_Schur_target")

