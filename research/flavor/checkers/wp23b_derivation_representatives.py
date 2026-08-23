#!/usr/bin/env python3
"""WP23b: exact derivation-backbone certificate. For one representative
of each of the four WP22 classes, exhibit the full factorization of
detC(z) directly from a single symbolic determinant computation and
verify each factor against its claimed structural form:

  * diagonal (84_159): Vandermonde gap product x bracket telescoping.
  * 4cycle_trivial (85_87): detC = -M(z-z^-1) chi_b(s).
  * 4cycle_leafcol_diff (85_205): W = (d02^2 - d21^2), difference of
    squares of the two leaf columns.
  * 6cycle_row_diff (85_94): W = (d01^2 + d02^2 - d20^2), row-Gram
    difference of the two cycle-touched rows.

Writes: results/wp23b_derivation_representatives.json
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from wp22_w_identification import texture_sym, sector_data, mask_slots, blocks_of
from wp23_topology_enumeration import canonical_phase_edge

z, lam = sp.symbols("z lam")

REPS = {
    "diagonal": (84, 159),
    "4cycle_trivial": (85, 87),
    "4cycle_leafcol_diff": (85, 205),
    "6cycle_row_diff": (85, 94),
}


def build(mu, md):
    pe, _ = canonical_phase_edge(mu, md)
    Yu, ue = texture_sym(mu, "u")
    Yd, de = texture_sym(md, "d")
    for M, entries, pfx in ((Yu, ue, "u"), (Yd, de, "d")):
        for i, j, s in entries:
            if pfx == pe[0] and (i, j) == (pe[1], pe[2]):
                M[i, j] = s * z
    return pe, sector_data(Yu), sector_data(Yd)


def detc(Hu, Hd):
    return sp.expand((Hu * Hd - Hd * Hu).det())


def sym(name):
    return sp.symbols(name, positive=True)


results = {}

# --- diagonal: detC = -(g01 g02 g12) * bracket, bracket = M(z-z^-1)
pe, Hu, Hd = build(*REPS["diagonal"])
g = {(a, b): sp.expand(Hu[a, a] - Hu[b, b]) for a, b in ((0, 1), (0, 2), (1, 2))}
V = sp.expand(g[(0, 1)] * g[(0, 2)] * g[(1, 2)])
D = detc(Hu, Hd)
ratio = sp.factor(sp.expand(D / V))
M = sym("d00") * sym("d01") * sym("d10") * sym("d11") * sym("d21") ** 2
ok = sp.expand(ratio + M * (z - 1 / z)) == 0 or sp.expand(ratio - M * (z - 1 / z)) == 0
results["diagonal"] = {"rep": "84_159", "detC_over_vandermonde": str(ratio),
                       "bracket_is_pm_M_zmzinv": bool(ok)}

# --- block21 representatives: detC = ±M(z-z^-1) chi_b(s) W
for cls in ("4cycle_trivial", "4cycle_leafcol_diff", "6cycle_row_diff"):
    mu, md = REPS[cls]
    pe, Hu, Hd = build(mu, md)
    bl = blocks_of(mask_slots(mu))
    sing = [b[0] for b in bl if len(b) == 1][0]
    blk = [b for b in bl if len(b) == 2][0]
    Hb = Hu.extract(blk, blk)
    chib = sp.Poly(Hb.charpoly(lam).as_expr(), lam)
    s = Hu[sing, sing]
    chi_at_s = sp.expand(chib.as_expr().subs(lam, s))
    D = detc(Hu, Hd)
    # divide out chi_b(s) and (z - z^-1); remainder must be ±monomial*W_form
    rem = sp.factor(sp.expand(D / (chi_at_s * (z - 1 / z))))
    entry = {"rep": f"{mu}_{md}", "detC_over_chib_zmzinv": str(rem)}
    def signmatch(a, b):
        if sp.expand(a - b) == 0:
            return 1
        if sp.expand(a + b) == 0:
            return -1
        return 0
    if cls == "4cycle_trivial":
        expected = sym("d00") * sym("d01") ** 2 * sym("d11") ** 2 * sym("d20") * sym("u00") * sym("u20")
        sgn = signmatch(rem, expected)
        entry["remainder_is_monomial"] = sgn != 0
        entry["sign"] = sgn
    elif cls == "4cycle_leafcol_diff":
        W = sym("d02") ** 2 - sym("d21") ** 2
        expected = sym("d00") * sym("d10") ** 2 * sym("d20") * sym("u00") * sym("u20") * W
        sgn = signmatch(rem, expected)
        entry["remainder_is_monomial_times_leafcol_diff"] = sgn != 0
        entry["sign"] = sgn
    else:
        W = sym("d01") ** 2 + sym("d02") ** 2 - sym("d20") ** 2
        expected = sym("d01") * sym("d10") * sym("d11") * sym("d20") * sym("u00") * sym("u20") * W
        sgn = signmatch(rem, expected)
        entry["remainder_is_monomial_times_row_diff"] = sgn != 0
        entry["sign"] = sgn
    results[cls] = entry

allok = all(all(vv for kk, vv in r.items() if kk.startswith(("bracket", "remainder")))
            for r in results.values())
out = {"purpose": "WP23b derivation backbone: exact factorization exhibited "
                  "on one representative per class",
       "all_checks_ok": allok, "representatives": results}
with open("results/wp23b_derivation_representatives.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1)[:1500])
print("ALL OK" if allok else "FAILURES PRESENT")
