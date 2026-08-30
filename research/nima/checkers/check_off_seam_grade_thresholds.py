from fractions import Fraction


sector_samples = (
    Fraction(51, 100),
    Fraction(3, 5),
    Fraction(3, 4),
    Fraction(1, 1),
)


def absolutely_convergent_grade(sigma: Fraction, grade: int) -> bool:
    return grade * sigma > 1


for sigma in sector_samples:
    assert sigma > Fraction(1, 2)
    assert all(absolutely_convergent_grade(sigma, grade) for grade in range(2, 20))

for sigma in (Fraction(51, 100), Fraction(3, 5), Fraction(3, 4), Fraction(1, 1)):
    assert not absolutely_convergent_grade(sigma, 1)

assert not absolutely_convergent_grade(Fraction(1, 2), 2)
assert absolutely_convergent_grade(Fraction(1, 2), 3)

print("all grades k>=2 converge absolutely at sampled points with Re(s)>1/2")
print("primitive grade fails through Re(s)=1")
print("square grade is critical exactly on the seam")
print("grades k>=3 converge on the seam")
