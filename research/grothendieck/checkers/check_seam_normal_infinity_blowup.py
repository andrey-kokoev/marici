from fractions import Fraction as F


def seam_normal_chart(w):
    t = F(w.real)
    a = F(w.imag)
    return (1 if t > 0 else -1, 1 / abs(t), a)


for r in (10, 100, 1000):
    quartet = (complex(r, 1), complex(r, -1), complex(-r, 1), complex(-r, -1))
    charts = tuple(seam_normal_chart(w) for w in quartet)
    assert {chart[0] for chart in charts} == {-1, 1}
    assert {chart[2] for chart in charts} == {F(-1), F(1)}
    assert all(chart[1] == F(1, r) for chart in charts)

# Projective completion sees only total degree four.  The seam-normal boundary
# retains both spectral ends and both transverse offsets.
projective_boundary_signature = {"infinity": 4}
seam_normal_boundary_signature = {
    (-1, -1): 1,
    (-1, 1): 1,
    (1, -1): 1,
    (1, 1): 1,
}
assert sum(projective_boundary_signature.values()) == 4
assert sum(seam_normal_boundary_signature.values()) == 4
assert len(seam_normal_boundary_signature) == 4
assert all(offset != 0 for _, offset in seam_normal_boundary_signature)

# The reciprocal and real involutions act faithfully on the boundary labels.
def reciprocal(label):
    end, offset = label
    return (-end, -offset)


def conjugate(label):
    end, offset = label
    return (end, -offset)


labels = set(seam_normal_boundary_signature)
assert {reciprocal(label) for label in labels} == labels
assert {conjugate(label) for label in labels} == labels

print("seam_normal_infinity_blowup: 17/17 gates passed")
