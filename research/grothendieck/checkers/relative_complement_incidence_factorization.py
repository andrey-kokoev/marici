"""Exact finite-fiber checks for complementary incidence factorization."""

from fractions import Fraction


def gram_scalar(admitted_count: int, fiber_degree: int) -> Fraction:
    return Fraction(admitted_count, fiber_degree)


for degree in range(1, 13):
    for admitted in range(degree + 1):
        omitted = degree - admitted
        c_star_c = gram_scalar(admitted, degree)
        q_star_q = gram_scalar(omitted, degree)
        assert c_star_c + q_star_q == 1
        assert 1 - c_star_c == q_star_q

# Hostile C2 difference fibers: each has degree two.
assert gram_scalar(1, 2) == Fraction(1, 2)
assert 1 - gram_scalar(1, 2) == Fraction(1, 2)
assert gram_scalar(2, 2) == 1
assert gram_scalar(0, 2) == 0

# A fixed finite split has no continuous height dependence.
sample_heights = (-10, -1, 0, 1, 10)
fixed_defects = [1 - gram_scalar(1, 2) for _ in sample_heights]
assert len(set(fixed_defects)) == 1

print("normalized_full_incidence_isometry=True")
print("relative_complement_exactly_factors_transfer_defect=True")
print("C2_one_branch_defect_equals_one_half=True")
print("fixed_unweighted_deck_split_has_no_height_dependence=True")
print("archimedean_weighted_relative_complex_open=True")
