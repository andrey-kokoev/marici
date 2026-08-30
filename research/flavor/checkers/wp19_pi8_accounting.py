#!/usr/bin/env python3
"""WP19: complete accounting of the pi/8 phase clustering.

Three ingredients, all exact or reproduced:

1. Branch cut.  The WP18 two delta-branches are NOT both viable
   against the paper's 17-observable fit: OBS17 includes |Vcd|, |Vtd|,
   |Vts| and the angles, which separate the branches.  Compute chi2 for
   each branch once (both branches are single quotient points, so one
   evaluation each suffices).

2. Atlas support.  Fold every WP18 exact-fit phase by the paper's
   convention (fold_phi -> [0, pi/2]) and bin into the paper's four
   phase windows (multiples of pi/8: 22.5/45/67.5/90 deg).  Compare the
   resulting support against the WP15b 134-class histogram
   {22.5: 32, 45: 30, 67.5: 49, 90: 23}.

3. Class-level match.  Per orbit, match the WP15b dominant classes
   (chi2_min < 4) against the WP18 atlas pinned phases.

4. Per-orbit pinned-phase completion.  For orbits holding an unmatched
   dominant class, enumerate the exact-fit fiber's folded pinned phases
   by dense multi-start and test each class phase against the completed
   set (1 deg tolerance).  Every converged physical10 root is gated by
   its physical16 image against the two quotient sheets over p* (the
   measured ten-coordinate projection certifies finite ambiguity, never
   uniqueness); only viable-sheet roots enter the pinned sets.

The statement established: the ensemble histogram's SUPPORT is the
folded pinned-phase set of the exact-fit atlas on the viable branch;
the clustering near pi/8 multiples decomposes as (CKM angles within
~1 deg of pi/8 multiples) + (per-chart inheritance pinning, WP14b) +
(window binning), with class multiplicities being scan-basin weights.

Outputs: research/flavor/results/wp19_pi8_accounting.json
"""
import json
import math
import sys
from collections import defaultdict

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, "checkers")
import wp7_ensemble as wp7
from wp16a_fiber_degree import physical10
from wp18a_branch_derivation import ROOT_A, ROOT_B
from wp18_branch_resolved_fibers import physical16

np.seterr(all="ignore")

WINDOWS = [22.5, 45.0, 67.5, 90.0]


def chi2_of(root):
    mu, md = 85, 234
    ps, slot = wp7.paper_phase_edge(mu, md)
    Yu, Yd = wp7.build_texture(mu, md, ps, slot, np.array(root))
    obs = wp7.observables17(Yu, Yd)
    pulls = (obs - wp7.CENTRAL) / wp7.SIGMA
    return float(np.sum(pulls**2)), pulls


def main():
    # 1. branch chi2
    chi2_A, pulls_A = chi2_of(ROOT_A)   # cos delta > 0 (viable) branch
    chi2_B, pulls_B = chi2_of(ROOT_B)   # cos delta < 0 branch
    names = [n for n, _, _ in wp7.OBS17]
    top_B = sorted(zip(names, pulls_B), key=lambda t: -abs(t[1]))[:4]
    print(f"small-delta branch chi2 = {chi2_A:.4f} (cut 20.28)")
    print(f"large-delta branch chi2 = {chi2_B:.2f}  "
          f"top pulls: " + ", ".join(f"{n} {p:+.1f}sigma" for n, p in top_B))

    viable_branch = ("small_cos_pos" if chi2_A < wp7.CHI2_3SIGMA_7DOF
                     else "large_cos_neg")

    # 2. atlas support from WP18 roots
    w18 = json.load(open("results/wp18_branch_resolved_fibers.json"))
    folded_viable = defaultdict(list)   # orbit key -> folded degrees
    all_folded = []
    for r in w18["per_representative"]:
        key = (r["orbit_index"], r["swap"])
        for branch, roots in r["roots"].items():
            for rt in roots:
                f = math.degrees(wp7.fold_phi(rt["phi_mod_2pi"]))
                all_folded.append((key, branch, f))
                if branch == viable_branch:
                    folded_viable[key].append(f)

    def bin_of(f):
        return min(WINDOWS, key=lambda w: abs(f - w))

    atlas_bins = defaultdict(int)
    max_dev = 0.0
    for key, fs in folded_viable.items():
        for f in fs:
            atlas_bins[bin_of(f)] += 1
            max_dev = max(max_dev, abs(f - bin_of(f)))
    print("atlas viable-branch folded-phase bins:",
          dict(sorted(atlas_bins.items())),
          f"max deviation {max_dev:.2f} deg")

    # 3. class-level match
    w15 = json.load(open("results/wp15b_dense_class_reduction.json"))
    hist = {float(k): v for k, v in
            w15["class_phase_histogram_folded_deg"].items()}
    dominant = [c for c in w15["class_table"] if c["chi2_min"] < 4.0]
    unmatched = []
    for c in dominant:
        cf = math.degrees(c["phi_folded"])
        oi = c["orbit_index"]
        cands = [f for (oi2, sw), fs in folded_viable.items()
                 if oi2 == oi for f in fs]
        if not cands or min(abs(cf - f) for f in cands) > 1.0:
            unmatched.append((oi, round(cf, 2), round(c["chi2_min"], 2)))
    # 4. per-orbit pinned-phase completion: for every orbit holding an
    # unmatched dominant class, enumerate the exact-fit fiber's folded
    # pinned phases by dense multi-start (class-phase anchors + uniform
    # random phases), cluster, then test each class phase against the
    # completed set.  Question answered: is every dominant chi2-class
    # phase a small perturbation of an exact pinned phase of its orbit?
    pilot = json.load(open("results/wp16a_fiber_degree_pilot.json"))
    p_star = np.array(pilot["p_star"])
    scale = np.abs(p_star)  # WP16 convention: relative per coordinate
    # physical16 branch gate (AGENTS.md fiber-claim policy): a converged
    # physical10 root lies on one of the two quotient sheets over p*;
    # only roots on the viable sheet may enter the pinned set.  The
    # sheet reference images are invariant constants, computed once
    # from the two orbit-15 branch roots.
    mu0, md0 = 85, 234
    ps0, slot0 = wp7.paper_phase_edge(mu0, md0)
    img_ref = {}
    for name, root in (("small_cos_pos", ROOT_A), ("large_cos_neg", ROOT_B)):
        Yu0, Yd0 = wp7.build_texture(mu0, md0, ps0, slot0, np.array(root))
        img_ref[name] = physical16(Yu0, Yd0)

    def branch_of(Yu, Yd):
        img = physical16(Yu, Yd)
        rel = {}
        for name, ref in img_ref.items():
            denom = np.maximum(np.abs(ref), 1e-12)
            rel[name] = float(np.max(np.abs(img - ref) / denom))
        return min(rel, key=rel.get), rel

    rep_of = {}
    for r in w18["per_representative"]:
        rep_of.setdefault(r["orbit_index"], r["member"])

    orbit_class_phases = defaultdict(set)
    for oi, cf, _c2 in unmatched:
        orbit_class_phases[oi].add(cf)

    def cluster(phases, tol=0.3):
        out_c = []
        for f in sorted(phases):
            if out_c and f - out_c[-1][-1] <= tol:
                out_c[-1].append(f)
            else:
                out_c.append([f])
        return [sum(c) / len(c) for c in out_c]

    orbit_pinned = {}
    matched = []
    genuinely_off = []
    for oi, cfs in sorted(orbit_class_phases.items()):
        mu, md = rep_of[oi]
        ps, slot = wp7.paper_phase_edge(mu, md)
        us, ds = wp7.mask_slots(mu), wp7.mask_slots(md)

        def resid(theta):
            Yu, Yd = wp7.build_texture(mu, md, ps, slot, theta)
            return (physical10(Yu, Yd) - p_star) / scale

        rng2 = np.random.default_rng(1000 + oi)
        found_phases = []
        branch_counts = defaultdict(int)
        anchors = ([math.radians(cf) for cf in sorted(cfs)] +
                   list(rng2.uniform(0.0, 2.0 * math.pi, 100)))
        for a in anchors:
            for _ in range(40):
                s = np.concatenate([
                    wp7.start_point(us, ds, rng2),
                    [a + rng2.uniform(-0.02, 0.02)]])
                try:
                    sol = least_squares(
                        resid, s, method="lm", ftol=1e-15, xtol=1e-15,
                        gtol=1e-15, max_nfev=2000)
                except Exception:
                    continue
                if float(np.max(np.abs(resid(sol.x)))) < 1e-7:
                    Yu_c, Yd_c = wp7.build_texture(
                        mu, md, ps, slot, sol.x)
                    br, _rel = branch_of(Yu_c, Yd_c)
                    branch_counts[br] += 1
                    if br == viable_branch:
                        found_phases.append(math.degrees(
                            wp7.fold_phi(float(sol.x[9]) % (2 * math.pi))))
                    break
        pinned = cluster(found_phases)
        # merge with the already-sampled viable-branch phases
        prior = [f for (oi2, sw), fs in folded_viable.items()
                 if oi2 == oi for f in fs]
        pinned = cluster(pinned + prior)
        orbit_pinned[oi] = {"pinned_deg": [round(f, 3) for f in pinned],
                            "branch_root_counts": dict(branch_counts)}
        for cf in sorted(cfs):
            d = min(abs(cf - f) for f in pinned)
            rec = {"orbit": oi, "class_phase_deg": cf,
                   "nearest_pinned_deg": round(
                       min(pinned, key=lambda f: abs(cf - f)), 3),
                   "distance_deg": round(d, 3)}
            (matched if d <= 1.0 else genuinely_off).append(rec)
    print(f"per-orbit completion: {len(matched)} class phases within "
          f"1 deg of a pinned phase, {len(genuinely_off)} off")
    for oi, fs in orbit_pinned.items():
        print(f"  orbit {oi}: pinned {fs['pinned_deg']} "
              f"branch-roots {fs['branch_root_counts']}")
    for rec in genuinely_off:
        print("  off-atlas:", rec)

    out = {
        "purpose": "WP19 accounting of the pi/8 clustering: branch cut "
                   "+ atlas support + class-level match",
        "branch_chi2": {"small_delta_cos_pos": chi2_A,
                        "large_delta_cos_neg": chi2_B,
                        "cut_3sigma": wp7.CHI2_3SIGMA_7DOF},
        "large_branch_top_pulls": {n: float(p) for n, p in top_B},
        "viable_branch": viable_branch,
        "atlas_viable_folded_bins_deg": {str(k): v for k, v in
                                         sorted(atlas_bins.items())},
        "atlas_max_deviation_from_window_deg": max_dev,
        "wp15b_class_histogram": {str(k): v for k, v in
                                  sorted(hist.items())},
        "dominant_classes_total": len(dominant),
        "dominant_classes_unmatched_before_topup": unmatched,
        "orbit_completion_physical16_gated": orbit_pinned,
        "class_phases_matched_within_1deg": matched,
        "class_phases_off_atlas": genuinely_off,
        "interpretation": ("histogram support = folded pinned phases of "
                           "the exact-fit atlas on the viable (cos "
                           "delta > 0) branch; the other branch fails "
                           "the 17-observable fit via |Vtd|/beta; "
                           "clustering near pi/8 multiples = CKM angles "
                           "near pi/8 multiples + WP14b inheritance "
                           "pinning + window binning; class "
                           "multiplicities are scan-basin weights.  All "
                           "exact-fit solves are physical10-fiber "
                           "solves: finite ambiguity, never uniqueness; "
                           "sheet membership of every root is certified "
                           "by its physical16 image, per the fiber-claim "
                           "policy"),
    }
    dest = "results/wp19_pi8_accounting.json"
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("->", dest)


if __name__ == "__main__":
    main()
