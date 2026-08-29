from dataclasses import dataclass


@dataclass(frozen=True)
class GradedClass:
    grade: str
    coefficient: int


direct = GradedClass("direct_grade", 1)
reciprocal = GradedClass("reciprocal_grade", 1)


def augmentation(x: GradedClass) -> int:
    return x.coefficient


def zero_augmentation(_: GradedClass) -> int:
    return 0


# Scalar equality forgets the grade distinction.
assert augmentation(direct) == augmentation(reciprocal)
assert zero_augmentation(direct) == zero_augmentation(reciprocal)

# The strict graded equalizer rejects the same pair.
assert direct != reciprocal

# Nonzero homogeneous classes can agree strictly only after their grades are
# identified. This models the seam equation without inspecting scalar zeros.
seam_direct = GradedClass("seam_grade", 1)
seam_reciprocal = GradedClass("seam_grade", 1)
assert seam_direct == seam_reciprocal
assert seam_direct.coefficient != 0

print("scalar equalizer: admits hostile cross-grade pair")
print("strict graded equalizer: rejects hostile pair")
print("nonzero strict equality: admitted after grade coincidence")
