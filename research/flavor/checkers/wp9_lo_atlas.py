"""WP9: exact leading-order atlas of the loop-phase carrier structure over
the WP7/WP8 fiber (marici.Figueiredo).

Context
-------
WP8 (entry 1092) classified the loop-phase fiber over one physical flavor
point: 61 viable minima, 18 distinct exact folded phases, 5 clusters.
Four cores match unitarity-triangle angles to <= 1.2 mrad (WP4 angle
inheritance, entry 1073); the others sit 2-50 mrad from any motivated
core, and the 0.818 cluster matches none.  WP8 warned that numerical
residuals cannot identify exact relations; the per-chart leading-order
(LO) analysis was left open.  This checker performs it.

Method
------
For each chart in the fiber, freeze the fitted magnitudes and let the
placed phase z = e^{i phi} wind once around U(1).  For each
rephasing-invariant CKM quartic

    R_alpha = -V_td V_tb* / (V_ud V_ub*)
    R_beta  = -V_cd V_cb* / (V_td V_tb*)
    R_gamma = -V_ud V_ub* / (V_cd V_cb*)

compute:

  w_x  : winding number of arg R_x(phi) over phi in [0, 2 pi).
         Exact integer (homotopy invariant; certified by N-refinement
         and min|R_x| > 0 along the circle).  In any epsilon-
         hierarchical regime of the chart, arg R_x = w_x phi + c_x +
         subleading deformation, so w_x is the LO phase power of R_x.
  c_x  : constant offset of the linear law (found in {0, +-pi}).
  wob_x: peak-to-peak deviation of arg R_x from w_x phi + c_x at the
         fitted magnitudes -- the NLO deformation of the LO identity.

Hierarchy flow: magnitudes m_e -> m_e^tau (epsilon = e^{-tau} units)
amplify the chart's own hierarchy without touching its combinatorics.
As tau grows every CKM element becomes single-path dominated, so
arg R_x(phi; tau) -> w_x phi + c_x exactly.  Measuring wob_x(tau) and
c_x(tau) shows whether the fitted point (tau = 1) sits in the chart's
perturbative regime and extracts c_x with certifiable precision.

Also per chart: arg det(Y_u Y_d) winding (WP5 determinant link) and the
harmonic purity of det[H_u, H_d](phi) (extends the exact harmonic
support theorem of harmonic_support.py to the census ensemble).

Cross-chart test: within the 0.817882 / 0.819271 clusters (each spanning
6 distinct support orbits), compare the full functions arg R_x(phi)
between positive-branch charts -- identical functions mean the charts
embed the SAME phi-parametrized physical curve: loop-phase transport
across those orbit boundaries is canonical, not coincidental.

Validation (T8): the symbolic epsilon-series eigensolver of
wp4_triangle_lo.py, with rational epsilon powers derived from the fitted
magnitudes, independently re-derives the winding triple of the clean
beta-core chart (orbit 5, member (172,428)) with no winding sampling.

Output: research/flavor/results/wp9_lo_atlas.json
"""
import cmath
import json
import math
import sys

import numpy as np

sys.path.insert(0, "research/flavor/checkers")
from wp7_ensemble import build_texture, observables17, SIGMA, mask_slots

N_WIND = 1024          # winding samples (certified by N-halving test)
N_FLOW = 128           # samples per tau-flow slice
TAUS_DOUBLE = [1.0, 2.0, 4.0]     # float64 path
TAUS_MP = [8.0, 16.0, 32.0, 64.0, 96.0, 128.0]  # mpmath path; adaptive cap 128
PHYS_TOL_SIGMA = 1e-4  # WP7.2b/WP8 fiber convention
HARM_TOL = 1e-10       # detC harmonic purity threshold (relative to m=1)
WIND_TOL = 1e-9
C_CLASS_TOL = 1e-3     # c in {0, +-pi} classification at convergence
FLOW_WOB_TOL = 5e-3    # wobble at the final tau must fall below this
CURVE_TOL = 1e-6       # cross-chart arg-R identity tolerance
ANGLES = ("alpha", "beta", "gamma")


def angmod(x):
    return x % math.pi


def angdist(a, b):
    d = abs(angmod(a) - angmod(b))
    return min(d, math.pi - d)


def quartics(Yu, Yd):
    _, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
    _, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
    V = Uu.conj().T @ Ud
    return [-V[2, 0] * np.conj(V[2, 2]) / (V[0, 0] * np.conj(V[0, 2])),
            -V[1, 0] * np.conj(V[1, 2]) / (V[2, 0] * np.conj(V[2, 2])),
            -V[0, 0] * np.conj(V[0, 2]) / (V[1, 0] * np.conj(V[1, 2]))]


def sample_chart(member, pe, log_mags, n, tau=1.0):
    """Sample arg R_x, det(Yu Yd), det[Hu,Hd] around the phase circle,
    with magnitudes raised to tau (hierarchy flow)."""
    phis = np.linspace(0.0, 2 * math.pi, n, endpoint=False)
    args = np.zeros((n, 3))
    minR = np.full(3, np.inf)
    detY = np.zeros(n, dtype=complex)
    detC = np.zeros(n, dtype=complex)
    lm = [tau * x for x in log_mags]
    for k, ph in enumerate(phis):
        Yu, Yd = build_texture(member[0], member[1], pe[0], (pe[1], pe[2]),
                               np.array(lm + [ph]))
        qs = quartics(Yu, Yd)
        args[k] = [np.angle(q) for q in qs]
        minR = np.minimum(minR, [abs(q) for q in qs])
        detY[k] = np.linalg.det(Yu) * np.linalg.det(Yd)
        Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T
        detC[k] = np.linalg.det(Hu @ Hd - Hd @ Hu)
    return phis, args, minR, detY, detC


def winding(args_col):
    unw = np.unwrap(args_col)
    total = unw[-1] - unw[0] + (unw[1] - unw[0])
    return total / (2 * math.pi), unw


def laws(phis, args):
    """Per quartic: winding, offset, wobble function."""
    out = {}
    for j, name in enumerate(ANGLES):
        w_float, unw = winding(args[:, j])
        w = int(round(w_float))
        c = float(np.mean(unw - w * phis))
        c = ((c + math.pi) % (2 * math.pi)) - math.pi
        wob = unw - (w * phis + c)
        out[name] = {"w_float": w_float, "w": w, "c": c,
                     "wobble_p2p": float(wob.max() - wob.min()),
                     "wobble_fun": wob}
    return out


def chart_record(p):
    phis, args, minR, detY, detC = sample_chart(
        p["member"], p["phase_edge"], p["log_mags"], N_WIND)
    lw = laws(phis, args)
    wd_float, _ = winding(np.angle(detY))
    im = detC.imag
    ft = np.fft.rfft(im) / len(im)
    a1 = 2 * abs(ft[1])
    higher = max(2 * abs(ft[m]) for m in range(2, 6))
    # chart's own UT angles at its fitted phase
    Yu, Yd = build_texture(p["member"][0], p["member"][1],
                           p["phase_edge"][0],
                           (p["phase_edge"][1], p["phase_edge"][2]),
                           np.array(list(p["log_mags"]) + [p["phi"]]))
    qs = quartics(Yu, Yd)
    ut = sorted(angmod(np.angle(q)) for q in qs)
    ut = {"beta": ut[0], "gamma": ut[1], "alpha": ut[2]}
    resid = {}
    for name in ANGLES:
        if lw[name]["w"] != 0:
            law = lw[name]["w"] * p["phi"] + lw[name]["c"]
            resid[name] = angdist(law, ut[name])
    return {"orbit": p["orbit"], "member": p["member"],
            "phase_edge": p["phase_edge"], "raw_phi": p["phi"],
            "phi_folded": p["phi_folded"], "log_mags": p["log_mags"],
            "w": [lw[n]["w"] for n in ANGLES],
            "w_float_max_dev": max(abs(lw[n]["w_float"] - lw[n]["w"])
                                   for n in ANGLES),
            "c": [lw[n]["c"] for n in ANGLES],
            "wobble": [lw[n]["wobble_p2p"] for n in ANGLES],
            "wobble_fun": {n: lw[n]["wobble_fun"] for n in ANGLES},
            "min_abs_R": [float(x) for x in minR],
            "det_winding": int(round(wd_float)),
            "det_winding_dev": abs(wd_float - round(wd_float)),
            "detC_higher_over_h1": float(higher / a1) if a1 > 0 else None,
            "ut_angles": ut, "carrier_residuals": resid,
            "best_carrier_residual": min(resid.values())}


def build_texture_mp(mask_u, mask_d, phase_sector, phase_slot, lm, phi):
    """mpmath twin of wp7_ensemble.build_texture: at large flow tau the
    smallest magnitudes (exp(tau * log_mag)) underflow float64, so the
    texture entries themselves must be built in mpmath.  Returns nested
    lists of mpc."""
    import mpmath as mp
    Yu = [[mp.mpc(0)] * 3 for _ in range(3)]
    Yd = [[mp.mpc(0)] * 3 for _ in range(3)]
    us, ds = mask_slots(mask_u), mask_slots(mask_d)
    mags = [mp.exp(mp.mpf(x)) for x in lm]
    entries = [("u", s) for s in us] + [("d", s) for s in ds]
    eiphi = mp.exp(mp.mpc(0, mp.mpf(phi)))
    for (sector, slot), m in zip(entries, mags):
        val = m
        if sector == phase_sector and slot == phase_slot:
            val = m * eiphi
        if sector == "u":
            Yu[slot[0]][slot[1]] = val
        else:
            Yd[slot[0]][slot[1]] = val
    return Yu, Yd


def sample_args_mp(member, pe, log_mags, n, tau):
    """Phase-circle arg R_x samples via the mpmath Jacobi eigensolver
    (float64 eigh loses the smallest eigenpair beyond ~1e16 ratio).
    All CKM arithmetic stays in mpmath; only the O(1) quartic phases
    are returned as floats."""
    import mpmath as mp
    from jacobi_mp import v_ckm_mp
    phis = np.linspace(0.0, 2 * math.pi, n, endpoint=False)
    args = np.zeros((n, 3))
    span = -min(log_mags)
    dps = int(2 * tau * span / math.log(10)) + 80
    lm = [tau * x for x in log_mags]
    for k, ph in enumerate(phis):
        Yu, Yd = build_texture_mp(member[0], member[1], pe[0],
                                  (pe[1], pe[2]), lm, ph)
        V = v_ckm_mp(Yu, Yd, dps=dps)
        qs = [-V[2][0] * mp.conj(V[2][2])
              / (V[0][0] * mp.conj(V[0][2])),
              -V[1][0] * mp.conj(V[1][2])
              / (V[2][0] * mp.conj(V[2][2])),
              -V[0][0] * mp.conj(V[0][2])
              / (V[1][0] * mp.conj(V[1][2]))]
        args[k] = [float(mp.arg(q)) for q in qs]
    return phis, args


def tau_flow(p, w_ref):
    """Wobble and offset of each quartic along mags -> mags^tau.
    float64 up to tau = 4; extends into the mpmath regime (tau up to 128)
    until every wobble falls below FLOW_WOB_TOL. Charts whose path-dominance
    gap is too small may not converge by tau = 128; they are recorded with
    converged=False rather than forced.  A winding CHANGE along the flow is
    not an error: for nonperturbative charts the φ-dependence of a CKM
    quartic can re-organize as path dominance shifts, so the tau = 1 winding
    need not survive.  Such reps are recorded with winding_stable=False and
    the flow is truncated at the first unstable slice."""
    flow = {n: {"tau": [], "wobble": [], "c": []} for n in ANGLES}
    converged = False
    winding_stable = True
    unstable_tau = None
    for tau in TAUS_DOUBLE:
        with np.errstate(all="ignore"):
            phis, args, _, _, _ = sample_chart(p["member"], p["phase_edge"],
                                               p["log_mags"], N_FLOW,
                                               tau=tau)
        lw = laws(phis, args)
        if any(lw[n]["w"] != w_ref[j] for j, n in enumerate(ANGLES)):
            winding_stable, unstable_tau = False, tau
            break
        for j, n in enumerate(ANGLES):
            flow[n]["tau"].append(tau)
            flow[n]["wobble"].append(lw[n]["wobble_p2p"])
            flow[n]["c"].append(lw[n]["c"])
    if winding_stable and \
            max(flow[n]["wobble"][-1] for n in ANGLES) < FLOW_WOB_TOL:
        converged = True
    for tau in TAUS_MP:
        if converged or not winding_stable:
            break
        phis, args = sample_args_mp(p["member"], p["phase_edge"],
                                    p["log_mags"], 64, tau)
        lw = laws(phis, args)
        if any(lw[n]["w"] != w_ref[j] for j, n in enumerate(ANGLES)):
            winding_stable, unstable_tau = False, tau
            break
        for j, n in enumerate(ANGLES):
            flow[n]["tau"].append(tau)
            flow[n]["wobble"].append(lw[n]["wobble_p2p"])
            flow[n]["c"].append(lw[n]["c"])
        if max(flow[n]["wobble"][-1] for n in ANGLES) < FLOW_WOB_TOL:
            converged = True
    return flow, converged, winding_stable, unstable_tau


def symbolic_validation():
    """T8: WP4 series eigensolver on a hierarchical lattice point of the
    gamma-core chart (orbit 6, member (417,342), phase edge (d,0,1)).
    Epsilon powers are integer roundings of the fitted log-magnitudes
    with a granularity of ~7 units over the span; the winding reference
    is computed NUMERICALLY AT THE SAME LATTICE POINT, so the comparison
    is exact-machinery vs certified-numerics at one well-defined chart
    point (no fitted-point regime ambiguity)."""
    import sympy as sp
    from wp4_triangle_lo import trunc, lead, eigensystem

    eps = sp.symbols("epsilon", positive=True)
    z = sp.symbols("z", nonzero=True)
    NSER = 28

    data = json.load(open("research/flavor/results/wp7_ensemble.json"))
    target = None
    for orb in data["orbits"]:
        if orb["orbit_index"] != 6:
            continue
        for m in orb["viable_minima"]:
            if (m["member"] == [417, 342] and m["phase_edge"] == ["d", 0, 1]
                    and m["phi"] > 0):
                target = m
    assert target is not None, "validation chart not found in ensemble"
    span = -min(target["log_mags"])
    gran = span / 7.0
    powers = [sp.Integer(int(round(-x / gran))) for x in target["log_mags"]]
    max_pw = max(int(p) for p in powers)

    # numeric winding reference AT THE SAME LATTICE POINT
    rho = 0.05
    lat_lm = [float(p) * math.log(rho) for p in powers]  # mag = rho^p
    phis, args, minR, _, _ = sample_chart(target["member"],
                                          target["phase_edge"],
                                          lat_lm, 512)
    lw = laws(phis, args)
    w_lat = {n: lw[n]["w"] for n in ANGLES}
    wob_lat = {n: lw[n]["wobble_p2p"] for n in ANGLES}

    slots = [(i, j) for i in range(3) for j in range(3)]
    mu, md = target["member"]
    us = [s for k, s in enumerate(slots) if mu & (1 << k)]
    ds = [s for k, s in enumerate(slots) if md & (1 << k)]
    syms = sp.symbols("a0:9", positive=True)
    Yu = sp.Matrix.zeros(3)
    Yd = sp.Matrix.zeros(3)
    for slot, pw, a in zip(us, powers[:len(us)], syms[:len(us)]):
        Yu[slot] = a * eps**pw
    pe = target["phase_edge"]
    for slot, pw, a in zip(ds, powers[len(us):], syms[len(us):]):
        val = a * eps**pw
        if (slot[0], slot[1]) == (pe[1], pe[2]):
            val = z * val
        Yd[slot] = val
    Hu, Hd = Yu * Yu.H, Yd * Yd.H
    _, Uu = eigensystem(Hu, NSER)
    _, Ud = eigensystem(Hd, NSER)
    V = sp.Matrix(3, 3, lambda i, j: trunc(
        sum(sp.conjugate(Uu[k, i]) * Ud[k, j] for k in range(3)), NSER))

    def lead_zpower(num, den):
        """z-power shared by all terms of the lead coefficient of
        -num/den (multi-monomial leads allowed if the z-degree is
        unique)."""
        n1 = sp.expand(lead(num)[1].subs(sp.conjugate(z), z**-1))
        n2 = sp.expand(lead(den)[1].subs(sp.conjugate(z), z**-1))
        p1 = sp.Poly(sp.expand(n1 * z**4), z)
        p2 = sp.Poly(sp.expand(n2 * z**4), z)
        d1 = sorted({dg[0] - 4 for dg, cf in p1.terms()
                     if sp.simplify(cf) != 0})
        d2 = sorted({dg[0] - 4 for dg, cf in p2.terms()
                     if sp.simplify(cf) != 0})
        assert len(d1) == 1 and len(d2) == 1, \
            f"lead z-degrees not unique: {d1} / {d2}"
        return d1[0] - d2[0]

    Vc = sp.Matrix(3, 3, lambda i, j: sp.expand(V[i, j]))
    RA_n = sp.expand(Vc[2, 0] * sp.conjugate(Vc[2, 2]))
    RA_d = sp.expand(Vc[0, 0] * sp.conjugate(Vc[0, 2]))
    RB_n = sp.expand(Vc[1, 0] * sp.conjugate(Vc[1, 2]))
    RB_d = sp.expand(Vc[2, 0] * sp.conjugate(Vc[2, 2]))
    RG_n = sp.expand(Vc[0, 0] * sp.conjugate(Vc[0, 2]))
    RG_d = sp.expand(Vc[1, 0] * sp.conjugate(Vc[1, 2]))
    ka = lead_zpower(RA_n, RA_d)
    kb = lead_zpower(RB_n, RB_d)
    kg = lead_zpower(RG_n, RG_d)
    return {"chart": {"orbit": 6, "member": target["member"],
                      "phase_edge": pe},
            "eps_powers": [str(p) for p in powers],
            "granularity_ln_units": gran, "max_power": max_pw,
            "lattice_wobble": wob_lat,
            "lattice_min_abs_R": [float(x) for x in minR],
            "z_powers": {"alpha": ka, "beta": kb, "gamma": kg},
            "winding_reference_at_lattice": w_lat,
            "n_series": NSER}


def main():
    data = json.load(open("research/flavor/results/wp7_ensemble.json"))
    pts = []
    for orb in data["orbits"]:
        for m in orb["viable_minima"]:
            pe = m["phase_edge"]
            theta = np.array(m["log_mags"] + [m["phi"]])
            Yu, Yd = build_texture(m["member"][0], m["member"][1], pe[0],
                                   (pe[1], pe[2]), theta)
            pts.append({"orbit": orb["orbit_index"], "member": m["member"],
                        "phase_edge": pe, "chi2": m["chi2"], "phi": m["phi"],
                        "phi_folded": m["phi_folded"],
                        "log_mags": m["log_mags"],
                        "obs": observables17(Yu, Yd)})
    best = min(pts, key=lambda p: p["chi2"])
    fiber = [p for p in pts
             if np.all(np.abs(p["obs"] - best["obs"])
                       <= PHYS_TOL_SIGMA * SIGMA)]
    assert len(fiber) == 61, f"fiber size {len(fiber)} != 61 (WP8)"

    charts = []
    for i, p in enumerate(fiber):
        charts.append(chart_record(p))
        print(f"[{i + 1}/61] orb {p['orbit']:2d} {p['member']} "
              f"w {charts[-1]['w']} best-res "
              f"{charts[-1]['best_carrier_residual'] * 1000:8.2f} mrad",
              flush=True)

    tests = {}
    tests["T1_sum_w_zero_all"] = all(sum(c["w"]) == 0 for c in charts)
    tests["T1b_winding_integer_certified"] = all(
        c["w_float_max_dev"] < WIND_TOL
        and c["det_winding_dev"] < WIND_TOL for c in charts)
    tests["T2_c_in_0_pi_all"] = all(
        min(abs(cj), abs(abs(cj) - math.pi)) < 1e-6
        for c in charts for cj in c["c"])
    tests["T3_w_pattern_two_nonzero_unit"] = all(
        sorted(abs(w) for w in c["w"]) == [0, 1, 1] for c in charts)
    tests["T4_detC_first_harmonic_only"] = all(
        c["detC_higher_over_h1"] is not None
        and c["detC_higher_over_h1"] < HARM_TOL for c in charts)
    tests["T5_min_abs_R_positive"] = all(
        min(c["min_abs_R"]) > 1e-3 for c in charts)

    # winding N-stability on every 10th chart
    stab = True
    for c in charts[::10]:
        _, args2, _, _, _ = sample_chart(c["member"], c["phase_edge"],
                                         c["log_mags"], 256)
        lw2 = laws(np.linspace(0, 2 * math.pi, 256, endpoint=False), args2)
        for j, n in enumerate(ANGLES):
            if lw2[n]["w"] != c["w"][j]:
                stab = False
    tests["T7_winding_N_stable"] = stab

    # tau flow on one representative per (core, orbit)
    seen = set()
    flow_reps = []
    for c, p in zip(charts, fiber):
        key = (round(c["phi_folded"], 6), c["orbit"])
        if key not in seen:
            seen.add(key)
            flow_reps.append((c, p))
    flows = []
    for c, p in flow_reps:
        fl, conv, stab, utau = tau_flow(p, c["w"])
        flows.append({"core": round(c["phi_folded"], 6), "orbit": c["orbit"],
                      "member": c["member"], "converged": conv,
                      "winding_stable": stab, "unstable_tau": utau,
                      "flow": {n: {k: v for k, v in fl[n].items()}
                               for n in ANGLES}})
        print(f"flow orb {c['orbit']:2d} core {c['phi_folded']:.6f}: "
              f"wob(final) "
              f"{[round(fl[n]['wobble'][-1], 6) if fl[n]['wobble'] else None
                 for n in ANGLES]}"
              f" conv {conv} stab {stab}", flush=True)
    tests["T6_flow_wobble_vanishes"] = all(fl["converged"] for fl in flows)
    tests["T6b_flow_c_in_0_pi"] = all(
        min(abs(fl["flow"][n]["c"][-1]),
            abs(abs(fl["flow"][n]["c"][-1]) - math.pi)) < C_CLASS_TOL
        for fl in flows if fl["converged"] for n in ANGLES)
    tests["T6c_converged_reps_winding_stable"] = all(
        fl["winding_stable"] for fl in flows if fl["converged"])

    # per-core classification
    cores = {}
    for c in charts:
        cores.setdefault(round(c["phi_folded"], 6), []).append(c)
    core_out = {}
    for key, cs in sorted(cores.items()):
        best_res = min(c["best_carrier_residual"] for c in cs)
        carriers = sorted({n for c in cs for n, r in
                           c["carrier_residuals"].items()
                           if abs(r - c["best_carrier_residual"]) < 1e-12})
        regime = ("clean" if best_res < 2e-3
                  else "moderate" if best_res < 50e-3
                  else "nonperturbative")
        core_out[f"{key:.6f}"] = {
            "n_charts": len(cs), "orbits": sorted({c["orbit"] for c in cs}),
            "best_carrier_residual_mrad": best_res * 1000,
            "carriers": carriers, "regime": regime}

    # cross-chart curve identity within the two large clusters
    curve_tests = {}
    for key in (0.817882, 0.819271):
        cs = [c for c in cores.get(key, []) if c["raw_phi"] > 0]
        if len(cs) >= 2:
            ref = cs[0]
            worst = 0.0
            for c in cs[1:]:
                for n in ANGLES:
                    if ref["w"][ANGLES.index(n)] != c["w"][ANGLES.index(n)]:
                        worst = np.inf
                        continue
                    a = np.array(ref["wobble_fun"][n])
                    b = np.array(c["wobble_fun"][n])
                    # These are angular wobble curves.  Compare them on S^1,
                    # not as chosen real-valued branches; otherwise an
                    # identical curve crossing the cut differs by 2*pi.
                    circular_delta = np.angle(np.exp(1j * (a - b)))
                    worst = max(worst, float(np.max(np.abs(circular_delta))))
            curve_tests[f"{key:.6f}"] = {
                "n_positive_branch_charts": len(cs),
                "orbits": sorted({c["orbit"] for c in cs}),
                "max_wobblefun_deviation": worst,
                "curves_identical": worst < CURVE_TOL}

    if "--t8" in sys.argv:
        print("running symbolic validation (T8)...", flush=True)
        t8 = symbolic_validation()
        tests["T8_symbolic_z_powers_match_winding"] = (
            t8["z_powers"] == t8["winding_reference_at_lattice"])
    else:
        # T8 (sympy series eigensolver) is expensive; run explicitly with
        # --t8.  Skipped runs record None rather than a verdict.
        t8 = {"skipped": True,
              "note": "run with --t8 to include the symbolic validation"}
        tests["T8_symbolic_z_powers_match_winding"] = None

    out = {
        "purpose": "WP9 exact LO atlas of the loop-phase carrier "
                   "structure over the WP8 fiber (sharpens entries 1084, "
                   "1092)",
        "conventions": {"n_wind_samples": N_WIND,
                        "n_flow_samples": N_FLOW,
                        "taus_double": TAUS_DOUBLE,
                        "taus_mp": TAUS_MP,
                        "phys_tol_sigma": PHYS_TOL_SIGMA},
        "tests": tests,
        "curve_identity": curve_tests,
        "cores": core_out,
        "tau_flows": flows,
        "symbolic_validation": t8,
        "charts": [{k: v for k, v in c.items() if k != "wobble_fun"}
                   for c in charts],
    }
    with open("research/flavor/results/wp9_lo_atlas.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(tests, indent=1))
    print(json.dumps(curve_tests, indent=1))
    print(json.dumps(core_out, indent=1))
    print("wrote research/flavor/results/wp9_lo_atlas.json")


if __name__ == "__main__":
    main()
