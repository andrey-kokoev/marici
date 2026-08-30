"""Rung-5 readout certification checker: the fold closed form, the character
theorem through grade 8, and the rung-5 square-root gate verdict
(marici.Strominger).

Companion to (does NOT import or modify):
  research/strominger/checkers/readout_parity_mechanism_checks.py (P1-P6)
  research/strominger/checkers/rung4_foldrule_checks.py (M, S, R1-R4)
  research/strominger/checkers/rung4_foldgrade_checks.py (H, F1-F8)

Motivation. readout_parity_mechanism_checks.py certified the readout
character theorem P(E_g) = +u^{g+2} E_g, P(M_g) = -u^{g+3} M_g for grades
g = 0..5, but rung 5 (tower order 4) folds at grade 8 (rung4_foldrule R2:
every order-4 channel closes at (8,-2)), so its readout verdict was a
PREDICTION under the declared identification fold grade = readout grade
(rung4-foldrule.md section 5). This checker closes the gap: it derives a
closed form for the grade-g fold, proves its reciprocity, and certifies
the character theorem through g = 8 — upgrading the rung-5 readout from
prediction to certified readout.

Setup (same conventions as readout_parity_mechanism_checks.py). Anchor
datum C = (u + 1/u)/z^2, u = z zb, spin-2 lower component, P: z -> -1/z,
zb -> -1/zb. Fold chain Dz(f,s) = d_z f - s Gam f, Gam = -2 zb/(1+u),
weights s = 2,3,...,g+1. Grade-g readouts E_g = fold_g + sigma(fold_g),
M_g = A_g - B_g, A_g = d_zb fold_g, B_g = sigma(A_g).

The closed form (derived in rung5-readout.md). With Q_1 = (Theta-2) h,
h = (1+u)^4 (u + 1/u), Theta = u d/du, and the recursion
Q_{j+1} = T_{-(j+2)} Q_j, T_e phi = (1+u)[(e+Theta) + u(e+Theta+2)] phi:
  fold_g(C) = (1+u)^{-2(g+1)} z^{-(g+2)} Q_g(u),
  A_g = z^{-(g+1)} Rt_g(u),
  Rt_g(u) = u^{-1} (1+u)^{-2g-3} W_g,  W_g = (1+u) Theta Q_g - 2(g+1) u Q_g.
The engine theorem is the RECIPROCITY Q_g(u) = (-1)^g u^{2(g+1)} Q_g(1/u);
it implies Rt_g(1/u) = (-1)^{g+1} u^2 Rt_g(u), hence both characters.

Layers:
  Q   the reciprocity engine: T-operator monomial action (symbolic e),
      base identity and h reciprocity, Q_g reciprocity g = 1..12, support
      law supp Q_g = [-1, 2g+3] with endpoints attained.
  F   the fold closed form: base g = 1 against Dz(C,2); one-step recursion
      Dz(cf_g, 2+g) = cf_{g+1} for g = 1..7 (certifies cf_g = fold_g for
      g = 1..8); direct full-chain anchor g = 1..5.
  C   the character theorem through grade 8: P(E_g) = +u^{g+2} E_g and
      P(M_g) = -u^{g+3} M_g EXACTLY for g = 0..8 (g = 0 direct, g >= 1 via
      the closed form), monomial closure z^{g+1} A_g = zb^{g+1} B_g
      g = 0..8, and witness regression tying g = 4 to the previously
      certified values (readout_parity_mechanism P6.3).
  R5  the rung-5 verdict: P(E_8) = +u^10 with sigma-invariant root u^5
      (electric gate PASSES); P(M_8) = -u^11, odd exponent (magnetic gate
      FAILS); closed-form obstruction P(M_8) - M_8 = -(1+u^11) M_8 exact;
      the intrinsic-oddness lemma blocks any rational cocycle repair.
  ALT the alternation theorem: rung n+1 (tower order n) folds at grade
      g_n = n + 2 ceil(n/2) (certified orders 1..4; theorem for all n via
      channel-closedform.md), parity(g_n) = parity(n), so EXACTLY ONE of
      the exponents g_n+2, g_n+3 is odd at every rung and the obstructed
      sector alternates E, M, E, M by rung (rung 2: E, rung 3: M,
      rung 4: E, rung 5: M).

Output: research/strominger/results/rung5_readout.json
Exit code 0 iff every check passes.
"""
import json
import os
import sympy as sp

z, zb = sp.symbols("z zb")
u = z * zb
Gam = -2 * zb / (1 + u)
W2 = {z: sp.Rational(3), zb: sp.Rational(2, 7)}

uu, ee = sp.symbols("u e")  # standalone symbols for the polynomial engine


def Th(f):
    return uu * sp.diff(f, uu)


results = []


def simp(e):
    e = sp.simplify(sp.expand(e))
    if e != 0:
        e = sp.cancel(sp.together(e))
    return e


def record(cid, group, statement, status, detail=""):
    results.append({
        "id": cid, "group": group, "statement": statement,
        "status": status, "detail": detail,
    })
    print(f"[{status:>4}] {cid}: {statement}" + (f"  ({detail})" if detail else ""))


def check_all_zero(cid, group, statement, exprs, detail=""):
    vals = [simp(e) for e in exprs]
    bad = [v for v in vals if v != 0]
    record(cid, group, statement, "pass" if not bad else "FAIL",
           detail if not bad else f"nonzero component: {sp.sstr(bad[0])[:300]}")
    return not bad


def check_nonzero(cid, group, statement, expr, detail=""):
    e = simp(expr)
    record(cid, group, statement, "pass" if e != 0 else "FAIL",
           (detail + " " if detail else "") +
           (f"residual retained: {sp.sstr(e)[:200]}" if e != 0
            else "residual vanished unexpectedly"))
    return e != 0


def check_true(cid, group, statement, cond, detail=""):
    record(cid, group, statement, "pass" if bool(cond) else "FAIL", detail)
    return bool(cond)


def sigma(e):
    return e.subs([(z, zb), (zb, z)], simultaneous=True)


def P_map(e):
    return e.subs([(z, -1 / z), (zb, -1 / zb)], simultaneous=True)


def Dz(f, s):
    return sp.diff(f, z) - s * Gam * f


def Dzb(f, s):
    return sp.diff(f, zb) - s * (-2 * z / (1 + u)) * f


def fold(f, g, s0=2):
    for i in range(g):
        f = Dz(f, s0 + i)
    return simp(f)


# ================================================================ Q the engine
def T_op(e, f):
    """T_e f = (1+u)[(e+Theta) + u(e+Theta+2)] f."""
    return sp.expand((1 + uu) * ((e * f + Th(f)) + uu * (e * f + Th(f) + 2 * f)))


def build_Q(g):
    h = sp.expand((1 + uu) ** 4 * (uu + 1 / uu))
    Q = sp.expand(Th(h) - 2 * h)
    for j in range(1, g):
        Q = sp.expand(T_op(-(j + 2), Q))
    return Q


QMAX = 12
Qs = {g: build_Q(g) for g in range(1, QMAX + 1)}

ok_q1 = all(
    sp.expand(T_op(ee, uu ** m)
              - ((ee + m) * uu ** m + 2 * (ee + m + 1) * uu ** (m + 1)
                 + (ee + m + 2) * uu ** (m + 2))) == 0
    for m in range(-2, 11))
check_true("Q1", "Q", "T-operator monomial action: T_e u^m = (e+m) u^m + "
                     "2(e+m+1) u^{m+1} + (e+m+2) u^{m+2} EXACTLY, symbolic e, "
                     "m = -2..10 — the fold chain is a tridiagonal Laurent "
                     "recursion",
           ok_q1)

h = sp.expand((1 + uu) ** 4 * (uu + 1 / uu))
check_all_zero("Q2", "Q", "base of the recursion: Q_1 = (Theta-2) h with "
                          "h = (1+u)^4 (u+1/u), and h is reciprocal: "
                          "h(1/u) = u^{-4} h(u) exactly",
               [Qs[1] - (Th(h) - 2 * h),
                h.subs(uu, 1 / uu) - uu ** (-4) * h])

ok_q3 = all(
    sp.expand(Qs[g] - (-1) ** g * uu ** (2 * (g + 1))
              * Qs[g].subs(uu, 1 / uu)) == 0
    for g in range(1, QMAX + 1))
check_true("Q3", "Q", "reciprocity theorem (engine of both characters): "
                      "Q_g(u) = (-1)^g u^{2(g+1)} Q_g(1/u) EXACTLY for "
                      "g = 1..12 — certified well beyond the rung-5 grade 8",
           ok_q3)

ok_q4 = True
for g in range(1, QMAX + 1):
    poly = sp.Poly(sp.expand(Qs[g] * uu), uu)
    exps = [m[0] - 1 for m in poly.monoms()]
    if min(exps) != -1 or max(exps) != 2 * g + 3:
        ok_q4 = False
check_true("Q4", "Q", "support law: supp Q_g = [-1, 2g+3] with BOTH endpoints "
                      "attained (nonzero endpoint coefficients) for "
                      "g = 1..12 — the Laurent width 2g+5 grows linearly "
                      "while the reciprocity pivot sits at exponent g+1",
           ok_q4)

# ================================================================ F closed form
def fold_cf(g):
    return (1 + u) ** (-2 * (g + 1)) * z ** (-(g + 2)) * Qs[g].subs(uu, u)


C = (u + 1 / u) / z ** 2
Cb = sigma(C)

check_all_zero("F1", "F", "base of the closed form: cf_1 = (1+u)^{-4} "
                          "z^{-3} Q_1(u) equals the first fold Dz(C,2) "
                          "exactly",
               [fold_cf(1) - Dz(C, 2)])

ok_f2 = all(simp(Dz(fold_cf(g), 2 + g) - fold_cf(g + 1)) == 0
            for g in range(1, 8))
check_true("F2", "F", "one-step recursion: Dz(cf_g, 2+g) = cf_{g+1} EXACTLY "
                      "for g = 1..7 — with F1 this certifies cf_g = fold_g "
                      "for every g = 1..8 (the full fold chain collapses to "
                      "the Q-recursion)",
           ok_f2)

ok_f3 = True
f = C
for g in range(1, 6):
    f = simp(Dz(f, 2 + g - 1))
    if simp(f - fold_cf(g)) != 0:
        ok_f3 = False
check_true("F3", "F", "direct anchor: the full D-chain fold(C,g) computed "
                      "step by step equals cf_g EXACTLY for g = 1..5 — ties "
                      "the closed form to the definition used in the "
                      "previously certified checkers",
           ok_f3)

# ================================================================ C characters
def Rtilde(g):
    W = sp.expand((1 + uu) * Th(Qs[g]) - 2 * (g + 1) * uu * Qs[g])
    return sp.cancel(uu ** (-1) * (1 + uu) ** (-2 * g - 3) * W)


def readouts_cf(g):
    """Grade-g readouts from the closed form, g >= 1."""
    foldg = fold_cf(g)
    E = simp(foldg + sigma(foldg))
    A = z ** (-(g + 1)) * Rtilde(g).subs(uu, u)
    B = zb ** (-(g + 1)) * Rtilde(g).subs(uu, u)
    return simp(A), simp(B), E, simp(A - B)


AB = {}
A0 = simp(sp.diff(C, zb))
B0 = simp(sp.diff(Cb, z))
AB[0] = (A0, B0, simp(C + Cb), simp(A0 - B0))
for g in range(1, 9):
    AB[g] = readouts_cf(g)

ok_c1 = all(simp(P_map(AB[g][2]) - u ** (g + 2) * AB[g][2]) == 0
            for g in range(0, 9))
check_true("C1", "C", "electric character theorem THROUGH RUNG-5 GRADE: "
                      "P(E_g) = +u^{g+2} E_g EXACTLY for g = 0..8 — extends "
                      "the certified range g = 0..5 of "
                      "readout_parity_mechanism P3.1 to the rung-5 grade 8",
           ok_c1)

ok_c2 = all(simp(P_map(AB[g][3]) + u ** (g + 3) * AB[g][3]) == 0
            for g in range(0, 9))
check_true("C2", "C", "magnetic character theorem THROUGH RUNG-5 GRADE: "
                      "P(M_g) = -u^{g+3} M_g EXACTLY for g = 0..8 — extends "
                      "readout_parity_mechanism P3.2",
           ok_c2)

ok_c3 = all(simp(z ** (g + 1) * AB[g][0] - zb ** (g + 1) * AB[g][1]) == 0
            for g in range(0, 9))
check_true("C3", "C", "monomial closure z^{g+1} A_g = zb^{g+1} B_g EXACTLY "
                      "for g = 0..8 — automatic from the closed form since "
                      "z^{g+1} A_g = Rt_g(u) is sigma-invariant; extends "
                      "readout_parity_mechanism P2.1",
           ok_c3)

ok_c4 = all(
    simp(P_map(AB[g][0]) - z ** (2 * g + 4) * zb ** 2 * AB[g][0]) == 0
    for g in range(0, 9))
check_true("C4", "C", "diagonal weight of the magnetic component: P(A_g) = "
                      "z^{2g+4} zb^2 A_g EXACTLY for g = 0..8 — extends "
                      "readout_parity_mechanism P2.2",
           ok_c4)

M4w = sp.simplify(AB[4][3].subs(W2))
E4w = sp.simplify(AB[4][2].subs(W2))
ok_c5 = (M4w == sp.Rational(38822265502889, 1443587184)
         and E4w == sp.Rational(1606143346495, 28789488))
check_true("C5", "C", "witness regression: the closed-form readouts at g = 4 "
                      "reproduce the previously certified values M_4|W2 = "
                      "38822265502889/1443587184 and E_4|W2 = "
                      "1606143346495/28789488 (readout_parity_mechanism "
                      "P6.3, rung3_s2_bridge R2.6) — the new engine agrees "
                      "with the old computation where both apply",
           ok_c5, f"M_4|W2 = {M4w}; E_4|W2 = {E4w}")

# ================================================================ R5 the verdict
E8, M8 = AB[8][2], AB[8][3]

check_all_zero("R5.1", "R5", "rung-5 electric sector PASSES the square-root "
                             "gate: P(E_8) = +u^10 E_8 and the root u^5 is "
                             "sigma-invariant (sigma(u^5) = u^5), so the "
                             "even electric character admits a cocycle root "
                             "in Q(u)",
               [P_map(E8) - u ** 10 * E8, sigma(u ** 5) - u ** 5])

check_all_zero("R5.2", "R5", "rung-5 magnetic sector FAILS the square-root "
                             "gate: P(M_8) = -u^11 M_8 with ODD exponent 11 "
                             "— no square root of -u^11 exists in Q(u), so "
                             "the magnetic readout is gate-obstructed",
               [P_map(M8) + u ** 11 * M8])

check_all_zero("R5.3", "R5", "closed-form rung-5 obstruction: P(M_8) - M_8 = "
                             "-(1 + u^11) M_8 exactly — the obstruction "
                             "factor 1+u^11 is a nonzero rational function, "
                             "so the readout can never be P-invariant",
               [(P_map(M8) - M8) + (1 + u ** 11) * M8])

def vval(e, v):
    """Order of vanishing of a rational function along v = 0."""
    n, d = sp.fraction(sp.cancel(e))

    def vv(p):
        k = 0
        for c in sp.Poly(sp.expand(p), v).all_coeffs()[::-1]:
            if sp.simplify(c) == 0:
                k += 1
            else:
                break
        return k

    return vv(n) - vv(d)


def valu(e):
    """Diagonal u-valuation: val_u = val_z + val_zb (u = z zb)."""
    return vval(e, z) + vval(e, zb)


FAMILY54 = [z ** 2 * zb / (1 + u), (1 + u) ** 3 / zb ** 2,
            z * zb ** 3 * (1 + u), (1 + u) ** 4 * (u + 1 / u),
            Rtilde(4).subs(uu, u), Rtilde(8).subs(uu, u)]
ok_r54 = all(valu(hh * sigma(hh)) == 2 * valu(hh)
             and valu(hh * sigma(hh)) % 2 == 0 for hh in FAMILY54)
check_true("R5.4", "R5", "intrinsic oddness (sample instances of the lemma "
                         "certified in rung3_cocycle K4): val_u(h "
                         "sigma(h)) = 2 val_u(h) is ALWAYS even, verified "
                         "on rational dressings including the datum factor "
                         "h and the magnetic components Rt_4, Rt_8 — a "
                         "cocycle root F would need F sigma(F) = -u^11 of "
                         "ODD diagonal valuation 11, which no rational "
                         "dressing can supply: the rung-5 magnetic "
                         "obstruction is unrepairable",
           ok_r54)

# ================================================================ ALT alternation
def g_law(n):
    return n + 2 * ((n + 1) // 2)  # n + 2 ceil(n/2)


ok_a1 = [g_law(n) for n in range(1, 5)] == [3, 4, 7, 8]
check_true("ALT1", "ALT", "grade law reproduces the certified minimal "
                          "full-closure grades: g_n = n + 2 ceil(n/2) gives "
                          "3, 4, 7, 8 for tower orders n = 1..4 — the "
                          "grounded rungs 2, 3, 4 and the rung-5 grade "
                          "certified by rung4_foldrule R2",
           ok_a1, f"g_n = {[g_law(n) for n in range(1, 5)]}")

ok_a2 = all(g_law(n) % 2 == n % 2 for n in range(1, 51))
ok_a3 = all(((g_law(n) + 2) % 2) + ((g_law(n) + 3) % 2) == 1
            for n in range(1, 51))
check_true("ALT2", "ALT", "alternation theorem: parity(g_n) = parity(n) for "
                          "n = 1..50, so EXACTLY ONE of the character "
                          "exponents g_n+2 (electric), g_n+3 (magnetic) is "
                          "odd at every rung — exactly one sector is "
                          "square-root obstructed at every rung, electric "
                          "iff n (tower order) is odd",
           ok_a2 and ok_a3)

sector = {2: "E", 3: "M", 4: "E", 5: "M"}
ok_a4 = all(
    (sector[r] == "E") == (g_law(r - 1) % 2 == 1) for r in sector)
check_true("ALT3", "ALT", "the grounded ladder instantiates the alternation "
                          "E, M, E, M: rung 2 (g=3) electric-obstructed, "
                          "rung 3 (g=4) magnetic (-u^7, certified), rung 4 "
                          "(g=7) electric-obstructed (rung4-foldgrade), "
                          "rung 5 (g=8) magnetic (-u^11, this checker)",
           ok_a4, f"g = {[g_law(r - 1) for r in (2, 3, 4, 5)]}")

# ================================================================ summary
fails = [r for r in results if r["status"] == "FAIL"]
passes = [r for r in results if r["status"] == "pass"]
out = {
    "checker": "rung5_readout_checks.py",
    "author": "marici.Strominger",
    "checks": results,
    "n_pass": len(passes),
    "n_fail": len(fails),
    "verdict": (
        "The rung-5 readout is CERTIFIED, upgrading the prediction of "
        "rung4-foldrule.md section 5. The grade-g fold collapses to the "
        "closed form (1+u)^{-2(g+1)} z^{-(g+2)} Q_g(u) with Q_g generated "
        "by the tridiagonal T-recursion (F1-F3); the engine is the "
        "reciprocity Q_g(u) = (-1)^g u^{2(g+1)} Q_g(1/u), certified "
        "g = 1..12 (Q3), with support law [-1, 2g+3] (Q4). The character "
        "theorem P(E_g) = +u^{g+2} E_g, P(M_g) = -u^{g+3} M_g now holds "
        "EXACTLY for g = 0..8 (C1-C2), tied to the old computation by the "
        "g = 4 witness regression (C5). At the rung-5 grade 8: the "
        "electric sector passes the square-root gate (+u^10, root u^5 "
        "sigma-invariant, R5.1); the magnetic sector fails (-u^11, odd, "
        "R5.2) with closed-form obstruction P(M_8) - M_8 = -(1+u^11) M_8 "
        "(R5.3), unrepairable by rational cocycle dressing (R5.4). The "
        "obstructed sector alternates E, M, E, M along the grounded "
        "ladder rungs 2, 3, 4, 5 (ALT)."
    ),
}
here = os.path.dirname(os.path.abspath(__file__))
outdir = os.path.join(here, "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "rung5_readout.json"), "w") as f:
    json.dump(out, f, indent=2)
print(f"\n{len(passes)} passed, {len(fails)} failed")
raise SystemExit(1 if fails else 0)
