#!/usr/bin/env python3
"""WP15c reduce: App.-V.b class counting for the fixed-phase ensemble.

Per pinned |phi| in {pi/8, 3pi/8, pi/2} (both signs pooled; the paper
identifies +-phi and pi+-phi, and no permutation can flip the sign):

  permutation classes: minima on one S3^3-orbit representative are
      identified iff a stabilizer permutation maps one's nine entry
      magnitudes onto the other's within 5% (phi is pinned, hence
      trivially equal).  Different representatives are different S3^3
      orbits and can never merge.
      Paper: 29 (pi/2), 35 (pi/8), 35 (3pi/8)  [= 99].

  rotation classes: cluster permutation classes whose best-fit chi2
      values agree to ~10 significant figures (paper's practical rule
      for the residual phase-preserving U(3)^3 rotations).
      Paper: 9 (pi/2), 10 (pi/8), 13 (3pi/8)  [= 32].

Outputs: research/flavor/results/wp15c_class_reduction.json
"""
import json
import math
from collections import defaultdict

from wp15b_class_reduction import matches, entries_of

PHI_LABELS = {22.5: "pi/8", 67.5: "3pi/8", 90.0: "pi/2"}
PAPER_PERM = {"pi/2": 29, "pi/8": 35, "3pi/8": 35}
PAPER_ROT = {"pi/2": 9, "pi/8": 10, "3pi/8": 13}


def sig_agree(a, b, sig=10):
    """Agreement to ~sig significant figures."""
    if a == b:
        return True
    scale = max(abs(a), abs(b), 1e-300)
    return abs(a - b) <= scale * 10.0 ** (-(sig - 1)) * 0.5 + 1e-12


def main():
    import glob
    from orbit_census import permute as _perm
    import itertools as _it
    _P = list(_it.permutations(range(3)))

    def canon_s3(member):
        mu, md = member
        best = None
        for pq in _P:
            for pu in _P:
                for pd in _P:
                    c = _perm(mu, md, pq, pu, pd)
                    if best is None or c < best:
                        best = c
        return best

    per_mag = defaultdict(list)   # phi_mag -> list of fit records
    for path in sorted(glob.glob("results/wp15c_fixed_phase*.json")):
        d = json.load(open(path))
        for r in d["results"]:
            rep = r["rep"]
            member = (rep["mask_u"], rep["mask_d"])
            for f in r["fits"]:
                for m in f["minima"]:
                    per_mag[f["phi_mag"]].append({
                        "orbit_index": rep["orbit_index"],
                        "swap": rep["swap"],
                        "variant": rep.get("variant", 0),
                        "member": member,
                        "canon": canon_s3(member),
                        "entries": entries_of(member, m["log_mags"]),
                        # folded (pinned) phase: the paper does not distinguish
                        # +-phi or pi+-phi, so class matching uses the label
                        "phi": f["phi_mag"],
                        "phi_pin": m["phi"],
                        "chi2": m["chi2"],
                        "log_mags": m["log_mags"],
                    })

    out = {"paper_targets": {"permutation_classes": PAPER_PERM,
                             "rotation_classes": PAPER_ROT},
           "groups": {}}
    for pmag, fits in sorted(per_mag.items()):
        label = PHI_LABELS[round(math.degrees(pmag), 1)]
        # permutation classes (within each rep/orbit only)
        parent = list(range(len(fits)))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        def union(a, b):
            parent[find(a)] = find(b)

        for x in range(len(fits)):
            for y in range(x + 1, len(fits)):
                a, b = fits[x], fits[y]
                if a["canon"] != b["canon"]:
                    continue  # different S3^3 orbits can never merge
                if matches(a["entries"], b["entries"], a["phi"], b["phi"]):
                    union(x, y)
        pclasses = defaultdict(list)
        for i in range(len(fits)):
            pclasses[find(i)].append(i)
        prows = []
        for members in pclasses.values():
            rep_i = min(members, key=lambda i: fits[i]["chi2"])
            f = fits[rep_i]
            prows.append({"size": len(members),
                          "orbit_index": f["orbit_index"],
                          "swap": f["swap"],
                          "chi2_min": f["chi2"],
                          "phi": f["phi"]})
        prows.sort(key=lambda r: r["chi2_min"])

        # rotation classes: cluster by 10-sig-fig chi2 agreement
        rparent = list(range(len(prows)))

        def rfind(a):
            while rparent[a] != a:
                rparent[a] = rparent[rparent[a]]
                a = rparent[a]
            return a

        for x in range(len(prows)):
            for y in range(x + 1, len(prows)):
                if sig_agree(prows[x]["chi2_min"], prows[y]["chi2_min"]):
                    rparent[rfind(x)] = rfind(y)
        rclasses = defaultdict(list)
        for i in range(len(prows)):
            rclasses[rfind(i)].append(i)

        out["groups"][label] = {
            "viable_fits": len(fits),
            "permutation_classes": len(prows),
            "rotation_classes": len(rclasses),
            "paper_permutation": PAPER_PERM[label],
            "paper_rotation": PAPER_ROT[label],
            "permutation_class_table": prows,
            "rotation_cluster_sizes": sorted((len(v) for v in rclasses.values()),
                                             reverse=True),
        }
        print(f"|phi|={label}: fits={len(fits)} "
              f"perm_classes={len(prows)} (paper {PAPER_PERM[label]}) "
              f"rot_classes={len(rclasses)} (paper {PAPER_ROT[label]})")

    dest = "results/wp15c_class_reduction.json"
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("->", dest)


if __name__ == "__main__":
    main()
