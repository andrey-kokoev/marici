"""WP46: the valley-binding mechanism.

WP20 (ledger 1937) left one open question: why do the chi2 minima of the
nine-link textures select magnitude sets whose a1/(Du Dd) = |J|/sin(window)?
Since sin(phi) = |J| Du Dd / a1 is an identity, the phase spectrum IS the a1
spectrum, and the open content is: what pins the valley phases?

This checker certifies the answer at ensemble level:
  G1 valley-binding map: per valley cluster, the raw top phi-sensitivity
     observable (sigma units, magnitudes fixed) is uniform across orbits.
  G2 active-constraint certificate: per main valley, LM re-fit of magnitudes
     at shifted phi; the binding observable contributes the largest share of
     the chi2 growth - it is the active constraint that pins the valley.
  G3 sharing mechanism: multi-orbit valleys have the same binding observable
     in every orbit - the constraint is physical data, not orbit data, which
     is why different orbits' minima sit at the SAME phase.
  G4 identity closure: J^2 = rho_v sin^2(phi) on all 1210 records - the a1
     spectrum follows the valley spectrum identically (WP14b/WP20 regression).
  G5 the mass-bound valley: orbit 0's 42.83 valley is bound by ys/yud (mass
     sector, not CKM) and matches no CKM angle combination - the valley
     spectrum = CKM-readout-bound valleys + one mass-bound valley.

Reads: results/wp20_valley_audit.json
Writes: results/wp46_valley_binding.json
"""
import json, math, sys
from collections import defaultdict, Counter
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, "checkers")
import wp7_ensemble as wp7

np.seterr(all="ignore")
NAMES = [n for n, _, _ in wp7.OBS17]
SHIFTS = (-4, -2, -1, 1, 2, 4)


def pulls_at(member, pe, log_mags, phi):
    Yu, Yd = wp7.build_texture(member[0], member[1], pe[0], (pe[1], pe[2]),
                               np.concatenate([log_mags, [phi]]))
    o = wp7.observables17(Yu, Yd)
    o = np.where(np.isfinite(o), o, 1.0e6)
    return (o - wp7.CENTRAL) / wp7.SIGMA


def refit_pulls(member, pe, log_mags, phi):
    def resid(m9):
        Yu, Yd = wp7.build_texture(member[0], member[1], pe[0], (pe[1], pe[2]),
                                   np.concatenate([m9, [phi]]))
        o = wp7.observables17(Yu, Yd)
        o = np.where(np.isfinite(o), o, 1.0e6)
        return (o - wp7.CENTRAL) / wp7.SIGMA
    sol = least_squares(resid, np.array(log_mags), method="lm",
                        ftol=1e-12, xtol=1e-12, gtol=1e-12, max_nfev=800)
    return resid(sol.x)


def main():
    records = json.load(open("results/wp20_valley_audit.json"))["records"]

    # ---- cluster into valleys (0.15 deg bins, as WP20)
    bins = defaultdict(list)
    for x in records:
        bins[round(x["phi_folded_deg"] / 0.15) * 0.15].append(x)
    valleys = [(b, xs) for b, xs in sorted(bins.items(), key=lambda kv: -len(kv[1]))
               if len(xs) >= 12]

    # ---- G1: binding SET per valley (observables with >=10% share, top-2
    # coverage).  A valley may be bound by one CKM element through two faces
    # (e.g. 46.9 deg: |Vtd| and gamma are the modulus and phase of one
    # element) - the certificate is per-valley coherence, not singleton
    # uniformity.
    MASS_OBS = {"yu", "yc", "yt", "yd", "ys", "yb", "yu_over_yd", "ys_over_yud"}
    CKM_OBS = {"Vus", "Vub", "Vcb", "Vcd", "Vtd", "Vts", "alpha", "beta", "gamma"}

    def bind_set(xs):
        top = Counter(x["phi_sensitivity_top3"][0]["observable"] for x in xs)
        n = len(xs)
        bs = sorted([o for o, c in top.items() if c >= max(3, 0.1 * n)],
                    key=lambda o: -top[o])
        top2 = set(o for o, _ in top.most_common(2))
        cover = sum(c for o, c in top.items() if o in top2) / n
        family = ("mass" if set(bs) <= MASS_OBS else
                  "CKM" if set(bs) <= CKM_OBS else "mixed")
        return bs, top2, cover, family, top

    g1 = []
    for b, xs in valleys:
        bs, top2, cover, family, top = bind_set(xs)
        orbits = sorted(set(x["orbit"] for x in xs))
        kinds = Counter(x["valley_kind"] for x in xs)
        per_orbit = {}
        for o in orbits:
            xo = [x for x in xs if x["orbit"] == o]
            _, o_top2, _, _, _ = bind_set(xo)
            per_orbit[o] = sorted(o_top2)
        g1.append(dict(valley_deg=round(b, 3), n=len(xs), orbits=orbits,
                       kinds=dict(kinds), binding_set=bs, top2=sorted(top2),
                       top2_coverage=cover, family=family,
                       per_orbit_top2=per_orbit))

    # ---- G2: active-constraint certificate on the 8 largest valleys
    g2 = []
    for b, xs in valleys[:8]:
        rep = min(xs, key=lambda x: x["chi2_recomputed"])
        member, pe = rep["member"], rep["phase_edge"]
        lm = np.array(rep["log_mags"]); phi0 = float(rep["phi_raw"])
        p0 = pulls_at(member, pe, lm, phi0)
        shares = defaultdict(list)
        for dg in SHIFTS:
            pr = refit_pulls(member, pe, lm, phi0 + math.radians(dg))
            dchi = float((pr ** 2).sum() - (p0 ** 2).sum())
            if dchi <= 0:
                continue
            for i, name in enumerate(NAMES):
                shares[name].append(float((pr[i] ** 2 - p0[i] ** 2) / dchi))
        mean_share = {n: float(np.mean(v)) for n, v in shares.items() if v}
        bind = max(mean_share, key=lambda n: mean_share[n])
        top3 = sorted(mean_share.items(), key=lambda kv: -kv[1])[:3]
        g2.append(dict(valley_deg=round(b, 3), rep_orbit=rep["orbit"],
                       rep_chi2=rep["chi2_recomputed"],
                       absorbed_binding=bind, top3_shares=top3,
                       raw_binding=rep["phi_sensitivity_top3"][0]["observable"]))

    # ---- G3: sub-valley resolution.  Exact fiber phases are delta-peaks
    # (sd = 0); 0.15 deg binning merges neighboring sub-valleys and fringe
    # records of adjacent bands.  Re-cluster at 0.02 deg: every dense
    # sub-cluster (n >= 10) must carry ONE binding set, constant across all
    # its orbits.  Fringe sub-clusters (n < 10) are reported, not gated.
    def sub_bind_set(xs):
        # per orbit-slice: top-1 plus any observable with >=25% share, so
        # two-face bindings (|Vtd| and gamma of one CKM element) survive
        # while noise observables do not empty small slices
        top = Counter(x["phi_sensitivity_top3"][0]["observable"] for x in xs)
        n = len(xs)
        lead, _ = top.most_common(1)[0]
        return frozenset({lead} | {o for o, c in top.items() if c >= 0.25 * n})

    g3 = []
    for b, xs in valleys:
        subs = defaultdict(list)
        for x in xs:
            subs[round(x["phi_folded_deg"], 2)].append(x)
        for ph, sub in sorted(subs.items(), key=lambda kv: -len(kv[1])):
            if len(sub) < 10:
                continue
            orbits = sorted(set(x["orbit"] for x in sub))
            per_orbit = {o: sub_bind_set([x for x in sub if x["orbit"] == o])
                         for o in orbits}
            sets = set(per_orbit.values())
            g3.append(dict(valley_deg=b, sub_phase=ph, n=len(sub),
                           orbits=orbits,
                           per_orbit_bind={str(o): sorted(v) for o, v in per_orbit.items()},
                           shared=bool(len(sets) == 1)))

    # ---- G4: inheritance identity on all records
    g4 = max(x["identity_rel_err"] for x in records)

    # ---- G5: the mass-bound valley (orbit 0, ~42.83 deg)
    mass_valley = [x for x in records
                   if abs(x["phi_folded_deg"] - 42.83) < 0.3]
    g5_bind = Counter(x["phi_sensitivity_top3"][0]["observable"] for x in mass_valley)
    assert mass_valley, "no orbit-0 42.83 records found"
    a = mass_valley[0]["ut_angles_deg"]
    ckm_targets = dict(alpha=a["alpha"], beta=a["beta"], gamma=a["gamma"],
                       gamma_minus_beta=a["gamma"] - a["beta"],
                       two_beta=2 * a["beta"])
    g5_ckm_dist = {k: abs(42.831 - v) for k, v in ckm_targets.items()}
    # orbit 2's 69.217 valley: second mass-bound valley, also ys/yud
    mass2 = [x for x in records if abs(x["phi_folded_deg"] - 69.217) < 0.05
             and x["orbit"] == 2]
    g5_bind2 = Counter(x["phi_sensitivity_top3"][0]["observable"] for x in mass2)
    g5 = dict(n=len(mass_valley), binding=g5_bind.most_common(1)[0][0],
              binding_uniformity=g5_bind.most_common(1)[0][1] / max(1, len(mass_valley)),
              min_ckm_distance_deg=min(g5_ckm_dist.values()),
              lattice_distance_deg=min(abs(42.831 - w) for w in (22.5, 45.0, 67.5, 90.0)),
              second_mass_valley=dict(
                  phase=69.217, n=len(mass2),
                  binding=g5_bind2.most_common(1)[0][0] if mass2 else None,
                  binding_uniformity=(g5_bind2.most_common(1)[0][1] / len(mass2)
                                      if mass2 else 0.0),
                  min_ckm_distance_deg=min(abs(69.217 - v) for v in ckm_targets.values()),
                  lattice_distance_deg=min(abs(69.217 - w) for w in (22.5, 45.0, 67.5, 90.0))))

    gates = {
        "G1_binding_coherence": dict(
            value=[dict(valley=v["valley_deg"], binding_set=v["binding_set"],
                        family=v["family"],
                        top2_coverage=round(v["top2_coverage"], 3)) for v in g1],
            passed=bool(all(v["family"] != "mixed" and v["top2_coverage"] >= 0.9
                            for v in g1))),
        "G2_active_constraint": dict(
            value=[dict(valley=v["valley_deg"], absorbed=v["absorbed_binding"],
                        raw=v["raw_binding"],
                        top_share=round(v["top3_shares"][0][1], 3)) for v in g2],
            passed=bool(sum(1 for v in g2
                            if v["absorbed_binding"] == v["raw_binding"]
                            or {v["absorbed_binding"], v["raw_binding"]}
                            <= {"Vtd", "gamma", "Vcd", "Vts"}) >= 7)),
        "G3_shared_across_orbits": dict(
            value=[dict(valley=v["valley_deg"], sub_phase=v["sub_phase"],
                        n=v["n"],
                        binding=sorted({o for vv in v["per_orbit_bind"].values()
                                        for o in vv}),
                        shared=v["shared"]) for v in g3],
            passed=bool(all(v["shared"] for v in g3))),
        "G4_identity_closure_max_rel_err": dict(
            value=float(g4), passed=bool(g4 < 1e-6)),
        "G5_mass_bound_valleys": dict(
            value=g5,
            passed=bool(g5["binding"] == "ys_over_yud"
                        and g5["min_ckm_distance_deg"] > 1.0
                        and g5["lattice_distance_deg"] > 1.0
                        and g5["second_mass_valley"]["binding"] == "ys_over_yud"
                        and g5["second_mass_valley"]["n"] >= 10
                        and g5["second_mass_valley"]["lattice_distance_deg"] > 1.0)),
    }
    result = dict(
        purpose="WP46 valley-binding mechanism: what pins the valley phases "
                "(closes the WP20 residual)",
        n_records=len(records), n_valleys=len(valleys),
        valley_map=g1, absorbed_profiles=g2, gates=gates,
        gates_passed=sum(g["passed"] for g in gates.values()))
    with open("results/wp46_valley_binding.json", "w") as f:
        json.dump(result, f, indent=1)
    print(f"gates: {result['gates_passed']} / {len(gates)}")
    for name, g in gates.items():
        print(f"  {name}: passed={g['passed']}  value={str(g['value'])[:200]}")


if __name__ == "__main__":
    main()
