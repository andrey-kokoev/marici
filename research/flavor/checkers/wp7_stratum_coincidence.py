"""WP7.2b: stratum-coincidence of the loop phase across support orbits
(marici.Figueiredo).

Question (sharp form of the WP3 chart-transition test, now decidable
on the rebuilt ensemble): when two DIFFERENT support orbits fit the
SAME physical flavor point, do their loop phases agree?

Method
------
For every viable minimum in wp7_ensemble.json:

  1. compute the 17 Tab.-S2 observables at the fitted point;
  2. group minima by physical point: two minima are in one group iff
     their 17-observable vectors agree to PHYS_TOL (relative to the
     Tab.-S2 sigma, i.e. the difference is experimentally
     indistinguishable);
  3. within each group, compare the folded loop phases across ORBITS;
  4. also record arg det(Yu Yd) per minimum (WP5 strong-CP channel:
     the loop phase may or may not enter the determinant matchings of
     a given chart).

Findings are empirical statements about the rebuilt nine-link
ensemble, not theorems; the complementary EXACT result (entry 1076)
is that phi is NOT invariant under the full U(3)^3 quotient -- a
general weak-basis rotation moves off the sparse stratum and destroys
the loop phase.  What is tested here is the stratum-restricted
question: phi transport between sparse charts at FIXED physics.

Output: research/flavor/results/wp7_stratum_coincidence.json
"""
import json
import math
import sys

import numpy as np

sys.path.insert(0, "research/flavor/checkers")
from wp7_ensemble import build_texture, observables17, OBS17, SIGMA

# Two minima are the same physical point if every observable agrees
# to this fraction of its Tab.-S2 sigma.  Converged LM minima agree
# to ~1e-7 sigma when they land on the same point; 1e-4 is far below
# any experimentally meaningful separation and far above convergence
# noise.
PHYS_TOL_SIGMA = 1e-4


def physical_invariants(m):
    """17 observables + arg det(Yu Yd) at one viable minimum."""
    pe = m["phase_edge"]
    theta = np.array(m["log_mags"] + [m["phi"]])
    Yu, Yd = build_texture(m["member"][0], m["member"][1],
                           pe[0], (pe[1], pe[2]), theta)
    obs = observables17(Yu, Yd)
    det = np.linalg.det(Yu @ Yd)
    argdet = math.atan2(det.imag, det.real)
    return obs, argdet


def main():
    data = json.load(open("research/flavor/results/wp7_ensemble.json"))

    # Flatten minima with orbit provenance and physics signature.
    pts = []
    for orb in data["orbits"]:
        for m in orb["viable_minima"]:
            obs, argdet = physical_invariants(m)
            pts.append({"orbit": orb["orbit_index"],
                        "member": m["member"],
                        "chi2": m["chi2"],
                        "phi": m["phi"],
                        "phi_folded": m["phi_folded"],
                        "argdet": argdet,
                        "obs": obs})

    # Group by physical point (greedy, best-chi2 first).
    groups = []
    for p in sorted(pts, key=lambda r: r["chi2"]):
        pulls = np.abs(p["obs"] / SIGMA)  # not used for grouping
        for g in groups:
            if np.all(np.abs(p["obs"] - g["ref_obs"])
                      <= PHYS_TOL_SIGMA * SIGMA):
                g["members"].append(p)
                break
        else:
            groups.append({"ref_obs": p["obs"], "members": [p]})

    # Keep groups that span more than one orbit: those are the
    # chart-transition tests.
    multi = []
    for g in groups:
        orbits = sorted({m["orbit"] for m in g["members"]})
        if len(orbits) < 2:
            continue
        phis = sorted({round(m["phi_folded"], 6) for m in g["members"]})
        argdets = sorted({round(m["argdet"], 4) for m in g["members"]})
        # phase agreement within the group, folded circle
        phi_vals = np.array([m["phi_folded"] for m in g["members"]])
        spread = float(phi_vals.max() - phi_vals.min())
        multi.append({
            "orbits": orbits,
            "n_members": len(g["members"]),
            "distinct_folded_phis": phis,
            "phi_spread_rad": spread,
            "distinct_argdet": argdets,
            "best_chi2": min(m["chi2"] for m in g["members"]),
        })
    multi.sort(key=lambda g: -g["n_members"])

    out = {
        "purpose": "WP7.2b loop-phase stratum coincidence: same "
                   "physical point across support orbits -> same phi?",
        "conventions": {
            "phys_tol_sigma": PHYS_TOL_SIGMA,
            "source": "wp7_ensemble.json viable minima",
            "complement": "entry 1076 exact result: phi NOT invariant "
                          "under full U(3)^3; this test is the "
                          "stratum-restricted question",
        },
        "n_minima": len(pts),
        "n_physical_points": len(groups),
        "n_multi_orbit_points": len(multi),
        "multi_orbit_points": multi,
    }
    with open("research/flavor/results/wp7_stratum_coincidence.json",
              "w") as f:
        json.dump(out, f, indent=1)

    print(f"minima {len(pts)}, distinct physical points {len(groups)}, "
          f"multi-orbit points {len(multi)}")
    for g in multi:
        print(f"  orbits {g['orbits']} members {g['n_members']:2d} "
              f"phis {g['distinct_folded_phis']} "
              f"spread {g['phi_spread_rad']:.5f} "
              f"argdet {g['distinct_argdet']}")
    print("wrote research/flavor/results/wp7_stratum_coincidence.json")


if __name__ == "__main__":
    main()
