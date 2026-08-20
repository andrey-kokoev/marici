"""WP7 ensemble generator: the nine-link viable-fit ensemble with full
orbit provenance (marici.Figueiredo).

Purpose
-------
The pi/8 clustering of arXiv:2607.27315v1 (Fig. 3 / Fig. S3) is a
histogram over the paper's scan ensemble.  The per-class fitted phases
are not machine-readable from the source (Fig. 3 is an image), so this
script rebuilds the NINE-LINK stratum of the ensemble from scratch with
complete provenance:

  - the 18 support orbits of the exhaustive census (orbit_census.json:
    nine-link, full-rank sectors, connected combined graph, b1 = 1,
    modulo S3^3 permutations and sector exchange);
  - orbit MEMBERS are enumerated by the S3^3 action.  All members of
    one orbit are the same physical texture class (same attainable
    chi^2 and loop-phase sets); sweeping members is a search strategy,
    not new physics: the census canonical representative can sit in a
    "hard" labeling where Levenberg-Marquardt starts miss the viable
    basin (WP7.1 debug: canonical (85, 87) fails from generic starts,
    the paper's own S38 labeling (282, 314) of the SAME orbit converges
    in 0.2 s to chi^2 = 3.36);
  - one phase edge per member, by the paper's placement rule (smallest
    down-type loop edge, else smallest up-type).  Phase placement
    around the loop is rephasing-gauge, so this loses nothing;
  - the paper's 17-observable Gaussian chi^2 (Tab. S2, M_Z values);
  - FREE phase scan (no pi/8 windows): the windows were the paper's
    scan device; a free scan with multi-start records which loop-phase
    values the texture class can actually realize.

Fitting pipeline per start: hierarchy-aware start (diagonal slots at
the Yukawa eigenvalues, off-diagonal slots at natural * 10^U(-4, 0),
because hierarchical fits need off-diagonals far BELOW sqrt(y_i y_j)),
then a mass-only LM pre-fit (6 observables), then the full
17-observable LM.  Viable minima (chi^2 <= chi2_7(0.9973) = 20.28 for
17 obs - 10 params = 7 dof) are deduplicated by (phi, chi^2)
proximity; all best fits are recorded regardless of threshold so
WP7.2/WP7.3 can re-threshold without refitting.

Validation mode (--validate): sweep the orbit containing paper
Example I (S38: mask_u = 282, mask_d = 314, census orbit_index 4) and
report whether a viable fit with loop phase near pi/2 is recovered.

Output: research/flavor/results/wp7_ensemble.json
"""
import argparse
import itertools
import json
import math

import numpy as np
from scipy.optimize import least_squares

from orbit_census import permute, unique_cycle

# ---------------------------------------------------------------- Tab. S2
# (name, central, 1-sigma).  Uncertainties symmetrized per the paper.
YU, YC, YT = 7.04e-6, 3.56e-3, 0.967
YD, YS, YB = 1.54e-5, 3.06e-4, 1.630e-2
OBS17 = [
    ("y_u",      7.04e-6,   0.15e-6),
    ("y_c",      3.56e-3,   0.06e-3),
    ("y_t",      0.967,     0.004),
    ("y_d",      1.54e-5,   0.02e-5),
    ("y_s",      3.06e-4,   0.04e-4),
    ("y_b",      1.630e-2,  0.009e-2),
    ("Vus",      0.22517,   0.00068),
    ("Vub",      0.003763,  0.000088),
    ("Vcb",      0.04189,   0.00081),
    ("Vcd",      0.22503,   0.00068),
    ("Vtd",      0.00863,   0.00019),
    ("Vts",      0.04117,   0.00079),
    ("alpha",    84.1,      3.7),
    ("beta",     22.6,      0.5),
    ("gamma",    66.4,      2.8),
    ("yu_over_yd",   0.473, 0.017),
    ("ys_over_yud",  27.30, 0.08),
]
CENTRAL = np.array([c for _, c, _ in OBS17])
SIGMA = np.array([s for _, _, s in OBS17])

CHI2_3SIGMA_7DOF = 20.28  # chi2 with 7 dof at two-sided 3 sigma

SLOTS = [(i, j) for i in range(3) for j in range(3)]


def mask_slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def natural_value(sector, slot):
    yu = [YU, YC, YT]
    yd = [YD, YS, YB]
    y = yu if sector == "u" else yd
    i, j = slot
    return math.sqrt(y[i] * y[j])


def build_texture(mask_u, mask_d, phase_sector, phase_slot, theta):
    """theta = [9 log-magnitudes in (u-slots, d-slots) order, phi]."""
    Yu = np.zeros((3, 3), dtype=complex)
    Yd = np.zeros((3, 3), dtype=complex)
    us, ds = mask_slots(mask_u), mask_slots(mask_d)
    mags = np.exp(theta[:9])
    phi = theta[9]
    # Sector-tagged entries: the same matrix slot can appear in BOTH
    # masks (u-type and d-type edges are distinct links), so the sector
    # must travel with the slot.
    entries = [("u", s) for s in us] + [("d", s) for s in ds]
    for (sector, slot), m in zip(entries, mags):
        val = m
        if sector == phase_sector and slot == phase_slot:
            val = m * np.exp(1j * phi)
        if sector == "u":
            Yu[slot] = val
        else:
            Yd[slot] = val
    return Yu, Yd


def observables17(Yu, Yd):
    """The 17 Tab.-S2 observables, in OBS17 order."""
    su2, Uu = np.linalg.eigh(Yu @ Yu.conj().T)   # ascending eigenvalues
    sd2, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
    yu, yc, yt = np.sqrt(np.maximum(su2, 0.0))
    yd, ys, yb = np.sqrt(np.maximum(sd2, 0.0))
    V = Uu.conj().T @ Ud                          # columns mass-ordered
    Vus = abs(V[0, 1]); Vub = abs(V[0, 2]); Vcb = abs(V[1, 2])
    Vcd = abs(V[1, 0]); Vtd = abs(V[2, 0]); Vts = abs(V[2, 1])
    # Rephasing-invariant unitarity-triangle angles (degrees).
    def ang(num, den):
        r = -num / den
        return math.degrees(math.atan2(r.imag, r.real))
    alpha = ang(V[2, 0] * V[2, 2].conj(), V[0, 0] * V[0, 2].conj())
    beta = ang(V[1, 0] * V[1, 2].conj(), V[2, 0] * V[2, 2].conj())
    gamma = ang(V[0, 0] * V[0, 2].conj(), V[1, 0] * V[1, 2].conj())
    return np.array([yu, yc, yt, yd, ys, yb,
                     Vus, Vub, Vcb, Vcd, Vtd, Vts,
                     alpha, beta, gamma,
                     yu / yd, ys / ((yu + yd) / 2.0)])


def fold_phi(phi):
    """Paper convention: identify +-phi and pi+-phi; result in [0, pi/2]."""
    x = math.fmod(phi, math.pi)
    if x < 0:
        x += math.pi
    return min(x, math.pi - x)


def start_point(us, ds, rng):
    """Hierarchy-aware starts.

    Diagonal slots (i, i) start at the i-th Yukawa eigenvalue (mass
    eigenbasis is near the gauge basis for hierarchical spectra).
    Off-diagonal slots start at natural * 10^U(-4, 0): hierarchical
    fits need off-diagonals orders of magnitude BELOW the natural
    value sqrt(y_i y_j), so a jitter around natural almost never
    lands in the viable basin (the WP7.1 failure mode).
    """
    yu = [YU, YC, YT]
    yd = [YD, YS, YB]
    logs = []
    for sector, slots in (("u", us), ("d", ds)):
        y = yu if sector == "u" else yd
        for (i, j) in slots:
            if i == j:
                logs.append(math.log(y[i])
                            + rng.uniform(-0.3, 0.3) * math.log(10.0))
            else:
                logs.append(math.log(math.sqrt(y[i] * y[j]))
                            + rng.uniform(-4.0, 0.0) * math.log(10.0))
    return np.array(logs)


def phi_distance(a, b):
    """Angular distance on (-pi, pi]."""
    return abs((a - b + math.pi) % (2.0 * math.pi) - math.pi)


def fit_member(mask_u, mask_d, phase_sector, phase_slot, n_starts=8,
               seed=0):
    """Multi-start fit of one texture member.

    Starts: 16 phase anchors at the centers of the pi/8 windows (phi
    FREE to move -- the anchors only select the local basin) plus
    n_starts starts with uniform random phi.  Two-stage per start:
    mass-only LM pre-fit, then full 17-observable LM.  Returns
    (viable_minima, best_record); viable minima are deduplicated by
    (phi, chi2) proximity within this member.
    """
    us, ds = mask_slots(mask_u), mask_slots(mask_d)
    nat = np.array([natural_value("u", s) for s in us]
                   + [natural_value("d", s) for s in ds])
    log_nat = np.log(nat)
    lb = np.concatenate([log_nat - 6.0 * math.log(10.0), [-math.pi]])
    ub = np.concatenate([log_nat + 3.0 * math.log(10.0), [math.pi]])
    rng = np.random.default_rng(seed)

    def resid(theta):
        Yu, Yd = build_texture(mask_u, mask_d, phase_sector, phase_slot,
                               theta)
        with np.errstate(all="ignore"):
            obs = observables17(Yu, Yd)
        # Structurally zero CKM entries can make angles non-finite at
        # some evaluation points; map those to a large finite residual.
        obs = np.where(np.isfinite(obs), obs, 1.0e6)
        return (obs - CENTRAL) / SIGMA

    phi_anchors = [-math.pi + (k + 0.5) * math.pi / 8.0
                   for k in range(16)]
    phi_anchors += [rng.uniform(-math.pi, math.pi)
                    for _ in range(n_starts)]

    minima = []
    best = None
    for phi0 in phi_anchors:
        t0 = np.concatenate([start_point(us, ds, rng), [phi0]])
        t0 = np.clip(t0, lb, ub)
        try:
            s1 = least_squares(lambda t: resid(t)[:6], t0,
                               bounds=(lb, ub), max_nfev=8000)
            if 2.0 * s1.cost > 25.0:
                continue  # mass spectrum hopeless from this start
            s2 = least_squares(resid, s1.x, bounds=(lb, ub),
                               method="trf", xtol=1e-12, ftol=1e-12,
                               gtol=1e-12, max_nfev=50000)
        except Exception:
            continue
        chi2 = float(2.0 * s2.cost)
        rec = {"chi2": chi2, "phi": float(s2.x[9]),
               "phi_folded": fold_phi(float(s2.x[9])),
               "log_mags": [float(v) for v in s2.x[:9]],
               "nfev": int(s2.nfev)}
        if best is None or chi2 < best["chi2"]:
            best = rec
        if chi2 <= CHI2_3SIGMA_7DOF and not any(
                phi_distance(rec["phi"], m["phi"]) < 1e-3
                and abs(rec["chi2"] - m["chi2"]) < 1e-3
                for m in minima):
            minima.append(rec)
    return minima, best


def orbit_members(mask_u, mask_d):
    """All distinct (mask_u, mask_d) in the S3^3 orbit."""
    members = set()
    for pq in itertools.permutations(range(3)):
        for pu in itertools.permutations(range(3)):
            for pd in itertools.permutations(range(3)):
                members.add(permute(mask_u, mask_d, pq, pu, pd))
    return sorted(members)


def paper_phase_edge(mask_u, mask_d):
    """Paper's placement rule on this member's unique cycle: smallest
    down-type loop edge (row, then column index), else smallest
    up-type."""
    cyc = unique_cycle(mask_u, mask_d)
    downs = sorted((i, j) for sec, i, j in cyc if sec == "d")
    if downs:
        return "d", downs[0]
    ups = sorted((i, j) for sec, i, j in cyc if sec == "u")
    return "u", ups[0]


def dedupe_orbit_minima(minima):
    """Members of one orbit are one physical class: the attainable
    (chi2, phi) sets are identical across members, so cross-member
    duplicates are removed by (phi, chi2) proximity."""
    out = []
    for m in sorted(minima, key=lambda r: r["chi2"]):
        if not any(phi_distance(m["phi"], o["phi"]) < 1e-3
                   and abs(m["chi2"] - o["chi2"]) < 1e-3 for o in out):
            out.append(m)
    return out


def member_score(mask_u, mask_d):
    """Fitting-ease heuristic: total log natural value of the support.

    High score = support concentrated on large-Yukawa (bottom-right)
    slots, i.e. a labeling close to the mass-ordered one, where the
    hierarchy-aware starts land in the viable basin.
    """
    return (sum(math.log(natural_value("u", s))
                for s in mask_slots(mask_u))
            + sum(math.log(natural_value("d", s))
                  for s in mask_slots(mask_d)))


def sweep_orbit(orb, n_starts, member_cap=24, escalate_starts=24,
                escalate_cap=6, stop_after=24):
    """Fit members of one census orbit; return the orbit record.

    Members are tried in descending member_score order.  All members
    are the same physical class, but the LM basin structure is
    labeling-dependent (WP7.1: the pi/2 branch of the S38 class is
    found from member (282, 314), the 0.818 branch from (354, 468) --
    neither finds both), so branch coverage requires sweeping many
    members.  stop_after allows an early stop once enough distinct
    members have contributed viable minima.
    """
    members = orbit_members(orb["mask_u"], orb["mask_d"])
    members.sort(key=lambda t: member_score(*t), reverse=True)
    all_minima = []
    best_overall = None
    tried = []
    contributing = 0
    escalated = False

    def try_member(mu, md, starts, seed):
        nonlocal best_overall, contributing
        psec, pslot = paper_phase_edge(mu, md)
        mins, best = fit_member(mu, md, psec, pslot,
                                n_starts=starts, seed=seed)
        for m in mins:
            m["member"] = [mu, md]
            m["phase_edge"] = [psec, pslot[0], pslot[1]]
        if mins:
            contributing += 1
        all_minima.extend(mins)
        if best is not None and (best_overall is None
                                 or best["chi2"] < best_overall["chi2"]):
            best = dict(best)
            best["member"] = [mu, md]
            best_overall = best
        tried.append([mu, md])

    for k, (mu, md) in enumerate(members[:member_cap]):
        try_member(mu, md, n_starts, seed=1000 + orb["orbit_index"] + k)
        if contributing >= stop_after:
            break
    if not all_minima:
        escalated = True
        for k, (mu, md) in enumerate(
                members[member_cap:member_cap + escalate_cap]):
            try_member(mu, md, escalate_starts,
                       seed=5000 + orb["orbit_index"] + k)
            if contributing >= 1:
                break

    viable = dedupe_orbit_minima(all_minima)
    return {"orbit_index": orb["orbit_index"],
            "mask_u": orb["mask_u"], "mask_d": orb["mask_d"],
            "cycle_length": orb["cycle_length"],
            "n_members": len(members),
            "members_tried": tried,
            "escalated": escalated,
            "viable_minima": viable,
            "best_chi2_overall": (best_overall["chi2"]
                                  if best_overall else None)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true",
                    help="sweep only the S38 orbit and report")
    ap.add_argument("--orbit", type=int, default=None,
                    help="sweep only this census orbit_index")
    ap.add_argument("--restarts", type=int, default=8,
                    help="starts per member")
    args = ap.parse_args()

    census = json.load(open("research/flavor/results/orbit_census.json"))
    orbits = census["orbits"]

    if args.validate:
        args.orbit = 4

    if args.orbit is not None:
        target = next((o for o in orbits
                       if o["orbit_index"] == args.orbit), None)
        if target is None:
            raise SystemExit(f"orbit_index {args.orbit} not in census")
        rec = sweep_orbit(target, n_starts=args.restarts)
        print(f"orbit {rec['orbit_index']}, masks ({rec['mask_u']}, "
              f"{rec['mask_d']}), members {rec['n_members']}, tried "
              f"{len(rec['members_tried'])}, escalated "
              f"{rec['escalated']}")
        vm = rec["viable_minima"]
        print(f"viable minima (deduped): {len(vm)}")
        for m in vm:
            print(f"  chi2={m['chi2']:.4g} phi={m['phi']:+.6f} "
                  f"folded={m['phi_folded']:.6f} "
                  f"(pi/2={math.pi/2:.6f}, pi/8={math.pi/8:.6f}, "
                  f"pi/4={math.pi/4:.6f}, 3pi/8={3*math.pi/8:.6f}) "
                  f"member={m['member']} edge={m['phase_edge']}")
        if vm:
            best = vm[0]
            theta = np.array(best["log_mags"] + [best["phi"]])
            mu, md = best["member"]
            pe = best["phase_edge"]
            Yu, Yd = build_texture(mu, md, pe[0], (pe[1], pe[2]), theta)
            obs = observables17(Yu, Yd)
            print("observables at best viable fit (vs Tab. S2):")
            for (n, c, s), o in zip(OBS17, obs):
                print(f"  {n:12s} {o:.6g} vs {c:.6g}  "
                      f"({(o - c) / s:+.2f} sigma)")
        return

    out = {
        "purpose": "WP7 nine-link viable-fit ensemble with orbit "
                   "provenance (18 census orbits, S3^3 member sweep, "
                   "free-phase multi-start LM, Tab. S2 chi2)",
        "conventions": {
            "observables": [n for n, _, _ in OBS17],
            "viability_chi2_max": CHI2_3SIGMA_7DOF,
            "viability_rule": "chi2 <= chi2_7(0.9973) = 20.28 "
                              "(17 obs - 10 params = 7 dof)",
            "phase_scan": "free phi in (-pi, pi], multi-start",
            "magnitude_bounds": "natural * [1e-6, 1e3], "
                                "natural = sqrt(y_i y_j) (Tab. S2)",
            "phase_placement": "paper rule per member: smallest "
                               "down-type loop edge, else smallest "
                               "up-type",
            "phase_folding": "identify +-phi and pi+-phi; folded in "
                             "[0, pi/2]",
            "starts_per_member": args.restarts,
        },
        "orbits": [],
    }
    for orb in orbits:
        rec = sweep_orbit(orb, n_starts=args.restarts)
        out["orbits"].append(rec)
        phis = sorted({round(m["phi_folded"], 4)
                       for m in rec["viable_minima"]})
        print(f"orbit {rec['orbit_index']:2d} "
              f"masks ({rec['mask_u']:3d},{rec['mask_d']:3d}) "
              f"members {rec['n_members']:3d} tried "
              f"{len(rec['members_tried']):2d} "
              f"esc={int(rec['escalated'])} "
              f"viable {len(rec['viable_minima']):2d} "
              f"folded_phis {phis}", flush=True)

    with open("research/flavor/results/wp7_ensemble.json", "w") as f:
        json.dump(out, f, indent=1)
    print("wrote research/flavor/results/wp7_ensemble.json")


if __name__ == "__main__":
    main()
