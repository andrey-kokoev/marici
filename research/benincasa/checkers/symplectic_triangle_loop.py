"""Exact audit of the Gaussian symplectic triangle-loop invariant."""

import json
from fractions import Fraction
from pathlib import Path


F = Fraction
J2 = [[F(0), F(1)], [F(-1), F(0)]]
I2 = [[F(1), F(0)], [F(0), F(1)]]
Z2 = [[F(1), F(0)], [F(0), F(-1)]]


def zeros(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n):
    a = zeros(n, n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def scale(s, a):
    return [[s * x for x in row] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def set_block(a, i, j, block):
    for r in range(2):
        for c in range(2):
            a[2 * i + r][2 * j + c] = block[r][c]


def block(a, i, j):
    return [[a[2 * i + r][2 * j + c] for c in range(2)] for r in range(2)]


def block_diag(blocks):
    out = zeros(2 * len(blocks), 2 * len(blocks))
    for i, b in enumerate(blocks):
        set_block(out, i, i, b)
    return out


def loop_value(v):
    c12 = block(v, 0, 1)
    c23 = block(v, 1, 2)
    c31 = block(v, 2, 0)
    return trace(mul(mul(mul(mul(mul(J2, c12), J2), c23), J2), c31))


# Source-derived rational pure covariance: overlapping two-mode squeezers on
# (1,2) and (2,3).
sq = eye(6)
ch, sh = F(5, 3), F(4, 3)
set_block(sq, 0, 0, scale(ch, I2))
set_block(sq, 1, 1, scale(ch, I2))
set_block(sq, 0, 1, scale(sh, Z2))
set_block(sq, 1, 0, scale(sh, Z2))

sq23 = eye(6)
ch23, sh23 = F(5, 3), F(4, 3)
set_block(sq23, 1, 1, scale(ch23, I2))
set_block(sq23, 2, 2, scale(ch23, I2))
set_block(sq23, 1, 2, scale(sh23, Z2))
set_block(sq23, 2, 1, scale(sh23, Z2))

mid_rotation = block_diag([
    I2,
    [[F(3, 5), F(4, 5)], [F(-4, 5), F(3, 5)]],
    I2,
])
symplectic = mul(mul(sq23, mid_rotation), sq)
v = scale(F(1, 2), mul(symplectic, transpose(symplectic)))
omega = block_diag([J2, J2, J2])
assert mul(mul(v, omega), v) == scale(F(1, 4), omega)
base_loop = loop_value(v)
assert base_loop == 0

# Independent local Sp(2)=SL(2) gauges.
gauges = [
    [[F(1), F(2)], [F(0), F(1)]],
    [[F(1), F(0)], [F(-3), F(1)]],
    [[F(2), F(1)], [F(1), F(1)]],
]
local = block_diag(gauges)
v_gauge = mul(mul(local, v), transpose(local))
assert mul(mul(v_gauge, omega), v_gauge) == scale(F(1, 4), omega)
assert loop_value(v_gauge) == base_loop

# Every pure three-mode Gaussian is locally reducible to a standard form with
# diagonal cross blocks (Serafini--Adesso, arXiv:0705.1136).  The candidate
# trace vanishes algebraically on all such blocks.
standard_form_tests = 0
for x1 in range(-2, 3):
    for x2 in range(-2, 3):
        for x3 in range(-2, 3):
            d1 = [[F(x1), F(0)], [F(0), F(x1 + 1)]]
            d2 = [[F(x2), F(0)], [F(0), F(x2 - 1)]]
            d3 = [[F(x3), F(0)], [F(0), F(x3 + 2)]]
            candidate = trace(mul(mul(mul(mul(mul(J2, d1), J2), d2), J2), d3))
            assert candidate == 0
            standard_form_tests += 1

packet = {
    "schema": "marici.symplectic-triangle-loop.v1",
    "candidate": "L_Omega=tr(J C12 J C23 J C31)",
    "gauge_law": "C_ij -> S_i C_ij S_j^T, S_i in Sp(2)",
    "invariance": "L_Omega is invariant by cyclic cancellation of local gauges",
    "source_packet": {
        "two_mode_squeeze": {"cosh": str(ch), "sinh": str(sh)},
        "second_two_mode_squeeze": {"cosh": str(ch23), "sinh": str(sh23)},
        "intermediate_phase_rotation": {"cos": "3/5", "sin": "4/5"},
        "loop_value": str(base_loop),
        "purity_verified": True,
        "local_gauge_replication": True,
    },
    "standard_form_zero_tests": standard_form_tests,
    "interpretation": "the candidate is gauge invariant but purity-annihilated on all pure three-mode Gaussian states; no Gaussian Bargmann phase survives at rank three",
}

out = Path(__file__).parent / "results" / "symplectic-triangle-loop.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
