"""Exact readout-parity mechanism checker: where the odd u^7 of the rung-3
magnetic obstruction P(M3) = -u^7 M3 is manufactured (marici.Strominger).

Companion to (does NOT import or modify):
  research/strominger/checkers/rung3_s2_bridge_checks.py (R1-R4)
  research/strominger/checkers/rung3_cocycle_checks.py (K1-K5)
  research/strominger/checkers/cocycle_bridge_gates_checks.py (C1-C3)

Motivation. rung3_cocycle_checks.py certified that every rung-3 coefficient-
line determinant has EVEN diagonal u-valuation, and the intrinsic-oddness
lemma (val_u(h sigma(h)) = 2 val_u(h)) forbids any rational cocycle dressing
from manufacturing odd parity. Yet the rung-3 magnetic READOUT carries the
odd character -u^7. This checker pinpoints the manufacturing step.

Setup. Anchor datum C = (u + 1/u)/z^2, u = z zb, spin-2 lower component,
P-invariant P(C) = z^4 C. Grade-g readouts on the rank sequence 2,...,2+g:
  electric  E_g = D_z^g C + D_zb^g Cb,
  magnetic  M_g = A_g - B_g,  A_g = d_zb D_z^g C,  B_g = d_z D_zb^g Cb = sigma(A_g).

Layers:
  P1 the datum: P-invariance, sigma-pairing, two-sheet decomposition
     C = C+ + C- (C+ = zb/z, C- = 1/(z^3 zb)), neither sheet P-invariant.
  P2 the grade-indexed monomial closure theorem: z^{g+1} A_g = zb^{g+1} B_g
     EXACTLY for g = 0..5, refining the certified two-term rung-3 identity
     (z^10+u^5) A = (zb^10+u^5) B to its monomial core z^5 A = zb^5 B
     (equivalence exact); separate weights P(A_g) = z^{2g+4} zb^2 A_g;
     the rung-1 identity z^4 A = zb^4 B is the g=3 member (the R2.4!
     obstruction is retained: z^4 A_4 - zb^4 B_4 is exactly nonzero).
  P3 the readout character theorem: P(E_g) = +u^{g+2} E_g and
     P(M_g) = -u^{g+3} M_g EXACTLY for g = 0..5. Parity corollary: the
     magnetic square-root gate fails iff g is even (rung 1, g=3: -u^6,
     passes; rung 3, g=4: -u^7, FAILS) — the parity alternates with the
     readout fold grade.
  P4 datum-gap independence: for C_k = (u^k + u^-k)/z^2, k = 1,2,3, the
     characters at g = 3,4 are identical (-u^{g+3} / +u^{g+2}) — the datum
     u-support contributes nothing to the exponent; the datum only supplies
     closure. The parity is manufactured by the projection grade alone.
  P5 the birth locus: per datum SHEET the monomial closure holds
     (z^{g+1} A_sheet = zb^{g+1} B_sheet exactly) but NO single u-character
     exists (typed obstruction: six candidate monomials, exact nonzero
     residuals) — the single character is born only at the P-invariant
     total, i.e. at the readout projection.
  P6 mechanism synthesis: the pre-closure decomposition
     P(M_g) = u^2 (z^{2g+2} A_g - zb^{2g+2} B_g) (even diagonal part only)
     versus the post-closure character -u^{g+3}: the odd exponent at g=4
     enters EXACTLY through the closure exponent g+1 = 5. Closed-form
     obstruction P(M_4) - M_4 = -(1 + u^7) M_4 exact; W2 witness values
     reproduced from rung3_s2_bridge_checks.py R2.6.

Output: research/strominger/results/readout_parity_mechanism.json
Exit code 0 iff every mandatory check passes and every typed obstruction
exhibits the declared nonzero residual.
"""
import json
import os
import sympy as sp

z, zb = sp.symbols("z zb")
u = z * zb
Gam = -2 * zb / (1 + u)
Gamb = -2 * z / (1 + u)
W2 = {z: sp.Rational(3), zb: sp.Rational(2, 7)}

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
    return sp.diff(f, zb) - s * Gamb * f


def fold(f, g, s0=2):
    for i in range(g):
        f = Dz(f, s0 + i)
    return simp(f)


def foldb(f, g, s0=2):
    for i in range(g):
        f = Dzb(f, s0 + i)
    return simp(f)


def readouts(Cd, g):
    """Grade-g electric/magnetic readouts and A, B on datum C (spin-2)."""
    A = simp(sp.diff(fold(Cd, g), zb))
    B = simp(sp.diff(foldb(sigma(Cd), g), z))
    E = simp(fold(Cd, g) + foldb(sigma(Cd), g))
    M = simp(A - B)
    return A, B, E, M


# ================================================================ P1 the datum
C = (u + 1 / u) / z ** 2
Cb = sigma(C)
Cp = zb / z                 # sheet +: u/z^2
Cm = 1 / (z ** 3 * zb)      # sheet -: 1/(u z^2)

check_all_zero("P1.1", "P1", "anchor datum: P(C) = z^4 C exactly (spin-2 "
                             "tensor invariance) and sigma(C) = C_zbzb",
               [P_map(C) - z ** 4 * C, sigma(C) - Cb])

check_all_zero("P1.2", "P1", "two-sheet decomposition C = C+ + C- with "
                             "C+ = zb/z (u-support +1) and C- = 1/(z^3 zb) "
                             "(u-support -1); sigma maps each sheet to the "
                             "same-u-support sheet of C_zbzb",
               [C - Cp - Cm, sigma(Cp) - u / zb ** 2,
                sigma(Cm) - 1 / (u * zb ** 2)])

rp = simp(P_map(Cp) - z ** 4 * Cp)
rm = simp(P_map(Cm) - z ** 4 * Cm)
check_true("P1.3!", "P1", "typed obstruction: neither sheet is P-invariant — "
                          "P(C+) - z^4 C+ and P(C-) - z^4 C- are both exactly "
                          "nonzero; P-invariance is a property of the total "
                          "datum only",
           rp != 0 and rm != 0,
           f"P(C+)-z^4 C+ = {sp.sstr(rp)[:80]}; "
           f"P(C-)-z^4 C- = {sp.sstr(rm)[:80]}")

# ================================================================ P2 closure
GRADES = range(0, 6)
AB = {}
for g in GRADES:
    A, B, E, M = readouts(C, g)
    AB[g] = (A, B, E, M)

ok21 = all(simp(z ** (g + 1) * AB[g][0] - zb ** (g + 1) * AB[g][1]) == 0
           for g in GRADES)
check_true("P2.1", "P2", "grade-indexed monomial closure theorem: "
                         "z^{g+1} A_g = zb^{g+1} B_g EXACTLY for g = 0..5 — "
                         "the rung-1 identity z^4 A = zb^4 B (g=3) and the "
                         "rung-3 core z^5 A = zb^5 B (g=4) are members of one "
                         "family",
           ok21)

ok22 = all(simp(P_map(AB[g][0]) - z ** (2 * g + 4) * zb ** 2 * AB[g][0]) == 0
           and simp(P_map(AB[g][1]) - z ** 2 * zb ** (2 * g + 4) * AB[g][1]) == 0
           for g in GRADES)
check_true("P2.2", "P2", "separate diagonal weights at every grade: "
                         "P(A_g) = z^{2g+4} zb^2 A_g and P(B_g) = z^2 "
                         "zb^{2g+4} B_g EXACTLY for g = 0..5 (g=3: z^10 zb^2; "
                         "g=4: z^12 zb^2, matching C3.2/R2.3)",
           ok22)

A4, B4 = AB[4][0], AB[4][1]
check_all_zero("P2.3", "P2", "the certified two-term rung-3 datum identity "
                             "(z^10+u^5) A = (zb^10+u^5) B (R2.4) is EXACTLY "
                             "equivalent to its monomial core z^5 A = zb^5 B "
                             "(z^10+u^5 = z^5(z^5+zb^5) and sigma)",
               [(z ** 10 + u ** 5) * A4 - (zb ** 10 + u ** 5) * B4,
                z ** 5 * A4 - zb ** 5 * B4,
                (z ** 10 + u ** 5) - z ** 5 * (z ** 5 + zb ** 5)])

check_nonzero("P2.4!", "P2", "typed obstruction (retained from R2.4!): the "
                             "rung-1 identity z^4 A = zb^4 B does NOT lift "
                             "verbatim to grade 4 — z^4 A_4 - zb^4 B_4 is "
                             "exactly nonzero; the correct lift is the "
                             "grade-indexed family z^{g+1} A = zb^{g+1} B",
              z ** 4 * A4 - zb ** 4 * B4)

# ================================================================ P3 characters
ok31 = all(simp(P_map(AB[g][2]) - u ** (g + 2) * AB[g][2]) == 0 for g in GRADES)
check_true("P3.1", "P3", "electric character theorem: P(E_g) = +u^{g+2} E_g "
                         "EXACTLY for g = 0..5 (g=2 rung-0 control: +u^4; "
                         "g=4 rung-3: +u^6)",
           ok31)

ok32 = all(simp(P_map(AB[g][3]) + u ** (g + 3) * AB[g][3]) == 0 for g in GRADES)
check_true("P3.2", "P3", "magnetic character theorem: P(M_g) = -u^{g+3} M_g "
                         "EXACTLY for g = 0..5 (g=3 rung-1: -u^6; g=4 rung-3: "
                         "-u^7)",
           ok32)

parity = [(g, (g + 3) % 2) for g in GRADES]
ok33 = (all(p == (1 if g % 2 == 0 else 0) for g, p in parity)
        and (3 + 3) % 2 == 0 and (4 + 3) % 2 == 1)
check_true("P3.3", "P3", "parity corollary: the magnetic character exponent "
                         "g+3 is ODD iff the fold grade g is EVEN — the "
                         "square-root gate fails iff g is even (rung 1 at "
                         "g=3 passes with -u^6; rung 3 at g=4 fails with "
                         "-u^7); the gate verdict alternates with the "
                         "readout grade",
           ok33, f"(g, exponent parity) = {parity}")

# ================================================================ P4 datum gap
ok41 = True
for k in (1, 2, 3):
    Ck = (u ** k + u ** (-k)) / z ** 2
    if simp(P_map(Ck) - z ** 4 * Ck) != 0:
        ok41 = False
        break
    for g in (3, 4):
        Ak, Bk, Ek, Mk = readouts(Ck, g)
        if simp(z ** (g + 1) * Ak - zb ** (g + 1) * Bk) != 0:
            ok41 = False
        if simp(P_map(Mk) + u ** (g + 3) * Mk) != 0:
            ok41 = False
        if simp(P_map(Ek) - u ** (g + 2) * Ek) != 0:
            ok41 = False
check_true("P4.1", "P4", "datum-gap independence: for C_k = (u^k+u^-k)/z^2, "
                         "k = 1,2,3, every datum is P-invariant, the monomial "
                         "closure holds, and the characters are IDENTICAL "
                         "(+u^{g+2} electric, -u^{g+3} magnetic at g = 3,4) "
                         "— the datum u-support contributes nothing to the "
                         "exponent; parity is manufactured by the projection "
                         "grade alone",
           ok41)

# ================================================================ P5 birth locus
ok51 = True
for g in (3, 4):
    for Ci in (Cp, Cm):
        Ai = simp(sp.diff(fold(Ci, g), zb))
        Bi = sigma(Ai)
        if simp(z ** (g + 1) * Ai - zb ** (g + 1) * Bi) != 0:
            ok51 = False
check_true("P5.1", "P5", "per-sheet closure: each datum sheet SEPARATELY "
                         "satisfies the monomial closure z^{g+1} A_sheet = "
                         "zb^{g+1} B_sheet exactly (g = 3,4) — closure is "
                         "sheetwise and does not require P-invariance",
           ok51)

ok52 = True
for g in (3, 4):
    for Ci in (Cp, Cm):
        Ai = simp(sp.diff(fold(Ci, g), zb))
        Mi = simp(Ai - sigma(Ai))
        # candidate single characters near the expected exponent
        for sgn in (1, -1):
            for e in (g + 1, g + 2, g + 3, g + 4, g + 5):
                if simp(P_map(Mi) - sgn * u ** e * Mi) == 0:
                    ok52 = False
check_true("P5.2!", "P5", "typed obstruction (birth locus): per datum sheet "
                          "the magnetic combination M_sheet = A_sheet - "
                          "sigma(A_sheet) carries NO single u-character "
                          "(ten candidate monomials +/-u^{g+1..g+5} per "
                          "sheet per grade, all exact nonzero residuals) — "
                          "the single character exists only for the "
                          "P-invariant total datum: it is BORN at the "
                          "readout projection",
           ok52)

# ================================================================ P6 synthesis
ok61 = all(
    simp(P_map(AB[g][3])
         - u ** 2 * (z ** (2 * g + 2) * AB[g][0] - zb ** (2 * g + 2) * AB[g][1])) == 0
    for g in GRADES)
check_true("P6.1", "P6", "pre-closure decomposition: P(M_g) = u^2 (z^{2g+2} "
                         "A_g - zb^{2g+2} B_g) EXACTLY for g = 0..5 — before "
                         "the datum closure is applied, the magnetic readout "
                         "carries only the EVEN diagonal factor u^2 times a "
                         "non-diagonal bracket; the odd exponent enters "
                         "post-closure through z^{g+1} A = zb^{g+1} B as "
                         "u^{g+1}",
           ok61)

check_all_zero("P6.2", "P6", "closed-form rung-3 obstruction: P(M_4) - M_4 = "
                             "-(1 + u^7) M_4 exactly — the obstruction "
                             "factor 1+u^7 is a nonzero rational function, "
                             "so the readout can never be P-invariant",
               [(P_map(AB[4][3]) - AB[4][3]) + (1 + u ** 7) * AB[4][3]])

M4w = sp.simplify(AB[4][3].subs(W2))
E4w = sp.simplify(AB[4][2].subs(W2))
ok63 = (M4w == sp.Rational(38822265502889, 1443587184)
        and E4w == sp.Rational(1606143346495, 28789488))
check_true("P6.3", "P6", "witness cross-check against rung3_s2_bridge R2.6: "
                         "M_4|W2 = 38822265502889/1443587184 and E_4|W2 = "
                         "1606143346495/28789488 exactly",
           ok63, f"M_4|W2 = {M4w}; E_4|W2 = {E4w}")

# ================================================================ summary
fails = [r for r in results if r["status"] == "FAIL"]
passes = [r for r in results if r["status"] == "pass"]
out = {
    "checker": "readout_parity_mechanism_checks.py",
    "author": "marici.Strominger",
    "checks": results,
    "n_pass": len(passes),
    "n_fail": len(fails),
    "verdict": (
        "The rung-3 magnetic odd character -u^7 is manufactured at the "
        "readout projection: the pre-closure readout carries only the even "
        "diagonal factor u^2 (P6.1); the grade-indexed monomial datum "
        "closure z^{g+1} A = zb^{g+1} B (P2.1) shifts in u^{g+1}; the "
        "character is -u^{g+3} exactly for g = 0..5 (P3.2), odd iff g is "
        "even (P3.3). The exponent is independent of the datum u-support "
        "gap k = 1,2,3 (P4.1), and per datum sheet no single character "
        "exists at all (P5.2!) — the single character is born only at the "
        "P-invariant total. Combined with the coefficient-line evenness "
        "theorem and the intrinsic-oddness lemma (rung3_cocycle K4/K5), "
        "this proves the R3.2 obstruction is born at readout projection, "
        "not inherited from the coefficient line, and that its parity is "
        "forced by the readout fold grade, not by any convention."
    ),
}
here = os.path.dirname(os.path.abspath(__file__))
outdir = os.path.join(here, "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "readout_parity_mechanism.json"), "w") as f:
    json.dump(out, f, indent=2)
print(f"\n{len(passes)} passed, {len(fails)} failed")
raise SystemExit(1 if fails else 0)
