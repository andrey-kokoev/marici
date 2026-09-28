"""Exact amplitude/intensity readouts of the declared Q^2 assembly prototype.

Uses the Euclidean metric and identity reference. These are explicit model
choices. No electromagnetic data enter the calculation. Writes no artifacts.
"""
from fractions import Fraction as F
from check_comparison_slot_reference_assembly import I, H, add, scale, mul, assemble


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(2)) for i in range(2))


def inner(a, b):
    return sum(a[i][j]*b[i][j] for i in range(2) for j in range(2))/2


def readouts(c):
    residual = add(c, scale(-1, I))
    amplitude = inner(I, c)
    intensity = inner(c, c)
    residual_power = inner(residual, residual)
    assert intensity == 1 + 2*inner(I, residual) + residual_power
    return amplitude, intensity, residual_power


for u, v in [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)),
             (F(1), F(-1)), (F(1, 10), F(1, 10))]:
    x, y, s, t = [I]*11, [I]*11, [I]*4, [I]*4
    x[0] = add(I, scale(u, H))
    y[0] = add(I, scale(v, transpose(H)))
    c = assemble(x, y, s, t)
    # The one modified x participates in eleven composites, likewise y.
    # Their intersection contributes one product term.
    expected = add(I, scale(F(1, 137),
                   add(add(scale(11*u, H), scale(11*v, transpose(H))),
                       scale(u*v, mul(transpose(H), H)))))
    assert c == expected
    amplitude, intensity, power = readouts(c)
    assert amplitude == 1 + u*v/F(274)
    assert power == (121*(u*u+v*v)+u*u*v*v)/F(2*137**2)
    assert intensity == 1 + u*v/F(137) + power
    print(f"u={u}, v={v}: amplitude={amplitude}, intensity={intensity}, residual_power={power}")

# Equal and opposite x-leg deviations cancel in this linear assembly.
x, y, s, t = [I]*11, [I]*11, [I]*4, [I]*4
x[0], x[1] = add(I, H), add(I, scale(-1, H))
assert readouts(assemble(x, y, s, t)) == (F(1), F(1), F(0))
print("Amplitude, intensity, interference, and two-leg product checks passed.")
