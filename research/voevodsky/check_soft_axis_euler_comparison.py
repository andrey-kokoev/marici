"""Check which gradient directions give a regular Euler certificate for K."""

from fractions import Fraction as Q


def add(*ps):
    out = {}
    for p in ps:
        for mon, c in p.items():
            out[mon] = out.get(mon, Q(0)) + c
            if not out[mon]:
                del out[mon]
    return out


def scale(p, c):
    return {m: c * x for m, x in p.items() if c * x}


def mul(p, q):
    out = {}
    for (ai, bi, ui), x in p.items():
        for (aj, bj, uj), y in q.items():
            if ui + uj >= 2:  # dual-number deformation
                continue
            mon = (ai + aj, bi + bj, ui + uj)
            out[mon] = out.get(mon, Q(0)) + x * y
    return {m: c for m, c in out.items() if c}


a = {(1, 0, 0): Q(1)}
u = {(0, 0, 1): Q(1)}
K = {(4, 0, 0): Q(1), (2, 0, 1): Q(1), (2, 2, 1): Q(-1)}
Ka = {(3, 0, 0): Q(4), (1, 0, 1): Q(2), (1, 2, 1): Q(-2)}
Kb = {(2, 1, 1): Q(-2)}
Ku = {(2, 0, 0): Q(1), (2, 2, 0): Q(-1)}

# The full (a,b,u) Euler certificate is polynomial and global.
full = add(mul(scale(a, Q(1, 4)), Ka), mul(scale(u, Q(1, 2)), Ku))
assert full == K

# With only (a,b), the a-Euler part leaves a residual requiring division by b.
residual = add(K, scale(mul(scale(a, Q(1, 4)), Ka), -1))
expected = {(2, 0, 1): Q(1, 2), (2, 2, 1): Q(-1, 2)}
assert residual == expected

# On b != 0 it is killed by B=-(1-b^2)/(4b), visibly a Laurent coefficient.
# At b=0, division by Ka would require A=a/4+u/(8a) modulo u^2.
# The negative a-power proves that no polynomial relative certificate extends there.
print("K = (a/4) K_a + (u/2) K_u: verified modulo u^2")
print("relative residual K-(a/4)K_a = (u a^2/2)(1-b^2)")
print("relative B coefficient = -(1-b^2)/(4b): pole at b=0")
print("at b=0 the required A = a/4 + u/(8a): pole at a=0")
print("verdict: a global comparison requires the deformation gradient K_u")
