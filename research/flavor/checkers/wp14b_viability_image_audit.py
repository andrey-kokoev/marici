"""WP14b: exact viability identity + the pi/8 image audit over the fitted
carrier groupoid (marici.Figueiredo).

Closes the brief's fourth-work-package audit at groupoid level.  Three
questions, all evaluated per chart of the WP9 atlas (61 charts, all over
ONE physical flavor point per WP10):

Q1 (viability identity).  WP12/WP13 give det[H_u,H_d] = 2i K_v sin(phi_v)
with K_v real, exact per chart.  Combined with the standard identity
det[H_u,H_d] = -2i J prod Delta_u prod Delta_d one gets

    J^2 = rho_v * sin^2(phi_v),   rho_v = K_v^2 / (disc(H_u) disc(H_d)),

with disc(H) = prod_{i<j} (lambda_i - lambda_j)^2 the characteristic
discriminant (a polynomial in the char coefficients, i.e. in CP-even
chart data; phi-free in the 49 mass-flat charts of WP12).  Verified here
NUMERICALLY at 40 dps per chart: K_v extracted as det C / (2 i sin phi)
must be real to input precision, and J from the CKM quartet
Im(V_us V_cb V_ub* V_cs*) must match det C / (-2i prod Delta) -- two
independent computations of the same identity.

Q2 (one physical point).  J, the six masses and the three CKM moduli must
be constant across the 61 charts to input precision (regression of WP10).

Q3 (image audit).  For each chart, compare the fitted phi (folded to
[0, pi/2]) against (a) the chart's OWN unitarity-triangle angles
{alpha, beta, gamma} -- the carrier hypothesis (WP7/WP9 angle
inheritance) -- and (b) the pi/8 lattice {0, pi/8, pi/4, 3pi/8, pi/2}.
If the clustering were lattice-driven, (b) should win; if it is angle
inheritance, (a) wins.  Grouped by phase core (WP9 cores), with the
clean/nonperturbative regime recorded.

Precision honesty: log_mags and phi are stored as IEEE doubles, so all
results carry input-precision ~1e-13 relative at best; mpmath dps=40
keeps arithmetic well below that.

Output: research/flavor/results/wp14b_viability_image_audit.json
"""
import json
import time
from collections import Counter, defaultdict

import mpmath as mp

mp.mp.dps = 40

SLOTS = [(i, j) for i in range(3) for j in range(3)]
LATTICE = [mp.mpf(0), mp.pi / 8, mp.pi / 4, 3 * mp.pi / 8, mp.pi / 2]
LATTICE_NAMES = ["0", "pi/8", "pi/4", "3pi/8", "pi/2"]


def mask_slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def build_numeric(mask_u, mask_d, phase_sector, phase_slot, log_mags, phi):
    Yu = mp.zeros(3, 3)
    Yd = mp.zeros(3, 3)
    entries = [("u", s) for s in mask_slots(mask_u)] + \
              [("d", s) for s in mask_slots(mask_d)]
    z = mp.exp(1j * mp.mpf(phi))
    for (sector, slot), lm in zip(entries, log_mags):
        val = mp.exp(mp.mpf(lm))
        if sector == phase_sector and tuple(slot) == tuple(phase_slot):
            val = z * val
        (Yu if sector == "u" else Yd)[slot[0], slot[1]] = val
    return Yu, Yd


def hermitian_eig(H):
    """Eigenvalues (sorted mpf) and eigenvector matrix of hermitian H."""
    E, ER = mp.eighe(H)
    order = sorted(range(3), key=lambda i: E[i])
    vals = [E[i] for i in order]
    vecs = mp.zeros(3, 3)
    for newc, oldc in enumerate(order):
        for r in range(3):
            vecs[r, newc] = ER[r, oldc]
    return vals, vecs


def analyze_chart(ch):
    mu, md = ch["member"]
    sec = ch["phase_edge"][0]
    slot = (ch["phase_edge"][1], ch["phase_edge"][2])
    Yu, Yd = build_numeric(mu, md, sec, slot, ch["log_mags"], ch["raw_phi"])
    Hu = Yu * Yu.H
    Hd = Yd * Yd.H

    ev_u, Uu = hermitian_eig(Hu)
    ev_d, Ud = hermitian_eig(Hd)
    masses_u = [mp.sqrt(v) for v in ev_u]
    masses_d = [mp.sqrt(v) for v in ev_d]

    # CKM and J via the quartet
    V = Uu.H * Ud
    J_quartet = mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2])
                      * mp.conj(V[1, 1]))

    def prod_delta(ev):
        return abs((ev[0] - ev[1]) * (ev[0] - ev[2]) * (ev[1] - ev[2]))

    Du = prod_delta(ev_u)
    Dd = prod_delta(ev_d)
    C = Hu * Hd - Hd * Hu
    detC = mp.det(C)
    # detC = -2i J Du Dd with J real  =>  detC/(-2i Du Dd) is real = J
    J_comm = mp.re(detC / (-2j * Du * Dd))

    phi = mp.mpf(ch["raw_phi"])
    K = detC / (2j * mp.sin(phi))
    K_real_residual = abs(mp.im(K))
    rho = mp.re(K) ** 2 / (Du ** 2 * Dd ** 2)
    lhs = J_comm ** 2
    rhs = rho * mp.sin(phi) ** 2
    ident_rel = abs(lhs - rhs) / max(abs(lhs), mp.mpf("1e-300"))

    # unitarity-triangle angles from V (PDG arg-ratio definitions):
    #   beta  = arg(-V_cd V_cb* / (V_td V_tb*))
    #   gamma = arg(-V_ud V_ub* / (V_cd V_cb*))
    #   alpha = arg(-V_td V_tb* / (V_ud V_ub*))
    def carg(x):
        return mp.arg(x)

    beta = carg(-V[1, 0] * mp.conj(V[1, 2]) / (V[2, 0] * mp.conj(V[2, 2])))
    gamma = carg(-V[0, 0] * mp.conj(V[0, 2]) / (V[1, 0] * mp.conj(V[1, 2])))
    alpha = carg(-V[2, 0] * mp.conj(V[2, 2]) / (V[0, 0] * mp.conj(V[0, 2])))
    # map into (0, pi)
    def norm_ang(a):
        a = mp.fmod(a + 2 * mp.pi, 2 * mp.pi)
        if a > mp.pi:
            a = 2 * mp.pi - a
        return a
    alpha, beta, gamma = norm_ang(alpha), norm_ang(beta), norm_ang(gamma)

    phi_f = mp.mpf(ch["phi_folded"])
    carriers = {"alpha": alpha, "beta": beta, "gamma": gamma}
    cres = {k: float(abs(phi_f - v)) for k, v in carriers.items()}
    best_carrier = min(cres, key=cres.get)
    lres = {n: float(abs(phi_f - v)) for n, v in zip(LATTICE_NAMES, LATTICE)}
    best_lattice = min(lres, key=lres.get)

    ckm_moduli = [float(abs(V[0, 1])), float(abs(V[1, 2])),
                  float(abs(V[0, 2]))]

    return {
        "orbit": ch["orbit"], "member": [mu, md],
        "phase_edge": ch["phase_edge"],
        "phi_folded": float(phi_f),
        "J_quartet": float(J_quartet),
        "J_commutator": float(J_comm),
        "J_absdiff": float(abs(abs(J_quartet) - abs(J_comm))),
        "K_real_residual": float(K_real_residual),
        "viability_identity_rel_err": float(ident_rel),
        "masses_u": [float(m) for m in masses_u],
        "masses_d": [float(m) for m in masses_d],
        "ckm_moduli_us_cb_ub": ckm_moduli,
        "ut_angles": {"alpha": float(alpha), "beta": float(beta),
                      "gamma": float(gamma)},
        "ut_angles_stored": ch["ut_angles"],
        "carrier_residuals": cres,
        "best_carrier": best_carrier,
        "best_carrier_residual": cres[best_carrier],
        "lattice_residuals": lres,
        "best_lattice": best_lattice,
        "best_lattice_residual": lres[best_lattice],
    }


def main():
    t0 = time.time()
    with open("results/wp9_lo_atlas.json", encoding="utf-8") as f:
        atlas = json.load(f)
    charts = atlas["charts"]

    rows = []
    for i, ch in enumerate(charts):
        rows.append(analyze_chart(ch))
        if (i + 1) % 10 == 0:
            print(f"[{i + 1}/61] ({time.time() - t0:.0f}s)", flush=True)

    # Q2: constancy across the groupoid (spread relative to magnitude)
    Js = [abs(r["J_commutator"]) for r in rows]
    J_spread = max(Js) - min(Js)
    mass_spread_u = max(max(r["masses_u"][k] for r in rows)
                        - min(r["masses_u"][k] for r in rows)
                        for k in range(3))
    mass_spread_d = max(max(r["masses_d"][k] for r in rows)
                        - min(r["masses_d"][k] for r in rows)
                        for k in range(3))
    ckm_spread = max(max(r["ckm_moduli_us_cb_ub"][k] for r in rows)
                     - min(r["ckm_moduli_us_cb_ub"][k] for r in rows)
                     for k in range(3))

    # Q3: per-core audit (cores keyed by rounded folded phi as in WP9)
    cores = defaultdict(list)
    for r in rows:
        cores[f"{r['phi_folded']:.6f}"].append(r)
    core_table = []
    for core, members in sorted(cores.items(), key=lambda kv: kv[0]):
        bc = Counter(m["best_carrier"] for m in members)
        bl = Counter(m["best_lattice"] for m in members)
        med_c = sorted(m["best_carrier_residual"] for m in members)
        med_l = sorted(m["best_lattice_residual"] for m in members)
        core_table.append({
            "phi_core": core,
            "n_charts": len(members),
            "best_carrier_votes": dict(bc),
            "best_lattice_votes": dict(bl),
            "median_carrier_residual": med_c[len(med_c) // 2],
            "median_lattice_residual": med_l[len(med_l) // 2],
            "carrier_wins": sum(
                1 for m in members
                if m["best_carrier_residual"] < m["best_lattice_residual"]),
        })

    out = {
        "purpose": "WP14b: per-chart exact viability identity "
                   "J^2 = rho_v sin^2(phi_v) with rho_v CP-even chart "
                   "data, plus the pi/8 image audit (carrier CKM angles "
                   "vs pi/8 lattice) over the 61-vertex fitted groupoid",
        "precision_note": "inputs are IEEE doubles from wp9_lo_atlas.json; "
                          "mpmath dps=40; residuals below ~1e-12 are "
                          "input-precision limited",
        "q1_viability_identity": {
            "max_K_imag_residual": max(r["K_real_residual"] for r in rows),
            "max_identity_rel_err": max(r["viability_identity_rel_err"]
                                        for r in rows),
            "max_abs_J_quartet_minus_commutator":
                max(r["J_absdiff"] for r in rows),
        },
        "q2_one_physical_point": {
            "J_min": min(Js), "J_max": max(Js), "J_spread": J_spread,
            "mass_spread_u": mass_spread_u,
            "mass_spread_d": mass_spread_d,
            "ckm_moduli_spread": ckm_spread,
        },
        "q3_image_audit": {
            "core_table": core_table,
            "charts_carrier_wins": sum(
                1 for r in rows
                if r["best_carrier_residual"] < r["best_lattice_residual"]),
            "charts_lattice_wins": sum(
                1 for r in rows
                if r["best_carrier_residual"] >= r["best_lattice_residual"]),
        },
        "charts": rows,
    }
    with open("results/wp14b_viability_image_audit.json", "w",
              encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({k: v for k, v in out.items() if k != "charts"},
                     indent=2))
    print(f"elapsed {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
