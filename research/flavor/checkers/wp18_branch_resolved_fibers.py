#!/usr/bin/env python3
"""WP18: branch-resolved chart fibers — erratum to the WP16 interpretation.

WP16 measured fibers of the composite map

    chart parameters -> physical quotient -> physical10
                       = (6 singular values, |Vus|, |Vub|, |Vcb|, J)

and read the multiplicity as chart-intrinsic.  That reading is wrong:
physical10 is generically TWO-to-one on the quotient.  The CKM block
(|Vus|, |Vub|, |Vcb|, signed J) fixes the PDG parameters
(s12, s13, s23, sin delta), leaving the cos-delta sign ambiguous; the
two branches delta and pi - delta have different |Vtd|, |Vcd|, |Vcs|,
|Vts| (verified: WP16's orbit-15 two-phase "fiber" is exactly one
preimage per branch, |Vtd| = 0.00873 vs 0.01129).

This checker reruns the covering orbit representatives, keeps each
root's FULL invariant image (physical16: 6 singular values + 9 |V|
entries + J), clusters roots into branches by sign of cos delta
(equivalently |Vtd|), and reports per-branch pre-image counts: the
honest chart fiber over ONE physical quotient point.

Outputs: research/flavor/results/wp18_branch_resolved_fibers.json
"""
import glob
import json
import math
import sys

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, "checkers")
import wp7_ensemble as wp7
from wp16a_fiber_degree import physical10


def physical16(Yu, Yd):
    """Complete generic quotient coordinate: 6 singular values, all 9
    CKM magnitudes, signed J."""
    su2, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
    sd2, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
    V = Uu.conj().T @ Ud
    J = (V[0, 1] * V[1, 2] * V[0, 2].conj() * V[1, 1].conj()).imag
    sv = np.sqrt(np.maximum(np.concatenate([su2, sd2]), 0.0))
    return np.concatenate([sv, np.abs(V).flatten(), [J]])


def main(n_starts=800, seed=81818):
    pilot = json.load(open("results/wp16a_fiber_degree_pilot.json"))
    p_star = np.array(pilot["p_star"])
    scale = np.abs(p_star)
    stab = json.load(open("results/wp16b_fiber_stability.json"))
    covering = stab["covering_representatives"]

    rng = np.random.default_rng(seed)
    rows = []
    for k, a in enumerate(covering):
        mu, md = a["member"]
        phase_sector, phase_slot = wp7.paper_phase_edge(mu, md)
        us, ds = wp7.mask_slots(mu), wp7.mask_slots(md)

        def resid(theta):
            Yu, Yd = wp7.build_texture(mu, md, phase_sector, phase_slot,
                                       theta)
            return (physical10(Yu, Yd) - p_star) / scale

        roots = []
        for _ in range(n_starts):
            s = np.concatenate([wp7.start_point(us, ds, rng),
                                [rng.uniform(-math.pi, math.pi)]])
            try:
                sol = least_squares(resid, s, method="lm",
                                    ftol=1e-15, xtol=1e-15, gtol=1e-15,
                                    max_nfev=2000)
            except Exception:
                continue
            if float(np.max(np.abs(resid(sol.x)))) < 1e-7:
                th = sol.x
                if not any(np.max(np.abs(q[:9] - th[:9])) < 1e-4
                           and wp7.phi_distance(q[9], th[9]) < 1e-4
                           for q in roots):
                    roots.append(th)
        # classify each root by its branch: |Vtd| relative to the two
        # branch values at p* (0.00873 small-delta branch,
        # 0.01129 large-delta branch)
        branches = {"small_cos_pos": [], "large_cos_neg": []}
        for th in roots:
            Yu, Yd = wp7.build_texture(mu, md, phase_sector, phase_slot,
                                       th)
            img = physical16(Yu, Yd)
            vtd = float(img[6 + 6])  # |V| row 2 col 0
            key = ("small_cos_pos" if abs(vtd - 0.0087282) < 2e-4
                   else "large_cos_neg")
            branches[key].append({
                "phi_mod_2pi": round(float((th[9] + math.pi)
                                           % (2 * math.pi) - math.pi), 6),
                "vtd": round(vtd, 8)})
        rows.append({"orbit_index": a["orbit_index"], "swap": a["swap"],
                     "member": [mu, md],
                     "total_roots": len(roots),
                     "per_branch": {kk: len(vv)
                                    for kk, vv in branches.items()},
                     "roots": branches})
        print(f"{k+1}/{len(covering)} orbit {a['orbit_index']} "
              f"swap={a['swap']}: total {len(roots)} = "
              f"{len(branches['small_cos_pos'])} small-delta + "
              f"{len(branches['large_cos_neg'])} large-delta",
              flush=True)

    tot_small = sum(r["per_branch"]["small_cos_pos"] for r in rows)
    tot_large = sum(r["per_branch"]["large_cos_neg"] for r in rows)
    out = {
        "purpose": "WP18 erratum: WP16 fibers are fibers of the "
                   "TWO-to-one observable coordinate physical10, not "
                   "chart-intrinsic multiplicities over one quotient "
                   "point; this rerun resolves every root by branch",
        "branch_witness": ("|Vtd| = 0.00873 (cos delta > 0) vs "
                           "0.01129 (cos delta < 0) at p*"),
        "n_starts_per_rep": n_starts,
        "accept_threshold_rel": 1e-7,
        "per_representative": rows,
        "total_roots_small_delta_branch": tot_small,
        "total_roots_large_delta_branch": tot_large,
    }
    dest = "results/wp18_branch_resolved_fibers.json"
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"totals: {tot_small} small-delta + {tot_large} large-delta")
    print("->", dest)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 800
    main(n)
