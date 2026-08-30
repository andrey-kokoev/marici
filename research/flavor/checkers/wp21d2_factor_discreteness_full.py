#!/usr/bin/env python3
"""WP21d v2 (full ensemble): which factor of the universal reduced form
    a1/(Du Dd) = M * W / (gap * D_other)
carries the discrete phase-cluster spectrum?  WP21d v1 covered only the
471 absorbed (W=+-1) textures; WP21e supplies the universal
factorization, so this audit covers ALL 1210 WP20 viable minima.

Per record the log-identity
    ln|a1/(DuDd)| = ln M + ln|W| - ln gap - ln D_other
is evaluated numerically (gap = sqrt(disc_b) for 2+1-block sectors, or
the product of the remaining eigenvalue gaps for diagonal sectors), the
identity is verified, and the four log-factors are analyzed:
  * ensemble spread;
  * within-cluster spread (level-set test);
  * correlation with phi_folded.

Reads: results/wp20_valley_audit.json,
       results/wp21e_universal_factorization.json
Writes: results/wp21d2_factor_discreteness_full.json
"""
import json, math, collections
import numpy as np

SLOTS = [(i, j) for i in range(3) for j in range(3)]

def mask_slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]

def tex_key(mu, md, pe):
    return f"{mu}_{md}_{pe[0]}{pe[1]}{pe[2]}"

def blocks_of(mask):
    cols = collections.defaultdict(set)
    for i, j in mask_slots(mask):
        cols[j].add(i)
    parent = list(range(3))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for rows in cols.values():
        rows = list(rows)
        for r in rows[1:]:
            parent[find(rows[0])] = find(r)
    comp = {}
    for i in range(3):
        comp.setdefault(find(i), []).append(i)
    return sorted(comp.values(), key=len)

def main():
    wp20 = json.load(open("results/wp20_valley_audit.json"))
    fac = json.load(open("results/wp21e_universal_factorization.json"))["census"]
    recs = wp20["records"]

    # emergent 1-D clusters on phi_folded (gap > 1.5 deg)
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
    print(f"clusters: {len(centers)} at {[round(c,2) for c in centers]}")

    rows, skipped = [], collections.Counter()
    for r in recs:
        mu, md = r["member"]; pe = r["phase_edge"]
        key = tex_key(mu, md, pe)
        f = fac.get(key)
        if not f or "factorization_type" not in f:
            skipped["no_factorization"] += 1; continue
        us, ds = mask_slots(mu), mask_slots(md)
        mags = np.exp(np.array(r["log_mags"]))
        phi = r["phi_raw"]
        Yu = np.zeros((3, 3), complex); Yd = np.zeros((3, 3), complex)
        val = {}
        for (i, j), m in zip(us, mags[:len(us)]):
            Yu[i, j] = m * (np.exp(1j*phi) if pe[0] == "u" and (i, j) == (pe[1], pe[2]) else 1)
            val[f"u{i}{j}"] = m
        for (i, j), m in zip(ds, mags[len(us):]):
            Yd[i, j] = m * (np.exp(1j*phi) if pe[0] == "d" and (i, j) == (pe[1], pe[2]) else 1)
            val[f"d{i}{j}"] = m
        Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T
        def vand(H):
            ev = np.linalg.eigvalsh(H)
            return abs((ev[0]-ev[1])*(ev[0]-ev[2])*(ev[1]-ev[2]))
        Du, Dd = vand(Hu), vand(Hd)
        # M from symbolic string
        M_val = 1.0
        import re as _re
        for facstr in _re.findall(r"[ud]\d\d(?:\*\*\d+)?", f["monomial_M"]):
            m = _re.fullmatch(r"([ud]\d\d)(?:\*\*(\d+))?", facstr)
            M_val *= val[m.group(1)] ** int(m.group(2) or 1)
        sec = f["decomposed_sector"]
        H, Do = (Hu, Dd) if sec == "u" else (Hd, Du)
        if f["factorization_type"] == "block21":
            bl = blocks_of(mu if sec == "u" else md)
            sing = [b[0] for b in bl if len(b) == 1][0]
            i, j = [b for b in bl if len(b) == 2][0]
            tr = (H[i, i] + H[j, j]).real
            det = (H[i, i]*H[j, j] - H[i, j]*H[j, i]).real
            s0 = H[sing, sing].real
            chi_s = s0*s0 - tr*s0 + det
            disc_b = tr*tr - 4*det
            gap = math.sqrt(abs(disc_b))
            a1 = math.sqrt(r["rho_v"]) * Du * Dd
            W_val = a1 / (M_val * abs(chi_s))
        else:  # diagonal
            g = {(0,1): (H[0,0]-H[1,1]).real, (0,2): (H[0,0]-H[2,2]).real, (1,2): (H[1,1]-H[2,2]).real}
            S = {tuple(x) for x in f["gap_subset_dividing_B"]}
            remaining = [x for x in ((0,1),(0,2),(1,2)) if x not in S]
            gap = 1.0
            for x in remaining:
                gap *= abs(g[x])
            a1 = math.sqrt(r["rho_v"]) * Du * Dd
            chi_s = 1.0
            for x in S:
                chi_s *= abs(g[x])
            W_val = a1 / (M_val * chi_s)
        reduced = M_val * W_val / (gap * Do)
        direct = a1 / (Du * Dd)
        rows.append({
            "key": key, "orbit": r["orbit"], "cluster": cluster_of(r["phi_folded_deg"]),
            "phi_folded_deg": r["phi_folded_deg"], "chi2": r["chi2_stored"],
            "type": f["factorization_type"], "W_terms": f.get("W_terms"),
            "lnM": math.log(M_val), "lnW": math.log(abs(W_val)),
            "lngap": math.log(gap), "lnDo": math.log(Do),
            "reduced_rel_err": abs(reduced - direct) / direct,
        })
    print(f"rows: {len(rows)}; skipped: {dict(skipped)}")
    maxrel = max(x["reduced_rel_err"] for x in rows)
    print(f"reduced-form max rel err: {maxrel:.3e}")

    def sd(v):
        return float(np.std(np.array(v)))
    names = ["lnM", "lnW", "lngap", "lnDo"]
    ens = {n: sd([x[n] for x in rows]) for n in names}
    ens["ln_a1_over"] = sd([x["lnM"]+x["lnW"]-x["lngap"]-x["lnDo"] for x in rows])
    print("ensemble std:", {k: round(v, 3) for k, v in ens.items()})

    by_cluster = collections.defaultdict(list)
    for x in rows:
        by_cluster[x["cluster"]].append(x)
    table = []
    for ci in sorted(by_cluster):
        xs = by_cluster[ci]
        if len(xs) < 5: continue
        e = {"cluster": ci, "center_deg": round(centers[ci], 3), "n": len(xs),
             "n_textures": len({x["key"] for x in xs})}
        for n in names:
            e[f"std_{n}"] = sd([x[n] for x in xs])
        e["std_ln_a1_over"] = sd([x["lnM"]+x["lnW"]-x["lngap"]-x["lnDo"] for x in xs])
        table.append(e)
        print(f"cluster {ci} phi={e['center_deg']:7.3f} n={e['n']:4d} tex={e['n_textures']:4d} "
              + " ".join(f"sd({n})={e[f'std_{n}']:.3f}" for n in names)
              + f" sd(sum)={e['std_ln_a1_over']:.4f}")
    phi_arr = np.array([x["phi_folded_deg"] for x in rows])
    corrs = {n: float(np.corrcoef(np.array([x[n] for x in rows]), phi_arr)[0, 1]) for n in names}
    print("corr(factor, phi):", {k: round(v, 3) for k, v in corrs.items()})

    out = {
        "purpose": "WP21d v2 full-ensemble factor-discreteness audit of "
                   "a1/(Du Dd) = M*W/(gap*D_other)",
        "n_rows": len(rows), "skipped": dict(skipped),
        "reduced_form_max_rel_err": maxrel,
        "emergent_cluster_centers_deg": centers,
        "ensemble_std": ens, "corr_with_phi": corrs, "cluster_table": table,
    }
    with open("results/wp21d2_factor_discreteness_full.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("-> results/wp21d2_factor_discreteness_full.json")

if __name__ == "__main__":
    main()
