"""Direct full-objective audit for the suspicious WP7 orbit 3.

Bypasses wp7_ensemble.fit_member's mass-only prefit, which may collapse the
large mass fiber onto one CP-poor basin before CKM observables are introduced.
No claim is made from one run; use independent seeds and labelings.
"""
import argparse
import json
import math
import sys

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, "research/flavor/checkers")
import wp7_ensemble as w


def run(mu, md, starts, seed):
    psec, pslot = w.paper_phase_edge(mu, md)
    us, ds = w.mask_slots(mu), w.mask_slots(md)
    nat = np.array([w.natural_value("u", s) for s in us]
                   + [w.natural_value("d", s) for s in ds])
    log_nat = np.log(nat)
    lb = np.concatenate([log_nat - 6 * math.log(10), [-math.pi]])
    ub = np.concatenate([log_nat + 3 * math.log(10), [math.pi]])
    rng = np.random.default_rng(seed)

    def resid(theta):
        yu, yd = w.build_texture(mu, md, psec, pslot, theta)
        with np.errstate(all="ignore"):
            obs = w.observables17(yu, yd)
        obs = np.where(np.isfinite(obs), obs, 1e6)
        return (obs - w.CENTRAL) / w.SIGMA

    best = None
    for k in range(starts):
        t0 = np.concatenate([w.start_point(us, ds, rng),
                             [rng.uniform(-math.pi, math.pi)]])
        t0 = np.clip(t0, lb, ub)
        fit = least_squares(resid, t0, bounds=(lb, ub), method="trf",
                            xtol=1e-11, ftol=1e-11, gtol=1e-11,
                            max_nfev=60000)
        chi2 = float(2 * fit.cost)
        if best is None or chi2 < best["chi2"]:
            best = {"chi2": chi2, "phi": float(fit.x[9]),
                    "log_mags": [float(x) for x in fit.x[:9]],
                    "nfev": int(fit.nfev)}
    return {"member": [mu, md], "phase_edge": [psec, *pslot],
            "starts": starts, "seed": seed, "best": best}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mu", type=int, default=84)
    ap.add_argument("--md", type=int, default=238)
    ap.add_argument("--starts", type=int, default=64)
    ap.add_argument("--seed", type=int, required=True)
    ns = ap.parse_args()
    print(json.dumps(run(ns.mu, ns.md, ns.starts, ns.seed), indent=2))
