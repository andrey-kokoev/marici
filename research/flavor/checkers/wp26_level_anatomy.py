"""WP26 v2: anatomy of the L levels - physical Vandermondes vs chart factors.

WP25a/25b reduced the phase spectrum to the realized values of
L = a1/(Du Dd) and showed the levels are per-class properties. WP21e's
reduced form is UNIVERSALLY

  L = M * W / (gap * D_other)

(block21: gap = sqrt(disc_b), the chi_b(s) of WP21 having cancelled
against Du_sec = sqrt(disc_b)*|chi_b(s)|; diagonal: gap = the
remaining-gap product). v1 of this checker wrongly re-inserted ln chi
into the L identity; its residual failures exposed exactly the
cancellation. v2 uses the correct identity throughout.

Structural content certified here:

  A. Du and Dd are PHYSICAL (functions of the squared quark masses):
     ln(Du*Dd) is constant across all 1210 minima at fit precision;
     ln D_other is constant within each sector-homogeneous subset and
     its global spread is exactly the u/d sector mixing (Du vs Dd).
  B. the corrected residual lnW = lnL - lnM + lngap + lnDo is ~0 on
     WP22's W=+-1 classes and equals ln|W| (bounded away from 0) on
     the 284 multi-term Gram-norm-difference textures.
  C. per-cluster anatomy: std of every chart factor log (lnM, lngap,
     lnW) vs std of lnL - what freezes in rigid clusters 1,2 and what
     compensates in conspiracy clusters 0,3,4; correlation matrices.
  D. lnK = ln(a1/D_sec) = lnM + lnW - lngap: the chart content of L,
     clustered the same way as lnL (D_sec physical).

Reads: results/wp20_valley_audit.json,
       results/wp21e_universal_factorization.json
Writes: results/wp26_level_anatomy.json
Run: ../.venv/Scripts/python checkers/wp26_level_anatomy.py
"""
import json, math, collections, sys
import numpy as np

sys.path.insert(0, 'checkers')
from wp25_center_selection import factor_rows

def main():
    wp20 = json.load(open("results/wp20_valley_audit.json"))
    fac = json.load(open("results/wp21e_universal_factorization.json"))["census"]
    recs = wp20["records"]

    phis = sorted(r["phi_folded_deg"] for r in recs)
    centers, cur = [], [phis[0]]
    for p in phis[1:]:
        if p - cur[-1] > 1.5:
            centers.append(sum(cur) / len(cur)); cur = [p]
        else:
            cur.append(p)
    centers.append(sum(cur) / len(cur))

    rows = factor_rows(recs, fac, centers)
    for x in rows:
        # corrected WP21e reduced form: L = M*W/(gap*D_other)
        x["lnW"] = x["lnL"] - x["lnM"] + x["lngap"] + x["lnDo"]
        x["lnK"] = x["lnL"] + x["lnDo"]          # = lnM + lnW - lngap
        x["lnDuDd"] = x["lnDo"] + (x["lnL"] - math.log(x["L"]) if False else 0.0)
    # lnDsec: D_sec = a1/L/D_other ... no: L = a1/(Du Dd) and D_other is
    # one factor; D_sec = (Du Dd)/D_other. Track ln(Du Dd) = ln(a1) - lnL
    # with ln(a1) = ln(sqrt(rho_v)) + ln(Du Dd) - circular. Instead:
    # Du Dd = a1/L and a1 = sqrt(rho_v)*Du*Dd => we cannot separate
    # without rho_v; use stored rho_v.
    rho = {i: r.get("rho_v") for i, r in enumerate(recs)}
    # rebuild rec index aligned with rows is fragile; instead compute
    # ln(Du Dd) = ln(a1) - lnL requires a1. factor_rows used
    # a1 = sqrt(rho_v)*Du*Dd, so ln(Du Dd) is NOT recoverable from the
    # row alone; add it via a second pass on recs is unnecessary:
    # physical constancy of Du*Dd follows from lnL + lnK identity? No.
    # Direct: lnDuDd = ln(a1) - ln(L), and a1 = sqrt(rho_v)*DuDd, so we
    # need rho_v per row. Attach it here by key+phi matching.
    by_key = {}
    for r in recs:
        mu, md = r["member"]; pe = r["phase_edge"]
        k = f"{mu}_{md}_{pe[0]}{pe[1]}{pe[2]}"
        by_key.setdefault(k, []).append(r)
    for x in rows:
        cands = by_key[x["key"]]
        r = min(cands, key=lambda r: abs(r["phi_folded_deg"] - x["phi_deg"]))
        rv = r["rho_v"]
        # a1 = sqrt(rho_v) * Du * Dd ; L = a1/(Du Dd)
        # => Du Dd = a1 / L and a1 = sqrt(rho_v) * Du * Dd
        # => Du Dd = sqrt(rho_v) * (Du Dd)^2 / a1 ... circular, so solve:
        # a1 = sqrt(rho_v)*(Du Dd) and L = a1/(Du Dd)
        # => (Du Dd) = a1/L = sqrt(rho_v)*(Du Dd)/L => Du Dd = L/sqrt(rho_v)
        x["lnDuDd"] = x["lnL"] - 0.5*math.log(rv)
        x["lnDsec"] = x["lnDuDd"] - x["lnDo"]

    n = len(rows)
    FACTORS = ["lnM", "lngap", "lnW", "lnL", "lnK", "lnDo", "lnDsec", "lnDuDd", "lnJ"]

    def stats(xs, keys):
        return {k: dict(mean=float(np.mean([x[k] for x in xs])),
                        std=float(np.std([x[k] for x in xs])),
                        min=float(np.min([x[k] for x in xs])),
                        max=float(np.max([x[k] for x in xs]))) for k in keys}

    out = {"purpose": "WP26 v2 level anatomy: physical Vandermondes vs chart factors",
           "n_minima": n, "centers": centers}
    out["global"] = stats(rows, FACTORS)

    # A. physical constancy of Du*Dd (both Vandermondes physical)
    out["physical_constancy"] = dict(
        lnDuDd_std=out["global"]["lnDuDd"]["std"],
        lnDo_std_global=out["global"]["lnDo"]["std"],
        note="lnDo global spread is the u/d sector mix (Du vs Dd); "
             "within sector-pure subsets it must sit at fit precision")

    # B. corrected lnW residual
    wterms = {k: v.get("W_terms") for k, v in fac.items()}
    res1 = [abs(x["lnW"]) for x in rows if wterms.get(x["key"]) == 1]
    resM = [abs(x["lnW"]) for x in rows if (wterms.get(x["key"]) or 0) >= 2]
    out["lnW_residual"] = dict(
        n_w1=len(res1), max_abs_lnW_w1=float(max(res1)) if res1 else None,
        n_multi=len(resM),
        min_abs_lnW_multi=float(min(resM)) if resM else None,
        max_abs_lnW_multi=float(max(resM)) if resM else None)

    # C. per-cluster anatomy
    by_cluster = collections.defaultdict(list)
    for x in rows:
        by_cluster[x["cluster"]].append(x)
    cl_out = {}
    CHART = ["lnM", "lngap", "lnW"]
    for ci in sorted(by_cluster):
        xs = by_cluster[ci]
        entry = dict(center=centers[ci], n=len(xs),
                     factors=stats(xs, FACTORS),
                     types=dict(collections.Counter(x["type"] for x in xs)),
                     sectors=dict(collections.Counter(x["sector"] for x in xs)))
        if len(xs) >= 10:
            X = np.array([[x[k] for k in CHART] for x in xs])
            with np.errstate(all="ignore"):
                C = np.corrcoef(X.T)
            entry["chart_corr"] = {f"{CHART[i]}~{CHART[j]}": float(C[i, j])
                                   for i in range(len(CHART)) for j in range(i+1, len(CHART))
                                   if np.isfinite(C[i, j])}
            L = np.array([x["lnL"] for x in xs])
            entry["corr_with_lnL"] = {k: float(np.corrcoef(X[:, i], L)[0, 1])
                                      for i, k in enumerate(CHART)
                                      if np.std(X[:, i]) > 0}
        cl_out[str(ci)] = entry
    out["clusters"] = cl_out

    json.dump(out, open("results/wp26_level_anatomy.json", "w"), indent=1)

    print("n minima:", n)
    pc = out["physical_constancy"]
    print("PHYSICAL: ln(Du Dd) global std = %.3e ; lnDo global std = %.3e (sector mix)" % (
        pc["lnDuDd_std"], pc["lnDo_std_global"]))
    rw = out["lnW_residual"]
    print("lnW residual: W=1 classes max |lnW| = %.3e (n=%d); multi-term [%.3e, %.3e] (n=%d)" % (
        rw["max_abs_lnW_w1"], rw["n_w1"], rw["min_abs_lnW_multi"],
        rw["max_abs_lnW_multi"], rw["n_multi"]))
    for ci, e in cl_out.items():
        f = e["factors"]
        print("cluster %s n=%d std: lnM %.2e lngap %.2e lnW %.2e | lnL %.2e lnK %.2e lnDo %.2e lnDsec %.2e" % (
            ci, e["n"], f["lnM"]["std"], f["lngap"]["std"], f["lnW"]["std"],
            f["lnL"]["std"], f["lnK"]["std"], f["lnDo"]["std"], f["lnDsec"]["std"]))
        if "corr_with_lnL" in e:
            print("   corr with lnL:", {k: round(v, 3) for k, v in e["corr_with_lnL"].items()})
    print("-> results/wp26_level_anatomy.json")

if __name__ == "__main__":
    main()
