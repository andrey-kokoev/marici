"""Variation-audit checker: the fold engine's character theorem is
HARD TO VARY (marici.Strominger).

Companion to (does NOT import or modify):
  research/strominger/checkers/rung5_readout_checks.py
  research/strominger/checkers/readout_parity_mechanism_checks.py

Motivation. rung5_readout_checks.py certified the character theorem
P(E_g) = +u^{g+2} E_g, P(M_g) = -u^{g+3} M_g for the baseline engine
(datum C = (u+1/u)/z^2, fold weights s = 2,3,...,g+1, connection
Gam = -2 zb/(1+u)) and with it the rung alternation E,M,E,M of the
square-root gate obstruction. Deutsch's hard-to-vary criterion asks:
which inputs does this explanation actually depend on? This checker
perturbs every engine input and certifies, for each variant and grades
g = 2,3 (baseline also g = 4), the EXACT structure of the ratio
R_X = P(X)/X for X in {E_g, M_g}:
  (i)   u-diagonality: R is a rational function of u alone;
  (ii)  norm-1 (Blaschke) law: R(u) R(1/u) = 1 — forced by P^2 = id
        and P(u) = 1/u, so it must hold for EVERY variant;
  (iii) monomiality: R = +/- u^e (pure character) or not;
  (iv)  leading valuation val_u(R).

Findings certified below.
  * Baseline (V0): monomial characters +u^{g+2}, -u^{g+3} (g = 2..4).
  * Datum freedom (V1, V8): the invariant datum class
    C_k = (u^k + u^{-k})/z^2 (k = 1,2,3) and any nonzero rescaling give
    the IDENTICAL characters. The theorem is not fine-tuned to the datum.
  * Engine rigidity (V2-V6): every perturbation of the weights
    (step 2, or start 3) or of the connection (numerator -1, denominator
    1+u^2, denominator (1+u)^2) destroys monomiality: R becomes a genuine
    non-monomial rational function — while REMAINING u-diagonal, norm-1,
    and with the baseline valuations val_u R_E = g+2, val_u R_M = g+3.
    The character "wants" to stay; what breaks is exactly the collapse of
    the Blaschke factor f(u)/u^d f(1/u) to 1.
  * Symmetry-class boundary (V7): a single-sheet datum C+ = zb/z (not
    invariant under the sheet exchange) also breaks monomiality and
    shifts the valuations to (g, g+1).

Hence the load-bearing core of the alternation explanation is the
connection Gamma = -2 zb/(1+u) together with unit weight increments
starting at 2; the datum may range freely over its invariant class.
The obstruction P(M) - M = -(1+u^{g+3}) M is a property of the ENGINE,
not of the anchor.

Layers:
  V0   baseline characters exact, g = 2..4.
  V1   datum-class invariance: gaps k = 2,3 and rescaling give the
       identical characters, g = 2,3 (scale: g = 2).
  INV  universal involution law: R(u) R(1/u) = 1 for every readout of
       every variant (including the baseline).
  KILL V2-V7: for each perturbed variant and g = 2,3 both ratios are
       u-diagonal, NON-monomial, norm-1, and carry the expected
       valuations (baseline-shifted for V2-V6; sheet-shifted for V7).

Output: research/strominger/results/variation_audit.json
Exit code 0 iff every check passes.
"""
import json
import os
import sympy as sp

z, zb = sp.symbols("z zb")
u = z * zb
uu = sp.Symbol("uu")

GAM0 = -2 * zb / (1 + u)
GAMB0 = -2 * z / (1 + u)

results = []


def simp(e):
    e = sp.together(sp.expand(e))
    if e != 0:
        e = sp.cancel(e)
    return e


def record(cid, group, statement, status, detail=""):
    results.append({
        "id": cid, "group": group, "statement": statement,
        "status": status, "detail": detail,
    })
    print(f"[{status:>4}] {cid}: {statement}"
          + (f"  ({detail})" if detail else ""), flush=True)


def check_true(cid, group, statement, cond, detail=""):
    record(cid, group, statement, "pass" if bool(cond) else "FAIL", detail)
    return bool(cond)


def sigma(e):
    return e.subs([(z, zb), (zb, z)], simultaneous=True)


def P_map(e):
    return e.subs([(z, -1 / z), (zb, -1 / zb)], simultaneous=True)


def readouts_param(Cd, g, wstart, wstep, Gam, Gamb):
    """Grade-g readouts with parameterized datum, weights, connection."""
    f, fb = Cd, sigma(Cd)
    for i in range(g):
        s = wstart + i * wstep
        f = simp(sp.diff(f, z) - s * Gam * f)
        fb = simp(sp.diff(fb, zb) - s * Gamb * fb)
    A = simp(sp.diff(f, zb))
    B = simp(sp.diff(fb, z))
    return simp(f + fb), simp(A - B)


def analyze_ratio(X):
    """Structure of R = P(X)/X: (u_diagonal, monomial (c,e)|None,
    valuation, norm1)."""
    R = simp(P_map(X) / X)
    Ru = sp.cancel(sp.together(R.subs([(zb, uu / z)], simultaneous=True)))
    diag = not Ru.has(z) and not (Ru.free_symbols - {uu})
    if not diag:
        return False, None, None, False
    num, den = sp.fraction(Ru)
    num = sp.Poly(sp.expand(num), uu)
    den = sp.Poly(sp.expand(den), uu)
    mon = None
    if len(num.monoms()) == 1 and len(den.monoms()) == 1:
        mon = (sp.Rational(num.LC(), den.LC()),
               num.monoms()[0][0] - den.monoms()[0][0])
    val = min(m[0] for m in num.monoms()) - min(m[0] for m in den.monoms())
    n1 = sp.cancel(Ru * Ru.subs(uu, 1 / uu)) == 1
    return True, mon, val, n1


C1 = (u + 1 / u) / z ** 2

# ---------------------------------------------------------------- V0 baseline
BASE_CHARS = {"E": (1, 2), "M": (-1, 3)}  # (sign, exponent offset from g)
for g in (2, 3, 4):
    E, M = readouts_param(C1, g, 2, 1, GAM0, GAMB0)
    for name, X in (("E", E), ("M", M)):
        sgn, off = BASE_CHARS[name]
        diag, mon, val, n1 = analyze_ratio(X)
        check_true(f"V0.g{g}.{name}", "V0",
                   f"baseline {name}_{g} has character "
                   f"{'+' if sgn > 0 else '-'}u^{g + off}",
                   diag and mon == (sgn, g + off) and val == g + off and n1,
                   f"monomial={mon}, val={val}, norm1={n1}")

# ------------------------------------------------------- V1 datum-class freedom
for k in (2, 3):
    Ck = (u ** k + u ** (-k)) / z ** 2
    for g in (2, 3):
        E, M = readouts_param(Ck, g, 2, 1, GAM0, GAMB0)
        for name, X in (("E", E), ("M", M)):
            sgn, off = BASE_CHARS[name]
            diag, mon, val, n1 = analyze_ratio(X)
            check_true(f"V1.k{k}.g{g}.{name}", "V1",
                       f"datum gap k={k}: {name}_{g} keeps character "
                       f"{'+' if sgn > 0 else '-'}u^{g + off}",
                       diag and mon == (sgn, g + off) and n1,
                       f"monomial={mon}, val={val}, norm1={n1}")

for g in (2,):
    E, M = readouts_param(7 * C1, g, 2, 1, GAM0, GAMB0)
    for name, X in (("E", E), ("M", M)):
        sgn, off = BASE_CHARS[name]
        diag, mon, val, n1 = analyze_ratio(X)
        check_true(f"V1.scale.g{g}.{name}", "V1",
                   f"datum rescaling 7*C: {name}_{g} keeps character "
                   f"{'+' if sgn > 0 else '-'}u^{g + off}",
                   diag and mon == (sgn, g + off) and n1,
                   f"monomial={mon}, val={val}, norm1={n1}")

# ------------------------------------------------- KILL perturbed engines V2-V7
VARIANTS = [
    ("V2", "weight step 2 (s=2,4,6,...)", C1, 2, 2, GAM0, GAMB0, (2, 3)),
    ("V3", "weight start 3 (s=3,4,5,...)", C1, 3, 1, GAM0, GAMB0, (2, 3)),
    ("V4", "connection numerator -1", C1, 2, 1,
     -zb / (1 + u), -z / (1 + u), (2, 3)),
    ("V5", "connection denominator 1+u^2", C1, 2, 1,
     -2 * zb / (1 + u ** 2), -2 * z / (1 + u ** 2), (2, 3)),
    ("V6", "connection denominator (1+u)^2", C1, 2, 1,
     -2 * zb / (1 + u) ** 2, -2 * z / (1 + u) ** 2, (2, 3)),
    ("V7", "single sheet C+ = zb/z", zb / z, 2, 1, GAM0, GAMB0, (0, 1)),
]

for tag, desc, Cd, ws, wk, Gam, Gamb, (offE, offM) in VARIANTS:
    offs = {"E": offE, "M": offM}
    for g in (2, 3):
        E, M = readouts_param(Cd, g, ws, wk, Gam, Gamb)
        for name, X in (("E", E), ("M", M)):
            diag, mon, val, n1 = analyze_ratio(X)
            ok = diag and mon is None and n1 and val == g + offs[name]
            check_true(f"{tag}.g{g}.{name}", "KILL",
                       f"{tag} ({desc}): {name}_{g} ratio non-monomial, "
                       f"norm-1, val_u = g+{offs[name]}",
                       ok,
                       f"diag={diag}, monomial={mon}, val={val}, norm1={n1}")

# ------------------------------------------------------------------- summary
passes = [r for r in results if r["status"] == "pass"]
fails = [r for r in results if r["status"] != "pass"]
out = {
    "schema": "marici.checker_results.v1",
    "checker": "variation_audit_checks.py",
    "author": "marici.Strominger",
    "checks": results,
    "n_pass": len(passes),
    "n_fail": len(fails),
    "verdict": (
        "The fold engine's character theorem is HARD TO VARY. The "
        "invariant datum class (gaps k = 1,2,3, arbitrary scale) leaves "
        "the characters +u^{g+2}, -u^{g+3} untouched (V0, V1), while "
        "every perturbation of the fold weights or of the connection "
        "Gamma = -2 zb/(1+u) destroys monomiality (KILL: V2-V6), and "
        "leaving the invariant datum class destroys it as well (V7). "
        "Across ALL variants the ratio P(X)/X stays u-diagonal and "
        "norm-1, R(u) R(1/u) = 1, as forced by P^2 = id; the perturbed "
        "engines differ from the baseline exactly by a nontrivial "
        "Blaschke factor f(u)/u^d f(1/u), and (for V2-V6) retain the "
        "baseline valuations g+2, g+3. The load-bearing core of the "
        "rung alternation is therefore the connection plus the unit "
        "weight increments; the datum is free within its invariant class."
    ),
}
here = os.path.dirname(os.path.abspath(__file__))
outdir = os.path.join(here, "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "variation_audit.json"), "w") as f:
    json.dump(out, f, indent=2)
print(f"\n{len(passes)} passed, {len(fails)} failed", flush=True)
raise SystemExit(1 if fails else 0)
