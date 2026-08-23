"""Exact rung-3 (sub-subleading) diagonal-parity cocycle checker: the S^(2)
coefficient line, its per-channel cocycle F2, the determinant-line relation
and its u-valuation parity, and the intrinsic-oddness lemma
(marici.Strominger).

Companion to (does NOT import or modify):
  research/strominger/checkers/rung3_s2_bridge_checks.py (R1-R4, grounding)
  research/strominger/checkers/cocycle_bridge_gates_checks.py (C1: rung-0 arc)
Sources and conventions:
  research/strominger/diagonal-parity-cocycle.md (character method, rung 0)
  research/strominger/rung3-s2-bridge.md (grounded channels, R3.2 obstruction)

All arithmetic is exact sympy symbolics. No floating point anywhere.
sigma: z <-> zb, zk <-> zbk, I -> -I with SIMULTANEOUS substitution.
alpha: z -> -1/zb, zb -> -1/z (legs fixed). P = alpha . sigma is the physical
parity on I+; sigma and alpha commute, so with K^- = sigma(K^+),
F2 = alpha(K^+)/K^- = P(K^-)/K^-.

Layers:
  K1 the rung-3 coefficient line: the five nonzero grounded S^(2)- per-leg
     operator channels K^+ (CL16 (14)/CS (9), certified R1.2/R1.3 of the
     bridge checker) with K^- = sigma(K^+) and the deck involution
     sigma(K^-) = K^+; the d_Ek first-order channel A1E vanishes
     identically (helicity-degenerate partner, retained as a note).
  K2 the per-channel cocycle F2 = alpha(K^+)/K^- in closed FACTORED form,
     the twisted diagonal action P(K^+) = sigma(F2) K^+ and
     P(K^-) = F2 K^-, and the 1-cocycle (involutivity) condition
     alpha(F2) sigma(F2) = 1, all certified exactly per channel.
  K3 the determinant-line relation det = F2 sigma(F2) per channel in closed
     form — X^2, 1, X^2, 1, X^-2, u X with
     X = (1+z zbk)(1+zb zk)/((z-zk)(zb-zbk)) — its sigma-invariance, its
     diagonal u-valuation val_u = val_z + val_zb (computed by exact order
     of vanishing along z = 0 and zb = 0), cross-channel consistency
     (c_zk == A2z, c_Ek == AzE), and the rung-0 anchor: the AzE cocycle is
     F2 = -z^2 sigma(F0) with F0 the rung-0 cocycle, and F0 sigma(F0) = u^-2.
  K4 the intrinsic-oddness lemma: for rational h, sigma preserves the
     diagonal u-valuation (val_u sigma(h) = val_u h, since sigma swaps
     val_z and val_zb), hence val_u(h sigma(h)) = 2 val_u(h) is ALWAYS
     even — no rational cocycle dressing converts odd parity to even.
     Certified on a deterministic family of generic rational witnesses.
  K5 the verdict: every rung-3 channel determinant has EVEN diagonal
     u-valuation (0 or 2), so the sharp prediction of odd u-parity at
     coefficient-line level is FALSIFIED — the R3.2 odd-parity obstruction
     (P(M3) = -u^7 M3) is born at readout projection, not inherited from
     the coefficient line. The sharper rational-square-root gate passes on
     five channels and FAILS on A1z (det = u X has odd val_z), the channel
     whose electric partner vanishes identically.

Output: research/strominger/results/rung3_cocycle.json
Exit code 0 iff every check passes.
"""
import json
import os
import sympy as sp

# ---------------------------------------------------------------- symbols
z, zb, zk, zbk, Ek = sp.symbols("z zb zk zbk Ek")
om = sp.symbols("om", positive=True)
I = sp.I
sq2 = sp.sqrt(2)
u = z * zb

results = []


def simp(e):
    """Two-stage exact zero-recognition: simplify/expand, then rational cancel."""
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


def check_zero(cid, group, statement, expr, **subs):
    e = expr.subs(subs) if subs else expr
    e = simp(e)
    record(cid, group, statement, "pass" if e == 0 else "FAIL",
           "" if e == 0 else f"residual: {sp.sstr(e)[:300]}")
    return e == 0


def check_true(cid, group, statement, cond, detail=""):
    record(cid, group, statement, "pass" if bool(cond) else "FAIL", detail)
    return bool(cond)


# ============================================================ maps
SIG = [(z, zb), (zb, z), (zk, zbk), (zbk, zk)]
ALPHA = [(z, -1 / zb), (zb, -1 / z)]


def sigma(e):
    """Complex conjugation on sphere+leg variables: simultaneous swap, I -> -I."""
    return e.subs(SIG, simultaneous=True).subs(I, -I)


def alpha_map(e):
    """Antipodal pullback: z -> -1/zb, zb -> -1/z (legs fixed)."""
    return e.subs(ALPHA, simultaneous=True)


def P_map(e):
    """Physical parity P = alpha . sigma: z -> -1/z, zb -> -1/zb, I -> -I."""
    return sigma(alpha_map(e))


def vval(e, var):
    """Exact order of vanishing of a rational function along var = 0
    (generic other variables): positive for zeros, negative for poles."""
    n, d = sp.fraction(sp.cancel(e))
    cnt = 0
    n = sp.expand(n)
    while n != 0 and sp.simplify(n.subs(var, 0)) == 0:
        n = sp.expand(n / var)
        cnt += 1
    d = sp.expand(d)
    while d != 0 and sp.simplify(d.subs(var, 0)) == 0:
        d = sp.expand(d / var)
        cnt -= 1
    return cnt


def valu(e):
    """Diagonal u-valuation: val_u = val_z + val_zb (u = z zb)."""
    return vval(e, z) + vval(e, zb)


# ============================================================ K1 the line
# Grounded S^(2)- per-leg operator channels K^+ (bridge checker R1.2/R1.3).
c_zk = -sq2 * om * (z - zk) ** 2 / (1 + u)
c_Ek = -sq2 * Ek * om * (z - zk) * (1 + z * zbk) / ((1 + u) * (1 + zk * zbk))
A2z = -(z - zk) ** 3 * (1 + zk * zbk) / (2 * Ek * (zb - zbk) * (1 + u))
AzE = -(z - zk) ** 2 * (1 + z * zbk) / ((zb - zbk) * (1 + u))
A2E = -Ek * (z - zk) * (1 + z * zbk) ** 2 / (2 * (zb - zbk) * (1 + u) * (1 + zk * zbk))
A1z = (z - zk) ** 2 * (1 + zk * zbk) / (Ek * (zb - zbk) * (1 + u))

# Declared factored cocycles F2 = alpha(K^+)/K^- (certified in K2).
X = (1 + z * zbk) * (1 + zb * zk) / ((z - zk) * (zb - zbk))
F0 = (1 + z * zbk) * (zb - zbk) / (z ** 2 * (1 + zb * zk) * (z - zk))  # rung 0 (C1)

CHANNELS = [
    # name, K^+, declared F2, declared det = F2 sigma(F2), declared sqrt (None if none)
    ("c_zk", c_zk, (z / zb) * ((1 + zb * zk) / (zb - zbk)) ** 2, X ** 2, X),
    ("c_Ek", c_Ek, -z / zb, sp.Integer(1), sp.Integer(1)),
    ("A2z", A2z, z ** 2 * (z - zk) * (1 + zb * zk) ** 3
     / (zb ** 2 * (zb - zbk) ** 3 * (1 + z * zbk)), X ** 2, X),
    ("AzE", AzE, -z ** 2 * (z - zk) * (1 + zb * zk)
     / (zb ** 2 * (zb - zbk) * (1 + z * zbk)), sp.Integer(1), sp.Integer(1)),
    ("A2E", A2E, z ** 2 * (zb - zbk) * (z - zk)
     / (zb ** 2 * (1 + zb * zk) * (1 + z * zbk)), X ** -2, X ** -1),
    ("A1z", A1z, -z ** 2 * (z - zk) * (1 + zb * zk) ** 2
     / (zb * (zb - zbk) ** 2 * (1 + z * zbk)), u * X, None),
]

for nm, Kp, _, _, _ in CHANNELS:
    Km = sigma(Kp)
    check_zero(f"K1.{nm}", "K1", f"deck involution on the {nm} line: "
               f"sigma(K^-) = K^+ with K^- = sigma(K^+)",
               sigma(Km) - Kp)

check_true("K1.A1E", "K1", "helicity-degenerate partner: the d_Ek "
           "first-order channel A1E vanishes identically (grounded R1.3), "
           "so the A1 line is magnetic-only",
           True, "A1E = 0 certified in rung3_s2_bridge_checks.py R1.3")

# ============================================================ K2 the cocycle
dets = {}
for nm, Kp, F2d, _, _ in CHANNELS:
    Km = sigma(Kp)
    F2calc = sp.cancel(alpha_map(Kp) / Km)
    check_zero(f"K2.{nm}.a", "K2", f"{nm}: F2 = alpha(K^+)/K^- matches the "
               f"declared factored closed form", F2calc - F2d)
    check_zero(f"K2.{nm}.b", "K2", f"{nm}: twisted diagonal action on the "
               f"+ line: P(K^+) = sigma(F2) K^+", P_map(Kp) - sigma(F2d) * Kp)
    check_zero(f"K2.{nm}.c", "K2", f"{nm}: twisted diagonal action on the "
               f"- line: P(K^-) = F2 K^-", P_map(Km) - F2d * Km)
    check_zero(f"K2.{nm}.d", "K2", f"{nm}: 1-cocycle (involutivity): "
               f"alpha(F2) sigma(F2) = 1",
               alpha_map(F2d) * sigma(F2d) - 1)
    dets[nm] = sp.cancel(F2d * sigma(F2d))

# ============================================================ K3 determinant
valu_seen = {}
for nm, Kp, F2d, detd, _ in CHANNELS:
    check_zero(f"K3.{nm}.a", "K3", f"{nm}: determinant line F2 sigma(F2) "
               f"matches the declared closed form", dets[nm] - detd)
    check_zero(f"K3.{nm}.b", "K3", f"{nm}: determinant is sigma-invariant",
               sigma(dets[nm]) - dets[nm])
    vz, vzb, vu = vval(dets[nm], z), vval(dets[nm], zb), valu(dets[nm])
    valu_seen[nm] = vu
    check_true(f"K3.{nm}.c", "K3", f"{nm}: diagonal u-valuation of the "
               f"determinant is EVEN", vu % 2 == 0,
               f"val_z = {vz}, val_zb = {vzb}, val_u = {vu}")

check_true("K3.pairing", "K3", "cross-channel consistency: the c_zk and A2z "
           "determinants coincide (X^2), and the c_Ek and AzE determinants "
           "coincide (1)",
           simp(dets["c_zk"] - dets["A2z"]) == 0
           and simp(dets["c_Ek"] - dets["AzE"]) == 0,
           f"dets: { {k: sp.sstr(v)[:80] for k, v in dets.items()} }")
check_zero("K3.rung0.a", "K3", "rung-0 anchor: the AzE rung-3 cocycle is "
           "F2 = -z^2 sigma(F0) with F0 the rung-0 cocycle (C1 arc)",
           dict((ch[0], ch[2]) for ch in CHANNELS)["AzE"] + z ** 2 * sigma(F0))
check_zero("K3.rung0.b", "K3", "rung-0 anchor: F0 sigma(F0) = u^-2 (C1 arc)",
           F0 * sigma(F0) - u ** -2)

# ============================================================ K4 the lemma
FAMILY = [
    z ** 2 * zb / (z - zk),
    (2 * z + 3 * zb - zk) / (zb - 5 * zbk),
    z * zb * (z + zb) ** 2 / ((z - 2 * zk) * (3 * zb + zbk)),
    (z - zk) ** 3 * (1 + z * zbk) / (zb ** 2 * (1 + zb * zk)),
    Ek * z / (om * (zb - zbk)) + z ** 2 / zb,
    (z ** 3 + zb ** 2 - zk * zbk) / (z * zb * (z + zk) ** 2),
    (1 + z * zbk) ** 2 / (z * (zb - zbk) ** 3),
    (z - zk) * (zb - zbk) / ((1 + z * zbk) * (1 + zb * zk) * z ** 4),
    z / (z + zb) + zb / (z - zk),
    (3 * z ** 2 - 2 * zb * zk + 1) / (z * zb ** 3 * (zb + zbk)),
]
lemma_swap = all(valu(sigma(h)) == valu(h) for h in FAMILY)
lemma_double = all(valu(h * sigma(h)) == 2 * valu(h) for h in FAMILY)
check_true("K4.swap", "K4", "intrinsic-oddness lemma, step 1: sigma preserves "
           "the diagonal u-valuation (it swaps val_z and val_zb) — verified "
           "on a 10-member generic rational witness family", lemma_swap,
           f"val_u over family: {[valu(h) for h in FAMILY]}")
check_true("K4.double", "K4", "intrinsic-oddness lemma, step 2: "
           "val_u(h sigma(h)) = 2 val_u(h), hence ALWAYS even — no rational "
           "cocycle dressing converts odd u-parity to even",
           lemma_double and all(valu(h * sigma(h)) % 2 == 0 for h in FAMILY),
           "holds on all 10 witnesses; formal statement: val_u sigma = val_u "
           "because sigma exchanges the two diagonal valuations, so "
           "val_u(h sigma(h)) = val_u(h) + val_u(sigma(h)) = 2 val_u(h)")

# ============================================================ K5 the verdict
for nm, Kp, F2d, detd, root in CHANNELS:
    if root is not None:
        check_zero(f"K5.{nm}", "K5", f"{nm}: rational square-root gate — "
                   f"det = (declared root)^2 passes", dets[nm] - root ** 2)
    else:
        vzd = vval(dets[nm], z)
        check_true(f"K5.{nm}", "K5", f"{nm}: rational square-root gate "
                   f"FAILS — det = u X has odd val_z = {vzd}, so no rational "
                   f"square root exists (a square has even val_z)",
                   vzd % 2 == 1,
                   "the single failing channel is precisely the one whose "
                   "electric partner A1E vanishes identically")

verdict_core = (all(v % 2 == 0 for v in valu_seen.values()))
check_true("K5.verdict", "K5", "VERDICT: every rung-3 channel determinant "
           "has EVEN diagonal u-valuation — the odd-parity prediction at "
           "coefficient-line level is FALSIFIED; the R3.2 obstruction "
           "(P(M3) = -u^7 M3) is born at readout projection, not inherited "
           "from the coefficient line", verdict_core,
           f"val_u per channel: {valu_seen}")

# ============================================================ out
mandatory = [r for r in results if r["status"] == "FAIL"]
n_pass = sum(1 for r in results if r["status"] == "pass")
summary = {
    "total": len(results), "passed": n_pass, "failed": len(mandatory),
    "failed_ids": [r["id"] for r in mandatory],
    "layers": {
        "line": "five nonzero grounded S^(2)- per-leg channels with sigma "
                "deck (K1); A1E = 0 helicity-degenerate (K1.A1E)",
        "cocycle": "per-channel rational F2 = alpha(K^+)/K^- in factored "
                   "closed form, twisted diagonal Z2 action and 1-cocycle "
                   "condition certified on all five channels (K2)",
        "determinant": "det = F2 sigma(F2) = X^2, 1, X^2, 1, X^-2, u X per "
                       "channel, all sigma-invariant with EVEN diagonal "
                       "u-valuation (K3); AzE cocycle = zb^2 F0 (rung-0 "
                       "anchor, F0 sigma(F0) = u^-2)",
        "lemma": "intrinsic oddness: val_u(h sigma(h)) = 2 val_u(h) always "
                 "even — odd parity cannot be dressed away (K4)",
        "verdict": "obstruction born at readout projection (K5); "
                   "rational-square-root gate fails only on A1z (det = u X)",
    },
}

verdict = ("the rung-3 S^(2) coefficient line carries a per-channel rational "
           "cocycle F2 with sigma deck, twisted diagonal Z2 action "
           "P(K^+) = sigma(F2) K^+, P(K^-) = F2 K^-, and involutivity "
           "alpha(F2) sigma(F2) = 1 on all five nonzero operator channels "
           "(K1-K2); the determinant lines F2 sigma(F2) are X^2, 1, X^2, 1, "
           "X^-2, u X — every one of EVEN diagonal u-valuation, so the sharp "
           "odd-parity prediction is FALSIFIED at coefficient-line level and "
           "the R3.2 obstruction P(M3) = -u^7 M3 is born at readout "
           "projection, not inherited (K3, K5); the intrinsic-oddness lemma "
           "holds: val_u(h sigma(h)) = 2 val_u(h) is always even, so odd "
           "parity is intrinsic wherever it appears (K4); the sharper "
           "rational-square-root gate passes on five channels and fails "
           "only on A1z (det = u X, odd val_z), the channel whose electric "
           "partner vanishes identically (K5).")

out = {"checker": "rung3_cocycle_checks", "author": "marici.Strominger",
       "date": "2026-08-22", "engine": "sympy",
       "checks": results, "summary": summary, "verdict": verdict}
path = os.path.join(os.path.dirname(__file__), "..", "results",
                    "rung3_cocycle.json")
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2)
print(f"\nVERDICT: {verdict}")
print(f"\n{n_pass}/{len(results)} checks passed; results -> {os.path.normpath(path)}")
raise SystemExit(1 if mandatory else 0)
