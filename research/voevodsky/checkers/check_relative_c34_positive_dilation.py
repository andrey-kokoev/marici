import json
import math
from pathlib import Path

OUT = Path(__file__).with_name("relative-c34-positive-dilation-v1.json")


def zeros(r, c):
    return [[0.0 for _ in range(c)] for _ in range(r)]


def eye(n):
    a = zeros(n, n)
    for k in range(n):
        a[k][k] = 1.0
    return a


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(ar, bc)) for bc in bt] for ar in a]


def vstack(*blocks):
    out = []
    for block in blocks:
        out.extend([row[:] for row in block])
    return out


def block2(a, b, c, d):
    return [ar + br for ar, br in zip(a, b)] + [cr + dr for cr, dr in zip(c, d)]


def maxabs(a):
    return max(abs(x) for row in a for x in row)


def gram(a):
    return matmul(transpose(a), a)


n = 4
i = eye(n)
z = zeros(n, n)

# P projects onto e1,e2. Q0=P. QT projects onto two rationally rotated vectors
# (3e1+4e3)/5 and (3e2+4e4)/5.
p = zeros(n, n)
p[0][0] = p[1][1] = 1.0
q0 = [row[:] for row in p]
qt = zeros(n, n)
for a, b in ((0, 2), (1, 3)):
    qt[a][a] = 9.0 / 25.0
    qt[a][b] = qt[b][a] = 12.0 / 25.0
    qt[b][b] = 16.0 / 25.0

dq = sub(qt, q0)
j2 = block2(i, z, z, scale(-1.0, i))
ft = vstack(qt, sub(i, qt))
f0 = vstack(q0, sub(i, q0))
psi = scale(1.0 / math.sqrt(2.0), vstack(ft, f0))
z2 = zeros(2 * n, 2 * n)
j4 = block2(j2, z2, z2, scale(-1.0, j2))

c = scale(0.5, add(ft, f0))
d = scale(0.5, sub(ft, f0))
psi_rot = vstack(c, d)
j4_rot = block2(z2, j2, j2, z2)

# Eight-leg ordered feature.
theta = scale(1.0 / math.sqrt(2.0), vstack(matmul(psi, p), psi))
z4 = zeros(4 * n, 4 * n)
k8 = block2(z4, j4, j4, z4)
# Real matrices represent the skew identity after multiplying both sides by i:
# theta^T [[0,-J],[J,0]] theta = (P*dQ-dQ*P)/2.
k8_skew_real = block2(z4, scale(-1.0, j4), j4, z4)

# B=P QT P is diagonal 9/25 on ran(P). Its first split is (B, sqrt(B(I-B))).
b = matmul(matmul(p, qt), p)
defect = zeros(n, n)
defect[0][0] = defect[1][1] = 12.0 / 25.0
first_split = vstack(b, defect)

checks = {
    "qt_projection": maxabs(sub(matmul(qt, qt), qt)),
    "q0_projection": maxabs(sub(matmul(q0, q0), q0)),
    "four_leg_isometry": maxabs(sub(gram(psi), i)),
    "four_leg_signed_readout": maxabs(sub(matmul(matmul(transpose(psi), j4), psi), dq)),
    "hadamard_positive_gram": maxabs(sub(add(gram(c), gram(d)), i)),
    "hadamard_difference_gram": maxabs(sub(gram(d), scale(0.5, matmul(dq, dq)))),
    "hadamard_cross_readout": maxabs(sub(matmul(matmul(transpose(psi_rot), j4_rot), psi_rot), dq)),
    "eight_leg_hermitian_placement": maxabs(
        sub(matmul(matmul(transpose(theta), k8), theta), scale(0.5, add(matmul(p, dq), matmul(dq, p))))
    ),
    "eight_leg_skew_placement_after_i_removed": maxabs(
        sub(matmul(matmul(transpose(theta), k8_skew_real), theta), scale(0.5, sub(matmul(dq, p), matmul(p, dq))))
    ),
    "first_defect_split_gram": maxabs(sub(gram(first_split), b)),
}

tolerance = 1e-12
passed = all(value < tolerance for value in checks.values())
result = {
    "schema": "marici.voevodsky.relative-c34-positive-dilation.v1",
    "dimension": n,
    "rotation_cos_sin": ["3/5", "4/5"],
    "dependencies": "python standard library only",
    "tolerance": tolerance,
    "checks": checks,
    "matrices": {"source_gram": gram(ft), "observer_gram": gram(f0), "signed_cross_readout": matmul(matmul(transpose(psi), j4), psi)},
    "passed": passed,
    "conclusion": (
        "The explicit finite-dimensional projection pair validates the four-leg relative isometry, Hadamard common/difference rotation, eight-leg ordered/skew readouts, and first dyadic defect split."
        if passed
        else "At least one relative C34 projection identity failed."
    ),
    "scope": "Algebraic finite-cutoff audit only; no semilocal trace-ideal, regulator-limit, gamma-normalization, or arithmetic claim.",
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not passed:
    raise SystemExit(1)
