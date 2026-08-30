#!/usr/bin/env python3
"""WP16b-stab: fiber-degree stabilization under increased start density.

WP16a (500 starts on the seed member (281,395)) found degree 1; WP16b
(100 starts on the orbit-15 canonical representative (85,234)) found
degree 2, verified genuine.  Image sets and fiber cardinalities are
orbit-invariant, so the discrepancy is pure sampling.  This checker
re-runs every covering representative plus the seed member at much
higher start density to stabilize the degree lower bounds.

Outputs: research/flavor/results/wp16b_fiber_stability.json
"""
import json
import math
import sys

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, "checkers")
import wp7_ensemble as wp7
from wp16a_fiber_degree import physical10


def solve_fiber(mu, md, p_star, scale, n_starts, rng):
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
            sol = least_squares(resid, s, method="lm", ftol=1e-15,
                                xtol=1e-15, gtol=1e-15, max_nfev=2000)
        except Exception:
            continue
        rmax = float(np.max(np.abs(resid(sol.x))))
        if rmax < 1e-7:
            th = sol.x
            if not any(np.max(np.abs(q[:9] - th[:9])) < 1e-4
                       and wp7.phi_distance(q[9], th[9]) < 1e-4
                       for q in roots):
                roots.append(th)
    return roots


DEST = "results/wp16b_fiber_stability.json"


def write_partial(rows, seed_row, n_starts):
    out = {"purpose": "WP16b degree stabilization: higher start density "
                      "on all covering representatives + the WP16a seed",
           "n_starts_per_rep": n_starts,
           "accept_threshold_rel": 1e-7,
           "note": "degrees are rigorous lower bounds; exact degrees "
                   "require polynomial homotopy methods",
           "covering_representatives": rows,
           "seed_member": seed_row}
    with open(DEST, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)


def main(n_starts=1500, seed_starts=2000, seed=31337):
    pilot = json.load(open("results/wp16a_fiber_degree_pilot.json"))
    p_star = np.array(pilot["p_star"])
    scale = np.abs(p_star)
    prev = json.load(open("results/wp16b_atlas_fiber.json"))

    # Resume: keep rows already computed by a killed earlier run.
    out_rows, seed_row = [], None
    try:
        old = json.load(open(DEST))
        if old.get("n_starts_per_rep") == n_starts:
            out_rows = old.get("covering_representatives") or []
            seed_row = old.get("seed_member")
            if seed_row and seed_row.get("starts") != seed_starts:
                seed_row = None
    except (OSError, json.JSONDecodeError):
        pass
    done = {(r["orbit_index"], r["swap"]) for r in out_rows}

    rng = np.random.default_rng(seed)
    covering = [a for a in prev["atlas"] if a["fiber_degree"] > 0]
    for k, a in enumerate(covering):
        if (a["orbit_index"], a["swap"]) in done:
            print(f"{k+1}/{len(covering)} orbit {a['orbit_index']} "
                  f"swap={a['swap']}: resumed, skipping", flush=True)
            continue
        mu, md = a["member"]
        roots = solve_fiber(mu, md, p_star, scale, n_starts, rng)
        out_rows.append({"orbit_index": a["orbit_index"], "swap": a["swap"],
                         "member": [mu, md],
                         "degree_100": a["fiber_degree"],
                         f"degree_{n_starts}": len(roots),
                         "phis_mod_2pi": sorted(
                             round(float((q[9] + math.pi)
                                         % (2 * math.pi) - math.pi), 6)
                             for q in roots)})
        write_partial(out_rows, seed_row, n_starts)
        print(f"{k+1}/{len(covering)} orbit {a['orbit_index']} "
              f"swap={a['swap']}: {a['fiber_degree']} -> {len(roots)}",
              flush=True)

    # The WP16a seed member, at even higher density.
    if seed_row is None:
        mu, md = pilot["seed_fit"]["member"]
        roots = solve_fiber(mu, md, p_star, scale, seed_starts, rng)
        seed_row = {"member": [mu, md], "starts": seed_starts,
                    "degree": len(roots),
                    "phis_mod_2pi": sorted(
                        round(float((q[9] + math.pi) % (2 * math.pi)
                                    - math.pi), 6) for q in roots)}
        write_partial(out_rows, seed_row, n_starts)
        print(f"seed member {seed_row['member']}: degree {len(roots)} "
              f"(WP16a found 1 with 500)", flush=True)
    else:
        print(f"seed member {seed_row['member']}: resumed, degree "
              f"{seed_row['degree']}", flush=True)

    write_partial(out_rows, seed_row, n_starts)
    print("->", DEST)


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    main(n)
