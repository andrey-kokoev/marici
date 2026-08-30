"""WP27: is the K spectrum seeded by the natural hierarchy point?

WP26 decomposed the five phase-cluster levels as L_c = K_c/D_other
with K = M*W/gap chart data and D_other physical. K is PHASE-FREE
(M and W are built from squared magnitudes; gap involves |H_ij|^2),
so K can be evaluated at ANY magnitude assignment, in particular at
the hierarchy-natural point nat(i,j) = sqrt(y_i y_j) that seeds the
fits. This checker evaluates ln K at the natural point for all 755
unique viable textures and asks:

  A. does the natural-point ln K distribution already show five peaks
     near the fitted cluster ln K values (=> the levels are seeded by
     the natural parameterization, a chart-of-chart effect), or is
     natural ln K broad/unclustered (=> the FIT does the selection)?
  B. is the natural point singular for any texture (W(nat) = 0, which
     forces the fit off the natural point)?
  C. per cluster: mean fitted ln K vs mean natural ln K (per decomposed
     sector for the mixed clusters).

Reads: results/wp20_valley_audit.json,
       results/wp21e_universal_factorization.json
Writes: results/wp27_natural_k.json
Run: ../.venv/Scripts/python checkers/wp27_natural_k.py
"""
import json, math, collections, re, sys
import numpy as np
import sympy as sp

sys.path.insert(0, 'checkers')
import wp7_ensemble as wp7
from wp25_center_selection import factor_rows, mask_slots, blocks_of

def natural_val(mu, md):
    val = {}
    for (i, j) in mask_slots(mu):
        val[f"u{i}{j}"] = wp7.natural_value("u", (i, j))
    for (i, j) in mask_slots(md):
        val[f"d{i}{j}"] = wp7.natural_value("d", (i, j))
    return val

def gram(val, pref, slots):
    H = np.zeros((3, 3))
    for a in range(3):
        for b in range(3):
            H[a, b] = sum(val.get(f"{pref}{a}{j}", 0.0) * val.get(f"{pref}{b}{j}", 0.0)
                          for j in range(3))
    return H

def natural_K(key, f):
    mu, md, pe = key.split("_")
    mu, md = int(mu), int(md)
    val = natural_val(mu, md)
    M_val = 1.0
    for facstr in re.findall(r"[ud]\d\d(?:\*\*\d+)?", f["monomial_M"]):
        m = re.fullmatch(r"([ud]\d\d)(?:\*\*(\d+))?", facstr)
        M_val *= val[m.group(1)] ** int(m.group(2) or 1)
    sec = f["decomposed_sector"]
    pref = sec
    H = gram(val, pref, None)
    if f["factorization_type"] == "block21":
        bl = blocks_of(mu if sec == "u" else md)
        sing = [b[0] for b in bl if len(b) == 1][0]
        i, j = [b for b in bl if len(b) == 2][0]
        tr = H[i, i] + H[j, j]
        det = H[i, i] * H[j, j] - H[i, j] * H[j, i]
        gap = math.sqrt(abs(tr * tr - 4 * det))
    else:
        g = {(0, 1): H[0, 0] - H[1, 1], (0, 2): H[0, 0] - H[2, 2], (1, 2): H[1, 1] - H[2, 2]}
        S = {tuple(x) for x in f["gap_subset_dividing_B"]}
        remaining = [x for x in ((0, 1), (0, 2), (1, 2)) if x not in S]
        gap = 1.0
        for x in remaining:
            gap *= abs(g[x])
    # W at natural values
    Wexpr = sp.sympify(f["W"])
    if Wexpr.is_number:
        W_val = abs(float(Wexpr))
    else:
        subs = {sp.symbols(k): v * v for k, v in val.items()}  # W uses d_ij**2
        W_val = abs(float(Wexpr.subs(subs)))
    return M_val, W_val, gap, val

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

    # fitted lnK per row (lnK = lnL + lnDo)
    rows = factor_rows(recs, fac, centers)
    fitted = collections.defaultdict(list)   # (cluster, sector) -> [lnK]
    for x in rows:
        x["lnK"] = x["lnL"] + x["lnDo"]
        fitted[(x["cluster"], x["sector"])].append(x["lnK"])

    nat = {}
    singular = []
    for key, f in fac.items():
        M_val, W_val, gap, val = natural_K(key, f)
        if W_val == 0.0 or gap == 0.0 or M_val == 0.0:
            singular.append(dict(key=key, W=W_val, gap=gap, M=M_val))
            nat[key] = None
        else:
            nat[key] = math.log(M_val) + math.log(W_val) - math.log(gap)

    out = {"purpose": "WP27 natural-point K audit", "centers": centers,
           "n_textures": len(fac), "n_singular_natural": len(singular),
           "singular": singular[:50]}
    # A. global natural lnK histogram vs fitted cluster means
    lnKs = np.array([v for v in nat.values() if v is not None])
    out["natural_lnK"] = dict(n=len(lnKs), mean=float(lnKs.mean()),
                              std=float(lnKs.std()),
                              min=float(lnKs.min()), max=float(lnKs.max()))
    # fitted cluster means per (cluster, sector)
    fm = {f"{c}{s}": dict(n=len(v), mean=float(np.mean(v)), std=float(np.std(v)))
          for (c, s), v in sorted(fitted.items())}
    out["fitted_lnK_by_cluster_sector"] = fm
    # natural lnK per texture cluster-membership: which cluster(s) does
    # each texture's fitted minima belong to? use dominant cluster per key
    key_cluster = {}
    for x in rows:
        key_cluster.setdefault(x["key"], collections.Counter())[x["cluster"]] += 1
    nat_by_domcluster = collections.defaultdict(list)
    for key, v in nat.items():
        if v is None or key not in key_cluster:
            continue
        dom = key_cluster[key].most_common(1)[0][0]
        nat_by_domcluster[dom].append(v)
    out["natural_lnK_by_dominant_cluster"] = {
        str(c): dict(n=len(v), mean=float(np.mean(v)), std=float(np.std(v)),
                     min=float(np.min(v)), max=float(np.max(v)))
        for c, v in sorted(nat_by_domcluster.items())}

    json.dump(out, open("results/wp27_natural_k.json", "w"), indent=1)
    print("textures:", len(fac), " singular at natural point:", len(singular))
    print("natural lnK: mean %.3f std %.3f range [%.2f, %.2f]" % (
        out["natural_lnK"]["mean"], out["natural_lnK"]["std"],
        out["natural_lnK"]["min"], out["natural_lnK"]["max"]))
    print("fitted lnK by (cluster, sector):")
    for k, v in fm.items():
        print("   %s n=%d mean %.3f std %.2e" % (k, v["n"], v["mean"], v["std"]))
    print("natural lnK by dominant fitted cluster:")
    for c, v in out["natural_lnK_by_dominant_cluster"].items():
        print("   cluster %s n=%d mean %.3f std %.3f range [%.2f, %.2f]" % (
            c, v["n"], v["mean"], v["std"], v["min"], v["max"]))
    print("-> results/wp27_natural_k.json")

if __name__ == "__main__":
    main()
