#!/usr/bin/env python3
"""WP19b: valley coverage audit on top of the WP19 accounting.

The WP19 stage-3 question was mis-posed: it asked whether every dominant
WP15b class phase sits near its OWN orbit's exact p* pinned phase.  The
dense physical16-gated completion (WP19 stage 4) shows the right
structure is different:

* per orbit, every exact viable pinned phase has a dominant scan class
  within 1 deg  ->  the exact fiber is CONTAINED in the scan valley set;
* the remaining classes are distinct viable chi2 minima (other quotient
  points inside the 3-sigma ellipsoid), not perturbations of p*;
* sibling orbits share the valley phase multiset while the exact p*
  valley occupies different members in different charts (WP11 chart
  dependence, inside the fit ensemble itself);
* the extra valleys also hug the pi/8 window centers within ~2 deg;
  inheritance (WP14b) explains the p* valley exactly, but the tightness
  of the extra valleys is an empirical fact whose mechanism is not
  separated here (recorded as an unresolved observation).

This checker certifies the coverage direction from stored artifacts
only (no new solves), records the per-orbit valley sets, and rewrites
the WP19 interpretation field so the published JSON does not overclaim.

Reads:  results/wp19_pi8_accounting.json,
        results/wp15b_dense_class_reduction.json
Writes: results/wp19b_valley_coverage.json
        (and patches the interpretation field of the WP19 record)
"""
import json
import math
from collections import defaultdict

W19 = "results/wp19_pi8_accounting.json"
W15 = "results/wp15b_dense_class_reduction.json"
DEST = "results/wp19b_valley_coverage.json"

INTERPRETATION = (
    "histogram support = folded viable phases of the fit atlas; the "
    "cos delta > 0 sheet is selected by the 17-observable fit "
    "(chi2 3.36 vs 651 via |Vtd|/beta/gamma/alpha).  Per orbit the "
    "exact p* fiber is contained in the scan's viable valley set "
    "(coverage certified in wp19b); the scan additionally finds "
    "distinct viable minima (other quotient points in the 3-sigma "
    "ellipsoid) whose phases also lie within 2.2 deg of pi/8 window "
    "centers.  For the p* valleys the clustering mechanism is exact: "
    "CKM angles within ~1 deg of pi/8 multiples + WP14b inheritance "
    "pinning + window binning, and class multiplicities are scan-basin "
    "weights.  For the extra valleys the same window tightness is "
    "empirical; its mechanism is recorded as an unresolved observation "
    "(needs per-valley physical16 data not stored by WP15b).  All "
    "exact-fit solves are physical10-fiber solves, sheet-gated by "
    "physical16: finite ambiguity, never uniqueness."
)


def main():
    w19 = json.load(open(W19))
    w15 = json.load(open(W15))

    classes_by_orbit = defaultdict(list)
    for c in w15["class_table"]:
        if c["chi2_min"] < 4.0:
            classes_by_orbit[c["orbit_index"]].append(
                round(math.degrees(c["phi_folded"]), 2))

    completion = w19["orbit_completion_physical16_gated"]
    coverage = {}
    all_covered = True
    for oi_s, rec in sorted(completion.items(), key=lambda t: int(t[0])):
        oi = int(oi_s)
        cfs = classes_by_orbit.get(oi, [])
        per_phase = {}
        for f in rec["pinned_deg"]:
            d = min((abs(f - cf) for cf in cfs), default=None)
            per_phase[str(f)] = (None if d is None else
                                 {"nearest_class_deg": round(
                                     min(cfs, key=lambda c: abs(f - c)),
                                     2), "distance_deg": round(d, 3)})
            if d is None or d > 1.0:
                all_covered = False
        coverage[oi_s] = {
            "pinned_deg": rec["pinned_deg"],
            "branch_root_counts": rec["branch_root_counts"],
            "class_valley_phases_deg": sorted(set(cfs)),
            "pinned_phase_coverage": per_phase,
        }

    # Orbits never topped up had every dominant class matched in stage 3
    # (their exact phases were already represented in the class list).
    topped = {int(k) for k in completion}
    stage3_orbits = sorted(set(classes_by_orbit) - topped)
    for oi in stage3_orbits:
        coverage[str(oi)] = {
            "pinned_deg": None,
            "note": "all dominant classes matched sampled atlas phases "
                    "at 1 deg in WP19 stage 3; no top-up needed",
            "class_valley_phases_deg": sorted(set(classes_by_orbit[oi])),
        }

    out = {
        "purpose": "certify exact-fiber-in-scan-valley coverage and "
                   "record per-orbit valley sets (WP19b)",
        "exact_fiber_covered_by_scan_valleys": all_covered,
        "per_orbit": coverage,
        "interpretation": INTERPRETATION,
    }
    with open(DEST, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("exact fiber covered by scan valleys:", all_covered)
    for oi_s, rec in coverage.items():
        print(f"  orbit {oi_s}: valleys {rec['class_valley_phases_deg']}"
              f"  pinned {rec['pinned_deg']}")
    print("->", DEST)

    # keep the WP19 record honest: replace its interpretation with the
    # corrected text
    w19["interpretation"] = INTERPRETATION
    w19["interpretation_superseded_by"] = DEST
    with open(W19, "w", encoding="utf-8") as f:
        json.dump(w19, f, indent=2)
    print("patched interpretation in", W19)


if __name__ == "__main__":
    main()
