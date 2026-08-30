#!/usr/bin/env python3
"""WP21d: which factor of the reduced a1 form drives the discrete
phase-cluster spectrum?

WP20 found 15 discrete phase clusters across 1210 viable minima, and
the inheritance identity J^2 = rho_v sin^2(phi) with
rho_v = (a1/(Du Dd))^2 makes a1/(Du Dd) = |J|/sin(phi) pointwise.
WP21a-c factor a1 = M * B with M a monomial and B an alternating
bracket absorbed by a Vandermonde factor: Du^2 = B^2 * Q_u (u-sector
absorption) or Dd^2 = B^2 * Q_d, so

    |a1|/(Du Dd) = M / (sqrt(Q_abs) * D_other)

-- a pure monomial over a gap factor times the other sector's
Vandermonde. This checker evaluates the three log-factors

    ln M,   -1/2 ln Q_abs,   -ln D_other

at every WP20 viable minimum and measures which one carries the
discreteness of the 15-cluster spectrum:

  * spread of each factor across the whole ensemble;
  * spread of each factor WITHIN each phase cluster (level-set test:
    if clusters are level sets of one factor, that factor is ~constant
    inside a cluster while the others vary);
  * correlation of each factor with phi_folded_deg.

Reads: results/wp20_valley_audit.json,
       results/wp21c_a1_cancellation_census.json
Writes: results/wp21d_factor_discreteness.json
"""
import json, math, re
from collections import defaultdict
import numpy as np

SLOTS = [(i, j) for i in range(3) for j in range(3)]


def mask_slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def tex_key(mu, md, pe):
    return f"{mu}_{md}_{pe[0]}{pe[1]}{pe[2]}"


def parse_monomial(monstr):
    """'d01*d10**2*d20' -> [('d01',1),('d10',2),('d20',1)]."""
    out = []
    for f in re.findall(r"[ud]\d\d(?:\*\*\d+)?", monstr):
        m = re.fullmatch(r"([ud]\d\d)(?:\*\*(\d+))?", f)
        assert m, f"unparseable factor {f!r} in {monstr!r}"
        out.append((m.group(1), int(m.group(2) or 1)))
    return out


def main():
    wp20 = json.load(open("results/wp20_valley_audit.json"))
    census = json.load(open("results/wp21c_a1_cancellation_census.json"))["census"]

    # cluster assignment: round phi_folded to clusters by 1-degree bins
    # after folding; cluster centers emerge from the data itself.
    recs = wp20["records"]
    # simple 1-D clustering: sort phi_folded_deg, split on gaps > 1.5 deg
    phis = sorted(r["phi_folded_deg"] for r in recs)
    centers, cur = [], [phis[0]]
    for p in phis[1:]:
        if p - cur[-1] > 1.5:
            centers.append(sum(cur) / len(cur)); cur = [p]
        else:
            cur.append(p)
    centers.append(sum(cur) / len(cur))
    def cluster_of(phi):
        return min(range(len(centers)), key=lambda i: abs(phi - centers[i]))
    print(f"emergent clusters: {len(centers)} at "
          f"{[round(c,2) for c in centers]}")

    rows = []
    skipped = defaultdict(int)
    for r in recs:
        mu, md = r["member"]
        pe = r["phase_edge"]
        key = tex_key(mu, md, pe)
        c = census.get(key)
        if not c or "monomial_M" not in c:
            skipped["no_census"] += 1; continue
        if not (c.get("Du2_over_B2_polynomial") or c.get("Dd2_over_B2_polynomial")
                or c.get("Du2Dd2_over_B2_polynomial")):
            skipped["not_absorbed"] += 1; continue
        # magnitudes keyed by symbol name
        us, ds = mask_slots(mu), mask_slots(md)
        mags = np.exp(np.array(r["log_mags"]))
        val = {}
        for (i, j), m in zip(us, mags[:len(us)]):
            val[f"u{i}{j}"] = m
        for (i, j), m in zip(ds, mags[len(us):]):
            val[f"d{i}{j}"] = m
        M_val = 1.0
        for sym, ex in parse_monomial(c["monomial_M"]):
            M_val *= val[sym] ** ex
        J = abs(r["J"]); rho = r["rho_v"]
        a1_over = math.sqrt(rho)               # |a1|/(Du Dd) = |J|/|sin phi|
        # |a1| = sqrt(rho) * Du * Dd; recover Du, Dd from rho and J? No:
        # use identity a1_over = |J|/|sin phi| as consistency only.
        # We need Du, Dd separately: rebuild numerically.
        # (cheap: eigh of Hu, Hd from log_mags + phi)
        phi = r["phi_raw"]
        Yu = np.zeros((3, 3), complex); Yd = np.zeros((3, 3), complex)
        for (i, j), m in zip(us, mags[:len(us)]):
            Yu[i, j] = m * (np.exp(1j * phi) if pe[0] == "u" and (i, j) == (pe[1], pe[2]) else 1)
        for (i, j), m in zip(ds, mags[len(us):]):
            Yd[i, j] = m * (np.exp(1j * phi) if pe[0] == "d" and (i, j) == (pe[1], pe[2]) else 1)
        def vand(Y):
            ev = np.linalg.eigvalsh(Y @ Y.conj().T)
            return abs((ev[0]-ev[1]) * (ev[0]-ev[2]) * (ev[1]-ev[2]))
        Du, Dd = vand(Yu), vand(Yd)
        a1 = a1_over * Du * Dd
        B_val = a1 / M_val
        if c.get("Du2_over_B2_polynomial"):
            Q = Du**2 / B_val**2; other = Dd; abs_sector = "u"
        elif c.get("Dd2_over_B2_polynomial"):
            Q = Dd**2 / B_val**2; other = Du; abs_sector = "d"
        else:
            Q = Du**2 * Dd**2 / B_val**2; other = 1.0; abs_sector = "combined"
        reduced = M_val / (math.sqrt(Q) * other)
        rows.append({
            "key": key, "orbit": r["orbit"], "cluster": cluster_of(r["phi_folded_deg"]),
            "phi_folded_deg": r["phi_folded_deg"], "chi2": r["chi2_stored"],
            "lnM": math.log(M_val), "lnQ_half": 0.5 * math.log(Q),
            "lnD_other": math.log(other), "abs_sector": abs_sector,
            "reduced_vs_direct_rel": abs(reduced - a1_over) / a1_over,
            "ln_a1_over": math.log(a1_over),
        })
    print(f"rows: {len(rows)}; skipped: {dict(skipped)}")
    maxrel = max(x["reduced_vs_direct_rel"] for x in rows)
    print(f"reduced-form max rel err: {maxrel:.3e}")

    def spread(vals):
        v = np.array(vals); return float(np.std(v))
    ens = {
        "lnM": spread([x["lnM"] for x in rows]),
        "neg_half_lnQ": spread([-x["lnQ_half"] for x in rows]),
        "neg_lnD_other": spread([-x["lnD_other"] for x in rows]),
        "ln_a1_over": spread([x["ln_a1_over"] for x in rows]),
    }
    print("ensemble std of log-factors:", {k: round(v, 3) for k, v in ens.items()})

    # within-cluster level-set test
    by_cluster = defaultdict(list)
    for x in rows:
        by_cluster[x["cluster"]].append(x)
    cluster_table = []
    for ci in sorted(by_cluster):
        xs = by_cluster[ci]
        if len(xs) < 5:
            continue
        entry = {
            "cluster": ci, "center_deg": round(centers[ci], 3), "n": len(xs),
            "phi_spread_deg": float(np.std([x["phi_folded_deg"] for x in xs])),
            "std_lnM": spread([x["lnM"] for x in xs]),
            "std_neg_half_lnQ": spread([-x["lnQ_half"] for x in xs]),
            "std_neg_lnD_other": spread([-x["lnD_other"] for x in xs]),
            "std_ln_a1_over": spread([x["ln_a1_over"] for x in xs]),
        }
        cluster_table.append(entry)
    for e in cluster_table:
        print(f"cluster {e['cluster']:2d} phi={e['center_deg']:7.3f} n={e['n']:4d} "
              f"sd(lnM)={e['std_lnM']:.3f} sd(-.5lnQ)={e['std_neg_half_lnQ']:.3f} "
              f"sd(-lnD)={e['std_neg_lnD_other']:.3f} sd(ln a1/DuDd)={e['std_ln_a1_over']:.4f}")

    # correlation of factors with phi across ensemble
    phi_arr = np.array([x["phi_folded_deg"] for x in rows])
    corrs = {}
    for name, vals in (("lnM", [x["lnM"] for x in rows]),
                       ("neg_half_lnQ", [-x["lnQ_half"] for x in rows]),
                       ("neg_lnD_other", [-x["lnD_other"] for x in rows])):
        corrs[name] = float(np.corrcoef(np.array(vals), phi_arr)[0, 1])
    print("corr(factor, phi_folded):", {k: round(v, 3) for k, v in corrs.items()})

    out = {
        "purpose": "WP21d factor-discreteness audit: which log-factor of the reduced "
                   "a1/(Du Dd) = M/(sqrt(Q) D_other) form carries the 15-cluster spectrum",
        "n_rows": len(rows), "skipped": dict(skipped),
        "reduced_form_max_rel_err": maxrel,
        "emergent_cluster_centers_deg": centers,
        "ensemble_std": ens, "corr_with_phi": corrs,
        "cluster_table": cluster_table,
    }
    with open("results/wp21d_factor_discreteness.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("-> results/wp21d_factor_discreteness.json")


if __name__ == "__main__":
    main()
