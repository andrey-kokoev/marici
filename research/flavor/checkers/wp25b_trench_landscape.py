"""WP25b: trench landscapes - are the five L levels universal attractors?

WP25a reduced cluster-center selection to the L = a1/(DuDd) level-set
spectrum. The immediate question: does EVERY texture's fixed-phi chi2
landscape trench at the same five phi values (universal attractors, fit
quality selects which are viable), or does each texture trench only at
its realized centers (per-texture accident)?

Method: for 11 representative textures (2 per cluster + the oddball),
sweep the folded phase phi in [0, pi/2] on a 1 deg grid with the phase
CLAMPED and the 9 magnitudes refit (mass-only LM pre-fit, then full
17-observable LM; warm continuation plus one fresh hierarchy-aware
start per grid point). Refine trench bottoms at 0.2 deg. At each bottom
compute J = Im det[Hu,Hd]/(2 Du Dd) and L = J/sin(phi) and compare
bottom phi values to the five WP25a centers.

v2 (results overwritten): v1 underpowered the fits and missed boundary
bottoms; the bug and repair are documented in landscape() below.

v3 (results overwritten): v2 swept the FOLDED phase in [0, pi/2], but
the viable trenches of several classes live at raw phases outside the
first quadrant (e.g. cluster-1 stored raw phi = -42.83 deg and
+110.28 deg, folding to 42.83 and 69.72). Signed unitarity-triangle
angles in the 17-observable target break the fold symmetry, so the
folded-domain sweep cannot reproduce those minima. v3 sweeps the RAW
phase on [-180, 180] deg (periodic bottom detection) and folds only
for reporting.

Reads: results/wp20_valley_audit.json (stored minima as seeds/gates).
Writes: results/wp25b_trench_landscape.json
Run: ../.venv/Scripts/python checkers/wp25b_trench_landscape.py
"""
import json, math, sys
import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, 'checkers')
import wp7_ensemble as wp7

REPS = {
    "0": ["267_302_d02", "267_309_d02"],
    "1": ["266_335_d00", "266_349_d00"],
    "2": ["270_348_d02", "270_369_d00"],
    "3": ["266_303_d00", "266_311_d01"],
    "4": ["267_271_d00", "267_279_d01"],
    "odd": ["311_273_u01"],
}
CENTERS = [23.15067360649863, 43.17287913134288, 46.907137936455435,
           68.38801847180338, 89.57230686320408]

def parse_key(key):
    mu, md, pe = key.split("_")
    return int(mu), int(md), pe[0], (int(pe[1]), int(pe[2]))

def fit_factory(mu, md, ps, slot):
    us, ds = wp7.mask_slots(mu), wp7.mask_slots(md)
    nat = np.array([wp7.natural_value("u", s) for s in us]
                   + [wp7.natural_value("d", s) for s in ds])
    log_nat = np.log(nat)
    lb = log_nat - 6.0 * math.log(10.0)
    ub = log_nat + 3.0 * math.log(10.0)

    def resid(logs, phi):
        theta = np.concatenate([logs, [phi]])
        Yu, Yd = wp7.build_texture(mu, md, ps, slot, theta)
        with np.errstate(all="ignore"):
            obs = wp7.observables17(Yu, Yd)
        obs = np.where(np.isfinite(obs), obs, 1.0e6)
        return (obs - wp7.CENTRAL) / wp7.SIGMA

    def fit_at(phi, t0):
        try:
            s1 = least_squares(lambda t: resid(t, phi)[:6], t0,
                               bounds=(lb, ub), max_nfev=3000)
            s2 = least_squares(lambda t: resid(t, phi), s1.x,
                               bounds=(lb, ub), xtol=1e-12, ftol=1e-12,
                               gtol=1e-12, max_nfev=15000)
            return s2.x, float(2.0 * s2.cost)
        except Exception:
            return None, float("inf")
    return us, ds, fit_at

def jl_at(mu, md, ps, slot, logs, phi):
    theta = np.concatenate([logs, [phi]])
    Yu, Yd = wp7.build_texture(mu, md, ps, slot, theta)
    Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T
    C = Hu @ Hd - Hd @ Hu
    detC = np.linalg.det(C)
    def vand(H):
        ev = np.linalg.eigvalsh(H)
        return abs((ev[0]-ev[1])*(ev[0]-ev[2])*(ev[1]-ev[2]))
    Du, Dd = vand(Hu), vand(Hd)
    J = detC.imag / (2.0 * Du * Dd)
    L = abs(J) / math.sin(phi) if abs(math.sin(phi)) > 1e-12 else float("nan")
    return J, L

def stored_minima_index():
    wp20 = json.load(open("results/wp20_valley_audit.json"))["records"]
    idx = {}
    for r in wp20:
        mu, md = r["member"]; pe = r["phase_edge"]
        key = f"{mu}_{md}_{pe[0]}{pe[1]}{pe[2]}"
        idx.setdefault(key, []).append(r)
    return idx

def landscape(mu, md, ps, slot, stored, seed=7):
    """WP25b v2: seeded-continuation landscape.

    v1 bug (results overwritten): the economy sweep (one fresh
    hierarchy-aware start per grid point + warm continuation from
    phi=0) never entered the viable basin for the diagonal-class
    cluster-1 textures (chi2 >= 175 vs stored 3.4) nor for the
    oddball (chi2 >= 8705 vs stored 3.5), and its endpoint-excluding
    bottom detector missed the near-90-deg cluster-4 trenches.  v2
    seeds every grid point with the texture's own STORED WP20 minimum
    magnitudes (already in the viable basin) plus continuation and one
    fresh start, validates the stored minima as a gate, and admits
    boundary bottoms.
    """
    us, ds, fit_at = fit_factory(mu, md, ps, slot)
    rng = np.random.default_rng(seed)
    recs = stored.get(f"{mu}_{md}_{ps}{slot[0]}{slot[1]}", [])
    seeds = [np.array(r["log_mags"]) for r in recs]
    # validation gate: stored minimum reproduces at its own phi
    gate = []
    for r, s in zip(recs, seeds):
        x, c = fit_at(r["phi_raw"], s)
        gate.append(dict(stored_phi=r["phi_folded_deg"], stored_chi2=r["chi2_stored"],
                         refit_chi2=c, ok=(c < r["chi2_stored"] + 0.5)))
    grid = [math.radians(a) for a in range(-180, 181)]  # v3: RAW phase
    N = len(grid)
    chi2_curve, sol_curve = [None]*N, [None]*N
    # pass 1: seeded at every grid point (stored seeds + fresh)
    for gi, phi in enumerate(grid):
        best_x, best_c = None, float("inf")
        for t0 in seeds + [wp7.start_point(us, ds, rng)]:
            x, c = fit_at(phi, t0)
            if c < best_c:
                best_x, best_c = x, c
        chi2_curve[gi], sol_curve[gi] = best_c, best_x
    # pass 2: continuation refinement around coarse local minima and
    # boundaries; admit boundary bottoms
    def local_min_indices(curve):
        idx = []
        for i in range(N):  # periodic: +/-180 deg is a seam, not an edge
            lo = curve[(i-1) % N]
            hi = curve[(i+1) % N]
            if curve[i] is not None and curve[i] <= lo and curve[i] <= hi and curve[i] < 16.0:
                idx.append(i)
        return idx
    bottoms = []
    for i in local_min_indices(chi2_curve):
        center = float(i - 180)  # grid index -> raw degrees
        warm_r = sol_curve[i]
        best_phi, best_c, best_x = math.radians(center), chi2_curve[i], warm_r
        for da in np.arange(-1.0, 1.0 + 1e-9, 0.2):
            phi_r = math.radians(center + da)
            t0 = warm_r if warm_r is not None else wp7.start_point(us, ds, rng)
            x, c = fit_at(phi_r, t0)
            if c < best_c:
                best_phi, best_c, best_x = phi_r, c, x
        if best_x is not None:
            J, L = jl_at(mu, md, ps, slot, best_x, best_phi)
            fd = math.degrees(wp7.fold_phi(best_phi))
            nc = min(range(5), key=lambda k: abs(fd - CENTERS[k]))
            bottoms.append(dict(phi_deg=fd, phi_raw_deg=math.degrees(best_phi),
                                chi2=best_c, J=J, L=L,
                                sinphi=math.sin(best_phi),
                                nearest_center=nc,
                                center_dev=fd - CENTERS[nc]))
    return chi2_curve, bottoms, gate

def main():
    stored = stored_minima_index()
    out = {"purpose": "WP25b v3 trench landscapes (raw-phase domain): universality of the five L levels",
           "centers": CENTERS,
           "grid": {"domain": "raw phi", "start_deg": -180, "step_deg": 1, "n": 361},
           "textures": {}}
    for ci, keys in REPS.items():
        for key in keys:
            mu, md, ps, slot = parse_key(key)
            curve, bottoms, gate = landscape(mu, md, ps, slot, stored)
            out["textures"][key] = dict(cluster=ci, bottoms=bottoms, gate=gate,
                                        chi2_curve=curve)
            bs = ", ".join(f"raw{b['phi_raw_deg']:.2f}/fold{b['phi_deg']:.2f}(chi2={b['chi2']:.1f})" for b in bottoms)
            g = "; ".join(f"stored {x['stored_phi']:.2f} chi2 {x['stored_chi2']:.2f} -> refit {x['refit_chi2']:.2f} ok={x['ok']}" for x in gate)
            print(f"{key} [{ci}]: {len(bottoms)} bottoms: {bs} | gate: {g}")
    summary = {}
    for k, cen in enumerate(CENTERS):
        viable, trench = [], []
        for key, t in out["textures"].items():
            devs = [(abs(b["phi_deg"] - cen), b["chi2"]) for b in t["bottoms"]]
            near = [c for d, c in devs if d < 0.75]
            if near:
                cmin = min(near)
                if cmin < 4.0:
                    viable.append(key)
                if cmin < 16.0:
                    trench.append(key)
        summary[str(k)] = dict(center=cen, viable_textures=viable,
                               trench_textures=trench)
    out["universality"] = summary
    json.dump(out, open("results/wp25b_trench_landscape.json", "w"), indent=1)
    print(json.dumps({k: dict(center=round(v["center"], 2),
                              n_viable=len(v["viable_textures"]),
                              n_trench=len(v["trench_textures"]))
                      for k, v in summary.items()}, indent=1))
    print("-> results/wp25b_trench_landscape.json")

if __name__ == "__main__":
    main()
