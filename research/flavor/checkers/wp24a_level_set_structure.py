#!/usr/bin/env python3
"""WP24a: realizable-level-set structure of the viable ensemble.

Joins the WP20 per-minimum records (1210 viable minima) with the WP22
class labels and analyzes the level sets of the folded phase /
reduced form r = a1/(Du Dd):

  * WP22 class x cluster cross-tab;
  * per-texture cluster spans (singleton vs paired);
  * the two pairing patterns (0,4) and (1,3);
  * per-pair chi2/J equality and the log-magnitude transformation
    signature (swap + constant-shift structure).

Reads: results/wp20_valley_audit.json, results/wp22_w_identification.json
Writes: results/wp24a_level_set_structure.json
"""
import json, math, statistics, collections
from collections import defaultdict

CENTERS = [23.15067360649863, 43.17287913134288, 46.907137936455435,
           68.38801847180338, 89.57230686320408]


def cluster_of(phi):
    return min(range(5), key=lambda i: abs(phi - CENTERS[i]))


def main():
    wp20 = json.load(open("results/wp20_valley_audit.json"))
    wp22 = json.load(open("results/wp22_w_identification.json"))["census"]
    recs = wp20["records"]

    per_tex = defaultdict(list)
    for r in recs:
        mu, md = r["member"]
        pe = r["phase_edge"]
        per_tex[f"{mu}_{md}_{pe[0]}{pe[1]}{pe[2]}"].append(r)

    class_xt = collections.Counter()
    valley_xt = collections.Counter()
    for r in recs:
        mu, md = r["member"]
        pe = r["phase_edge"]
        key = f"{mu}_{md}_{pe[0]}{pe[1]}{pe[2]}"
        cl = cluster_of(r["phi_folded_deg"])
        class_xt[(wp22[key]["class"], cl)] += 1
        valley_xt[(r["valley_kind"], cl)] += 1

    span_counts = collections.Counter()
    pairs = []
    for name, rs in per_tex.items():
        cls = defaultdict(list)
        for r in rs:
            cls[cluster_of(r["phi_folded_deg"])].append(r)
        span = tuple(sorted(cls))
        span_counts[span if len(span) > 1 else "singleton"] += 1
        if len(span) == 2 and all(len(v) == 1 for v in cls.values()):
            a, b = cls[span[0]][0], cls[span[1]][0]
            dchi2 = abs(a["chi2_stored"] - b["chi2_stored"])
            dJ = abs(a["J"] - b["J"]) / abs(a["J"])
            la, lb = a["log_mags"], b["log_mags"]
            delta = [round(y - x, 9) for x, y in zip(la, lb)]
            # swap detection: pair (i,j) with la[i]==lb[j], la[j]==lb[i]
            swaps = [(i, j) for i in range(9) for j in range(i + 1, 9)
                     if abs(la[i] - lb[j]) < 1e-6 and abs(la[j] - lb[i]) < 1e-6
                     and abs(la[i] - lb[i]) > 1e-6]
            const_groups = collections.Counter(
                round(d, 6) for d in delta if abs(d) > 1e-6)
            pairs.append({
                "texture": name, "pattern": list(span),
                "phi_pair": [a["phi_folded_deg"], b["phi_folded_deg"]],
                "dchi2": dchi2, "dJ_rel": dJ,
                "swaps": swaps,
                "delta": delta,
                "dominant_shift": const_groups.most_common(2),
                "sin2_sum": (math.sin(math.radians(a["phi_folded_deg"])) ** 2
                             + math.sin(math.radians(b["phi_folded_deg"])) ** 2),
            })

    sin2 = defaultdict(list)
    for p in pairs:
        sin2[tuple(p["pattern"])].append(p["sin2_sum"])
    sin2_stats = {str(k): {"n": len(v), "mean": statistics.mean(v),
                           "std": statistics.pstdev(v)}
                  for k, v in sin2.items()}

    out = {
        "purpose": "WP24a realizable-level-set structure of the viable ensemble",
        "n_minima": len(recs), "n_textures": len(per_tex),
        "cluster_centers_deg": CENTERS,
        "class_cluster_crosstab": {f"{c}|{k}": n for (c, k), n in sorted(class_xt.items())},
        "valley_cluster_crosstab": {f"{v}|{k}": n for (v, k), n in sorted(valley_xt.items())},
        "span_counts": {str(k): v for k, v in span_counts.items()},
        "sin2_pair_stats": sin2_stats,
        "max_pair_dchi2": max(p["dchi2"] for p in pairs),
        "max_pair_dJ_rel": max(p["dJ_rel"] for p in pairs),
        "pairs": pairs,
    }
    with open("results/wp24a_level_set_structure.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("span counts:", dict(span_counts))
    print("max dchi2:", out["max_pair_dchi2"], "max dJ rel:", out["max_pair_dJ_rel"])
    print("sin2 stats:", json.dumps(sin2_stats, indent=1))
    print("-> results/wp24a_level_set_structure.json")


if __name__ == "__main__":
    main()
