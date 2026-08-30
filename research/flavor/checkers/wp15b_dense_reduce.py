#!/usr/bin/env python3
"""WP15b (dense): merge the dense full-member scan with the WP7 ensemble
and rerun the paper-rule class reduction (App. V.a of arXiv:2607.27315v1).

Inputs:
  results/wp15b_dense_orbit*.json  (dense scan: all (3,3)-filtered members
                                    of all 18 census orbits, both S3^3
                                    halves, 24 starts/member)
  results/wp7_ensemble.json        (original WP7 sweep; unioned in)

Paper rule: two fits are identified iff an S3^3 row/column permutation
maps one's support onto the other's with all nine entry magnitudes within
5% and |phi| within 0.1 deg.  Comparison target: 156 classes (from the
paper's 2398 fits; raw fit counts are scan-density dependent).

Outputs: research/flavor/results/wp15b_dense_class_reduction.json
"""
import glob
import json
import math
from collections import defaultdict

from wp15b_class_reduction import (ENTRY_TOL, PHI_TOL, PERMS, entries_of,
                                   matches)
from orbit_census import permute


def canon_s3(member):
    mu, md = member
    best = None
    for pq in PERMS:
        for pu in PERMS:
            for pd in PERMS:
                a, b = permute(mu, md, pq, pu, pd)
                if best is None or (a, b) < best:
                    best = (a, b)
    return best


def main():
    fits = []
    per_orbit = {}

    for path in sorted(glob.glob("results/wp15b_dense_orbit*.json")):
        d = json.load(open(path))
        oi = d["orbit_index"]
        rec = per_orbit.setdefault(oi, {
            "orbit_index": oi, "mask_u": d["mask_u"], "mask_d": d["mask_d"],
            "cycle_length": d["cycle_length"],
            "members_scanned": d["members_scanned"],
            "viable_minima": 0, "best_chi2": d["best_chi2_overall"],
            "halves": {},
        })
        for half in d["s3_orbits"]:
            key = "swapped" if half["sector_swapped"] else "canonical"
            hv = sum(len(m["viable_minima"]) for m in half["member_results"])
            rec["halves"][key] = {
                "representative": half["representative"],
                "members_scanned": half["members_scanned"],
                "viable_minima": hv,
                "best_chi2": half["best_chi2"],
            }
            rec["viable_minima"] += hv
            for m in half["member_results"]:
                for v in m["viable_minima"]:
                    fits.append({
                        "orbit_index": oi,
                        "member": tuple(v["member"]),
                        "entries": entries_of(v["member"], v["log_mags"]),
                        "phi": v["phi"],
                        "phi_folded": v["phi_folded"],
                        "chi2": v["chi2"],
                        "source": "dense",
                    })

    n_dense = len(fits)

    d7 = json.load(open("results/wp7_ensemble.json"))
    for o in d7["orbits"]:
        for m in o.get("viable_minima", []):
            fits.append({
                "orbit_index": o["orbit_index"],
                "member": tuple(m["member"]),
                "entries": entries_of(m["member"], m["log_mags"]),
                "phi": m["phi"],
                "phi_folded": m["phi_folded"],
                "chi2": m["chi2"],
                "source": "wp7",
            })

    n_wp7 = len(fits) - n_dense
    print(f"dense fits: {n_dense}, wp7 fits: {n_wp7}, "
          f"total: {len(fits)}")

    # Paper policy (App. V.a): "For a given texture, our scan looks for
    # the best possible chi2 solution"; distinct viable fits of one
    # texture come from the different pi/8 phase windows.  Keep only the
    # best-chi2 minimum per (member, phase window) before reduction.
    best_pw = {}
    for f in fits:
        w = int(math.floor((f["phi"] + math.pi) / (math.pi / 8.0)))
        key = (f["member"], w)
        if key not in best_pw or f["chi2"] < best_pw[key]["chi2"]:
            best_pw[key] = f
    dropped = len(fits) - len(best_pw)
    fits = list(best_pw.values())
    print(f"after best-per-(member,window) filter: {len(fits)} "
          f"(dropped {dropped} extra local minima)")

    groups = defaultdict(list)
    for idx, f in enumerate(fits):
        groups[canon_s3(f["member"])].append(idx)

    parent = list(range(len(fits)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        parent[find(a)] = find(b)

    n_pairs = 0
    for idxs in groups.values():
        for x in range(len(idxs)):
            for y in range(x + 1, len(idxs)):
                a, b = fits[idxs[x]], fits[idxs[y]]
                n_pairs += 1
                if matches(a["entries"], b["entries"], a["phi"], b["phi"]):
                    union(idxs[x], idxs[y])
    print("same-orbit fit pairs tested:", n_pairs)

    classes = defaultdict(list)
    for i in range(len(fits)):
        classes[find(i)].append(i)
    print("classes:", len(classes))

    rows = []
    for members in classes.values():
        rep = min(members, key=lambda i: fits[i]["chi2"])
        f = fits[rep]
        rows.append({
            "size": len(members),
            "orbit_index": f["orbit_index"],
            "chi2_min": f["chi2"],
            "phi_abs": abs(f["phi"]),
            "phi_folded": f["phi_folded"],
        })
    rows.sort(key=lambda r: (r["orbit_index"], r["chi2_min"]))

    def bin22(x):
        return round(math.degrees(x) / 22.5) * 22.5

    hist_classes = defaultdict(int)
    for r in rows:
        hist_classes[bin22(r["phi_folded"])] += 1
    hist_fits = defaultdict(int)
    for f in fits:
        hist_fits[bin22(f["phi_folded"])] += 1

    out = {
        "purpose": "WP15b dense: paper-rule class reduction of the merged "
                   "dense + WP7 viable-fit ensemble",
        "paper_targets": {"viable_fits": 2398, "classes": 156},
        "dense_fits": n_dense,
        "wp7_fits": n_wp7,
        "ensemble_fits": len(fits),
        "ensemble_fits_after_window_policy_note": (
            "ensemble_fits is AFTER the best-per-(member,window) policy; "
            "pre-policy total is dense_fits + wp7_fits"),
        "same_orbit_pairs_tested": n_pairs,
        "classes": len(rows),
        "class_phase_histogram_folded_deg":
            {str(k): hist_classes[k] for k in sorted(hist_classes)},
        "fit_phase_histogram_folded_deg":
            {str(k): hist_fits[k] for k in sorted(hist_fits)},
        "per_orbit": [per_orbit[k] for k in sorted(per_orbit)],
        "class_table": rows,
    }
    with open("results/wp15b_dense_class_reduction.json", "w",
              encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("folded class histogram (deg):", dict(sorted(hist_classes.items())))
    print("folded fit histogram (deg):", dict(sorted(hist_fits.items())))
    for r in out["per_orbit"]:
        flag = "" if r["viable_minima"] else "  <-- NONVIABLE"
        print(f"orbit {r['orbit_index']:2d}: viable={r['viable_minima']:4d} "
              f"best_chi2={r['best_chi2']:.2f} halves={r['halves']}{flag}")


if __name__ == "__main__":
    main()
