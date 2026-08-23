#!/usr/bin/env python3
"""WP21a: symbolic structure of the first-harmonic amplitude a1 of
det[Hu,Hd] for the paper's nine-link texture (masks 85/234, phase on
Yd[0,1]).

a1 is defined by detC(z) = a1 (z - z^{-1}) = 2i a1 sin(phi), z = e^{i phi},
with a1 a real Laurent-free polynomial in the edge magnitudes.

This checker:
  1. builds Yu, Yd symbolically (magnitudes as positive symbols, phase
     edge carrying z);
  2. computes det[Hu,Hd] exactly and confirms support {z^+1, z^-1} only
     (symbolic first-harmonic check for this texture);
  3. extracts a1 as a polynomial in the magnitudes, factors it, and
     lists its monomial support;
  4. tests numerically (random positive assignments, exact rationals)
     that a1 == detC(z=i... )/2i at phi=pi/2 with the same magnitudes;
  5. writes results/wp21a_a1_symbolic.json.
"""
import json
import sympy as sp

# edge magnitude symbols
u00, u02, u11, u12 = sp.symbols("u00 u02 u11 u12", positive=True)
d01, d10, d12, d20, d21 = sp.symbols("d01 d10 d12 d20 d21", positive=True)
z = sp.symbols("z")  # the phase exponential; z* = 1/z on the unit circle

# mask 85 = bits {0,2,4,6}: Yu[0,0], Yu[0,2], Yu[1,1], Yu[2,0]
Yu = sp.Matrix([
    [u00, 0, u02],
    [0, u11, 0],
    [u12, 0, 0],
])
# mask 234 = bits {1,3,5,6,7}: Yd[0,1] (phase edge), Yd[1,0], Yd[1,2], Yd[2,0], Yd[2,1]
Yd = sp.Matrix([
    [0, d01 * z, 0],
    [d10, 0, d12],
    [d20, d21, 0],
])

Yuc = Yu.conjugate()
Ydc = Yd.conjugate().subs(1 / z, 1 / z)
# conjugate of z is 1/z (unit circle)
Ydc = Yd.conjugate()
for i in range(3):
    for j in range(3):
        Ydc[i, j] = Ydc[i, j].subs(sp.conjugate(z), 1 / z)

Hu = Yu * Yuc.T
Hd = Yd * Ydc.T
C = Hu * Hd - Hd * Hu
detC = sp.expand(C.det())

# collect by powers of z (detC is Laurent: multiply through by z)
poly = sp.Poly(sp.expand(detC * z), z)
terms = [(e - 1, c) for (e,), c in poly.terms()]
support = sorted(e for e, _ in terms)
print("detC z-support:", support)
assert support == [-1, 1], f"unexpected support {support}"

a1 = sp.expand(next(c for e, c in terms if e == 1))
a1m = sp.expand(next(c for e, c in terms if e == -1))
print("a1 (coeff of z):")
print(" ", a1)
print("coeff of z^-1:", a1m)
print("a1 + coeff(z^-1) =", sp.simplify(a1 + a1m))

# factor
a1f = sp.factor(a1)
print("factored a1:")
print(" ", a1f)

# monomial support
p = sp.Poly(a1, u00, u02, u11, u12, d01, d10, d12, d20, d21)
monos = p.terms()
print("monomial count:", len(monos))
for m, c in monos:
    print("  ", c, dict(zip(("u00", "u02", "u11", "u12", "d01", "d10", "d12", "d20", "d21"), m)))

# numeric cross-check with exact rationals at phi = pi/2
import random
random.seed(21)
syms = [u00, u02, u11, u12, d01, d10, d12, d20, d21]
vals = {s: sp.Rational(random.randint(1, 9), random.randint(1, 9)) for s in syms}
subs_all = list(vals.items()) + [(z, sp.I)]
detC_at_i = sp.N(complex(detC.subs(subs_all)), 30)
a1_num = sp.N(a1.subs(vals), 30)
# detC(i) should equal 2i a1
resid = abs(complex(detC_at_i) - 2j * complex(a1_num))
print("numeric residual |detC(i) - 2i a1|:", resid)
assert resid < 1e-25, resid

out = {
    "texture": {"mask_u": 85, "mask_d": 234, "phase_edge": ["d", 0, 1]},
    "detC_support": support,
    "a1_expanded": str(a1),
    "a1_factored": str(a1f),
    "monomial_count": len(monos),
    "monomials": [
        {"coeff": str(c),
         "exponents": dict(zip(("u00", "u02", "u11", "u12", "d01", "d10", "d12", "d20", "d21"), m))}
        for m, c in monos
    ],
    "numeric_residual": float(resid),
}

# WP21b: the alternating bracket cancels against a Vandermonde factor.
# Hu block structure: singleton u11^2 plus the {0,2} block
# [[u00^2+u02^2, u00*u12], [u00*u12, u12^2]] with eigenvalues lam+, lam-.
# Claim: B = -(u11^2-lam+)(u11^2-lam-) and
# Du = |B| (lam+ - lam-), so a1/Du = d01*d10^2*d20^2*d21*u00*u12/(lam+-lam-).
lam_sum = u00**2 + u02**2 + u12**2
lam_prod = u02**2 * u12**2
lam_gap = sp.sqrt(lam_sum**2 - 4 * lam_prod)
B = a1 / (d01 * d10**2 * d20**2 * d21 * u00 * u12)
B = sp.expand(B)
char_at_singleton = sp.expand(u11**4 - lam_sum * u11**2 + lam_prod)
bracket_is_neg_char = sp.simplify(B + char_at_singleton) == 0
print("B == -(char poly of Hu block at u11^2):", bracket_is_neg_char)
Du_expr = sp.Abs(char_at_singleton) * lam_gap  # up to sign: Du = |B| * gap
a1_over_Du = sp.simplify(
    d01 * d10**2 * d20**2 * d21 * u00 * u12 / lam_gap)
print("a1/(Du*Dd) = d01*d10^2*d20^2*d21*u00*u12 / ((lam+-lam-)*Dd)")

# numeric confirmation of the cancellation with exact rationals
eigs = sp.solve(sp.Symbol("L")**2 - lam_sum * sp.Symbol("L") + lam_prod,
                sp.Symbol("L"))
valsL = {sp.Symbol("L"): 1}  # placeholder
num = {s: float(v) for s, v in vals.items()}
import numpy as _np
Hu_num = _np.array(Hu.subs(num)).astype(float)
ev = _np.linalg.eigvalsh(Hu_num)
Du_num = abs((ev[0]-ev[1]) * (ev[0]-ev[2]) * (ev[1]-ev[2]))
a1_over_Du_num = float(a1.subs(vals)) / Du_num
reduced_num = float(a1_over_Du.subs(num))
cancel_resid = abs(abs(a1_over_Du_num) - abs(reduced_num)) / abs(a1_over_Du_num)
sign_B = float(sp.sign(B.subs(vals)))
print("numeric cancellation residual (abs):", cancel_resid,
      "; sign(B) =", sign_B)
assert cancel_resid < 1e-12, cancel_resid

out["wp21b_cancellation"] = {
    "bracket_equals_negative_char_poly_at_singleton": bracket_is_neg_char,
    "a1_over_Du_reduced": str(a1_over_Du),
    "lambda_gap": str(lam_gap),
    "numeric_residual": cancel_resid,
}

with open("results/wp21a_a1_symbolic.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)
print("-> results/wp21a_a1_symbolic.json")
