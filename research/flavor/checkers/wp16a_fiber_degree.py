#!/usr/bin/env python3
"""WP16a: fiber degree of one sparse chart over one exact physical point.

The chart map sends a gauge-fixed texture point theta = (9 log-magnitudes,
loop phase phi) on a fixed support member to the 10-dimensional physical
coordinate

    p = (y_u, y_c, y_t, y_d, y_s, y_b, |V_us|, |V_ub|, |V_cb|, J).

(For 3x3 Yukawa pairs, dim {(Y_u,Y_d)}/U(3)^3 = 36 - 27 + 1 = 10, and the
six singular values plus three CKM magnitudes plus the signed Jarlskog
invariant are a generically complete coordinate set, so "same p" IS "same
physical point" up to the discrete completion ambiguity.)

Pilot question: over the exact image point of the global-best WP15b fit,
how many DISTINCT exact preimages does one fixed chart carry?  We take the
best viable minimum, compute its exact image p*, then solve the square
system chart(theta) = p* from many hierarchy-aware starts with a tight LM
solve and cluster the roots.

Outputs: research/flavor/results/wp16a_fiber_degree_pilot.json
"""
import glob
import json
import math
import sys

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, "checkers")
import wp7_ensemble as wp7


def physical10(Yu, Yd):
    """The 10-dim physical coordinate: 6 singular values, 3 CKM
    magnitudes, signed Jarlskog J = Im(V_us V_cb V_ub* V_cs*)."""
    obs = wp7.observables17(Yu, Yd)
    su2, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
    sd2, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
    V = Uu.conj().T @ Ud
    J = (V[0, 1] * V[1, 2] * V[0, 2].conj() * V[1, 1].conj()).imag
    return np.array([obs[0], obs[1], obs[2], obs[3], obs[4], obs[5],
                     obs[6], obs[7], obs[8], J])


def find_global_best():
    best = None
    for path in sorted(glob.glob("results/wp15b_dense_orbit*.json")):
        d = json.load(open(path))
        for half in d["s3_orbits"]:
            for m in half["member_results"]:
                for v in m["viable_minima"]:
                    if best is None or v["chi2"] < best["chi2"]:
                        best = {**v, "orbit_index": d["orbit_index"]}
    return best


def main(n_starts=500, seed=20260822):
    best = find_global_best()
    mu, md = best["member"]
    phase_sector, phase_slot = wp7.paper_phase_edge(mu, md)
    us, ds = wp7.mask_slots(mu), wp7.mask_slots(md)

    theta_star = np.array(list(best["log_mags"]) + [best["phi"]])
    Yu, Yd = wp7.build_texture(mu, md, phase_sector, phase_slot, theta_star)
    p_star = physical10(Yu, Yd)

    scale = np.abs(p_star)  # relative residual normalization per coordinate

    def resid(theta):
        Yu, Yd = wp7.build_texture(mu, md, phase_sector, phase_slot, theta)
        return (physical10(Yu, Yd) - p_star) / scale

    # Sanity: the seed itself must solve the system exactly.
    r0 = resid(theta_star)
    sanity = float(np.max(np.abs(r0)))

    rng = np.random.default_rng(seed)
    roots = []

    def try_add(theta, rmax):
        for q in roots:
            if (np.max(np.abs(q["theta"][:9] - theta[:9])) < 1e-4
                    and wp7.phi_distance(q["theta"][9], theta[9]) < 1e-4):
                return False
        roots.append({"theta": theta.tolist(), "resid_max_rel": rmax})
        return True

    starts = [theta_star]
    for _ in range(n_starts):
        logs = wp7.start_point(us, ds, rng)
        starts.append(np.concatenate([logs, [rng.uniform(-math.pi,
                                                         math.pi)]]))
    n_tried = 0
    for s in starts:
        n_tried += 1
        try:
            sol = least_squares(resid, s, method="lm",
                                ftol=1e-15, xtol=1e-15, gtol=1e-15,
                                max_nfev=2000)
        except Exception:
            continue
        rmax = float(np.max(np.abs(resid(sol.x))))
        if rmax < 1e-7:
            try_add(sol.x, rmax)

    roots_out = []
    for q in roots:
        th = q["theta"]
        roots_out.append({
            "phi": th[9],
            "phi_folded_deg": math.degrees(wp7.fold_phi(th[9])),
            "log_mags": th[:9],
            "resid_max_rel": q["resid_max_rel"],
            "matches_seed": bool(
                np.max(np.abs(np.array(th[:9]) - theta_star[:9])) < 1e-4
                and wp7.phi_distance(th[9], theta_star[9]) < 1e-4),
        })

    out = {
        "purpose": "WP16a pilot: exact fiber of one chart over the exact "
                   "image point of the global-best WP15b viable minimum",
        "physical_coordinate": "(yu,yc,yt,yd,ys,yb,|Vus|,|Vub|,|Vcb|,J)",
        "seed_fit": {"orbit_index": best["orbit_index"], "member": [mu, md],
                     "chi2_vs_data": best["chi2"], "phi": best["phi"]},
        "phase_edge": [phase_sector, list(phase_slot)],
        "p_star": p_star.tolist(),
        "seed_self_residual_max_rel": sanity,
        "n_starts": n_tried,
        "accept_threshold_rel": 1e-7,
        "fiber_degree": len(roots_out),
        "fiber_elements": roots_out,
    }
    dest = "results/wp16a_fiber_degree_pilot.json"
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"seed self-residual (max rel): {sanity:.3e}")
    print(f"starts: {n_tried}, exact roots found: {len(roots_out)}")
    for i, r in enumerate(roots_out):
        print(f"  root {i}: phi={r['phi']:+.6f} "
              f"(folded {r['phi_folded_deg']:.3f} deg) "
              f"resid={r['resid_max_rel']:.2e} seed={r['matches_seed']}")
    print("->", dest)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    main(n)
