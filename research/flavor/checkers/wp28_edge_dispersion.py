"""WP28: edge dispersion - is the fitted magnitude vector universal per edge?

WP26 found lnM frozen in the rigid phase clusters (std 1e-3..1e-2) while the
conspiracy clusters hold lnL fixed by compensation. If each EDGE's fitted
magnitude were a universal function of the physical point within a cluster,
M-freeze would be trivially explained. This checker tests that edge-wise
universality hypothesis and contrasts it with the collective lnM freeze:

  A. pooled dispersion: per (cluster, sector, slot), std of fitted log-mag
     across all minima of all texture classes in the cluster;
  B. within-class dispersion: per (texture class, sector, slot), std across
     that class's own minima (do a class's minima move edges at all?);
  C. collective contrast: per cluster, within-class and between-class std of
     lnM (the monomial the WP26 reduced form freezes), vs the edge stds;
  D. frozen-edge census: groups with std < 0.01 and n >= 40, identified
     against logs of the central quark Yukawa couplings.

Reads: results/wp20_valley_audit.json,
       results/wp21e_universal_factorization.json
Writes: results/wp28_edge_dispersion.json
Run: ../.venv/Scripts/python checkers/wp28_edge_dispersion.py
"""
import json, math, collections, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wp25_center_selection import mask_slots, tex_key, factor_rows

CENTERS = [23.15067360649863, 43.17287913134288, 46.907137936455435,
           68.38801847180338, 89.57230686320408]
LN_CENTRAL_Y = {"ln y_u": math.log(7.04e-6), "ln y_c": math.log(3.56e-3),
                "ln y_t": math.log(0.967), "ln y_d": math.log(1.54e-5),
                "ln y_s": math.log(3.06e-4), "ln y_b": math.log(1.63e-2)}

def cluster_of(phi_deg):
    return min(range(len(CENTERS)), key=lambda i: abs(phi_deg - CENTERS[i]))

def main():
    wp20 = json.load(open("results/wp20_valley_audit.json"))
    fac = json.load(open("results/wp21e_universal_factorization.json"))["census"]
    recs = [r for r in wp20["records"]
            if fac.get(tex_key(*r["member"], r["phase_edge"]), {}).get("factorization_type")]

    pooled = collections.defaultdict(list)      # (cluster, sector, slot) -> logs
    per_class = collections.defaultdict(list)   # (key, sector, slot) -> logs
    class_cluster = {}
    for r in recs:
        mu, md = r["member"]; pe = r["phase_edge"]
        key = tex_key(mu, md, pe)
        cl = cluster_of(r["phi_folded_deg"])
        class_cluster[key] = cl
        us, ds = mask_slots(mu), mask_slots(md)
        logs = r["log_mags"]
        for (i, j), v in zip(us, logs[:len(us)]):
            pooled[(cl, "u", i, j)].append(v)
            per_class[(key, "u", i, j)].append(v)
        for (i, j), v in zip(ds, logs[len(us):]):
            pooled[(cl, "d", i, j)].append(v)
            per_class[(key, "d", i, j)].append(v)

    # A. pooled dispersion
    A = []
    for (cl, sec, i, j), vals in sorted(pooled.items()):
        a = np.array(vals)
        A.append(dict(cluster=cl, sector=sec, slot=[i, j], n=len(a),
                      mean=float(a.mean()), std=float(a.std())))
    big = [g for g in A if g["n"] >= 20]
    A_nonuniversal = sum(1 for g in big if g["std"] > 0.3)

    # D. frozen-edge census
    frozen = []
    for g in A:
        if g["n"] >= 40 and g["std"] < 0.01:
            nearest = min(LN_CENTRAL_Y.items(), key=lambda kv: abs(kv[1] - g["mean"]))
            frozen.append(dict(g, nearest_central=nearest[0],
                               ln_central=nearest[1],
                               offset=g["mean"] - nearest[1]))

    # B. within-class dispersion (classes with >= 3 minima on that edge)
    B = []
    for (key, sec, i, j), vals in sorted(per_class.items()):
        if len(vals) >= 3:
            B.append(dict(key=key, cluster=class_cluster[key], sector=sec,
                          slot=[i, j], n=len(vals), std=float(np.std(vals))))
    B_stds = sorted(b["std"] for b in B)

    # C. lnM contrast
    rows = factor_rows(wp20["records"], fac, CENTERS)
    by_key = collections.defaultdict(list)
    for row in rows:
        by_key[row["key"]].append(row)
    C = {}
    for cl in range(len(CENTERS)):
        keys = [k for k, rs in by_key.items() if rs[0]["cluster"] == cl]
        means, within = [], []
        for k in keys:
            v = [r["lnM"] for r in by_key[k]]
            means.append(float(np.mean(v)))
            if len(v) >= 3:
                within.append(float(np.std(v)))
        edge_stds = [g["std"] for g in big if g["cluster"] == cl]
        C[str(cl)] = dict(
            n_classes=len(keys),
            lnM_between_class_std=float(np.std(means)) if len(means) > 1 else 0.0,
            lnM_within_class_std_median=float(np.median(within)) if within else None,
            edge_std_median=float(np.median(edge_stds)) if edge_stds else None,
            edge_std_max=float(max(edge_stds)) if edge_stds else None)

    gates = {
        "G1_edge_nonuniversality_dominant": dict(
            value=f"{A_nonuniversal}/{len(big)}",
            passed=len(big) > 0 and A_nonuniversal >= 0.8 * len(big)),
        "G2_frozen_edges_exactly_two": dict(
            value=[(f["cluster"], f["sector"], f["slot"]) for f in frozen],
            passed=len(frozen) == 2
                   and any(f["cluster"] == 1 and f["sector"] == "u" and f["slot"] == [2, 2]
                           and abs(f["offset"]) < 1e-3 for f in frozen)
                   and any(f["cluster"] == 3 and f["sector"] == "u" and f["slot"] == [0, 2]
                           and abs(f["offset"]) < 0.03 for f in frozen)),
        "G3_collective_freeze_contrast": dict(
            value=dict(cluster2=C.get("2"), cluster1_between=C.get("1", {}).get("lnM_between_class_std")),
            passed=C.get("2", {}).get("lnM_between_class_std", 1) < 0.01
                   and C.get("1", {}).get("lnM_between_class_std", 1) < 0.1
                   and C.get("2", {}).get("edge_std_median", 0) > 0.5),
        "G4_within_class_uniqueness": dict(
            value=dict(n_groups=len(B),
                       median_std=B_stds[len(B_stds)//2] if B_stds else None),
            passed=len(B) >= 500 and B_stds[len(B_stds)//2] < 0.01),
    }
    out = dict(
        purpose=__doc__.strip().splitlines()[0],
        n_minima=len(recs), n_classes=len(class_cluster),
        pooled_groups=A, frozen_edges=frozen,
        within_class_groups=B,
        within_class_std_median=B_stds[len(B_stds)//2] if B_stds else None,
        within_class_std_max=B_stds[-1] if B_stds else None,
        lnM_contrast=C, gates=gates,
        gates_passed=sum(1 for g in gates.values() if g["passed"]),
        interpretation=(
            "Two-level structure. WITHIN a texture class the fitted magnitude "
            "vector is essentially unique (median within-class edge std 2e-4): "
            "each class has one sharp magnitude point. ACROSS classes of the "
            "same cluster the edge logs disperse 1.0..3.3, so no edge-wise "
            "cluster universality - except two mass-pinned anchor edges, "
            "cluster-1 u(2,2) frozen to ln y_t CENTRAL to 7e-18 (not the "
            "pointwise fitted top coupling, the scan center) and cluster-3 "
            "u(0,2) near ln y_c (offset 0.016). Yet lnM is frozen BETWEEN "
            "classes in rigid clusters (cluster 2: 1.3e-3; cluster 1: 0.079) "
            "and not in conspiracy clusters (3.8..9.5). So the rigid-cluster "
            "monomial is a cluster-level collective invariant realized by "
            "wildly different individual edge assignments - invisible at the "
            "single-edge level, sharp at the monomial level."))
    json.dump(out, open("results/wp28_edge_dispersion.json", "w"), indent=1)
    print(json.dumps(dict(gates={k: (v["passed"], v["value"]) for k, v in gates.items()},
                          frozen=frozen, lnM_contrast=C), indent=1))

if __name__ == "__main__":
    main()
