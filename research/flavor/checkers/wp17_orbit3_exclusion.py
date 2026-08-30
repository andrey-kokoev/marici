#!/usr/bin/env python3
"""WP17: orbit-3 exclusion — exact inverse solve onto one physical point.

Orbit 3 (canonical support pair (84, 238)) is the WP15 nonviable orbit
whose failure is NOT one of the WP13 structural J == 0 cases: its best
WP15b fit has chi2 ~ 3835, dominated by |Vub| (fit 4.6e-5 vs 3.76e-3,
pull -42 sigma) and beta (0.28 deg vs 22.6 deg, -45 sigma).  Question:
is the exclusion a fitting artifact or does the chart's attainable image
genuinely miss the physical region?

Test: exact inverse solve of both sector halves ((84,238) and (238,84))
onto the FULL physical coordinate p* = (6 singular values, |Vus|, |Vub|,
|Vcb|, signed J) of the WP16a seed point.  10 residuals vs 10 chart
parameters (9 log-magnitudes + phi), so a generic exact preimage is
locally isolated and LM finds it reliably when it exists.  Zero accepted
roots across many randomized starts is strong empirical exclusion; a
certified exclusion would need an analytic boundary statement (tracked
as the open WP17 theorem).

Outputs: research/flavor/results/wp17_orbit3_exclusion.json
"""
import json
import math
import sys

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, "checkers")
import wp7_ensemble as wp7
from wp16a_fiber_degree import physical10

HALVES = [("up84_down238", 84, 238), ("up238_down84", 238, 84)]


def main(n_starts=2000, seed=417):
    pilot = json.load(open("results/wp16a_fiber_degree_pilot.json"))
    p_star = np.array(pilot["p_star"])
    scale = np.abs(p_star)

    rng = np.random.default_rng(seed)
    report = []
    for label, mu, md in HALVES:
        phase_sector, phase_slot = wp7.paper_phase_edge(mu, md)
        us, ds = wp7.mask_slots(mu), wp7.mask_slots(md)

        def resid(theta):
            # LM is unbounded: unattainable targets drive |theta| to
            # overflow, where eigh raises.  Clip to a generous physical
            # box and return a large finite residual on non-finite
            # evaluations so the solve degrades gracefully.
            theta = np.clip(theta, -60.0, 5.0)
            try:
                with np.errstate(all="ignore"):
                    Yu, Yd = wp7.build_texture(mu, md, phase_sector,
                                               phase_slot, theta)
                    v = (physical10(Yu, Yd) - p_star) / scale
            except Exception:
                return np.full(10, 1e6)
            if not np.all(np.isfinite(v)):
                return np.full(10, 1e6)
            return v

        roots = []
        best = None
        for _ in range(n_starts):
            logs = wp7.start_point(us, ds, rng)
            s = np.concatenate([logs, [rng.uniform(-math.pi, math.pi)]])
            try:
                sol = least_squares(resid, s, method="lm",
                                    ftol=1e-15, xtol=1e-15, gtol=1e-15,
                                    max_nfev=2000)
            except Exception:
                continue
            r = resid(sol.x)
            rmax = float(np.max(np.abs(r)))
            if best is None or rmax < best:
                best = rmax
            if rmax < 1e-7:
                th = sol.x
                if not any(np.max(np.abs(q[:9] - th[:9])) < 1e-4
                           and wp7.phi_distance(q[9], th[9]) < 1e-4
                           for q in roots):
                    roots.append(th)
        report.append({"half": label, "member": [mu, md],
                       "n_starts": n_starts,
                       "exact_preimages": len(roots),
                       "best_rel_residual": best,
                       "phis": [round(float(q[9]), 6) for q in roots]})
        best_str = f"{best:.3e}" if best is not None else "n/a"
        print(f"{label} {mu, md}: {len(roots)} exact preimages in "
              f"{n_starts} starts (best rel residual {best_str})",
              flush=True)

    out = {
        "purpose": "WP17: exact inverse solve of orbit 3 (both sector "
                   "halves) onto the WP16a physical point p*; zero "
                   "preimages = empirical chart exclusion",
        "target_source": "results/wp16a_fiber_degree_pilot.json",
        "accept_threshold_rel": 1e-7,
        "halves": report,
        "conclusion": ("empirical exclusion (no exact preimage found)"
                       if all(r["exact_preimages"] == 0 for r in report)
                       else "PREIMAGE FOUND — exclusion claim false"),
        "caveat": ("zero-result from randomized LM starts is not a "
                   "certified exclusion; the analytic boundary theorem "
                   "for orbit 3's attainable image remains open"),
    }
    dest = "results/wp17_orbit3_exclusion.json"
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("->", dest)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    main(n)
