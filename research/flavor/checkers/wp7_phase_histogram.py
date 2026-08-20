"""WP7.2/WP7.3: orbit-collapsed fitted-phase histogram vs the paper's
pi/8 clustering, plus a prior sweep (marici.Figueiredo).

Input: research/flavor/results/wp7_ensemble.json (WP7.1 rebuild of the
nine-link stratum: 18 support orbits mod S3^3 + sector exchange,
viable LM minima from the member sweep).

The paper's Fig. 3 histograms fitted loop phases over its scan
ensemble (2398 free-scan fits, 156 permutation classes including
ten-link textures) and reports clustering near multiples of pi/8; the
fixed-phase scan admits classes at phi = pi/8, 3pi/8, pi/2 (29 + 35 +
35 = 99 classes).  WP7 asks whether the clustering survives:

  WP7.2  collapse of the ensemble by support orbit (multiplicity
         removed: each orbit counts once, not once per member/branch);
  WP7.3  prior changes: uniform-over-fits vs uniform-over-orbits vs
         chi^2-likelihood weighting.

Conventions
-----------
- folded phase in [0, pi/2] (identify +-phi, pi+-phi), as in the
  paper's figures;
- BRANCH_TOL: viable minima within 0.03 rad (on the folded circle of
  circumference pi) are one branch; branch phase = folded phi of the
  branch's minimum-chi2 minimum;
- per-orbit best branch = minimum-chi2 branch (the Fig.-3 analog:
  one phase per class);
- lattice: multiples of pi/8 in [0, pi/2] = {0, pi/8, pi/4, 3pi/8,
  pi/2}.  Distance to lattice on the folded circle (0 and pi/2 are
  DISTINCT lattice points, not identified -- the fold identifies
  +-phi and pi+-phi only);
- clustering statistic: for a tolerance Delta, an orbit/branch is
  "on lattice" if its folded phase is within Delta of a multiple of
  pi/8.  Null model: uniform on [0, pi/2], giving on-lattice
  probability p0(Delta) = min(1, 5*Delta / (pi/2)) for Delta <= pi/16
  (windows around interior points have width 2*Delta, around the two
  endpoints width Delta each -- total 8*Delta + 2*Delta = 10*Delta...
  computed EXACTLY below as the measure of the Delta-neighborhood of
  the lattice inside [0, pi/2]).

Output: research/flavor/results/wp7_phase_histogram.json
"""
import json
import math

BRANCH_TOL = 0.03          # rad, folded-circle distance
LATTICE = [k * math.pi / 8.0 for k in range(5)]   # 0 .. pi/2
HALF = math.pi / 2.0


def folded_dist(a, b):
    """Distance on the folded segment [0, pi/2] (plain distance; the
    fold endpoints are not identified)."""
    return abs(a - b)


def lattice_dist(phi):
    return min(folded_dist(phi, l) for l in LATTICE)


def lattice_measure(delta):
    """Exact Lebesgue measure of the Delta-neighborhood of the
    pi/8 lattice inside [0, pi/2]."""
    pts = [0.0, HALF]
    for l in LATTICE:
        pts.append(min(HALF, l + delta))
        pts.append(max(0.0, l - delta))
    # integrate via sorted breakpoints
    pts = sorted(set(pts))
    total = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        mid = 0.5 * (a + b)
        if lattice_dist(mid) <= delta:
            total += b - a
    return total


def cluster_branches(minima):
    """Greedy clustering of viable minima into branches on folded
    phi; minima sorted by chi2 so the best minimum seeds its branch.
    Branch phase: folded phi of the branch's minimum-chi2 member."""
    branches = []
    for m in sorted(minima, key=lambda r: r["chi2"]):
        phi = m["phi_folded"]
        for br in branches:
            if folded_dist(phi, br["phi"]) < BRANCH_TOL:
                br["members"].append(m)
                if m["chi2"] < br["chi2"]:
                    br["chi2"] = m["chi2"]
                    br["phi"] = phi
                break
        else:
            branches.append({"phi": phi, "chi2": m["chi2"],
                             "members": [m]})
    branches.sort(key=lambda b: b["chi2"])
    return branches


def main():
    data = json.load(open("research/flavor/results/wp7_ensemble.json"))
    orbits = data["orbits"]

    orbit_records = []
    for orb in orbits:
        branches = cluster_branches(orb["viable_minima"])
        best = branches[0] if branches else None
        orbit_records.append({
            "orbit_index": orb["orbit_index"],
            "mask_u": orb["mask_u"], "mask_d": orb["mask_d"],
            "cycle_length": orb["cycle_length"],
            "n_members": orb["n_members"],
            "members_tried": len(orb["members_tried"]),
            "escalated": orb["escalated"],
            "n_viable_minima": len(orb["viable_minima"]),
            "n_branches": len(branches),
            "best_chi2_overall": orb["best_chi2_overall"],
            "branches": [{"phi_folded": b["phi"], "chi2": b["chi2"],
                          "n_minima": len(b["members"])}
                         for b in branches],
            "best_branch_phi": best["phi"] if best else None,
            "best_branch_chi2": best["chi2"] if best else None,
        })

    fitted = [r for r in orbit_records if r["best_branch_phi"] is not None]
    unfitted = [r["orbit_index"] for r in orbit_records
                if r["best_branch_phi"] is None]

    # ------------------------------------------------ WP7.2 collapse
    # Convention A (Fig.-3 analog): best branch per orbit.
    best_phis = [r["best_branch_phi"] for r in fitted]
    # Convention B: all branches, orbit-collapsed (each branch once).
    all_phis = [b["phi_folded"] for r in fitted for b in r["branches"]]
    # Convention C (uniform-over-fits): every viable minimum.
    fit_phis = [m["phi_folded"] for o, r in zip(orbits, orbit_records)
                for m in o["viable_minima"]]

    def on_lattice(phi, delta):
        return lattice_dist(phi) <= delta

    deltas = [0.01, 0.02, 0.035, 0.05, 0.075, 0.10]
    hist = {}
    for name, phis in (("best_branch_per_orbit", best_phis),
                       ("all_branches_orbit_collapsed", all_phis),
                       ("uniform_over_fits", fit_phis)):
        n = len(phis)
        rows = []
        for d in deltas:
            k = sum(1 for p in phis if on_lattice(p, d))
            p0 = lattice_measure(d) / HALF
            rows.append({"delta": d, "on_lattice": k, "total": n,
                         "fraction": k / n if n else None,
                         "null_uniform_fraction": p0,
                         "excess_over_null": (k / n - p0) if n else None})
        hist[name] = {"n": n, "by_delta": rows,
                      "phis_sorted": sorted(round(p, 6) for p in phis)}

    # ------------------------------------------------ WP7.3 priors
    # chi2-likelihood weighting over branches: w = exp(-chi2/2),
    # normalized per convention.
    def weighted_on_lattice(delta):
        num = den = 0.0
        for r in fitted:
            for b in r["branches"]:
                w = math.exp(-0.5 * b["chi2"])
                den += w
                if on_lattice(b["phi_folded"], delta):
                    num += w
        return num / den if den else None

    wp73 = {"by_delta": [
        {"delta": d,
         "weighted_fraction_on_lattice": weighted_on_lattice(d),
         "null_uniform_fraction": lattice_measure(d) / HALF}
        for d in deltas]}

    out = {
        "purpose": "WP7.2 orbit-collapsed fitted-phase histogram vs "
                   "pi/8 lattice; WP7.3 prior sweep",
        "stratum": "nine-link textures only (paper's 156 classes "
                   "include ten-link); 18 support orbits mod S3^3 + "
                   "sector exchange",
        "conventions": {
            "branch_tol_rad": BRANCH_TOL,
            "lattice": [round(l, 6) for l in LATTICE],
            "phase_folding": "[0, pi/2], endpoints not identified",
            "paper_fixed_phase_classes": {"pi/8": 29, "3pi/8": 35,
                                          "pi/2": 35},
        },
        "orbits": orbit_records,
        "unfitted_orbits": unfitted,
        "histograms": hist,
        "wp73_chi2_weighted": wp73,
    }
    with open("research/flavor/results/wp7_phase_histogram.json", "w") as f:
        json.dump(out, f, indent=1)

    # console summary
    print(f"orbits fitted: {len(fitted)}/18, unfitted: {unfitted}")
    for name in hist:
        h = hist[name]
        print(f"\n[{name}] n={h['n']}")
        print("  phis:", h["phis_sorted"])
        for row in h["by_delta"]:
            print(f"  delta={row['delta']:.3f}: on-lattice "
                  f"{row['on_lattice']}/{row['total']} "
                  f"({(row['fraction'] or 0):.2f}) vs null "
                  f"{row['null_uniform_fraction']:.2f}")
    print("\nWP7.3 chi2-weighted on-lattice fraction:")
    for row in wp73["by_delta"]:
        print(f"  delta={row['delta']:.3f}: "
              f"{row['weighted_fraction_on_lattice']:.2f} vs null "
              f"{row['null_uniform_fraction']:.2f}")
    print("\nwrote research/flavor/results/wp7_phase_histogram.json")


if __name__ == "__main__":
    main()
