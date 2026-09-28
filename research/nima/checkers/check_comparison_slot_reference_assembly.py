"""Typed linear toy assembly for the proposed 121+16 comparison domain.

All endpoint and intermediate spaces are copies of Q^2, with separately
labelled roles A, B, U, V. No physical carrier adapter is asserted.
Writes no artifacts. Run directly.
"""
from fractions import Fraction as F

I = ((F(1), F(0)), (F(0), F(1)))
ZERO = ((F(0), F(0)), (F(0), F(0)))
H = ((F(0), F(1)), (F(0), F(0)))

def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))

def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)

def mul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def assemble(x, y, s, t):
    # x_i:A->U, y_j:U->B; s_a:A->V, t_b:V->B.
    # Four state labels are provisionally realized as maps, not just values.
    assert len(x) == len(y) == 11
    assert len(s) == len(t) == 4
    slots = [mul(v, u) for v in y for u in x]
    slots += [mul(v, u) for v in t for u in s]
    assert len(slots) == 137
    total = ZERO
    for slot in slots:
        total = add(total, slot)
    return scale(F(1, 137), total)

reference = I  # d:A->B in these chosen coordinates
x, y, s, t = [I]*11, [I]*11, [I]*4, [I]*4
baseline = assemble(x, y, s, t)
assert baseline == reference
assert add(baseline, scale(-1, reference)) == ZERO

# One arrow-leg perturbation affects eleven composite slots.
x_one = x.copy()
x_one[0] = add(I, H)
residual_one = add(assemble(x_one, y, s, t), scale(-1, reference))
assert residual_one == scale(F(11, 137), H)

# Two opposite perturbations cancel without removing any slots.
x_cancel = x_one.copy()
x_cancel[1] = add(I, scale(-1, H))
assert assemble(x_cancel, y, s, t) == reference

# One state-leg perturbation affects four slots.
s_one = s.copy()
s_one[0] = add(I, H)
residual_state = add(assemble(x, y, s_one, t), scale(-1, reference))
assert residual_state == scale(F(4, 137), H)

# Direct-reference changes matter even when all indirect comparisons are fixed.
shifted_reference = add(I, H)
assert add(baseline, scale(-1, shifted_reference)) == scale(-1, H)

print("137 slots retained in every test.")
print("All composites agree with reference: residual 0.")
print("One arrow-leg perturbation H: residual (11/137) H.")
print("Opposite arrow-leg perturbations: residual 0, no slot deletion.")
print("One state-leg perturbation H: residual (4/137) H.")
print("Reference alone shifted by H: residual -H.")
print("Exact assembly checks passed; no EM scalar readout or feedback law supplied.")
