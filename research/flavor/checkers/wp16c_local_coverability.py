#!/usr/bin/env python3
"""WP16c: local coverability — Jacobian regularity at fiber preimages.

WP16b found that 21/36 orbit representatives carry an exact preimage of
the physical point p* (41 roots total at 100 starts).  A chart whose
10-dim parameterization (9 log-magnitudes + phi) -> physical10 has full
Jacobian rank at a preimage covers an open neighborhood of p* by the
inverse function theorem.  This checker re-solves each covering
representative (moderate start count) and computes the numerical
Jacobian rank and condition number at every distinct root found.

Interpretation:
  full rank at >=1 root in a rep  => that chart class covers an open
                                     patch around p*;
  all covering reps full rank      => the atlas covers an open
                                      neighborhood of the physical
                                      point (local coverability);
  rank-deficient roots             => boundary/branch points of the
                                      chart map (recorded, not hidden).

Outputs: research/flavor/results/wp16c_local_coverability.json
"""
import json
import math
import sys

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, "checkers")
import wp7_ensemble as wp7
from wp16a_fiber_degree import physical10


def jacobian(mu, md, phase_sector, phase_slot, theta, p_star, scale):
    f0 = (physical10(*wp7.build_texture(mu, md, phase_sector,
                                        phase_slot, theta)) - p_star) / scale
    J = np.zeros((10, 10))
    for j in range(10):
        h = 1e-6 * max(1.0, abs(theta[j]))
        tp = theta.copy(); tp[j] += h
        tm = theta.copy(); tm[j] -= h
        fp = (physical10(*wp7.build_texture(mu, md, phase_sector,
                                            phase_slot, tp)) - p_star) / scale
        fm = (physical10(*wp7.build_texture(mu, md, phase_sector,
                                            phase_slot, tm)) - p_star) / scale
        J[:, j] = (fp - fm) / (2 * h)
    return J


def main(n_starts=200, seed=60221):
    pilot = json.load(open("results/wp16a_fiber_degree_pilot.json"))
    p_star = np.array(pilot["p_star"])
    scale = np.abs(p_star)
    atlas = json.load(open("results/wp16b_atlas_fiber.json"))
    covering = [a for a in atlas["atlas"] if a["fiber_degree"] > 0]

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
        root_rows = []
        for th in roots:
            with np.errstate(all="ignore"):
                J = jacobian(mu, md, phase_sector, phase_slot, th,
                             p_star, scale)
                sv = np.linalg.svd(J, compute_uv=False)
            rank = int(np.sum(sv > 1e-8 * sv[0])) if sv[0] > 0 else 0
            cond = float(sv[0] / sv[-1]) if sv[-1] > 0 else float("inf")
            root_rows.append({
                "phi_mod_2pi": round(float((th[9] + math.pi)
                                           % (2 * math.pi) - math.pi), 6),
                "jacobian_rank": rank,
                "min_singular_value": float(sv[-1]),
                "condition_number": cond,
            })
        full = sum(1 for r in root_rows if r["jacobian_rank"] == 10)
        rows.append({"orbit_index": a["orbit_index"], "swap": a["swap"],
                     "member": [mu, md], "roots_found": len(roots),
                     "full_rank_roots": full, "roots": root_rows})
        print(f"{k+1}/{len(covering)} orbit {a['orbit_index']} "
              f"swap={a['swap']}: {len(roots)} roots, {full} full-rank",
              flush=True)

    reps_with_patch = sum(1 for r in rows if r["full_rank_roots"] > 0)
    out = {
        "purpose": "WP16c: Jacobian regularity of the chart map at exact "
                   "preimages of p*; full rank => chart covers an open "
                   "patch of the physical quotient around p*",
        "p_star_source": "results/wp16a_fiber_degree_pilot.json",
        "n_starts_per_rep": n_starts,
        "accept_threshold_rel": 1e-7,
        "rank_threshold_rel": 1e-8,
        "covering_representatives": rows,
        "reps_with_full_rank_root": reps_with_patch,
        "reps_tested": len(rows),
        "conclusion": (
            f"{reps_with_patch}/{len(rows)} covering representatives "
            "have at least one full-rank preimage"
            + (" — atlas covers an open neighborhood of p*"
               if reps_with_patch == len(rows) else "")),
    }
    dest = "results/wp16c_local_coverability.json"
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(out["conclusion"])
    print("->", dest)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    main(n)
