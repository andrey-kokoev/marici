#!/usr/bin/env python3
"""WP16b: atlas fiber over one exact physical point.

Over p* (the exact image of the global-best WP15b fit, computed in
WP16a), ask for EVERY chart class of the paper's texture space:

    does this chart carry an exact preimage of p*, and how many?

Since attainable image sets are S3^3-orbit invariant and the paper's
texture space is 36 S3^3 orbits (18 exchange orbits x both sector
halves), the atlas question reduces to 36 representatives.  Any chart
with an exact preimage of p* fits the measured data with
chi2(p*) = 3.36 < 20.28, so the answer is automatically a sub-atlas of
the WP15b viable classes — a built-in consistency check.

Outputs: research/flavor/results/wp16b_atlas_fiber.json
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


def main(n_starts=100, seed=977):
    pilot = json.load(open("results/wp16a_fiber_degree_pilot.json"))
    p_star = np.array(pilot["p_star"])
    scale = np.abs(p_star)

    reps = []
    for path in sorted(glob.glob("results/wp15b_dense_orbit*.json")):
        d = json.load(open(path))
        for half in d["s3_orbits"]:
            mu, md = half["representative"]
            reps.append({"orbit_index": d["orbit_index"],
                         "swap": bool(half["sector_swapped"]),
                         "member": (mu, md)})

    rng = np.random.default_rng(seed)
    atlas = []
    for k, rep in enumerate(reps):
        mu, md = rep["member"]
        phase_sector, phase_slot = wp7.paper_phase_edge(mu, md)
        us, ds = wp7.mask_slots(mu), wp7.mask_slots(md)

        def resid(theta):
            Yu, Yd = wp7.build_texture(mu, md, phase_sector, phase_slot,
                                       theta)
            return (physical10(Yu, Yd) - p_star) / scale

        roots = []
        for _ in range(n_starts):
            logs = wp7.start_point(us, ds, rng)
            s = np.concatenate([logs, [rng.uniform(-math.pi, math.pi)]])
            try:
                sol = least_squares(resid, s, method="lm",
                                    ftol=1e-15, xtol=1e-15, gtol=1e-15,
                                    max_nfev=2000)
            except Exception:
                continue
            rmax = float(np.max(np.abs(resid(sol.x))))
            if rmax < 1e-7:
                th = sol.x
                if not any(np.max(np.abs(q[:9] - th[:9])) < 1e-4
                           and wp7.phi_distance(q[9], th[9]) < 1e-4
                           for q in roots):
                    roots.append(th)
        entry = {**rep, "fiber_degree": len(roots),
                 "phis": [round(float(q[9]), 6) for q in roots]}
        atlas.append(entry)
        print(f"rep {k+1}/36 orbit {rep['orbit_index']} "
              f"swap={rep['swap']} {rep['member']} -> degree {len(roots)}",
              flush=True)

    covering = [a for a in atlas if a["fiber_degree"] > 0]
    out = {
        "purpose": "WP16b: exact atlas fiber over the WP16a point p*; "
                   "one representative per S3^3 orbit, both halves",
        "p_star_source": "results/wp16a_fiber_degree_pilot.json",
        "n_starts_per_rep": n_starts,
        "accept_threshold_rel": 1e-7,
        "representatives_tested": len(atlas),
        "representatives_with_preimage": len(covering),
        "total_exact_preimages": sum(a["fiber_degree"] for a in atlas),
        "atlas": atlas,
    }
    dest = "results/wp16b_atlas_fiber.json"
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"covering representatives: {len(covering)}/36, "
          f"total exact preimages: {out['total_exact_preimages']}")
    print("->", dest)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    main(n)
