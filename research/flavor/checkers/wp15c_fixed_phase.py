#!/usr/bin/env python3
"""WP15c -- App-V.b fixed-phase ensemble reproduction.

Pin the loop phase at |phi| in {pi/8, 3pi/8, pi/2} (both signs; the paper
identifies +-phi and pi+-phi), 9 free magnitudes, same 17-observable chi2
and 3-sigma viability as App. V.a.

Scan strategy: one canonical member per S3^3 orbit suffices, because the
attainable set of fits (modulo S3^3) is permutation-invariant across the
orbit.  The 36 orbits = 18 census exchange-orbits x two sector identifications
(canonical + swapped).

Paper targets (App. V.b):
    1412 viable fits (density-dependent, not a target)
    permutation classes:  pi/2: 29,  pi/8: 35,  3pi/8: 35   (= 99)
    rotation classes:     pi/2:  9,  pi/8: 10,  3pi/8: 13   (= 32)
Rotation mod-out rule: fits converging to the same minimum to ~10
significant figures in chi2 are identified.

Outputs results/wp15c_fixed_phase.json.
"""

import importlib.util
import itertools
import json
import math
import sys
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("wp15d", HERE / "wp15d_sensitivity.py")
w15d = importlib.util.module_from_spec(spec)
sys.modules["wp15d"] = w15d
spec.loader.exec_module(w15d)
wp7 = w15d.wp7

PHI_MAGS = [math.pi / 8.0, 3.0 * math.pi / 8.0, math.pi / 2.0]
# Paper App. V.b pins phi at {+-pi/8, +-3pi/8, +-pi/2, +-5pi/8, +-7pi/8}
# and folds +-phi, pi+-phi into the three labels pi/8, 3pi/8, pi/2.
PHI_PINS = [s * m for m in PHI_MAGS[:2] for s in (+1.0, -1.0)]
PHI_PINS += [s * (math.pi - m) for m in PHI_MAGS[:2] for s in (+1.0, -1.0)]
PHI_PINS += [math.pi / 2.0, -math.pi / 2.0]
N_STARTS = 128


def canonical_s3(mu, md):
    """Orbit canonical form under S3^3 only (no sector exchange)."""
    import orbit_census as oc
    best = None
    for pq in itertools.permutations(range(3)):
        for pu in itertools.permutations(range(3)):
            for pd in itertools.permutations(range(3)):
                c = oc.permute(mu, md, pq, pu, pd)
                if best is None or c < best:
                    best = c
    return best


def orbit_representatives(variant=0):
    """36 S3^3-orbit representatives: census canonical + swap.  variant=0
    uses the S3^3-canonical member; variant=k>0 uses the k-th other
    member of the same orbit (hierarchy-aware starts are not
    permutation-invariant, so member diversity widens basin coverage)."""
    cen = json.load(open(HERE.parent / "results" / "orbit_census.json"))
    reps = []
    seen = set()
    for o in cen["orbits"]:
        for mu, md, sw in ((o["mask_u"], o["mask_d"], False),
                           (o["mask_d"], o["mask_u"], True)):
            cm = canonical_s3(mu, md)
            if cm in seen:
                continue
            seen.add(cm)
            if variant > 0:
                mems = [m for m in wp7.orbit_members(*cm) if m != cm]
                mu2, md2 = sorted(mems)[(variant - 1) % len(mems)]
                reps.append({"orbit_index": o["orbit_index"], "swap": sw,
                             "variant": variant,
                             "mask_u": mu2, "mask_d": md2})
            else:
                reps.append({"orbit_index": o["orbit_index"], "swap": sw,
                             "variant": 0,
                             "mask_u": cm[0], "mask_d": cm[1]})
    return reps


def load_free_minima():
    """All free-phase viable minima from the dense scan + WP7 ensemble,
    grouped by S3^3-only canonical member."""
    import glob
    groups = defaultdict(list)
    def add(member, log_mags, phi):
        groups[canonical_s3(*member)].append(
            {"member": tuple(member), "log_mags": log_mags, "phi": phi})
    for path in sorted(glob.glob(str(HERE.parent / "results" / "wp15b_dense_orbit*.json"))):
        d = json.load(open(path))
        for half in d["s3_orbits"]:
            for m in half["member_results"]:
                for v in m["viable_minima"]:
                    add(v["member"], v["log_mags"], v["phi"])
    d7 = json.load(open(HERE.parent / "results" / "wp7_ensemble.json"))
    for o in d7["orbits"]:
        for m in o.get("viable_minima", []):
            add(m["member"], m["log_mags"], m["phi"])
    return groups


def transport(log_mags, src_member, dst_member):
    """Express a fit's magnitudes on a permutation-equivalent member.
    Returns log-mags in dst (u-slots, d-slots) order, or None if the
    members are not S3^3-related."""
    import orbit_census as oc
    mu, md = src_member
    ru, rd = dst_member
    us = [s for k, s in enumerate(oc.SLOTS) if mu & (1 << k)]
    ds = [s for k, s in enumerate(oc.SLOTS) if md & (1 << k)]
    mag = {}
    for (sec, slots), off in ((("u", us), 0), (("d", ds), len(us))):
        for s, lm in zip(slots, log_mags[off:] if off else log_mags):
            mag[(sec, s)] = lm
    rus = [s for k, s in enumerate(oc.SLOTS) if ru & (1 << k)]
    rds = [s for k, s in enumerate(oc.SLOTS) if rd & (1 << k)]
    for pq in itertools.permutations(range(3)):
        for pu in itertools.permutations(range(3)):
            for pd in itertools.permutations(range(3)):
                if oc.permute(mu, md, pq, pu, pd) != (ru, rd):
                    continue
                ipq = [pq.index(i) for i in range(3)]
                ipu = [pu.index(i) for i in range(3)]
                ipd = [pd.index(i) for i in range(3)]
                out = []
                for sec, slots in (("u", rus), ("d", rds)):
                    for (i, j) in slots:
                        j2 = ipu[j] if sec == "u" else ipd[j]
                        out.append(mag[(sec, (ipq[i], j2))])
                return out
    return None


def fit_orbit(rep, seed_groups):
    """All deduplicated viable minima for one orbit representative at each
    of the paper's ten pinned phase values {+-pi/8, +-3pi/8, +-pi/2,
    +-5pi/8, +-7pi/8} (folded labels pi/8, 3pi/8, pi/2).  Starts:
    hierarchy-aware random plus transported free-phase minima from the
    same S3^3 orbit whose folded phase lies in the folded target window."""
    mu, md = rep["mask_u"], rep["mask_d"]
    pe = wp7.paper_phase_edge(mu, md)
    seeds = seed_groups.get(canonical_s3(mu, md), [])
    us, ds = wp7.mask_slots(mu), wp7.mask_slots(md)
    nat = np.array([wp7.natural_value("u", s) for s in us]
                   + [wp7.natural_value("d", s) for s in ds])
    log_nat = np.log(nat)
    lb = log_nat - 6.0 * math.log(10.0)
    ub = log_nat + 3.0 * math.log(10.0)

    from scipy.optimize import least_squares

    out = []
    for pin in PHI_PINS:
        pmag = wp7.fold_phi(pin)
        minima = []
        # transported seeds for this folded phase window
        seed_starts = []
        half_w = math.pi / 8.0 + 1e-9
        for c in seeds:
            if abs(wp7.fold_phi(c["phi"]) - pmag) > half_w:
                continue
            t = transport(c["log_mags"], c["member"], (mu, md))
            if t is not None:
                seed_starts.append(t)
        rng = np.random.default_rng(1234)
        phi = pin

        def resid(logm):
            theta = np.concatenate([logm, [phi]])
            Yu, Yd = wp7.build_texture(mu, md, pe[0], tuple(pe[1]), theta)
            with np.errstate(all="ignore"):
                obs = wp7.observables17(Yu, Yd)
            obs = np.where(np.isfinite(obs), obs, 1.0e6)
            return (obs - wp7.CENTRAL) / wp7.SIGMA

        starts = [np.clip(np.array(s, dtype=float), lb, ub)
                  for s in seed_starts]
        starts += [np.clip(np.array(wp7.start_point(us, ds, rng),
                                    dtype=float), lb, ub)
                   for _ in range(N_STARTS)]
        for t0 in starts:
            try:
                s1 = least_squares(lambda t: resid(t)[:6], t0, bounds=(lb, ub),
                                   max_nfev=8000)
                if 2.0 * s1.cost > 25.0:
                    continue
                s2 = least_squares(resid, s1.x, bounds=(lb, ub), method="trf",
                                   xtol=1e-12, ftol=1e-12, gtol=1e-12,
                                   max_nfev=50000)
            except Exception:
                continue
            chi2 = float(2.0 * s2.cost)
            if chi2 > wp7.CHI2_3SIGMA_7DOF:
                continue
            lm = [float(v) for v in s2.x]
            if not any(max(abs(a - b) for a, b in zip(lm, m["log_mags"])) < 1e-3
                       for m in minima):
                minima.append({"phi": phi, "chi2": chi2, "log_mags": lm})
        out.append({"phi_pin": pin, "phi_mag": pmag, "minima": minima,
                    "n_seeds": len(seed_starts)})
    return {"rep": rep, "phase_edge": pe, "fits": out}


def entries_vec(mu, md, log_mags):
    """Entry magnitudes as a slot-indexed dict {'u_ij': ..., 'd_ij': ...}."""
    us, ds = wp7.mask_slots(mu), wp7.mask_slots(md)
    mags = np.exp(log_mags)
    v = {}
    for (sector, slots), off in ((("u", us), 0), (("d", ds), len(us))):
        for s, m in zip(slots, mags[off:] if off else mags):
            v[f"{sector}{s[0]}{s[1]}"] = float(m)
    return v


def main():
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    variant = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    suffix = "" if variant == 0 else f"_v{variant}"
    reps = orbit_representatives(variant=variant)
    seed_groups = load_free_minima()
    print(f"{len(reps)} S3^3-orbit representatives (variant {variant}), "
          f"{sum(len(v) for v in seed_groups.values())} free-phase seed minima")
    results = []
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for i, r in enumerate(ex.map(fit_orbit, reps, [seed_groups] * len(reps))):
            n = sum(len(f["minima"]) for f in r["fits"])
            print(f"rep {i}: orbit {r['rep']['orbit_index']} swap={r['rep']['swap']} "
                  f"({r['rep']['mask_u']},{r['rep']['mask_d']}) -> {n} viable minima",
                  flush=True)
            results.append(r)
    dest = HERE.parent / "results" / f"wp15c_fixed_phase{suffix}.json"
    dest.write_text(json.dumps({"phi_mags": PHI_MAGS, "phi_pins": PHI_PINS,
                                "variant": variant, "results": results}, indent=1))
    print("->", dest)


if __name__ == "__main__":
    main()
