from fractions import Fraction


def conjugate(z: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (z[0], -z[1])


def holomorphic_reciprocal(z: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (1 - z[0], -z[1])


def reciprocal_conjugate(z: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (1 - z[0], z[1])


seam = (Fraction(1, 2), Fraction(3, 1))
off_seam = (Fraction(3, 4), Fraction(3, 1))

# A nonreal seam point is not fixed by holomorphic reciprocity.
assert holomorphic_reciprocal(seam) != seam
assert reciprocal_conjugate(seam) == seam

# An off-seam point is moved horizontally by reciprocal conjugation.
assert reciprocal_conjugate(off_seam) != off_seam
assert reciprocal_conjugate(reciprocal_conjugate(off_seam)) == off_seam

# J and K commute, and their composite is the seam reflection I.
for point in (seam, off_seam):
    jk = holomorphic_reciprocal(conjugate(point))
    kj = conjugate(holomorphic_reciprocal(point))
    assert jk == kj == reciprocal_conjugate(point)

generic_orbit = {
    off_seam,
    holomorphic_reciprocal(off_seam),
    conjugate(off_seam),
    reciprocal_conjugate(off_seam),
}
assert len(generic_orbit) == 4

print("holomorphic reciprocity fixed locus: not the critical line")
print("reciprocal conjugation fixed locus: critical line")
print("generic symmetry packet: Klein-four orbit of size four")
